# Generated by Django 3.0.7 on 2020-06-29 12:39

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20200628_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(default='uk', max_length=2),
            preserve_default=False,
        ),
    ]
