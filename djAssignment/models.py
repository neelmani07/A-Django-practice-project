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

    type_of_compo = models.CharField(max_length=50,validators=[validate_type_of_icons])
    val = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    nodes = models.CharField(max_length=50, default="systems")
    pageAssigned = models.ForeignKey('Page',on_delete=CASCADE, blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.nodes = "system"
        try:
            Compo.full_clean(self)
        except ValidationError as e:
            pass
        super(Compo, self).save(*args, **kwargs)

    def __str__(self):
        return self.type_of_compo+"  "+self.val+"  "+self.style

class Page(models.Model):

    component = models.ManyToManyField('Compo', through='PageCompoMap')
    name = models.CharField(max_length=50, default= 'Thank you')

    def __str__(self):
       return "page name="+self.name
       


class PageCompoMap(models.Model):
    page = models.ForeignKey('Page', on_delete=CASCADE)
    compo = models.ForeignKey(Compo, on_delete=CASCADE)
    date = models.CharField(max_length=100)
    time_field = models.TimeField(null=True, blank=True)
    
    def __str__(self):
        return "{}_{}".format(self.page.__str__(), self.compo.__str__())


