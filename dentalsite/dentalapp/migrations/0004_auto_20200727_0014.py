# Generated by Django 3.0.8 on 2020-07-26 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalapp', '0003_auto_20200726_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='services',
            name='image',
        ),
        migrations.AddField(
            model_name='services',
            name='fav_icon',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
