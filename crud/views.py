from django.shortcuts import render
from django.views import generic
from .models import Goods
from .forms import GoodsCreateForm, GoodsUpdateForm, ImageSizeLimitationForm
from django.shortcuts import get_object_or_404,redirect,reverse

class GoodsCreate(generic.CreateView):
    form_class = GoodsCreateForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_create'


class GoodsList(generic.ListView):
    model = Goods
    template_name = 'crud/goods_list.html'


class GoodsDetail(generic.DetailView):
    model = Goods
    template_name = 'crud/goods_detail.html'

class GoodsUpdate(generic.UpdateView):
    model = Goods
    form_class = GoodsUpdateForm
    template_name = 'crud/goods_update.html'
    success_url = '/crud/goods_list'


class GoodsDelete(generic.DeleteView):
    model = Goods
    template_name = 'crud/goods_delete.html'
    success_url = '/crud/goods_list'


class GoodsCreateWithImageSizeLimitation(generic.CreateView):
    form_class = ImageSizeLimitationForm
    template_name = 'crud/goods_create.html'
    success_url = '/crud/goods_list'


class CustomDelete(generic.DeleteView):
    def post(self, request, *args, **kwargs):
        goods_item = get_object_or_404(Goods, pk=kwargs['pk'])
        goods_item.custom_delete()
        return redirect(reverse('crud:goods_list'))

    def get_queryset(self):
        return Goods.objects.all()