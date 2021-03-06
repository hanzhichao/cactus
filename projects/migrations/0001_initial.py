# Generated by Django 2.0.3 on 2020-03-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('domain', models.CharField(max_length=500, verbose_name='域名')),
            ],
            options={
                'verbose_name': '环境',
                'verbose_name_plural': '环境',
            },
        ),
        migrations.CreateModel(
            name='EnvHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Env', verbose_name='环境')),
            ],
            options={
                'verbose_name': '请求头配置',
                'verbose_name_plural': '请求头配置',
            },
        ),
        migrations.CreateModel(
            name='EnvVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
                ('env', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Env', verbose_name='环境')),
            ],
            options={
                'verbose_name': '环境变量',
                'verbose_name_plural': '环境变量',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.AddField(
            model_name='env',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目'),
        ),
    ]
