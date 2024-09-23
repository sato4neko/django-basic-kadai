from django.contrib import admin
from .models import Product, Category
from django.utils.safestring import mark_safe

#一覧画面をカスタマイズ
class ProductAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'price', 'category', 'image', 'description')
     search_fields = ('name',)
     list_filter = ('category',)

     def image(self, obj):
          return mark_safe('<img src="{}" style="width:100px height:auto;">'.format(obj.img.url))

#一覧画面にカテゴリーを追加
class CategoryAdmin(admin.ModelAdmin):
     list_display = ('id', 'name')
     search_fields = ('name',)


#管理画面に表示
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
