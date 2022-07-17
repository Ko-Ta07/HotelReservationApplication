from accounts.models import CustomUser
from django.db import models
import datetime

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
  
# 部屋タイプモデルクラス
class Room(models.Model):
    ROOMTYPE_CHOICES = [(1,'シングル'), (2,'ツイン'), (3,'ダブル'), (4,'キング')]
    hotel = models.ForeignKey(Hotel, verbose_name='宿泊施設名称',on_delete=models.CASCADE)
    roomtype = models.IntegerField(verbose_name='部屋のタイプ', choices=ROOMTYPE_CHOICES)
    image = models.ImageField(upload_to='images', verbose_name='部屋イメージ画像', null=True, blank=True)
    name = models.CharField('部屋名',max_length=100)
    number_of_guest = models.IntegerField(verbose_name='宿泊人数')
    roomcharge = models.IntegerField(verbose_name='大人1名(税込)')
    total_amount = models.IntegerField(verbose_name='合計(税込)', default=None, null=True)
    no_smoking = models.BooleanField(verbose_name='禁煙ルーム',default=True)
    outdoor_bath = models.BooleanField(verbose_name='露天風呂',default=True)
    
    def __str__(self):
        return f'{self.name}（{self.hotel}）' 

# 宿泊プランモデルクラス
class BookingPlan(models.Model):
    MEAL_CHOICES = [(1,'食事なし'), (2,'朝のみ'), (3,'朝・夕')]
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None, null=True)
    planname = models.CharField('プラン名', max_length=100)
    meal = models.IntegerField(verbose_name='食事', choices=MEAL_CHOICES, default=1)
    checkin = models.TimeField(verbose_name='チェックイン', default='15:00')
    checkout = models.TimeField(verbose_name='チェックアウト', default='11:00')
    short_description = models.TextField('プラン概要', default='')
    description = models.TextField('プラン説明', default='')
    roomcharge = models.IntegerField(verbose_name='大人1名(税込)')
    total_amount = models.IntegerField(verbose_name='合計(税込)', default=None, null=True)
    start_reception = models.DateField(verbose_name='受付開始日')
    end_reception = models.DateField(verbose_name='受付終了日')
    image = models.ImageField(upload_to='images', verbose_name='プランイメージ画像', null=True, blank=True)
    room = models.ManyToManyField(Room, blank=True)    
    
    def __str__(self):
        return self.planname
    
# 予約フォームモデルクラス
class Booking(models.Model):
    STAYDAY_CHOICES = [(1,'1泊'), (2,'2泊'), (3,'3泊'), (4,'4泊'), 
                       (5,'5泊'), (6,'6泊'), (7,'7泊'), (8,'8泊'), (9,'9泊'),]
    
    CHECKIN_TIME_CHOICES = [(datetime.time(14, 0),'14:00'), (datetime.time(15, 0),'15:00'), (datetime.time(16, 0),'16:00'), (datetime.time(17, 0),'17:00'),
                            (datetime.time(18, 0),'18:00'), (datetime.time(19, 0),'19:00'), (datetime.time(20, 0),'20:00'), (datetime.time(21, 0),'21:00'), 
                            (datetime.time(22, 0),'22:00'), (datetime.time(23, 0),'23:00'), ]#(datetime.time(24, 0),'24:00')]
    
    PREF_CHOICES = [(1,'北海道'), (2,'青森県'), (3,'岩手県'), (4,'宮城県'), (5,'秋田県'),
                    (6,'山形県'), (7,'福島県'), (8,'茨城県'), (9,'栃木県'), (10,'群馬県'),
                    (11,'埼玉県'), (12,'千葉県'), (13,'東京都'), (14,'神奈川県'), (15,'新潟県'),
                    (16,'富山県'), (17,'石川県'), (18,'福井県'), (19,'山梨県'), (20,'長野県'),
                    (21,'岐阜県'), (22,'静岡県'), (23,'愛知県'), (24,'三重県'), (25,'滋賀県'),
                    (26,'京都府'), (27,'大阪府'), (28,'兵庫県'), (29,'奈良県'), (30,'和歌山県'),
                    (31,'鳥取県'), (32,'島根県'), (33,'岡山県'), (34,'広島県'), (35,'山口県'),
                    (36,'徳島県'), (37,'香川県'), (38,'愛媛県'), (39,'高知県'), (40,'福岡県'),
                    (41,'佐賀県'), (42,'長崎県'), (43,'熊本県'), (44,'大分県'), (45,'宮崎県'),
                    (46,'鹿児島県'), (47,'沖縄県')]
    
    AGE_CHOICES = [(1,'10-17才'), (2,'18-19才'), (3,'20-24才'), (4,'25-29才'),
                   (5,'30-34才'), (6,'35-39才'), (7,'40-49才'), (8,'50-59才'),
                   (9,'60才以上'),]
    
    stayplan = models.ForeignKey(BookingPlan, verbose_name='宿泊プラン', on_delete=models.CASCADE)
    checkindate = models.DateField(verbose_name='チェックイン日')
    stay = models.IntegerField(verbose_name='泊数', choices=STAYDAY_CHOICES)
    checkintime = models.TimeField(verbose_name='チェックイン予定時間', choices=CHECKIN_TIME_CHOICES)
    number_of_rooms = models.IntegerField(verbose_name='部屋数')
    number_of_guests = models.IntegerField(verbose_name='宿泊人数')
    first_name = models.CharField('宿泊者氏名(姓)', max_length=100)
    last_name = models.CharField('宿泊者氏名(名)', max_length=100)
    first_name_kana = models.CharField('宿泊者氏名(姓カナ)', max_length=100)
    last_name_kana = models.CharField('宿泊者氏名(名カナ)', max_length=100)
    post = models.CharField('住所(郵便番号)', max_length=10)
    prefecture = models.IntegerField(verbose_name='住所(都道府県)', choices=PREF_CHOICES)
    address = models.CharField('住所(市町村名・番地)', max_length=100)
    tel = models.CharField('電話番号', max_length=15)
    age = models.IntegerField(verbose_name='年代', choices=AGE_CHOICES)
    email = models.EmailField(verbose_name='メールアドレス')
    remarks = models.TextField('その他備考欄', default='', blank=True)
    loginuser = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE) 
   
    def __str__(self):
        return self.first_name + self.last_name