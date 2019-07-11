# Generated by Django 2.0 on 2019-07-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('slug', models.SlugField(blank=True)),
                ('director', models.CharField(max_length=64)),
                ('company', models.CharField(blank=True, max_length=128)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('email2', models.EmailField(blank=True, max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('phone2', models.CharField(blank=True, max_length=15)),
                ('emp_size', models.CharField(blank=True, max_length=16)),
                ('website', models.CharField(blank=True, max_length=64)),
                ('industry_type', models.CharField(blank=True, max_length=64)),
                ('city', models.CharField(blank=True, max_length=32)),
                ('state', models.CharField(blank=True, max_length=32)),
                ('country', models.CharField(blank=True, max_length=32)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('details', models.TextField(blank=True)),
            ],
        ),
    ]
