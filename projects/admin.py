from django.contrib import admin
from .models import Post, Techs, Kura, Comment, Profile

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    filter_horizontal =('techs',)

admin.site.register(Profile)
admin.site.register(Post,PostAdmin)
admin.site.register(Techs)
admin.site.register(Kura)
admin.site.register(Comment)