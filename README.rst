============
Django Honey
============

A drop in replacement for `django templates <https://docs.djangoproject.com/en/1.3/#the-template-layer>`_ 
using `jinja2 <http://jinja.pocoo.org/>`_ or `mako <http://www.makotemplates.org/>`_.

*Honey is under active development to add more features.  In its current state
it is completely usable and fairly stable as it relies heavily on the tested, tried
and true existing django loaders.  New features and bells and whistles will be added
in the near future.*

Installation
============
**Note:** Currently installation is a manual process involving downloading the code and running
``setup.py install``.  If this doesn't make sense to you then maybe wait until
an official release is completed.

Jinja2
------
Install the template loader in your django project, by updating your
``TEMPLATE_LOADERS`` with the jinja2 loader like this::

    TEMPLATE_LOADERS = (
        'honey.jinja2.Loader',
    )

You can leave the django loaders in place, just mind the order of the loaders
as the first match will always win.

Settings
^^^^^^^^
The following are settings are checked, but not required. Place them in the
django project settings (usually settings.py).

=========================== ======== ====================================================================
Setting Name                Default  Explanation
=========================== ======== ====================================================================
JINJA2_USE_FILESYSTEM       True     Look in all the folders listed in
                                     ``TEMPLATE_LOADERS`` for templates.
JINJA2_USE_APP_DIRECTORIES  True     Look in all apps ``templates`` folders.
JINJA2_ENVIRONMENT          {}       A dict with all environment settings to pass to the jinja
                                     `Environment <http://jinja.pocoo.org/docs/api/#jinja2.Environment>`_
                                     object.
=========================== ======== ====================================================================

Url/Reverse
^^^^^^^^^^^
Right now there are no custom tags.  However there is a ``url_for`` function
always available in scope.  It is a based on the ``url`` template tag and can be
used in a simalar way::

    <a href='{{ url_for('home_view') }}'>Home</a>

**More helpers and template tags are coming.**

Mako
----
*Mako support is planned to be removed from honey.*

Be sure that you have installed the mako package. You must add the loaders to 
your ``settings.py``::

    TEMPLATE_LOADERS = (
        'honey.MakoFileSystemLoader',
        'honey.MakoAppDirLoader'
    )

If you are still using the django templates you can leave those in the ``TEMPLATE_LOADERS``
setting, just keep in mind that the loaders are tried in order so name your 
templates wisely.

With the loaders in place you can use `mako`_ templates like you would django
templates.

Plans
=====
* Integration with django templating system. (**Done**)
* Template paths that work like the django template loader. (**Done**)
* Common helpers (urls, humanize, loremipsum etc) available in a context manager.
* Html helpers (links, forms etc) available in a context manager.
* Integration with django caching.

Change Log
==========
**v0.0.1**
    * Full drop in replacement of django templates using custom template loaders
      for mako.
    * Mako ``Lookup`` classes to support inheritance and other template loading
      from inside template rendering.
    * Basic tests for the template loaders.
