# Generated by Django 3.2.13 on 2022-05-16 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20220516_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='replay',
            new_name='parent',
        ),
    ]
