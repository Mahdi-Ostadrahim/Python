# Generated by Django 3.2.16 on 2022-10-14 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approach',
            new_name='approved',
        ),
    ]
