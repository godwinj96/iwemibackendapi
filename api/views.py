from multiprocessing import context
from unicodedata import category
from django.forms import NullBooleanField
from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Book, Category, SubCategory
from .serializers import BookSerializer, CategorySerializer, SubCategorySerializer
from rest_framework import generics
# from .forms import LoginForm

# Create your views here.

class BookList(generics.ListCreateAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        query =self.request.query_params.get('q')
        if query is not None:
            queryset = queryset.filter(
                name__icontains=query
            )
            return queryset
        

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class CategoryList(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        queryset = Category.objects.all()
        query =self.request.query_params.get('q')
        if query is not None:
            queryset = queryset.filter(
                name=query
            )
            return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer

    # def get_queryset(self):
    #     id =self.request.query_params.get('pk')
    queryset = Category.objects.all()


class SubCategoryList(generics.ListCreateAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()


class SubCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SubCategorySerializer
    queryset = SubCategory.objects.all()

# books = [
#     {'id':1, 'name':'Half Of A Yellow Sun', 'author':'Chimamanda Ngozi Adichie'},
#     {'id':2, 'name':'Things Fall Apart', 'author':'Chinua Achebe'},
#     {'id':3, 'name':'The Magicians', 'author':'Lev Grossman'},
# ]

# def home(request):

#     q = request.GET.get('q', '') 
#     if q:
#         books = Book.objects.filter(sub_category__name__icontains=q)
#     else: ''

#     books = Book.objects.filter(sub_category__name__icontains=q)

#     categorys = Category.objects.all()
#     subcategorys = SubCategory.objects.all()


#     context = {'books': books, 'categorys': categorys, 'subcategorys': subcategorys}
#     return render(request, 'base/home.html', context)

# def book(request, pk):
#     book = Book.objects.get(id=pk)

#     books = Book.objects.all()


#     categorys = Category.objects.all()
#     subcategorys = SubCategory.objects.all()

#     context = {'book' : book,'books': books, 'categorys': categorys, 'subcategorys': subcategorys}
#     return render(request, 'base/book.html', context)


# def login_form(request):
#     form = LoginForm()

#     categorys = Category.objects.all()
#     subcategorys = SubCategory.objects.all()

    
#     context = {'form': form}
#     return render(request, 'base/login_form.html', context)

# def search(request):

#     categorys = Category.objects.all()
#     subcategorys = SubCategory.objects.all()

#     q = request.GET.get('q')
#     books = Book.objects.filter(
#         Q(sub_category__name__icontains=q)  | 
#         Q(name__icontains=q)  | 
#         Q(abstract__icontains=q) | 
#         Q(category__name__icontains=q)
#         )

#     context = {'books': books, 'categorys': categorys, 'subcategorys': subcategorys, 'q': q}
#     return render(request, 'base/search.html', context)


