# Generated by Django 5.1.3 on 2024-12-10 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_book_options_alter_vazifa_options_book_mualif'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Book',
            new_name='Books',
        ),
    ]
