from django.views.generic.list_detail import object_list, object_detail

from shortwave.models import Wave, Command


def wave_list(request):
    """
    A list view of all shortwaves.

    Templates:
        :template:`shortwave/wave_list.html`
    Context:
        wave_list
            A list of :model:`shortwave.Wave` objects.

    """
    return object_list(request, queryset=Wave.objects.all(), paginate_by=50,
        template_object_name='wave')


def wave_detail(request, username):
    """
    A custom command file for use with Shortwave.

    This view returns a custom command file to be used in conjunction with
    `Shaun Inman`_'s Shortwave_ service.

    .. _Shaun Inman: http://shauninman.com/
    .. _Shortwave: http://shortwaveapp.com/

    Templates:
        :template:`shortwave/wave_detail.txt`
    Context:
        wave
            A :model:`shortwave.Wave` object.
        command_list
            A list of all :model:`shortwave.Command` objects related
            to ``wave``.

    """
    extra_context = {
        'command_list': Command.objects.filter(wave__user__username=username),
    }

    return object_detail(request, queryset=Wave.objects.all(),
        extra_context=extra_context, mimetype='text/plain; charset=utf-8',
        slug=username, slug_field='user__username',
        template_object_name='wave', template_name='shortwave/wave_detail.txt')
