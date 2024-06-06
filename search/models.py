from django.db import models
from django.core.validators import MaxValueValidator

class GoodsGroup(models.Model):
    name = models.CharField('商品グループ',unique=True, max_length=10, null=True)

    def __str__(self):
        return self.name


class CustomGoods(models.Model):
    name = models.CharField('商品名', unique=True, max_length=100, null=True)
    management_code = models.CharField('管理コード', unique=True, max_length=20)
    price = models.IntegerField('価格', validators=[MaxValueValidator(1000000000)])
    release_date = models.DateField('発売日', blank=True, null=True)
    release_flag = models.BooleanField('発売済み', default=False)
    description = models.CharField('説明', max_length=100000)
    image = models.ImageField('画像', null=True, blank=True, upload_to='goods_images/')
    state_flag = models.BooleanField('運用状況', default=True)
    group = models.ForeignKey(GoodsGroup, on_delete=models.CASCADE, verbose_name='商品グループ')

    def __str__(self):
        return self.name
