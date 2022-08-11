
from django.contrib.admin.decorators import register
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save,pre_save
from .models import CafeOwner, CoffeeShop
from utils import create_slug
@receiver(post_save,sender=CafeOwner )
def send_new_owner_email(sender, instance, created, **kwargs):
    if created == True:
        send_mail(
    'New Cafe Owner',
    f'A new cafe owner has joined named {instance.first_name}',
    'sender@test.com',
    ["receiver@test.com"],
)
@receiver(pre_save,sender=CoffeeShop  )
def slugify_coffee_shop(sender, instance, **kwargs):
    if not instance.slug: # is empty or not ? so we use not oe None
        # print(instance)
        # print(instance.slug)
        instance.slug = create_slug(instance)
        # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!11")
        # print(instance.slug)
        # instance.save()