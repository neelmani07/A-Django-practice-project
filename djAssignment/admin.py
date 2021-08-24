from django.contrib import admin
from django.db import models

from .models import Page,Compo, PageCompoMap

class CompoAdmin(admin.ModelAdmin):
    model = Compo
    list_display = ['type_of_compo', 'val' , 'style' , 'nodes']

class CompoTabularInline(admin.TabularInline):
    model = Compo

class PageAdmin(admin.ModelAdmin):
    inlines = [CompoTabularInline]
    model = Page
    list_display = ['name']

class PageCompoMapAdmin(admin.ModelAdmin):
#    inlines = [CompoTabularInline]
    model = PageCompoMap
    list_display = ['date','page','compo']

admin.site.register(Page, PageAdmin)
admin.site.register(Compo, CompoAdmin)
admin.site.register(PageCompoMap, PageCompoMapAdmin)


