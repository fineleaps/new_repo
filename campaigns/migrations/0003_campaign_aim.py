# Generated by Django 2.0 on 2019-06-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_campaign_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='aim',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
