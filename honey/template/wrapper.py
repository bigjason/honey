"""
MakoTemplate is a django friendly wrapper for the mako Template objects.
"""

from django.template.context import BaseContext

from mako.template import Template

class MakoTemplate(object):
    """Represents a Mako template to the django template system.
    """
    def __init__(self, source, template_dirs, lookup):
        extra_dirs = template_dirs or ()
        lookup = lookup(extra_dirs)
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
