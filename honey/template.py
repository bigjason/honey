from os import path
from xml.sax.saxutils import escape, quoteattr

from django.conf import settings
from django.http import HttpResponse
from django.template import TemplateDoesNotExist, Context
from django.template.context import BaseContext
from django.core.urlresolvers import reverse

from mako.template import Template
from mako.lookup import TemplateCollection

class DjangoTemplateLookup(TemplateCollection):
    def get_template(self, uri, relativeto=None):
        for folder in settings.TEMPLATE_DIRS:
            file_name = path.join(folder, uri)
            if path.exists(file_name):
                return Template(filename=file_name, lookup=self)
        else:
            raise TemplateDoesNotExist()
lookup = DjangoTemplateLookup()

def context_to_dict(dictionary):
    result = {}
    if isinstance(dictionary, BaseContext):
        for d in dictionary:
            result.update(d)
    elif isinstance(dictionary, dict):
        result.update(dictionary)
    return result

def render_to_string(template_name, dictionary=None, context_instance=None):
    dictionary = dictionary if dictionary != None else {}
    if context_instance is None:
        context_instance = Context(dictionary)
    else:
        context_instance.update(dictionary)

    mako_context = context_to_dict(dictionary)
    #for ctx_dict in context_instance:
    #    mako_context.update(ctx_dict)

    mako_context['url'] = mako_reverse
    mako_context['link'] = link

    template = lookup.get_template(template_name)

    return template.render(**mako_context)

def render_to_response(template_name, dictionary=None, context_instance=None, mimetype='text/html'):
    return HttpResponse(render_to_string(template_name=template_name, 
                                         dictionary=dictionary, 
                                         context_instance=context_instance),
                        mimetype=mimetype)

def mako_reverse(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)

def link(name, label, *args, **kwargs):
    attrs = ""
    return '<a href="{}"/>{}</a>'.format(mako_reverse(name, *args), label)
