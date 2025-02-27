from rest_framework import serializers
from .models import Category, SubCategory, Book, Discipline

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):


    class Meta:
        model= SubCategory
        fields= '__all__'


class DisciplineSerializer(serializers.ModelSerializer):


    class Meta:
        model = Discipline
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model= Book
        fields= '__all__'
        lookup_field = ['category', 'subcategory']
        