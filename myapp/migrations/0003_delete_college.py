# Generated by Django 4.1 on 2023-11-08 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_college_delete_school"),
    ]

    operations = [
        migrations.DeleteModel(
            name="College",
        ),
    ]