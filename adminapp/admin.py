from django.contrib import admin
from .models import Posts

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
  list_display = [field.name for field in Posts._meta.fields] # show all fields