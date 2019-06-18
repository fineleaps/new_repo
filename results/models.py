from django.db import models
from django.core.exceptions import ValidationError


class Result(models.Model):

    ResultChoices = (('Lead', 'Lead'), ('View', 'View'), ('DNC', 'DNC'))

    prospect_campaign_relation = models.OneToOneField('campaigns.ProspectCampaignRelation', on_delete=models.CASCADE)
    on = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey('portal.Executive', on_delete=models.CASCADE)
    result_choice = models.CharField(max_length=2, choices=ResultChoices)
    details = models.TextField(blank=True)

    def __str__(self):
        return "{} -{} - {}".format(self.prospect_campaign_relation.prospect, self.prospect_campaign_relation.campaign,
                              self.result_choice)
    #
    # def clean(self):
    #     if self.prospect_campaign_relation and not self.prospect_campaign_relation.attempted:
    #         raise ValidationError('Prospect must be attempted to save attempt result')
