# Generated by Django 4.1b1 on 2022-07-10 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0009_alter_photo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="guests",
            field=models.IntegerField(help_text="How many people will be staying?"),
        ),
    ]
