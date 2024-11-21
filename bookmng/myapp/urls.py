from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from.views import *

router=DefaultRouter()
router.register('authors',Authorview)
router.register('Category',Categoryview)
router.register('Book',Bookview)



urlpatterns = [
     path('', include(router.urls)),
     path('listbooks/', views.list_books, name='list_books'),
     path('update_book/<int:id>/', views.update_book, name='update_book'),
     path('add_book/', views.add_book, name='add_book'),
     path('add_author/', views.add_author, name='add_author'),
     path('add_category/', views.add_category, name='add_category'),
     path('author_list/', views.author_list, name='author_list'),
     path('category_list/', views.category_list, name='category_list'),
     path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    
     
     
]    