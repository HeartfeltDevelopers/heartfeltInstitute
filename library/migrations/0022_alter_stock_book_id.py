# Generated by Django 4.2.5 on 2023-09-30 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0021_alter_stock_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="book_id",
            field=models.CharField(
                default="BOOK-8142-2023", max_length=20, unique=True
            ),
        ),
    ]
