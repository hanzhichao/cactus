# Generated by Django 2.0.3 on 2020-03-14 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
        ('projects', '0001_initial'),
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('markdown', models.TextField(default='', verbose_name='内容')),
            ],
            options={
                'verbose_name': '接口文档',
                'verbose_name_plural': '接口文档',
            },
        ),
        migrations.CreateModel(
            name='ApiGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '接口组',
                'verbose_name_plural': '接口组',
            },
        ),
        migrations.CreateModel(
            name='BinaryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('file_path', models.FileField(upload_to='', verbose_name='上传文件')),
            ],
            options={
                'verbose_name': '复合表单参数',
                'verbose_name_plural': '复合表单参数',
            },
        ),
        migrations.CreateModel(
            name='FormVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'verbose_name': '表单参数',
                'verbose_name_plural': '表单参数',
            },
        ),
        migrations.CreateModel(
            name='HeaderVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'verbose_name': '请求头',
                'verbose_name_plural': '请求头',
            },
        ),
        migrations.CreateModel(
            name='JSONVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'verbose_name': 'JSON参数',
                'verbose_name_plural': 'JSON参数',
            },
        ),
        migrations.CreateModel(
            name='MultipartVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'verbose_name': '复合表单参数',
                'verbose_name_plural': '复合表单参数',
            },
        ),
        migrations.CreateModel(
            name='ParamVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('value', models.CharField(max_length=200, verbose_name='变量值')),
            ],
            options={
                'verbose_name': 'URL参数',
                'verbose_name_plural': 'URL参数',
            },
        ),
        migrations.CreateModel(
            name='RawData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('key', models.CharField(max_length=200, verbose_name='变量')),
                ('content_type', models.CharField(choices=[('text/plain', '纯文本'), ('text/html', 'HTML'), ('application/xml', 'XML'), ('application/json', 'JSON')], default='text/plain', max_length=100, verbose_name='内容类型')),
                ('data', models.TextField(verbose_name='请求数据')),
            ],
            options={
                'verbose_name': 'Raw请求数据',
                'verbose_name_plural': 'Raw请求数据',
            },
        ),
        migrations.CreateModel(
            name='RequestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
            options={
                'verbose_name': '请求数据',
                'verbose_name_plural': '请求数据',
            },
        ),
        migrations.AddField(
            model_name='api',
            name='data_type',
            field=models.CharField(choices=[('none', '无'), ('form', '表单'), ('json', 'JSON'), ('raw', '原始'), ('multipart', '复合表单'), ('binary', '二进制')], default='none', max_length=15, verbose_name='内容类型'),
        ),
        migrations.AddField(
            model_name='api',
            name='method',
            field=models.CharField(choices=[('get', 'GET'), ('post', 'POST'), ('put', 'PUT'), ('delete', 'DELETE'), ('head', 'HEAD'), ('patch', 'PATCH'), ('options', 'OPTIONS')], default='get', max_length=10, verbose_name='请求方法'),
        ),
        migrations.AddField(
            model_name='api',
            name='path',
            field=models.CharField(default=1, max_length=200, verbose_name='接口路径'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requestdata',
            name='api',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apis.Api', verbose_name='接口'),
        ),
        migrations.AddField(
            model_name='requestdata',
            name='step',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='paramvariable',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='multipartvariable',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='jsonvariable',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='headervariable',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='formvariable',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='binarydata',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.RequestData', verbose_name='请求数据'),
        ),
        migrations.AddField(
            model_name='apidoc',
            name='api',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apis.Api', verbose_name='接口'),
        ),
        migrations.AddField(
            model_name='api',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apis.ApiGroup', verbose_name='接口组'),
            preserve_default=False,
        ),
    ]
