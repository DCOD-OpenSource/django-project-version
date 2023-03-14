A django-project-version documentation
======================================

|GitHub|_ |Coveralls|_ |pypi-license|_ |pypi-version|_ |pypi-python-version|_ |pypi-django-version|_ |pypi-format|_ |pypi-wheel|_ |pypi-status|_

    *django-project-version is a Django reusable app to show your project version*

.. contents::

Installation
------------
* Obtain your copy of source code from the git repository: ``$ git clone https://github.com/DCOD-OpenSource/django-project-version.git``. Or download the latest release from https://github.com/DCOD-OpenSource/django-project-version/tags/.
* Run ``$ python ./setup.py install`` from the repository source tree or unpacked archive. Or use pip: ``$ pip install django-project-version``.

Configuration
-------------
* Add ``"djversion"`` to ``settings.INSTALLED_APPS``.

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "djversion",
    ]

Settings
--------
``DJVERSION_VERSION``
    Contains project version. Defaults to ``None``.

``DJVERSION_UPDATED``
    Contains project update date or datetime. Defaults to ``None``.

``DJVERSION_FORMAT_STRING``
    Contains version and updated format string. Defaults to ``"{version} ({updated})"``.

``DJVERSION_GIT_REPO_PATH``
    Contains path to git repository from where version info can get. Defaults to ``None``.

``DJVERSION_GIT_USE_TAG``
    Indicate usage of git repository current tag as project version. Defaults to ``False``.

``DJVERSION_GIT_USE_COMMIT``
    Indicate usage of git repository last commit hash as project version. Defaults to ``False``.

Usage
-----
If you want always have ``"VERSION"`` variable in templates context, just add ``"djversion.context_processors.version"`` to ``settings.TEMPLATE_CONTEXT_PROCESSORS``

.. code-block:: python

    # settings.py

    TEMPLATE_CONTEXT_PROCESSORS += [
        "djversion.context_processors.version",
    ]


Or you can use ``project_version`` templatetag which can be loaded from ``djversion_tags``.

.. code-block:: django

    {# footer.html #}

    {% load djversion_tags %}

    {% project_version as VERSION %}
    {{ VERSION }}

Also simple management command ``print-version`` which prints project version to stdout is available. Just run: ``$ django-admin print-version``.

Advanced features
-----------------
If you want to have REST-style view with your project version:

* Install ``django-project-version`` with additional dependencies: ``$ pip install django-project-version[rest]``.
* Extend you ``settings.INSTALLED_APPS`` by adding ``"rest_framework"``.

.. code-block:: python

    # settings.py

    INSTALLED_APPS += [
        "rest_framework",
    ]

* Add ``"djversion"`` to your URLs definitions:

.. code-block:: python

    # urls.py

    from django.urls import re_path, include


    urlpatterns += [
        re_path(r"^version/", include("djversion.urls")),
    ]

Or to use information from the project git repository as project version:

* Install ``django-project-version`` with additional dependencies: ``$ pip install django-project-version[git]``.
* Configure git related settings.

Contributing
------------
- `Fork it <https://github.com/DCOD-OpenSource/django-project-version/>`_
- Install `GNU Make <https://www.gnu.org/software/make/>`_
- Install and configure `pyenv <https://github.com/pyenv/pyenv/>`_ and `pyenv-virtualenv plugin <https://github.com/pyenv/pyenv-virtualenv/>`_
- Install and configure `direnv <https://github.com/direnv/direnv/>`_
- Create environment config from example

.. code-block:: bash

    cp .env.example .env

- Install development dependencies:

.. code-block:: bash

    make install

- Create your fix/feature branch:

.. code-block:: bash

    git checkout -b my-new-fix-or-feature

- Check code style and moreover:

.. code-block:: bash

    make check

- Run tests:

.. code-block:: bash

    make test

- Push to the branch:

.. code-block:: bash

    git push origin my-new-fix-or-feature

- `Create a new Pull Request <https://github.com/DCOD-OpenSource/django-project-version/compare/>`_

Licensing
---------
django-project-version uses the MIT license. Please check the MIT-LICENSE file for more details.

Contacts
--------
**Project Website**: https://github.com/DCOD-OpenSource/django-project-version/

**Author**: DCOD <contact@d-cod.com>

For contributors list see CONTRIBUTORS file.


.. |GitHub| image:: https://github.com/DCOD-OpenSource/django-project-version/workflows/build/badge.svg
    :alt: GitHub
.. |Coveralls| image:: https://coveralls.io/repos/github/DCOD-OpenSource/django-project-version/badge.svg?branch=master
    :alt: Coveralls
.. |pypi-license| image:: https://img.shields.io/pypi/l/django-project-version
    :alt: License
.. |pypi-version| image:: https://img.shields.io/pypi/v/django-project-version
    :alt: Version
.. |pypi-django-version| image:: https://img.shields.io/pypi/djversions/django-project-version
    :alt: Supported Django version
.. |pypi-python-version| image:: https://img.shields.io/pypi/pyversions/django-project-version
    :alt: Supported Python version
.. |pypi-format| image:: https://img.shields.io/pypi/format/django-project-version
    :alt: Package format
.. |pypi-wheel| image:: https://img.shields.io/pypi/wheel/django-project-version
    :alt: Python wheel support
.. |pypi-status| image:: https://img.shields.io/pypi/status/django-project-version
    :alt: Package status
.. _GitHub: https://github.com/DCOD-OpenSource/django-project-version/actions/
.. _Coveralls: https://coveralls.io/github/DCOD-OpenSource/django-project-version?branch=master
.. _pypi-license: https://pypi.org/project/django-project-version/
.. _pypi-version: https://pypi.org/project/django-project-version/
.. _pypi-django-version: https://pypi.org/project/django-project-version/
.. _pypi-python-version: https://pypi.org/project/django-project-version/
.. _pypi-format: https://pypi.org/project/django-project-version/
.. _pypi-wheel: https://pypi.org/project/django-project-version/
.. _pypi-status: https://pypi.org/project/django-project-version/
