from django.db import models
from django.contrib.auth.models import AbstractUser

from django.core.exceptions import ValidationError

import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

from PIL import Image

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
    radius = models.PositiveIntegerField(verbose_name = 'Choose Radius', validators = [exempt_zero], default = 1)
    postal_code = models.CharField(max_length = 7, default = None, null = True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    share_badge = models.PositiveIntegerField(default = 0, verbose_name = 'Share Badges')
    donate_badge = models.PositiveIntegerField(default = 0, verbose_name = 'Donate Badges')

    location = models.CharField(max_length = 255, default = None, null = True)
    profile_pic = models.ImageField(default = 'default_profile.png', upload_to = 'uploads/profile/', null = True, blank = True)

    def save(self, *args, **kwargs):

        if self.profile_pic:
            img = Image.open(self.profile_pic)

            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            output = BytesIO()

            #Preserve aspect ratio
            original_width, orignal_height = img.size
            aspect_ratio = round(original_width / orignal_height)
            final_height = 150
            final_width = aspect_ratio * final_height

            img = img.resize((final_width, final_height))

            img.save(output, format = 'JPEG', quality = 90, save = False)
            output.seek(0)

            self.profile_pic = InMemoryUploadedFile(output, 'ImageField', f"{self.username}_profile.jpg", 'image/jpeg', sys.getsizeof(output), None)

        super(Member, self).save(*args, **kwargs)



    '''def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        SIZE = (250, 250)

        if self.profile_pic:
            pic = Image.open(self.profile_pic.path)
            pic.thumbnail(SIZE, Image.LANCZOS)
            pic.save(self.profile_pic.path)'''
    
    def __str__(self):
        return self.username
