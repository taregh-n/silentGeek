# Generated by Django 3.2.13 on 2022-05-15 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('notify', models.CharField(max_length=50)),
                ('seen', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['content_type', 'object_id'], name='notificatio_content_743343_idx'),
        ),
    ]