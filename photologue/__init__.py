import os
from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

__version__ = '2.7.dev0'

PHOTOLOGUE_TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))

# Code below very much inspired by Django's own configurable user model.

def get_gallery_model():
    """Return the Gallery model that is active in this project."""
    from django.db.models import get_model

    PHOTOLOGUE_GALLERY_MODEL = getattr(settings, 'PHOTOLOGUE_GALLERY_MODEL', 'photologue.BaseGallery')
    try:
        app_label, model_name = PHOTOLOGUE_GALLERY_MODEL.split('.')
    except ValueError:
        raise ImproperlyConfigured("PHOTOLOGUE_GALLERY_MODEL must be of the form 'app_label.model_name'")
    gallery_model = get_model(app_label, model_name)
    if gallery_model is None:
        raise ImproperlyConfigured("PHOTOLOGUE_GALLERY_MODEL refers to model '%s' that has not been installed" % PHOTOLOGUE_GALLERY_MODEL)
    return gallery_model
