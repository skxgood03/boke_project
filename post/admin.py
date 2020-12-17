from django.contrib import admin
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title','created') #详情要显示的字段
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post,PostModelAdmin)  #还需要在相应的表添加啊类名
