# Generated by Django 2.0.3 on 2020-03-13 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('projects', '0002_auto_20200313_2355'),
        ('apis', '0003_auto_20200314_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('file_path', models.FilePathField(verbose_name='上传文件')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
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
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('content_type', models.CharField(choices=[('text/plain', '纯文本'), ('text/html', 'HTML'), ('application/xml', 'XML'), ('application/json', 'JSON')], default='text/plain', max_length=100, verbose_name='内容类型')),
                ('data', models.TextField(verbose_name='请求数据')),
            ],
            options={
                'verbose_name': 'Raw请求数据',
                'verbose_name_plural': 'Raw请求数据',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例',
            },
        ),
        migrations.CreateModel(
            name='TestStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.Api', verbose_name='接口')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestCase', verbose_name='测试用例')),
            ],
            options={
                'verbose_name': '测试步骤',
                'verbose_name_plural': '测试步骤',
            },
        ),
        migrations.CreateModel(
            name='TestSuite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='描述')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project', verbose_name='项目')),
            ],
            options={
                'verbose_name': '测试套件',
                'verbose_name_plural': '测试套件',
            },
        ),
        migrations.AddField(
            model_name='testcase',
            name='suite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestSuite', verbose_name='测试套件'),
        ),
        migrations.AddField(
            model_name='rawdata',
            name='step',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='paramvariable',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='multipartvariable',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='jsonvariable',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='headervariable',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='formvariable',
            name='step',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
        migrations.AddField(
            model_name='binarydata',
            name='step',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cases.TestStep', verbose_name='测试步骤'),
        ),
    ]
