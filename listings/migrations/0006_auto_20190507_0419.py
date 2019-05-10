# Generated by Django 2.2 on 2019-05-07 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20190507_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='agent',
            field=models.ForeignKey(limit_choices_to={'groups': 'agent'}, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
