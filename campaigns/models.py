from django.db import models
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from django.http import HttpResponse
from results.models import Result
from django.urls import reverse_lazy
from clients.models import Client


class Campaign(models.Model):

    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=64)
    aim = models.CharField(max_length=128, blank=True)
    slug = models.SlugField(blank=True)
    is_active = models.BooleanField(default=True)
    script = models.TextField(blank=True)
    details = models.TextField(blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    executives = models.ManyToManyField('portal.User', blank=True)
    prospects = models.ManyToManyField('prospects.Prospect', blank=True, through='ProspectCampaignRelation')

    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def get_active_status(self):
        return "Active" if self.is_active else "Not Active"

    @property
    def get_executives(self):
        return self.executives.all()

    @property
    def get_client(self):
        return self.client

    @property
    def get_client_display_text(self):
        return self.client.get_display_text

    @property
    def get_aim(self):
        if self.aim:
            return self.aim
        else:
            return "--"

    @property
    def get_short_form(self):
        return self.name[:15]

    @property
    def get_display_text(self):
        return self.name

    @property
    def get_admin_absolute_url(self):
        return reverse_lazy("crm_admin:campaign_detail", kwargs={'slug': self.slug})

    @property
    def get_admin_update_url(self):
        return reverse_lazy("crm_admin:campaign_update", kwargs={'slug': self.slug})

    @property
    def get_admin_delete_url(self):
        return reverse_lazy("crm_admin:campaign_delete", kwargs={'slug': self.slug})

    @property
    def get_absolute_url(self):
        return reverse_lazy("portal:campaign_detail", kwargs={'slug': self.slug})


    @property
    def prospects_attempted(self):
        return self.prospects.filter(prospectcampaignrelation__attempted=True)

    @property
    def prospects_non_attempted(self):
        return self.prospects.filter(prospectcampaignrelation__attempted=False)

    @property
    def prospect_get(self):
        f_prospect = self.prospects_non_attempted.first()
        if f_prospect:
            f_prospect.prospectcampaignrelation.make_attempted()
            return f_prospect
        else:
            return False

    @property
    def get_all_leads(self):
        return Result.objects.filter(prospect_campaign_relation__campaign=self, result_choice="Lead")

    @property
    def get_all_views(self):
        return Result.objects.filter(prospect_campaign_relation__campaign=self, result_choice="View")

    @property
    def get_all_dncs(self):
        return Result.objects.filter(prospect_campaign_relation__campaign=self, result_choice="DNC")


def assign_slug(sender, instance, *args, **kwargs):
    slug_text = slugify(instance.name)
    if instance.slug != slug_text:
        instance.slug = slug_text
        instance.save()


pre_save.connect(assign_slug, sender=Campaign)


class ProspectCampaignRelation(models.Model):
    prospect = models.OneToOneField('prospects.Prospect', on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    from_date = models.DateField(auto_now_add=True)
    attempted = models.BooleanField(default=False)
    details = models.TextField(blank=True)

    def __str__(self):
        return "{} -- {}".format(self.prospect, self.campaign)

    def make_attempted(self):
        self.attempted = True
        self.save()
        """ Remember to use .filter with update method if this got slow"""

    class Meta:
        unique_together = ('prospect', 'campaign')
