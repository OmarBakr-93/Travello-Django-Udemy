from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Property(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='property/')
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    place = models.ForeignKey('Place', related_name='propertyPlace', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', related_name='propertyCategory', on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Property, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
      
    def get_absolute_url(self):
        return reverse('property:property_detail', kwargs={'slug': self.slug})
      
      
class PropertyImages(models.Model):
    property = models.ForeignKey(Property, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='propertyImages/')
    
    def __str__(self):
        return str(self.property) 
    
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
      
class Property_Review(models.Model):
    author = models.ForeignKey(User, related_name='review_author', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='review_property', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    feedback = models.TextField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return str(self.property)
      

Count = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),]

class Property_Book(models.Model):
    user = models.ForeignKey(User, related_name='book_owner', on_delete=models.CASCADE)
    property = models.ForeignKey(Property, related_name='book_property', on_delete=models.CASCADE)
    date_from = models.DateField(default=timezone.now)
    date_to = models.DateField(default=timezone.now)
    guest = models.IntegerField(choices=Count, default=1)
    children = models.IntegerField(choices=Count, default=0)
    
    def __str__(self):
        return str(self.property)
