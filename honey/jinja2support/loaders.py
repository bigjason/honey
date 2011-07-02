"""
MakoFileSystemLoader and MakoAppDirLoader are user facing template loaders for
mako templates. 
"""
from django.template.loaders import app_directories, filesystem
from django.conf import settings
from jinja2 import FileSystemLoader, Environment

from .wrapper import Jinja2Template

## Internal Jinja2 Enviormenet Setup ##

fs_loader = FileSystemLoader(searchpath=settings.TEMPLATE_DIRS)
app_loader = FileSystemLoader(searchpath=app_directories.app_template_dirs)

fs_env = Environment(loader=fs_loader)
app_env = Environment(loader=app_loader)

## Django Loaders ##

class Jinja2FileSystemLoader(filesystem.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (Jinja2Template(source, template_dirs, fs_env), origin)

class Jinja2AppDirLoader(app_directories.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (Jinja2Template(source, template_dirs, app_env), origin)
