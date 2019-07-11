from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify


class Client(models.Model):

    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True)
    director = models.CharField(max_length=64)
    company = models.CharField(max_length=128, blank=True)
    email = models.EmailField(blank=True)
    email2 = models.EmailField(blank=True)
    phone = models.CharField(max_length=15, blank=True)
    phone2 = models.CharField(max_length=15, blank=True)
    emp_size = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=64, blank=True)
    industry_type = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    details = models.TextField(blank=True)

    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_display_text(self):
        return self.name

    @property
    def get_campaigns(self):
        return self.campaign_set.all()

    @property
    def get_active_campaigns(self):
        return self.campaign_set.filter(is_active=True)


    @property
    def get_admin_absolute_url(self):
        return reverse_lazy("crm_admin:client_detail", kwargs={'slug': self.slug})

    @property
    def get_admin_update_url(self):
        return reverse_lazy("crm_admin:client_update", kwargs={'slug': self.slug})

    @property
    def get_admin_delete_url(self):
        return reverse_lazy("crm_admin:client_delete", kwargs={'slug': self.slug})


def assign_slug(sender, instance, *args, **kwargs):
    slug_text = slugify(instance.name)
    if instance.slug != slug_text:
        instance.slug = slug_text
        instance.save()


post_save.connect(assign_slug, sender=Client)
