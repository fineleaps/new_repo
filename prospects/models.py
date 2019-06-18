from django.db import models


class Prospect(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=15, blank=True)
    direct_or_extension = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)
    company = models.CharField(max_length=128, blank=True)
    emp_size = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=64, blank=True)
    job_title = models.CharField(max_length=64, blank=True)
    industry_type = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def get_display_text(self):
        return self.full_name

    def __str__(self):
        return self.full_name

    @property
    def campaigns_assigned(self):
        return self.campaign_set.all()

