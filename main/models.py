from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(blank=False)
    parent_organization = models.ForeignKey('Organization', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.parent_organization:
            return self.parent_organization.name + ' — ' + self.name
        else:
            return self.name


class Host(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(blank=False)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        if self.first_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.last_name


class Appointment(models.Model):
    scheduled_time = models.TimeField()
    pickup_time = models.TimeField(auto_now_add=True)
    host = models.ForeignKey('Host', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.scheduled_time)
