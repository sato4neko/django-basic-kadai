from django.db import models
from django.urls import reverse

# Modelを追加
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
# 一覧画面で表示される名称を変更
    def __str__(self):
        return self.name
# 新規作成・編集完了時のリダイレクト先
    def get_absolute_url(self):
         return reverse('list')