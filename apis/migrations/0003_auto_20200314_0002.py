# Generated by Django 2.0.3 on 2020-03-13 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_auto_20200313_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apidoc',
            options={'verbose_name': '接口文档', 'verbose_name_plural': '接口文档'},
        ),
        migrations.RemoveField(
            model_name='apidoc',
            name='description',
        ),
        migrations.RemoveField(
            model_name='apidoc',
            name='name',
        ),
    ]
