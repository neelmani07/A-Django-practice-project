from django.contrib import admin
from django.db import models
from .models import Page,Compo, PageCompoMap

class PageAdmin(admin.ModelAdmin):
    model = Page
    list_display = ['name']

class CompoAdmin(admin.ModelAdmin):
    model = Compo
    list_display = ['type_of_compo', 'val' , 'style']

admin.site.register(Page, PageAdmin)
admin.site.register(Compo, CompoAdmin)
admin.site.register(PageCompoMap)

