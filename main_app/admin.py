from django.contrib import admin
from .models import Profile
from .models import Post
from .models import City
from .models import Comment
# Register your models here.


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'country',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(City,CityAdmin)
