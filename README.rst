.. django-project-version
.. README.rst

A django-project-version documentation
======================================

    *django-project-version is a django reusable app to show your project version*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``git clone https://github.com/DCOD-OpenSource/django-project-version.git``. Or download the latest release from https://github.com/DCOD-OpenSource/django-project-version/tags/.
* Run ``python ./setup.py install`` from repository source tree or unpacked archive. Or use pip: ``pip install django-project-version``.

Configuration
-------------
Add ``"djversion"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS += (
        "djversion",
    )


Settings
--------
``DJVERSION_VERSION``
    Contains project version. Defaults to ``None``.

``DJVERSION_UPDATED``
    Contains project update date or datetime. Defaults to ``None``.

``DJVERSION_FORMAT_STRING``
    Contains version and updated format string. Defaults to ``"{version} ({updated})"``.

Usage
-----
If you want always have ``VERSION`` variable in templates context, just add ``"djversion.context_processors.version"`` to ``settings.TEMPLATE_CONTEXT_PROCESSORS``

.. code-block:: python

    TEMPLATE_CONTEXT_PROCESSORS += (
        "djversion.context_processors.version",
    )


Or you can use ``project_version`` assignment templatetag which can be loaded from ``djversion_tags``.

For example:

.. code-block:: django

    {% load djversion_tags %}

    {% project_version as VERSION %}
    {{ VERSION }}


Licensing
---------
django-project-version uses the MIT license. Please check the MIT-LICENSE file for more details.

Contacts
--------
**Project Website**: https://github.com/DCOD-OpenSource/django-project-version/

**Author**: Alexei Andrushievich <vint21h@vint21h.pp.ua>

For other authors list see AUTHORS file.
