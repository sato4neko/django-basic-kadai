from django.contrib import admin
from .models import Product

#一覧画面をカスタマイズ
class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price')
     search_fields = ('name',)
#管理画面にProductを表示
admin.site.register(Product, ProductAdmin)
