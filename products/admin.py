from django.contrib import admin
from .models import Product, Comment




class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','stars','active']


admin.site.register(Comment,CommentAdmin)

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price']
    inlines = [CommentInLine,]