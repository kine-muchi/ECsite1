from django.shortcuts import render
from django.views import generic
from .models import GoodsGroup, CustomGoods
from .forms import GroupCreationForm, CustomGoodsCreationForm, CustomGoodsSearchForm


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


class CustomGoodsList(generic.ListView):
    model = CustomGoods
    form_class = CustomGoodsSearchForm
    template_name = 'search/custom_goods_list.html'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(generic.ListView, self).get_context_data(**kwargs)
        context.update(dict(form=self.form_class, query_string=self.request.GET.urlencode()))

        q_name = self.request.GET.get('name')
        q_management_code = self.request.GET.get('management_code')
        q_group = self.request.GET.get('group')
        q_price_begin = self.request.GET.get('price_begin')
        q_price_end = self.request.GET.get('price_end')

        context['form'] = CustomGoodsSearchForm(initial={
            'name': q_name, 'management_code': q_management_code, 'group': q_group, 'price_begin': q_price_begin,
            'price_end': q_price_end})

        return context


    def get_queryset(self):
        customgoods = CustomGoods.objects.all().select_related('group')
        q_name = self.request.GET.get('name')
        q_management_code = self.request.GET.get('management_code')
        q_group = self.request.GET.get('group')
        q_price_begin = self.request.GET.get('price_begin')
        q_price_end = self.request.GET.get('price_end')

        if q_name:
            customgoods = customgoods.filter(name__icontains=q_name)
        if q_management_code:
            customgoods = customgoods.filter(management_code__icontains=q_management_code)
        if q_group:
            customgoods = customgoods.filter(group=q_group)
        if q_price_begin:
            customgoods = customgoods.filter(price__gte=q_price_begin)
        if q_price_end:
            customgoods = customgoods.filter(price__lte=q_price_end)

        return customgoods

