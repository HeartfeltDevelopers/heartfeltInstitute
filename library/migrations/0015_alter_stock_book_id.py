# Generated by Django 4.2.5 on 2023-09-25 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("library", "0014_alter_stock_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="book_id",
            field=models.CharField(
                default="BOOK-3427-2023", max_length=20, unique=True
            ),
        ),
    ]
