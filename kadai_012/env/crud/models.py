from django.db import models
from django.urls import reverse

# カテゴリーModelを追加
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# 商品説明Modelを追加
class Description(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
         return self.name

# Modelを追加
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    img = models.ImageField(blank=True, null=True, default='noImage.png')
    description = models.CharField(max_length=200)

# 一覧画面で表示される名称を変更
    def __str__(self):
        return self.name
# 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
        return reverse('list')