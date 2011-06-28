"""
The lookups are used internally by mako to find templates during includes, 
namespace etc.
"""
from os import path

from django.conf import settings
from django.template import TemplateDoesNotExist
from django.template.loaders import app_directories

from mako.template import Template
from mako.lookup import TemplateCollection

class DjangoMakoTemplateLookupBase(TemplateCollection):
    def __init__(self, extra_folders=()):
        self.extra_folders = tuple(extra_folders)

    def get_template(self, uri, relativeto=None):
        for folder in self.folders + self.extra_folders:
            file_name = path.join(folder, uri)
            if path.exists(file_name):
                return Template(filename=file_name, lookup=self)
        else:
            raise TemplateDoesNotExist(uri)

class FileSystemTemplateLookup(DjangoMakoTemplateLookupBase):
    """Mako template lookup that emulates the filesystem django template loader.
    """
    folders = tuple(settings.TEMPLATE_DIRS)

class AppDirectoriesTemplateLookup(DjangoMakoTemplateLookupBase):
    """Mako template lookup that emulates the filesystem app_directories 
    template loader.
    """
    folders = app_directories.app_template_dirs
