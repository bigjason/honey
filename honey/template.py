from os import path

from django.conf import settings
from django.template import TemplateDoesNotExist, Context
from django.template.context import BaseContext
from django.core.urlresolvers import reverse
from django.template.loaders import app_directories, filesystem

from mako.template import Template
from mako.lookup import TemplateCollection

class DjangoMakoTemplateLookup(TemplateCollection):
    """Mako template lookup that emulates the filesystem django template loader.
    """
    def __init__(self, extra_folders=()):
        self.extra_folders = tuple(extra_folders)
    
    def get_template(self, uri, relativeto=None):
        for folder in tuple(settings.TEMPLATE_DIRS) + self.extra_folders:
            file_name = path.join(folder, uri)
            if path.exists(file_name):
                return Template(filename=file_name, lookup=self)
        else:
            raise TemplateDoesNotExist(uri)

class MakoTemplate(object):
    """Represents a Mako template to the django template system.
    """
    def __init__(self, source, template_dirs):
        extra_dirs = template_dirs or ()
        lookup = DjangoMakoTemplateLookup(extra_dirs)
        self.template = Template(text=source, lookup=lookup)
    
    def render(self, context):
        mako_context = self.context_to_dict(context)
        return self.template.render(**mako_context)

    @staticmethod
    def context_to_dict(context):
        result = {}
        if isinstance(context, BaseContext):
            for d in context:
                result.update(d)
        elif isinstance(context, dict):
            result.update(context)
        return result

class MakoFileSystemLoader(filesystem.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (MakoTemplate(source, template_dirs), origin)

class MakoAppDirLoader(app_directories.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (MakoTemplate(source, template_dirs), origin)
