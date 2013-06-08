# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'photologue_gallery')

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table(db.shorten_name(u'photologue_gallery_photos'))

        # Adding model 'BaseGallery'
        db.create_table(u'photologue_basegallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('tags', self.gf('photologue.models.TagField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'photologue', ['BaseGallery'])

        # Adding M2M table for field photos on 'BaseGallery'
        m2m_table_name = db.shorten_name(u'photologue_basegallery_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('basegallery', models.ForeignKey(orm[u'photologue.basegallery'], null=False)),
            ('photo', models.ForeignKey(orm[u'photologue.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['basegallery_id', 'photo_id'])


        # Changing field 'GalleryUpload.gallery'
        db.alter_column(u'photologue_galleryupload', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.BaseGallery'], null=True))

    def backwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'photologue_gallery', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50, unique=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('title_slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True)),
            ('is_public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('tags', self.gf('photologue.models.TagField')(max_length=255, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'photologue', ['Gallery'])

        # Adding M2M table for field photos on 'Gallery'
        m2m_table_name = db.shorten_name(u'photologue_gallery_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'photologue.gallery'], null=False)),
            ('photo', models.ForeignKey(orm[u'photologue.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gallery_id', 'photo_id'])

        # Deleting model 'BaseGallery'
        db.delete_table(u'photologue_basegallery')

        # Removing M2M table for field photos on 'BaseGallery'
        db.delete_table(db.shorten_name(u'photologue_basegallery_photos'))


        # Changing field 'GalleryUpload.gallery'
        db.alter_column(u'photologue_galleryupload', 'gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['photologue.Gallery'], null=True))

    models = {
        u'photologue.basegallery': {
            'Meta': {'object_name': 'BaseGallery'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'galleries'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['photologue.Photo']"}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'photologue.galleryupload': {
            'Meta': {'object_name': 'GalleryUpload'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['photologue.BaseGallery']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'zip_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'photologue.photo': {
            'Meta': {'ordering': "['-date_added']", 'object_name': 'Photo'},
            'caption': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'crop_from': ('django.db.models.fields.CharField', [], {'default': "'center'", 'max_length': '10', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_taken': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_related'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tags': ('photologue.models.TagField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'title_slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'photologue.photoeffect': {
            'Meta': {'object_name': 'PhotoEffect'},
            'background_color': ('django.db.models.fields.CharField', [], {'default': "'#FFFFFF'", 'max_length': '7'}),
            'brightness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'color': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'contrast': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'filters': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'reflection_size': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'reflection_strength': ('django.db.models.fields.FloatField', [], {'default': '0.6'}),
            'sharpness': ('django.db.models.fields.FloatField', [], {'default': '1.0'}),
            'transpose_method': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'})
        },
        u'photologue.photosize': {
            'Meta': {'ordering': "['width', 'height']", 'object_name': 'PhotoSize'},
            'crop': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'effect': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': u"orm['photologue.PhotoEffect']"}),
            'height': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'increment_count': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '40'}),
            'pre_cache': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quality': ('django.db.models.fields.PositiveIntegerField', [], {'default': '70'}),
            'upscale': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'watermark': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'photo_sizes'", 'null': 'True', 'to': u"orm['photologue.Watermark']"}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        u'photologue.watermark': {
            'Meta': {'object_name': 'Watermark'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'opacity': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'scale'", 'max_length': '5'})
        }
    }

    complete_apps = ['photologue']