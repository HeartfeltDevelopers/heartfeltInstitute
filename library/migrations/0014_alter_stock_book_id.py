<<<<<<< HEAD
# Generated by Django 4.2.5 on 2023-09-26 18:26
=======
# Generated by Django 4.2.5 on 2023-09-25 05:39
>>>>>>> online_class

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("library", "0013_alter_stock_book_id"),
=======
        ('library', '0013_alter_stock_book_id'),
>>>>>>> online_class
    ]

    operations = [
        migrations.AlterField(
<<<<<<< HEAD
            model_name="stock",
            name="book_id",
            field=models.CharField(
                default="BOOK-1721-2023", max_length=20, unique=True
            ),
=======
            model_name='stock',
            name='book_id',
            field=models.CharField(default='BOOK-3298-2023', max_length=20, unique=True),
>>>>>>> online_class
        ),
    ]
