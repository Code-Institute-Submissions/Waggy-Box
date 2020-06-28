# Generated by Django 3.0.7 on 2020-06-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0011_auto_20200626_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='description_five',
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='county',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='email',
            field=models.EmailField(default='Please enter your email address', max_length=254),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='full_name',
            field=models.CharField(default='Please enter your full name', max_length=50),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='phone_number',
            field=models.CharField(default='Please enter your phone number', max_length=20),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='street_address1',
            field=models.CharField(default='Please enter address line 1', max_length=80),
        ),
        migrations.AlterField(
            model_name='usermembership',
            name='town_or_city',
            field=models.CharField(default='Please enter your City', max_length=40),
        ),
    ]