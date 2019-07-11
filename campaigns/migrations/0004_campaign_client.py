# Generated by Django 2.0 on 2019-07-11 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('campaigns', '0003_campaign_aim'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='clients.Client'),
        ),
    ]