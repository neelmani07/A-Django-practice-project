from django.contrib import admin
from django.db import models

from .models import Page,Compo, PageCompoMap

class CompoAdmin(admin.ModelAdmin):
    model = Compo
    list_display = ['type_of_compo', 'val' , 'style' , 'nodes']

class CompoTabularInline(admin.TabularInline):
    model = Compo

class PageAdmin(admin.ModelAdmin):
    #inlines = [CompoTabularInline]
    model = Page
    list_display = ['name','section']

class PageCompoMapAdmin(admin.ModelAdmin):
#    inlines = [CompoTabularInline]
    model = PageCompoMap
    list_display = ['time_field','date','page','component']

admin.site.register(Page, PageAdmin)
admin.site.register(Compo, CompoAdmin)
admin.site.register(PageCompoMap, PageCompoMapAdmin)


