# Generated by Django 4.2.5 on 2023-09-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0015_alter_stock_book_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="book_id",
            field=models.CharField(
                default="BOOK-9115-2023", max_length=20, unique=True
            ),
        ),
    ]
