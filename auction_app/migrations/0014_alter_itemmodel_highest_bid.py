# Generated by Django 4.2.16 on 2024-12-16 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction_app", "0013_alter_itemmodel_item_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="itemmodel",
            name="highest_bid",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=None, max_digits=10, null=True
            ),
        ),
    ]
