# Generated by Django 2.0.3 on 2020-03-16 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='env',
            name='variables',
            field=models.ManyToManyField(to='projects.Variable', verbose_name='环境变量'),
        ),
    ]
