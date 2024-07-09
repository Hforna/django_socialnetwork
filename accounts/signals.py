from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.core.mail import send_mail
from core import settings
from profiles.models import Profile, UserInfos

User = get_user_model()

@receiver(post_save, sender=User)
def send_email_if_user_created(sender, instance, created, *args, **kwargs):
    if created:
        profile = Profile.objects.create(user_profile=instance, profile_name=instance.username)
        user_infos = UserInfos.objects.create(user=instance)
        profile.save()
        user_infos.save()
        print(instance.email)
        send_mail(
            subject="Account created with success",
            message=f"Hi {instance.username} your account was created",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list= [instance.email],
        fail_silently=False
        )