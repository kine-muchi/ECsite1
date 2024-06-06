from django import forms
from .models import GoodsGroup, CustomGoods

class GroupCreationForm(forms.ModelForm):
    class Meta:
        model = GoodsGroup
        fields = ("name",)


class CustomGoodsCreationForm(forms.ModelForm):
    class Meta:
        model = CustomGoods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image', 'group')


class CustomGoodsSearchForm(forms.Form):
    group = forms.ModelChoiceField(queryset=GoodsGroup.objects, label='グループ', required=False, empty_label='選択してください')
    name = forms.CharField(label='商品名', required=False)
    management_code = forms.CharField(label='管理コード', required=False)
    price_begin = forms.IntegerField(label='価格下限', required=False)
    price_end = forms.IntegerField(label='価格上限', required=False)

