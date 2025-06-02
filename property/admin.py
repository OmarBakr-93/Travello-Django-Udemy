from django.contrib import admin
from .models import Property, PropertyImages, Place, Category, Property_Review, Property_Book

from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

admin.site.register(Property, SummernoteModelAdmin)
admin.site.register(PropertyImages)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(Property_Review)
admin.site.register(Property_Book)

