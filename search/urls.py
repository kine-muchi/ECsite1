from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'search'
urlpatterns = [
    path('group_create/', login_required(views.GroupCreateView.as_view()), name='group_create'),
    path('custom_goods_create/', login_required(views.CustomGoodsCreateView.as_view()), name='custom_goods_create'),
]
