from django.shortcuts import  render,get_object_or_404,redirect
from .models  import  User,Post,Album,Photo,Comment,ToDo
from django.views import View
from django.http import HttpResponse
from .forms import CommentForm,UserForm




user_data ={
 "id":1,
 "name":"Müslüm",
  "surname":"Türk",
  "email":"muslum.turk@n2mobil.com.tr",
  "adress":{
    "street":"Çamlıca Mahallesi",
    "suite":"Apt.556",
    "city":"Ankara",
    "zipcode":"06200",
    "geo":{
     "lat":"39.950289",
     "lng":"32.7732722"
    }
       
     },
     "phone":"+90 555 555 55 55 ",
     "website":"www.n2mobil.com.tr",
     "company":{
      "name":"N2Mobil Araç Takip Sistemleri A.Ş",
     }
    },
 
post_data ={
"userid":1,
"id":1,
 "title":"Merhaba",
 "body":"Merhaba Ben Müslüm Türk",

  }

album_data={
   "userıd":1,
   "id":1,
   "title":"Albümüm",
}
photo_data={
   "album_id":1,
   "id":1,
   "title":"çok güzel fotoğraf",
    "url":"https://via.placeholder.com/600/92c952",
    "thumbnailUrl":"https://via.placeholder.com/150/92c952",
}

comment_data={
   "post_id":1,
   "id":1,
   "name":"comment model",
   "email":"info@n2mobil.com.tr",
   "body":"comment body",
}
todolist_data={
    "userid":1,
     "id":1,
     "title":"todolist model",
     "completed":"False"
 }

def  kullanici(request):
 return render (request , 'kullanici.html')

def  kullaniciliste(request):
 users=User.objects.all()
 return render (request , 'kullaniciliste.html',{'users':users})


def KullaniciPostGörüntüle(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    posts = Post.objects.filter(user=user)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            
            comment.post = post
      
            if request.user.is_authenticated:
                comment.user = request.user
         
            comment.save()
            return redirect(request.path)
    else:
        form = CommentForm()

    return render(request, 'kullanicidetay.html', {
        'user': user,
        'posts': posts,
        'form': form,
    })


    
    

         
          
            

    




def KullaniciDetay(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    posts = Post.objects.filter(user=user)
    
    albums = Album.objects.filter(user=user)
    todos=ToDo.objects.filter(user=user)
 
    

    album_photos = []
    for album in albums:
        photos = Photo.objects.filter(album=album)
        album_photos.append({
            'album': album,
            'photos': photos,
            
        })
    
     
    
    return render(request, 'kullanicidetay.html', {
        'user': user,
        'posts': posts,
        'album_photos': album_photos,
        'todos':todos,
     
    })
    

  
def  todoekle(request):
   
    users = User.objects.all()
    todos = ToDo.objects.all()
    if request.method == 'POST':
        selected_user_id = request.POST.get('user')
        todo_title = request.POST.get('title')
        completed = request.POST.get('completed') == '1'  
        
        
        new_todo = ToDo.objects.create(user_id=selected_user_id, title=todo_title, completed=completed)
        new_todo.save()

        return redirect('kullanicitodoekle') 

    return render(request, 'kullanicitodoekle.html', {'users': users,'todos': todos})

def  kullaniciekle(request):
    if request.method == 'POST':
     
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        
        
        adress = {
            "street": request.POST.get('street'),
            "suite": request.POST.get('suite'),
            "city": request.POST.get('city'),
            "zipcode": request.POST.get('zipcode'),
            "geo": {
                "lat": request.POST.get('latitude'),
                "lng": request.POST.get('longitude')
            }
        }


        company = {
            "name": request.POST.get('company')
        }

  
        new_user = User(
            name=name,
            surname=surname,
            username=username,
            email=email,
            phone=phone,
            website=website,
            adress=adress,
            company=company
        )
        new_user.save() 

        return redirect('kullaniciliste') 

    return render(request, 'kullaniciekle.html')  

def kullanicisil(request):
    users = User.objects.all() 
    if request.method == "POST":
        user_id = request.POST.get('user_id') 
        if user_id:
            user = get_object_or_404(User, id=user_id)  
            user.delete()  
            return redirect('kullaniciliste')  
    return render(request, 'kullanicisil.html', {'users': users})  


