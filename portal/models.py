from django.db import models
import datetime
from django.db.models.signals import post_save
from django.contrib.auth.models import User as Django_User_Model
from django.urls import reverse_lazy
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)

    phone = models.CharField(max_length=13, blank=True)

    employee_id = models.CharField(max_length=12, blank=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    date_of_birth = models.DateField(blank=True, null=True)
    details = models.TextField(blank=True)

    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.get_email_name

    @property
    def get_display_text(self):
        if self.get_full_name:
            return self.get_full_name
        else:
            return self.__str__()

    @property
    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name) if (self.first_name or self.last_name) else ""

    @property
    def get_email_name(self):
        email_str = str(self.email)
        return email_str[:email_str.rfind("@")]

    @property
    def get_employee_id(self):
        if self.employee_id:
            return self.employee_id
        else:
            return "Unknown"

    @property
    def get_age(self):
        try:
            return datetime.date.today() - self.date_of_birth
        except:
            return "Unknown"

    @property
    def get_leads(self):
        return self.result_set.filter(result_choice="Lead")

    @property
    def get_dncs(self):
        return self.result_set.filter(result_choice="DNC")

    @property
    def get_views(self):
        return self.result_set.filter(result_choice="View")

    @property
    def get_admin_update_url(self):
        return reverse_lazy("crm_admin:executive_update", kwargs={"id": self.id})

    @property
    def get_admin_delete_url(self):
        return reverse_lazy("crm_admin:executive_delete", kwargs={"id": self.id})

    @property
    def get_active_campaigns(self):
        return self.campaign_set.filter(is_active=True)

    @property
    def get_campaigns(self):
        return self.campaign_set.all()

    def get_leads_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="Lead", prospect_campaign_relation__campaign_id=campaign_id)

    def get_dncs_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="DNC", prospect_campaign_relation__campaign_id=campaign_id)

    def get_views_by_campaign(self, campaign_id):
        return self.result_set.filter(result_choice="View", prospect_campaign_relation__campaign_id=campaign_id)
