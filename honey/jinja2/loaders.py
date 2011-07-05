"""
Jinja2FileSystemLoader and Jinja2AppDirLoader are user facing template loaders for
jinja2 templates.
"""
from __future__ import absolute_import

from os import path

from django.template.loaders import app_directories
from django.template.loader import BaseLoader
from django.conf import settings
from jinja2 import FileSystemLoader, Environment

from .wrapper import Jinja2Template

## Settings from django ##
JINJA2_USE_FILESYSTEM = getattr(settings, 'HONEY_JINJA2_USE_FILESYSTEM', True)
JINJA2_USE_APP_DIRECTORIES = getattr(settings,
                                     'HONEY_JINJA2_USE_APP_DIRECTORIES', True)
JINJA2_ENVIRONMENT = {'auto_reload': True}
JINJA2_ENVIRONMENT.update(getattr(settings, 'JINJA2_ENVIRONMENT', {}))

## Internal Jinja2 Environment Setup ##

folders = []
if JINJA2_USE_FILESYSTEM:
    folders += settings.TEMPLATE_DIRS
if JINJA2_USE_APP_DIRECTORIES:
    folders += app_directories.app_template_dirs

internal_loader = FileSystemLoader(searchpath=folders)
env = Environment(loader=internal_loader)

## Django Loaders ##

class Loader(BaseLoader):
    is_usable = True

    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (Jinja2Template(source, template_dirs, env), origin)

    def load_template_source(self, template_name, template_dirs=None):
        for folder in folders:
            name = path.join(folder, template_name)
            if path.exists(name):
                with open(name, 'r') as f:
                    source = f.read()
                return (source, name)
            # No template found
        raise TemplateDoesNotExist(template_name)
