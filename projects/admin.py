from django.contrib import admin
from .models import Post, Techs

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('techs',)

admin.site.register(Post,PostAdmin)
admin.site.register(Techs)