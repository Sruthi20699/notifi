# Generated by Django 4.2.8 on 2023-12-21 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_remove_notification_id_alter_notification_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='created_at',
        ),
        migrations.AddField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
