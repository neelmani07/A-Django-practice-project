from django.db import models

class Compo(models.Model):
    type = models.CharField(max_length=50)
    val = models.CharField(max_length=50)
    style = models.CharField(max_length=50)

    def __str__(self):
        return self.type,self.val,self.style

class Page(models.Model):
    sections = models.IntegerField(default=0)
    compo =models.ForeignKey(Compo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sections,self.compo


