from django.db.models.signals import post_save

from django.conf import settings
from django.db import models

import stripe
from django_countries.fields import CountryField

stripe.api_key = settings.STRIPE_SECRET_KEY

MEMBERSHIP_CHOICES = (
    ('Regular', 'reg'),
    ('Premium', 'prem'),
    ('Free', 'free'),
)


# Membership type View for DB admin
class Membership(models.Model):
    membership_type = models.CharField(
        choices=MEMBERSHIP_CHOICES,
        default='Free',
        max_length=30, null=False, blank=False)
    price = models.IntegerField(default=15)
    description_one = models.TextField(default="DESCRIPTION")
    description_two = models.TextField(default="DESCRIPTION")
    description_three = models.TextField(default="DESCRIPTION")
    description_four = models.TextField(default="DESCRIPTION")
    stripe_plan_id = models.CharField(max_length=40)

    def __str__(self):
        return self.membership_type


class UserMembership(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=40)
    membership = models.ForeignKey(Membership, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=50,  null=False)
    email = models.EmailField(max_length=254,  null=False)
    phone_number = models.CharField(max_length=20,  null=False)
    country = CountryField(blank_label='Country',  default="Ireland" )
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40,  null=False)
    street_address1 = models.CharField(max_length=80,  null=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80,  null=False)

    def __str__(self):
        return self.user.username


def post_save_usermembership_create(
        sender, instance, created, *args, **kwargs):
    user_membership, created = UserMembership.objects.get_or_create(
        user=instance)

    if user_membership.stripe_customer_id is None or user_membership.stripe_customer_id == '':
        new_customer_id = stripe.Customer.create(email=instance.email)
        # free_membership = Membership.objects.get(membership_type='Free')
        user_membership.stripe_customer_id = new_customer_id['id']
        # user_membership.membership = free_membership
        user_membership.save()


post_save.connect(post_save_usermembership_create,
                  sender=settings.AUTH_USER_MODEL)


class Subscription(models.Model):
    user_membership = models.ForeignKey(
        UserMembership, on_delete=models.CASCADE)
    stripe_subscription_id = models.CharField(max_length=40)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user_membership.user.username
