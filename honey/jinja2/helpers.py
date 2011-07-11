from __future__ import absolute_import

from django.core.urlresolvers import reverse

def url_for(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)

def jinja2_helpers(request):
    print "I am updated."
    return dict(
        url_for=url_for,
        request=request
    )
