# Generated by Django 2.2 on 2019-04-30 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='bedroos',
            new_name='bedrooms',
        ),
    ]