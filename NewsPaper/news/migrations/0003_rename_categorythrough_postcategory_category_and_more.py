# Generated by Django 4.2.3 on 2023-09-07 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_mailing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcategory',
            old_name='categoryThrough',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='postcategory',
            old_name='postThrough',
            new_name='post',
        ),
    ]
