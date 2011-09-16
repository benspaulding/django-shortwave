from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from shortwave.models import Wave, Command


# Inlines.

class CommandInline(admin.TabularInline):
    extra = 3
    model = Command


# Admins.

class WaveAdmin(admin.ModelAdmin):
    inlines = (CommandInline, )
    list_display = ('user', 'command_count', 'kill_defaults')
    list_filter = ('kill_defaults', )
    raw_id_fields = ('user', )
    search_fields = ('user__username', )

    def command_count(self, obj):
        return obj.commands.count()
    command_count.short_description = _(u'No. of commands')


class CommandAdmin(admin.ModelAdmin):
    list_display = ('trigger', 'description', 'wave')
    list_display_links = ('trigger', 'description')
    raw_id_fields = ('wave', )
    search_fields = ('description', 'url', 'wave__user__username')


admin.site.register(Wave, WaveAdmin)
admin.site.register(Command, CommandAdmin)
