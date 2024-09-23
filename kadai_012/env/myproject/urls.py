"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.TopView.as_view(), name="top.html"),
    #データ一覧画面のURL設定
    path('crud/', views.ProductListView.as_view(), name="list"),
    #商品を新規作成するためのViewのURL
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    #商品を編集するためのViewのURL
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    #商品を削除するためのViewのURL
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    #商品を削除するためのViewのURL
    path('crud/detail/<int:pk>', views.ProductDetailView.as_view(), name="detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)