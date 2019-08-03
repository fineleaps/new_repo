from django.db import models
from django.urls import reverse_lazy
from django.db.models.signals import post_save


class Prospect(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    phone = models.CharField(max_length=15, blank=True)
    direct_or_extension = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=64, blank=True)
    company = models.CharField(max_length=128, blank=True)
    emp_size = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=64, blank=True)
    industry_type = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=32, blank=True)
    state = models.CharField(max_length=32, blank=True)
    country = models.CharField(max_length=32, blank=True)
    zip_code = models.CharField(max_length=12, blank=True, null=True)
    details = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def get_admin_update_url(self):
        return reverse_lazy("crm_admin:prospect_update", kwargs={"id": self.id})

    @property
    def get_admin_delete_url(self):
        return reverse_lazy("crm_admin:prospect_delete", kwargs={"id": self.id})

    @property
    def is_campaign_attempted(self):
        return self.prospectcampaignrelation.attempted

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


class ProspectUpdate(models.Model):

    prospect_campaign_relation = models.ForeignKey("campaigns.ProspectCampaignRelation", on_delete=models.CASCADE)
    by = models.ForeignKey("portal.User", on_delete=models.CASCADE)

    phone = models.CharField(max_length=15, blank=True)
    direct_or_extension = models.CharField(max_length=16, blank=True)
    email = models.EmailField(blank=True)
    job_title = models.CharField(max_length=64, blank=True)
    company = models.CharField(max_length=128, blank=True)
    emp_size = models.CharField(max_length=16, blank=True)
    website = models.CharField(max_length=64, blank=True)
    industry_type = models.CharField(max_length=64, blank=True)

    is_approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.by.get_display_text, self.prospect_campaign_relation.prospect.get_display_text)

    def approve_updates(self):
        prospect = self.prospect_campaign_relation.prospect
        if self.phone:
            prospect.phone = self.phone
        if self.direct_or_extension:
            prospect.direct_or_extension = self.direct_or_extension
        if self.job_title:
            prospect.job_title = self.job_title
        if self.company:
            prospect.company = self.company
        if self.email:
            prospect.email = self.email
        if self.industry_type:
            prospect.industry_type = self.industry_type
        if self.website:
            prospect.website = self.website
        if self.emp_size:
            prospect.emp_size = self.emp_size
        prospect.save()

    def decline_updates(self):
        self.delete()

    @property
    def get_admin_update_url(self):
        return reverse_lazy("crm_admin:prospect_update_update", kwargs={"id": self.id})

    @property
    def get_admin_delete_url(self):
        return reverse_lazy("crm_admin:prospect_update_delete", kwargs={"id": self.id})


def check_updates(instance, sender, created, *args, **kwargs):
    if created:
        prospect = instance.prospect_campaign_relation.prospect
        to_be_approved = False
        if not prospect.phone:
            prospect.phone = instance.phone
        elif prospect.phone != instance.phone:
            to_be_approved = True
        if not prospect.direct_or_extension:
            prospect.direct_or_extension = instance.direct_or_extension
        elif prospect.direct_or_extension != instance.direct_or_extension:
            to_be_approved = True
        if not prospect.email:
            prospect.email = instance.email
        elif prospect.email != instance.email:
            to_be_approved = True
        if not prospect.job_title:
            prospect.job_title = instance.job_title
        elif prospect.job_title != instance.job_title:
            to_be_approved = True
        if not prospect.company:
            prospect.company = instance.company
        elif prospect.company != instance.company:
            to_be_approved = True
        if not prospect.industry_type:
            prospect.industry_type = instance.industry_type
        elif prospect.industry_type != instance.industry_type:
            to_be_approved = True
        if not prospect.website:
            prospect.website = instance.website
        elif prospect.website != instance.website:
            to_be_approved = True
        if not prospect.emp_size:
            prospect.emp_size = instance.emp_size
        elif prospect.emp_size != instance.emp_size:
            to_be_approved = True
        if not to_be_approved:
            prospect.is_approved = True
        prospect.save()
        instance.save()

post_save.connect(ProspectUpdate, check_updates)
