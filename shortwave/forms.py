import re

from django.forms.fields import RegexField
from django.utils.translation import ugettext_lazy as _


# Match any number of alpha-numeric characters or a single `*` character.
trigger_re = re.compile(r'^(?:(?:\w)+|(?:\*)?)$')

class CommandTriggerField(RegexField):
    """
    Form field for a Shortwave command trigger.

    Valid values are any number of alpha-numeric characters or `*`.

    """

    default_error_messages = {
        'invalid': _(u'Enter a valid trigger.'),
    }

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        RegexField.__init__(self, trigger_re, max_length, min_length, *args,
                            **kwargs)
