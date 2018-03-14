from django.contrib import admin

from .forms import SpecialForm
from .settings import EXPOSE_MODEL_TO_ADMIN


if EXPOSE_MODEL_TO_ADMIN:
    from .models import Preference

    class PreferenceAdmin(admin.ModelAdmin):

        list_display = ('app', 'name')
        search_fields = ['app', 'name']
        list_filter = ['app']
        ordering = ['app', 'name']
        form = SpecialForm


    admin.site.register(Preference, PreferenceAdmin)
