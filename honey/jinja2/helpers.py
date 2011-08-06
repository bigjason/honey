from __future__ import absolute_import
import os
import posixpath
from os import path

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.finders import find as static_files_find

from .exceptions import StaticFileNotFoundError

def url_for(name, *args, **kwargs):
    return reverse(name, args=args, kwargs=kwargs)


def link(name, text, *args, **kwargs):
    return '<a href="{0}">{1}</a>'.format(reverse(name, *args, **kwargs), text)


def static_url(name):
    file_path = static_files_find(posixpath.normpath(name))
    if not file_path or not path.exists(file_path):
        raise StaticFileNotFoundError(
            "Could not find the static file '{0}'.".format(file_path or "")
        )

    return u"{0}{1}?b={2}".format(
        settings.STATIC_URL,
        name,
        int(os.stat(file_path).st_mtime)
    )


def javascript(name):
    return '<script src="{0}" type="text/javascript"></script>'.format(
        static_url(name)
    )


def css(name):
    return '<link rel="stylesheet" href="{0}" type="text/css" />'.format(
        static_url(name)
    )


def img(name, alt=""):
    return '<img src="{0}" alt="{1}" />'.format(name, alt)


def jinja2_helpers(request):
    return dict(
        request=request,
        settings=settings,
        url_for=url_for,
        link=link,
        static_url=static_url,
        javascript=javascript,
        css=css
    )
