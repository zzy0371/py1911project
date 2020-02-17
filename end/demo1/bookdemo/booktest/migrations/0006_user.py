# Generated by Django 3.0.3 on 2020-02-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0005_auto_20200215_0959'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码')),
            ],
            options={
                'verbose_name': '用户模型类',
                'verbose_name_plural': '用户模型类',
                'db_table': '用户类',
                'ordering': ['id'],
            },
        ),
    ]