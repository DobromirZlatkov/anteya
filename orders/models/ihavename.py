from django.db import models


# Create your models here.
class IHaveName(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name
