from django import forms
from .models import Book, Author,Category

class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name']
        widgets= {
            'name':forms.TextInput(attrs={'class':'form-control'})
        }
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['cat_name']
        widgets={
        'cat_name': forms.TextInput(attrs={'class': 'form-control'})
                }
                
        
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['book_name','book_description','author','categories']
        widgets={
        'book_name': forms.TextInput(attrs={'class': 'form-control'}),
        'book_description':forms.Textarea(attrs={'class':'forms-control'}),                
        'author': forms.Select(attrs={'calss':'forms-control'}),
        'categories':forms.SelectMultiple(attrs={'class':'form-control'})
        }
                    