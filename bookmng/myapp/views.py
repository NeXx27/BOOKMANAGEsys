from django.shortcuts import render, redirect,get_object_or_404
from .models import Book,Category,Author
from .forms import BookForm, AuthorForm, CategoryForm
from .serializers import *
from rest_framework import viewsets


class Authorview(viewsets.ModelViewSet):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer

class Categoryview(viewsets.ModelViewSet):
    queryset= Category.objects.all()
    serializer_class=CategorySerializer

class Bookview(viewsets.ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=BookSerializer




def list_books(request):
    books=Book.objects.all()
    return render(request,'myapp/list_books.html',{'books':books} )

def author_list(request):
    author=Author.objects.all()
    return render(request,'myapp/author_list.html',{'author':author} )

def category_list(request):
    category=Category.objects.all()
    return render(request,'myapp/category_list.html',{'category':category} )

def add_book(request):
    if request.method== 'POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form=BookForm()
        return render(request,'myapp/add_book.html',{'form':form})


def update_book(request, id):
    book = get_object_or_404(Book, id=id )
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')  # Redirect to your item list view
    else:
        form = BookForm(instance=book)
    return render(request, 'myapp/update_book.html', {'form': form})

def add_author(request):
    if request.method == 'POST':
        form=AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form=AuthorForm()
        return render(request,'myapp/add_author.html',{'form':form})

def add_category(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
    else:
        form=CategoryForm()
        return render(request,'myapp/add_category.html',{'form':form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'myapp/delete_book.html', {'book': book})


# @api_view(['DELETE'])
# def delete_multiple_entries(request):
#     ids = Book.data.get('ids', []) # Assuming IDs are sent in JSON array
#     if not ids:
#         return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         Book.objects.filter(id__in=ids).delete()
#         return Response({"message": "Entries deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
#     except Exception as e:
#         return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)