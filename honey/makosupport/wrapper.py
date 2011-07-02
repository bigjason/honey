"""
MakoTemplate is a django friendly wrapper for the mako Template objects.
"""
from mako.template import Template

from honey.utils import context_to_dict

class MakoTemplate(object):
    """Represents a Mako template to the django template system.
    """
    def __init__(self, source, template_dirs, lookup):
        extra_dirs = template_dirs or ()
        lookup = lookup(extra_dirs)
        self.template = Template(text=source, lookup=lookup)

    def render(self, context):
        mako_context = context_to_dict(context)
        return self.template.render(**mako_context)

