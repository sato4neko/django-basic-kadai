from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy

class TopView(TemplateView):
    template_name = "top.html"
#Viewを追加
class ProductListView(ListView):
    model = Product
    template_name = "list.html"
#Viewを追加
    paginate_by = 3
#商品を新規作成するためのViewを追加
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
#商品を編集するためのViewを追加
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    template_name_suffix = '_update_form'
#商品を削除するためのViewを追加
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list')
#商品詳細のためのViewを追加
class ProductDetailView(DetailView):
    model = Product
    template_name = "crud/product_detail.html"
    success_url = reverse_lazy('list')