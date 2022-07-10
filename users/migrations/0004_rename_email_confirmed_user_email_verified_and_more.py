# Generated by Django 4.1b1 on 2022-07-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_user_email_confirmed_alter_user_currency_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="email_confirmed",
            new_name="email_verified",
        ),
        migrations.AddField(
            model_name="user",
            name="email_secret",
            field=models.CharField(blank=True, default="", max_length=120),
        ),
    ]