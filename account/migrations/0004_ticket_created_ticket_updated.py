# Generated by Django 4.0.3 on 2022-03-09 07:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='تاریخ ایجاد'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='تاریخ آخرین ویرایش'),
        ),
    ]