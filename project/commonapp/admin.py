from django.contrib import admin
from .models import Category, New, Article



def time_to_pudge(modeladmin, request, queryset):
    queryset.update(title='PUDGE')

time_to_pudge.short_description='ПУДЖ!!!'

class NewAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in New._meta.get_fields()]
    list_fields = ['title', 'category', 'text']
    search_fields = ['title', 'category__name']
    actions=[time_to_pudge]
class ArticleAdmin(admin.ModelAdmin):
    # list_display - это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = ('title', 'category', 'so_cool') # оставляем только имя и цену товара

admin.site.register(Category)
admin.site.register(New, NewAdmin)
admin.site.register(Article, ArticleAdmin)