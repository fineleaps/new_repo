from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User as Django_User_Model

User_Model = Django_User_Model
#
# class User(Django_User_Model):
#
#     class Meta:
#         proxy = True
#         # ordering = ('first_name', )
#
#     def get_display_text(self):
#         return self.executive.first_name


def create_executive(instance, sender, *args, **kwargs):
    if not hasattr(instance, 'executive'):
        Executive.objects.create(user=instance)


post_save.connect(create_executive, sender=Django_User_Model)


class Executive(models.Model):
    user = models.OneToOneField(User_Model, on_delete=models.PROTECT)

    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)

    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=13, blank=True)

    employee_id = models.CharField(max_length=12, blank=True)

    date_of_birth = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return self.user.__str__()

    @property
    def get_display_text(self):
        if self.first_name:
            return self.first_name
        else:
            return self.user.username

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def get_employee_id(self):
        if self.employee_id:
            return self.employee_id
        else:
            return "Not entered yet"

    @property
    def get_age(self):
        return datetime.date.today() - self.date_of_birth

    @property
    def get_leads(self):
        return self.result_set.filter(result_choice="Lead")

    @property
    def get_dncs(self):
        return self.result_set.filter(result_choice="DNC")

    @property
    def get_views(self):
        return self.result_set.filter(result_choice="View")

    def get_leads_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="Lead", prospect_campaign_relation__campaign_id=campaign_id)

    def get_dncs_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="DNC", prospect_campaign_relation__campaign_id=campaign_id)

    def get_views_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="View", prospect_campaign_relation__campaign_id=campaign_id)


