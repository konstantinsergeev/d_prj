# Generated by Django 5.1.4 on 2024-12-28 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='sites',
            field=models.ManyToManyField(to='sites.site'),
        ),
    ]