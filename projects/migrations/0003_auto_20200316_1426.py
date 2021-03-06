# Generated by Django 2.0.3 on 2020-03-16 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200316_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '请求头配置',
                'verbose_name_plural': '请求头配置',
            },
        ),
        migrations.CreateModel(
            name='ProjectVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '项目变量',
                'verbose_name_plural': '项目变量',
            },
        ),
        migrations.RemoveField(
            model_name='env',
            name='variables',
        ),
        migrations.DeleteModel(
            name='Variable',
        ),
    ]
