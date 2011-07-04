"""
Jinja2FileSystemLoader and Jinja2AppDirLoader are user facing template loaders for
jinja2 templates.
"""
from __future__ import absolute_import

from django.template.loaders import app_directories, filesystem
from django.conf import settings
from jinja2 import FileSystemLoader, Environment

from .wrapper import Jinja2Template

## Settings from django ##
JINJA2_USE_FILESYSTEM = getattr(settings, 'HONEY_JINJA2_USE_FILESYSTEM', True)
JINJA2_USE_APP_DIRECTORIES = getattr(settings, 'HONEY_JINJA2_USE_APP_DIRECTORIES',
                                          True)
JINJA2_ENVIRONMENT = getattr(settings, 'JINJA2_ENVIRONMENT', {})
JINJA2_ENVIRONMENT.update({'auto_reload': True})

## Internal Jinja2 Environment Setup ##

dirs = []
if JINJA2_USE_FILESYSTEM:
    dirs += settings.TEMPLATE_DIRS
if JINJA2_USE_APP_DIRECTORIES:
    dirs += app_directories.app_template_dirs
internal_loader = FileSystemLoader(searchpath=dirs)
env = Environment(loader=internal_loader)

## Django Loaders ##

class Loader(filesystem.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (Jinja2Template(source, template_dirs, env), origin)
