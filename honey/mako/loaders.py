"""
MakoFileSystemLoader and MakoAppDirLoader are user facing template loaders for
mako templates. 
"""
from __future__ import absolute_import

from django.template.loaders import app_directories, filesystem

from .lookup import FileSystemTemplateLookup, AppDirectoriesTemplateLookup
from .wrapper import MakoTemplate

class MakoFileSystemLoader(filesystem.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (MakoTemplate(source, template_dirs, FileSystemTemplateLookup), origin)

class MakoAppDirLoader(app_directories.Loader):
    def load_template(self, template_name, template_dirs=None):
        source, origin = self.load_template_source(template_name, template_dirs)
        return (MakoTemplate(source, template_dirs, AppDirectoriesTemplateLookup), origin)
