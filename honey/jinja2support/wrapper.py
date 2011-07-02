from honey.utils import context_to_dict

class Jinja2Template(object):
    def __init__(self, source, template_dirs, enviorment):
        self.template = enviorment.from_string(source)

    def render(self, context):
        jinja_context = context_to_dict(context)
        return self.template.render(**jinja_context)
