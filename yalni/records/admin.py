from django.contrib import admin

from .models import Assembled

class AssembledAdmin(admin.ModelAdmin):
    list_display = ['customer', 'chasis', 'motherboard', 'configuration', 'entered']
admin.site.register(Assembled, AssembledAdmin)
