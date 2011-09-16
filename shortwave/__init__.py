"""
=================================================
 Django app for managing Shortwave command files
=================================================

This application provides the ability for users to create and manage
custom command files for use with Shortwave_.

Using the instructions found in the `default commands file`_, users can add
their own commands to a custom wave file. They can then provide the URL of
their custom commands file to Shortwave_ and save their new bookmarklet.

From that point users can add, delete, and change their custom commands from a
Web interface and their bookmarklet updates immediately (that's the beauty of
Shortwave_).

Refer to the documentation_ for further information.

.. _Shortwave: http://shortwaveapp.com/
.. _default commands file: http://shortwaveapp.com/waves.txt
.. _Django: http://www.djangoproject.com/
.. _documentation: http://readthedocs.org/docs/django-shortwave/

"""

from django.utils.translation import ugettext_lazy as _


VERSION = '0.9.1'

# Mark the app_label for translation.
_(u'shortwave')
