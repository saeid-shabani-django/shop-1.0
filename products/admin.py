from django.contrib import admin
from .models import Product, Comment
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin



class CommentAdmin(admin.ModelAdmin):
    list_display = ['author','stars','active']


admin.site.register(Comment,CommentAdmin)

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title','price']
#     inlines = [CommentInLine,]






@admin.register(Product)
class ProductAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price']
    inlines = [CommentInLine, ]

    @admin.display(description='تاریخ ایجاد', ordering='created')
    def get_created_jalali(self, obj):
        return datetime2jalali(obj.created).strftime('%a, %d %b %Y %H:%M:%S')