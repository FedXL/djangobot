# Generated by Django 4.2.5 on 2023-09-24 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_alter_user_login'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teleuser',
            name='code',
        ),
    ]
