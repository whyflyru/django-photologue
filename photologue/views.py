#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.views.generic.dates import ArchiveIndexView, DateDetailView, DayArchiveView, MonthArchiveView, YearArchiveView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from photologue import get_gallery_model
from photologue.models import Photo

Gallery = get_gallery_model()


class PhotoView(object):
    queryset = Photo.objects.filter(is_public=True)

class PhotoListView(PhotoView, ListView):
    paginate_by = 20

class PhotoDetailView(PhotoView, DetailView):
    slug_field = 'title_slug'

class PhotoDateView(PhotoView):
    date_field = 'date_added'

class PhotoDateDetailView(PhotoDateView, DateDetailView):
    slug_field = 'title_slug'

class PhotoArchiveIndexView(PhotoDateView, ArchiveIndexView):
    pass

class PhotoDayArchiveView(PhotoDateView, DayArchiveView):
    pass

class PhotoMonthArchiveView(PhotoDateView, MonthArchiveView):
    pass

class PhotoYearArchiveView(PhotoDateView, YearArchiveView):
    pass

#gallery Views
class GalleryView(object):
    queryset = Gallery.objects.filter(is_public=True)
    template_name = 'photologue/gallery_archive.html'

class GalleryListView(GalleryView, ListView):
    paginate_by = 1
    template_name = 'photologue/gallery_list.html'

class GalleryDetailView(GalleryView, DetailView):
    slug_field = 'title_slug'
    template_name = 'photologue/gallery_detail.html'

class GalleryDateView(GalleryView):
    date_field = 'date_added'
    template_name = 'photologue/gallery_detail.html'

class GalleryDateDetailView(GalleryDateView, DateDetailView):
    slug_field = 'title_slug'
    template_name = 'photologue/gallery_detail.html'

class GalleryArchiveIndexView(GalleryDateView, ArchiveIndexView):
    template_name = 'photologue/gallery_archive.html'

class GalleryDayArchiveView(GalleryDateView, DayArchiveView):
    template_name = 'photologue/gallery_archive_day.html'

class GalleryMonthArchiveView(GalleryDateView, MonthArchiveView):
    template_name = 'photologue/gallery_archive_month.html'

class GalleryYearArchiveView(GalleryDateView, YearArchiveView):
    template_name = 'photologue/gallery_archive_year.html'

