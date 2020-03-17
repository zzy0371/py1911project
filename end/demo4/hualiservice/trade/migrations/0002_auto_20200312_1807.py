# Generated by Django 3.0.4 on 2020-03-12 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trade', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flower', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='cart',
            name='flower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flower.Flower', verbose_name='鲜花'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterUniqueTogether(
            name='orderdetail',
            unique_together={('order', 'flower')},
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'flower')},
        ),
    ]
