# Generated by Django 4.2.5 on 2023-09-23 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='login',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]