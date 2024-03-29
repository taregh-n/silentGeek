# Generated by Django 3.2.13 on 2022-05-14 16:43

from django.db import migrations, models
import django.utils.timezone
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='create',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=300, verbose_name='خلاصه'),
        ),
        migrations.AlterField(
            model_name='post',
            name='update',
            field=django_jalali.db.models.jDateTimeField(auto_now=True),
        ),
    ]
