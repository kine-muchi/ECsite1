from django.shortcuts import render
from django.views import generic
from .models import GoodsGroup, CustomGoods
from .forms import GroupCreationForm, CustomGoodsCreationForm#, CustomGoodsSearchForm


class GroupCreateView(generic.CreateView):
    model = GoodsGroup
    success_url = '/search/group_create'
    template_name = 'search/group_create.html'
    form_class = GroupCreationForm

class CustomGoodsCreateView(generic.CreateView):
    model = CustomGoods
    success_url = '/search/custom_goods_create'
    template_name = 'search/custom_goods_create.html'
    form_class = CustomGoodsCreationForm

