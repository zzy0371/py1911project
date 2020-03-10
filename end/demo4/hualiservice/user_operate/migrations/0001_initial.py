# Generated by Django 3.0.4 on 2020-03-09 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flower', '0002_auto_20200309_1731'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveIntegerField(default=0, verbose_name='评星')),
                ('comment', models.CharField(max_length=200, verbose_name='评论')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.Flower', verbose_name='鲜花')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='CommentImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='commentimg/', verbose_name='评论图')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_operate.Comment', verbose_name='评论')),
            ],
        ),
        migrations.CreateModel(
            name='Collect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='收藏时间')),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.Flower', verbose_name='鲜花')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]