# Generated by Django 4.2.8 on 2023-12-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_notification_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='id',
        ),
        migrations.AlterField(
            model_name='notification',
            name='created_at',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
