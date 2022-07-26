from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

from apps.member.models import Member

class Category(models.Model):
    CATEGORY_CHOICES = (
    ('TY', 'Toys'),
    ('AP', 'Apparels'),
    ('BO', 'Books'),
    ('ST', 'Stationery'),
    ('FU', 'Furniture'),
    ('HW', 'Hardwares'),
    ('SN', 'Snacks'),
    ('EL', 'Electronics'),
    ('HI', 'Household_Items'),
    ('SP', 'Sports'),
    ('GR', 'Groceries'),
    ('OT', 'Others')
    )

    title = models.CharField(choices = CATEGORY_CHOICES, max_length = 2, verbose_name = 'Categories')
    slug = models.SlugField(max_length = 255)
    ordering = models.IntegerField(default = 0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title
        
class Item(models.Model):
    LABEL_CHOICES = (
        ('NW', 'New'),
        ('OL', 'Old'),
        ('US', 'Used'),
        ('UN', 'Unused'),
        ('DM', 'Damaged')
    )
    #category = models.ForeignKey(Category, related_name = 'items', on_delete = models.CASCADE)
    category = models.CharField(choices = Category.CATEGORY_CHOICES, max_length = 2, verbose_name = 'Categories')
    cat_slug = models.SlugField(max_length = 255, default = None)
    member = models.ForeignKey(Member, related_name = 'items', on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    label = models.CharField(choices = LABEL_CHOICES, max_length = 2, verbose_name = 'Labels')
    slug = models.SlugField(max_length = 255)
    description = models.TextField(blank = True, null = True)
    price = models.DecimalField(max_digits = 6, decimal_places = 2)
    date_added = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to = 'uploads/', blank = True, null = True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title

    def get_thumbnail(self):
            if self.thumbnail:
                return self.thumbnail.url
            else:
                if self.image:
                    self.thumbnail = self.make_thumbnail(self.image)
                    self.save()

                    return self.thumbnail.url
                else:
                    return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size = (300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality = 85)

        thumbnail = File(thumb_io, name = image.name)

        return thumbnail