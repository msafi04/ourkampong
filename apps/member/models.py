from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

def exempt_zero(value):
    if value == 0 and value > 5:
        raise ValidationError(
                            ('Please enter a value from 1 to 5'),
                            params={'value': value},
                        )

class Member(AbstractUser):
    RADIUS_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    ]
    #radius = models.IntegerField(verbose_name = 'Choose Radius', choices = RADIUS_CHOICES, default = RADIUS_CHOICES[0])
    email = models.EmailField(verbose_name = 'Email Address', max_length = 255, unique = True)
    radius = models.PositiveIntegerField(verbose_name = 'Choose Radius', validators = [exempt_zero])
    postal_code = models.CharField(max_length = 7, default = None, null = True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    share_badge = models.PositiveIntegerField(default = 0, verbose_name = 'Share Badges')
    donate_badge = models.PositiveIntegerField(default = 0, verbose_name = 'Donate Badges')

    location = models.CharField(max_length = 255, default = None, null = True)
    profile_pic = models.ImageField(default = 'default_profile.png', upload_to = 'uploads/profile/', null = True, blank = True)

