"""
To use, add the following to the sitemap definition section of your project's
urls.py:

...
from photologue.sitemaps import PhotologueSitemap

sitemaps = {...
            'photologue': PhotologueSitemap
            ...
            }
etc...

"""

from django.contrib.sitemaps import Sitemap

from photologue import get_gallery_model
from photologue.models import Photo

Gallery = get_gallery_model()

class PhotologueSitemap(Sitemap):
    priority = 0.5

    def items(self):
        # The following code is very basic and will probably cause problems with
        # large querysets.
        return list(Gallery.objects.filter(is_public=True)) \
                                    + list(Photo.objects.filter(is_public=True))

    def lastmod(self, obj):
            return obj.date_added


