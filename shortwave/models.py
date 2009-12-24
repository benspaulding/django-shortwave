from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from shortwave import forms


class CommandTriggerField(models.CharField):
    """Model field for a Shortwave command trigger."""

    description = _(u'Shortwave command trigger')

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 10)
        models.CharField.__init__(self, *args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'form_class': forms.CommandTriggerField}
        defaults.update(kwargs)
        return super(CommandTriggerField, self).formfield(**defaults)


class Wave(models.Model):
    """A collection of commands relating to a user."""

    user = models.OneToOneField(User, verbose_name=_(u'user'),
        limit_choices_to={'is_active': True})
    kill_defaults = models.BooleanField(_(u'kill default commands'),
        help_text=_(u'Selecting this removes all default Shortwave commands.'))

    class Meta:
        ordering = ('user', )
        verbose_name = _(u'wave')
        verbose_name_plural = _(u'waves')

    def __unicode__(self):
        return "%s" % self.user

    @models.permalink
    def get_absolute_url(self):
        return ('shortwave-wave-detail', (), {'username': self.user})


class Command(models.Model):
    """A Shortwave command."""

    wave = models.ForeignKey(Wave, verbose_name=_(u'wave'),
        related_name='commands')
    trigger = CommandTriggerField(_(u'trigger'))
    url = models.CharField(_(u'URL'), max_length=255)
    description = models.CharField(_(u'description'), max_length=75)

    class Meta:
        ordering = ('trigger', 'wave')
        unique_together = ('trigger', 'wave')
        verbose_name = _(u'command')
        verbose_name_plural = _(u'commands')

    def __unicode__(self):
        return "%s (%s)" % (self.description, self.trigger)
