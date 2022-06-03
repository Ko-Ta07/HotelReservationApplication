from cProfile import label
from distutils.command.upload import upload
from accounts.models import CustomUser
from django.db import models
from django.utils import timezone

# 宿泊施設情報モデルクラス
class Hotel(models.Model):
    name = models.CharField('宿泊施設名称', max_length=100)
    address = models.CharField('住所', max_length=100)
    tel = models.CharField('電話番号', max_length=100)
    description = models.TextField('施設説明', default='', blank=True)
    image = models.ImageField(upload_to='images', verbose_name='施設イメージ画像', null=True, blank=True)
    spa = models.BooleanField(verbose_name='温泉',default=True)
    highclass = models.BooleanField(verbose_name='ハイクラスホテル',default=True)
    ido = models.FloatField(verbose_name='緯度', null=True, blank=True, default=0)
    keido = models.FloatField(verbose_name='経度', null=True, blank=True, default=0)
    
    def __str__(self):
        return self.name

# スタッフモデルクラス
class Staff(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name='スタッフ', on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, verbose_name='店舗', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.hotel}:{self.user}' 
    
# 部屋タイプモデルクラス
class Room(models.Model):
    hotel = models.ForeignKey(Hotel, verbose_name='宿泊施設名称',on_delete=models.CASCADE)
    roomtype = models.IntegerField(verbose_name='部屋のタイプ')
    image = models.ImageField(upload_to='images', verbose_name='部屋イメージ画像', null=True, blank=True)
    name = models.CharField('宿泊者氏名',max_length=100)
    number_of_guest = models.IntegerField(verbose_name='宿泊人数')
    roomcharge = models.IntegerField(verbose_name='金額')
    no_smoking = models.BooleanField(verbose_name='禁煙ルーム',default=True)
    outdoor_bath = models.BooleanField(verbose_name='露天風呂',default=True)
    
    def __str__(self):
        return self.hotel

# 宿泊プランモデルクラス
class BookingPlan(models.Model):
    planname = models.CharField('プラン名', max_length=100)
    description = models.TextField('プラン説明', default='')
    roomcharge = models.IntegerField(verbose_name='金額')
    start_reception = models.DateField(verbose_name='受付開始日')
    end_reception = models.DateField(verbose_name='受付終了日')
    image = models.ImageField(upload_to='images', verbose_name='部屋イメージ画像', null=True, blank=True)
    room = models.ManyToManyField(Room, blank=True)    # ManytoManyFieldの紐づけ先が違う？
    
    def __str__(self):
        return self.planname
    
# 予約フォームモデルクラス
class Booking(models.Model):
    stayplan = models.ForeignKey(BookingPlan, verbose_name='宿泊プラン', on_delete=models.CASCADE)
    checkindate = models.DateField(verbose_name='チェックイン日')
    stay = models.IntegerField(verbose_name='泊数')
    checkintime = models.TimeField(verbose_name='チェックイン予定時間')
    number_of_rooms = models.IntegerField(verbose_name='部屋数')
    number_of_guests = models.IntegerField(verbose_name='宿泊人数')
    first_name = models.CharField('宿泊者氏名(姓)', max_length=100)
    last_name = models.CharField('宿泊者氏名(名)', max_length=100)
    first_name_kana = models.CharField('宿泊者氏名(姓カナ)', max_length=100)
    last_name_kana = models.CharField('宿泊者氏名(名カナ)', max_length=100)
    post = models.CharField('住所(郵便番号)', max_length=10)
    prefecture = models.IntegerField(verbose_name='住所(都道府県)')
    address = models.CharField('住所(市町村名・番地)', max_length=100)
    tel = models.CharField('電話番号', max_length=15)
    age = models.IntegerField(verbose_name='年代')
    email = models.EmailField(verbose_name='メールアドレス')
    remarks = models.TextField('その他備考欄', default='', blank=True)
   #loginuser = models.Foreignkey()  紐づけ先が分からないので一旦コメントアウト
   
    def __str__(self):
        return self.stayplan
