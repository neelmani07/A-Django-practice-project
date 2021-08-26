from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_type_of_icons(value):
        list_type = ['icon','image','heading','body','link']
        if value not in list_type:
            raise ValidationError(
                _('not one of the icon types. must be from %s'%(list_type).__str__())
            )
class Compo(models.Model):

    ICON = 'ic'
    IMAGE = 'im'
    HEADING ='h'
    BODY = 'b'
    LINK = 'l'

    CHOICES = [
        (ICON, _('icons')),
        (IMAGE, _('image')),
        (HEADING, _('heading')),
        (BODY, _('body')),
        (LINK, _('link')),
    ]

    type_of_compo = models.CharField(max_length=50,choices=CHOICES) # choices 
    val = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    nodes = models.CharField(max_length=50, default="systems")
    pageAssigned = models.ForeignKey('PageCompoMap',on_delete=CASCADE, blank=True, null=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['type_of_compo', 'val', 'style'], name='uniqueComponents')
        ]

    def save(self, *args, **kwargs):
        self.nodes = "system"
        #try:
        #    Compo.full_clean(self)
        #except ValidationError as e:
        #    pass
        super(Compo, self).save(*args, **kwargs)

    def __str__(self):
        return self.type_of_compo+"  "+self.val+"  "+self.style

class Page(models.Model):
    section = models.IntegerField()
    component = models.ManyToManyField('Compo', through='PageCompoMap')
    name = models.CharField(max_length=50, default= 'Thank you')
    id= models.AutoField(primary_key=True, null=False)
    #class Meta:
    #    unique_together = (("name", "section"),)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['section', 'name'], name='uniquePages')
        ]
    def __str__(self):
       return "page name="+self.name+ "  section="+self.section.__str__()
       


class PageCompoMap(models.Model):
    page = models.ForeignKey('Page', on_delete=CASCADE)
    component = models.ForeignKey('Compo', on_delete=CASCADE)
    #section
    date = models.CharField(max_length=100)
    time_field = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return "{}_{}".format(self.page.__str__(), self.component.__str__())


