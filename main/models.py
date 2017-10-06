from django.db import models
from datetime import datetime


class BaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    class Meta:
        abstract = True


class Organization(BaseModel):

    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(blank=False)
    parent_organization = models.ForeignKey('Organization', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        def get_full_name(Organization):
            if Organization.parent_organization:
                return get_full_name(Organization.parent_organization) + ' — ' + Organization.name
            else:
                return Organization.name
        return get_full_name(self)


class Host(BaseModel):

    titles = [('Dr', 'Docteur')]
    title = models.CharField(blank=True, null=True, max_length=30, choices=titles)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(blank=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        elif self.first_name and self.title:
            return self.title + ' ' + self.first_name + ' ' + self.last_name
        else:
            return self.last_name


class Appointment(BaseModel):

    scheduled_time = models.TimeField()
    pickup_time = models.TimeField()
    host = models.ForeignKey('Host', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.host) + ' — ' + str(self.scheduled_time)
