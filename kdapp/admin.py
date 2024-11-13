from django.contrib import admin
from .models import Comment,Post,Album,ToDo

admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(Album)
admin.site.register(ToDo)

# Register your models here.
