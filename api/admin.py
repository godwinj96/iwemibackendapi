from django.contrib import admin

# Register your models here.

from .models import Book
from .models import Category
from .models import SubCategory
from .models import Discipline

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Discipline)
