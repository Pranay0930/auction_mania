# Generated by Django 4.2.16 on 2024-12-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction_app", "0004_alter_itemmodel_item_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="usermodel",
            name="credits",
            field=models.IntegerField(default=0),
        ),
    ]
