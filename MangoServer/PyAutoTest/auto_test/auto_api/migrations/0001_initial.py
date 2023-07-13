# Generated by Django 4.1.5 on 2023-07-13 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_user', '0001_initial'),
        ('auto_system', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(verbose_name='接口的类型')),
                ('name', models.CharField(max_length=64, verbose_name='用例名称')),
                ('client', models.SmallIntegerField(verbose_name='什么端')),
                ('method', models.SmallIntegerField(verbose_name='请求方法')),
                ('url', models.CharField(max_length=1024, verbose_name='请求url')),
                ('header', models.CharField(max_length=2048, null=True, verbose_name='请求头')),
                ('body', models.TextField(null=True, verbose_name='请求数据')),
                ('body_type', models.SmallIntegerField(null=True, verbose_name='请求数据类型')),
                ('rely', models.CharField(max_length=100, null=True, verbose_name='依赖的用例id')),
                ('ass', models.SmallIntegerField(null=True, verbose_name='断言')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_case',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiCaseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='测试组名称')),
                ('case_id', models.CharField(max_length=1048, null=True, verbose_name='存放组内所有用例ID')),
                ('case_name', models.CharField(max_length=1048, null=True, verbose_name='存放组内所有用例名称')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
                ('time_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.timetasks')),
            ],
            options={
                'db_table': 'api_case_group',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('request_url', models.CharField(max_length=1048, null=True, verbose_name='请求的url')),
                ('request_header', models.TextField(null=True, verbose_name='请求头')),
                ('request_body', models.TextField(null=True, verbose_name='请求体')),
                ('response_header', models.TextField(null=True, verbose_name='响应头')),
                ('response_body', models.TextField(null=True, verbose_name='响应体')),
                ('code', models.IntegerField(null=True, verbose_name='响应的code码')),
                ('response_time', models.TimeField(null=True, verbose_name='响应时间')),
                ('ass_res', models.SmallIntegerField(null=True, verbose_name='断言结果')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase')),
                ('case_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicasegroup')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.testobject')),
            ],
            options={
                'db_table': 'api_result',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='公共类型')),
                ('client', models.SmallIntegerField(null=True, verbose_name='什么端')),
                ('public_type', models.SmallIntegerField(null=True, verbose_name='值的类型')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('key', models.CharField(max_length=128, null=True, verbose_name='键')),
                ('value', models.CharField(max_length=2048, null=True, verbose_name='值')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_public',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiAssertions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='依赖名称')),
                ('ass_type', models.SmallIntegerField(null=True, verbose_name='依赖类型')),
                ('value', models.CharField(max_length=1048, null=True, verbose_name='值')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_ass',
                'ordering': ['-id'],
            },
        ),
    ]
