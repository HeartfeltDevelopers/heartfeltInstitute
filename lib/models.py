from django.db import models

# Create your models here.
class t_url(models.Model):
    title = models.CharField(max_length=20, default='', null=True, blank=True)
    category = models.CharField(max_length=20, default='', null=True, blank=True)
    url = models.CharField(max_length=30, default='', null=True, blank=True)
    status = models.CharField(max_length=20, default='', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title