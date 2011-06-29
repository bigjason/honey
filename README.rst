============
Django Honey
============

A drop in replacement for `django templates <https://docs.djangoproject.com/en/1.3/#the-template-layer>`_ 
using `mako <http://www.makotemplates.org/>`_.

*Honey is under active development to add more features.  In its current state
it is completely usable and fairly stable as it relies heavily on the tested, tried
and true existing django loaders.  New features and bells and whistles will be added
in the near future.*

Installation
============
**Note:** Currently installation is a manual process involving downloading the code and running
``setup.py install``.  If this doesn't make sense to you then maybe wait until
an official release is completed.

Add to django settings
----------------------
You must add the loaders to your ``settings.py``::

    TEMPLATE_LOADERS = (
        'honey.template.MakoFileSystemLoader',
        'honey.template.MakoAppDirLoader'
    )

If you are still using the django templates you can leave those in the ``TEMPLATE_LOADERS``
setting, just keep in mind that the loaders are tried in order so name your 
templates wisely.

With the loaders in place you can use `mako`_ templates like usual.

Plans
=====
* Integration with django templating system. (**Done**)
* Template paths that work like the django template loader. (**Done**)
* Per app and global helpers using mako `defs <http://www.makotemplates.org/docs/defs.html>`_ and python modules.
* Integration with django caching.
* Common helpers (urls, links, pagination etc).

Change Log
==========
**v0.0.1**
    * Full drop in replacement of django templates using custom template loaders.
    * Mako ``Lookup`` classes to support inheritence and other template loading 
      from inside mako template rendering.
    * Basic tests for the template loaders.