from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    

class Discipline(models.Model):
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.name
    


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200, null=True, blank=True)
    abstract =  models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)
    discipline = models.ForeignKey(Discipline, on_delete=models.SET_NULL, null=True)
    year_published = models.DateField()
    date_uploaded = models.DateTimeField(auto_now_add=True,)
    is_open_access = models.BooleanField(null=True, blank=True)
    is_approved = models.BooleanField(null=True, blank=True)
    # file = models.FileField()
    
    def __str__(self):
        return self.name
    
