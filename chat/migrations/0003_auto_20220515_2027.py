# Generated by Django 3.2.13 on 2022-05-15 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20220514_2113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatreply',
            options={'verbose_name': 'گپ', 'verbose_name_plural': 'گپ ها'},
        ),
        migrations.AlterField(
            model_name='chatreply',
            name='chat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_reply', to='chat.chat'),
        ),
        migrations.AlterField(
            model_name='chatreply',
            name='comment',
            field=models.TextField(max_length=500),
        ),
    ]