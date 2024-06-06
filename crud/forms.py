from django import forms
from .models import Goods

class GoodsCreateForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 
                'price', 'release_date', 
                'release_flag', 'description', 'image')


class GoodsUpdateForm(forms.ModelForm):
    class Meta:
        model =Goods
        fields = ('name', 'management_code', 
                'price', 'release_date', 
                'release_flag', 'description', 'image')


class ImageSizeLimitationForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ('name', 'management_code', 'price', 'release_date', 'release_flag', 'description', 'image')

    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image.size > 10 * 1024:
                raise forms.ValidationError(" ファイルサイズが大きすぎます")
            return image