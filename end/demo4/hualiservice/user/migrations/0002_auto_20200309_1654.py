# Generated by Django 3.0.4 on 2020-03-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='headImg',
            field=models.ImageField(default='head/default_head.png', upload_to='head/', verbose_name='头像'),
        ),
    ]