# Generated by Django 3.2.13 on 2022-05-14 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=300),
        ),
    ]
