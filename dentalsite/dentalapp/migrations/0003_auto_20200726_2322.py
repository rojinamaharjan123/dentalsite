# Generated by Django 3.0.8 on 2020-07-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentalapp', '0002_auto_20200726_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]