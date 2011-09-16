.. _installation:

Installation
============

Requirements
------------

``django-shortwave`` requires Python 2.4 or newer and a functional
installation of Django 1.2 or newer. Further, the Django admin must be
installed. (It most likely is.)


The Package
-----------

To install this package, run the following command at the root of the
package directory::

    python setup.py install

If you have the Python ``pip`` utility available, you can
also type the following to download and install in one step::

    pip install django-shortwave

Or if you prefer using ``easy_install``::

    easy_install django-shortwave

Or if you’d prefer you can simply place the included ``shortwave``
directory somewhere on your Python path, or symlink to it from
somewhere on your Python path; this is useful if you’re working from a
Git checkout. (Source code is on GitHub_.)

.. _GitHub: https://github.com/benspaulding/django-shortwave/

You can now install the app in your Django project.


The App
-------

First, add ``shortwave`` to your ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        …
        'django.contrib.admin',
        'shortwave',
        …
    )

Next, add ``shortwave.urls`` to your ``urlpatterns``::

    urlpatterns = patterns('',
        …
        (r'^admin/', include(admin.site.urls)),
        (r'^shortwave/', include('shortwave.urls')),
        …
    )

Finally, add the appropriate tables to your database by running the Django
``syncdb`` management command.
