# Generated by Django 4.1.1 on 2022-09-21 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
