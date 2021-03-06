# Generated by Django 4.0.4 on 2022-06-12 01:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_alter_booking_checkintime_alter_booking_stayplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='loginuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='booking',
            name='age',
            field=models.IntegerField(choices=[('10-17', '10-17才'), ('18-19', '18-19才'), ('20-24', '20-24才'), ('25-29', '25-29才'), ('30-34', '30-34才'), ('35-39', '35-39才'), ('40-49', '40-49才'), ('50-59', '50-59才'), ('60', '60才以上')], verbose_name='年代'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkintime',
            field=models.TimeField(choices=[('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00'), ('22:00', '22:00'), ('23:00', '23:00'), ('24:00', '24:00')], verbose_name='チェックイン予定時間'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='prefecture',
            field=models.IntegerField(choices=[(1, '北海道'), (2, '青森県'), (3, '岩手県'), (4, '宮城県'), (5, '秋田県'), (6, '山形県'), (7, '福島県'), (8, '茨城県'), (9, '栃木県'), (10, '群馬県'), (11, '埼玉県'), (12, '千葉県'), (13, '東京都'), (14, '神奈川県'), (15, '新潟県'), (16, '富山県'), (17, '石川県'), (18, '福井県'), (19, '山梨県'), (20, '長野県'), (21, '岐阜県'), (22, '静岡県'), (23, '愛知県'), (24, '三重県'), (25, '滋賀県'), (26, '京都府'), (27, '大阪府'), (28, '兵庫県'), (29, '奈良県'), (30, '和歌山県'), (31, '鳥取県'), (32, '島根県'), (33, '岡山県'), (34, '広島県'), (35, '山口県'), (36, '徳島県'), (37, '香川県'), (38, '愛媛県'), (39, '高知県'), (40, '福岡県'), (41, '佐賀県'), (42, '長崎県'), (43, '熊本県'), (44, '大分県'), (45, '宮崎県'), (46, '鹿児島県'), (47, '沖縄県')], verbose_name='住所(都道府県)'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='stay',
            field=models.IntegerField(choices=[('1', '1泊'), ('2', '2泊'), ('3', '3泊'), ('4', '4泊'), ('5', '5泊'), ('6', '6泊'), ('7', '7泊'), ('8', '8泊'), ('9', '9泊')], verbose_name='泊数'),
        ),
        migrations.AlterField(
            model_name='bookingplan',
            name='end_reception',
            field=models.DateField(verbose_name='受付終了日'),
        ),
        migrations.AlterField(
            model_name='bookingplan',
            name='start_reception',
            field=models.DateField(verbose_name='受付開始日'),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
