from django.db import models
from django.core.validators import MaxValueValidator

class Goods(models.Model):
    name = models.CharField('商品名', unique=True, max_length=10, null=True)
    management_code = models.CharField('管理コード', unique=True, max_length=20)
    price = models.PositiveIntegerField('価格', validators=[MaxValueValidator(1000000000)])
    release_date = models.DateField('発売日', blank=True, null=True)
    release_flag = models.BooleanField('発売済み', default=False)
    description = models.CharField('商品説明', max_length=100000)
    image = models.ImageField('商品画像', null=True, blank=True, upload_to='goods_images/')
    state_flag = models.BooleanField('運用状況', default=True)

    def __str__(self):
        return self.name
    
    def custom_delete(self):
        self.state_flag = False
        self.save()