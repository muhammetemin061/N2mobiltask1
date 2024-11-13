from django import forms
from .models import Post,Comment,ToDo,User

 
class  PostForm(forms.ModelForm):
     class  Meta:
        model=Post
        fields=['user','title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['name', 'email', 'body']

class TodoForm(forms.ModelForm):
    class   Meta:
        model=ToDo
        fields=['title','completed']        

   
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'surname', 'username', 'email', 'adress', 'phone', 'website', 'company', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'İsim giriniz'}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Soyisim giriniz'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kullanıcı adı giriniz'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-posta giriniz'}),
            'adress': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Adres JSON formatında'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon numarası'}),
            'website': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Web sitesi'}),
            'company': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Şirket JSON formatında'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enlem'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Boylam'}),
        }
