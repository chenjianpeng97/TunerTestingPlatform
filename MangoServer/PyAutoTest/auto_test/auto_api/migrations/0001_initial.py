# Generated by Django 4.1.5 on 2024-04-28 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='测试用例名称')),
                ('case_flow', models.CharField(max_length=2000, null=True, verbose_name='步骤顺序')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('level', models.SmallIntegerField(null=True, verbose_name='用例级别')),
                ('front_custom', models.JSONField(null=True, verbose_name='前置自定义')),
                ('front_sql', models.JSONField(null=True, verbose_name='前置sql')),
                ('posterior_sql', models.JSONField(null=True, verbose_name='后置sql')),
                ('case_people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user', verbose_name='用例责任人')),
                ('module_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectmodule')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_case',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiCaseDetailed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('case_sort', models.IntegerField(null=True, verbose_name='用例排序')),
                ('url', models.CharField(max_length=1024, null=True, verbose_name='请求url')),
                ('header', models.TextField(max_length=2048, null=True, verbose_name='请求头')),
                ('params', models.JSONField(null=True, verbose_name='参数')),
                ('data', models.JSONField(null=True, verbose_name='data')),
                ('json', models.JSONField(null=True, verbose_name='json')),
                ('file', models.JSONField(null=True, verbose_name='file')),
                ('front_sql', models.JSONField(null=True, verbose_name='前置sql')),
                ('ass_sql', models.JSONField(null=True, verbose_name='sql断言')),
                ('ass_response_whole', models.TextField(null=True, verbose_name='响应全匹配断言')),
                ('ass_response_value', models.JSONField(null=True, verbose_name='响应值断言')),
                ('posterior_sql', models.JSONField(null=True, verbose_name='后置sql')),
                ('posterior_response', models.JSONField(null=True, verbose_name='后置响应处理')),
                ('posterior_sleep', models.CharField(max_length=64, null=True, verbose_name='步骤顺序')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
            ],
            options={
                'db_table': 'api_case_detailed',
            },
        ),
        migrations.CreateModel(
            name='ApiInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(verbose_name='接口的类型')),
                ('name', models.CharField(max_length=1024, verbose_name='接口名称')),
                ('client', models.SmallIntegerField(verbose_name='什么端')),
                ('url', models.CharField(max_length=1024, verbose_name='请求url')),
                ('method', models.SmallIntegerField(verbose_name='请求方法')),
                ('header', models.JSONField(max_length=2048, null=True, verbose_name='请求头')),
                ('params', models.JSONField(null=True, verbose_name='参数')),
                ('data', models.JSONField(null=True, verbose_name='data')),
                ('json', models.JSONField(null=True, verbose_name='json')),
                ('file', models.JSONField(null=True, verbose_name='file')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('module_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectmodule')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_info',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='自定义变量类型')),
                ('client', models.SmallIntegerField(null=True, verbose_name='什么端')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('key', models.CharField(max_length=128, null=True, verbose_name='键')),
                ('value', models.CharField(max_length=2048, null=True, verbose_name='值')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'api_public',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ApiInfoResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('case_sort', models.IntegerField(null=True, verbose_name='用例排序')),
                ('url', models.TextField(null=True, verbose_name='请求url')),
                ('headers', models.TextField(null=True, verbose_name='请求头')),
                ('params', models.TextField(null=True, verbose_name='参数')),
                ('data', models.TextField(null=True, verbose_name='data')),
                ('json', models.TextField(null=True, verbose_name='json')),
                ('file', models.TextField(null=True, verbose_name='file')),
                ('response_code', models.CharField(max_length=64, null=True, verbose_name='响应code码')),
                ('response_time', models.CharField(max_length=64, null=True, verbose_name='响应时间')),
                ('response_headers', models.TextField(null=True, verbose_name='响应headers')),
                ('response_text', models.TextField(null=True, verbose_name='响应文本')),
                ('response_json', models.TextField(null=True, verbose_name='响应文本json对象')),
                ('status', models.SmallIntegerField(null=True, verbose_name='断言结果')),
                ('error_message', models.CharField(max_length=1024, null=True, verbose_name='失败原因')),
                ('all_cache', models.TextField(null=True, verbose_name='执行到这个用例时的缓存数据')),
                ('assertion', models.TextField(null=True, verbose_name='断言')),
                ('api_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apiinfo')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase')),
                ('case_detailed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicasedetailed')),
            ],
            options={
                'db_table': 'api_info_result',
            },
        ),
        migrations.CreateModel(
            name='ApiCaseResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('status', models.SmallIntegerField(null=True, verbose_name='断言结果')),
                ('error_message', models.CharField(max_length=1024, null=True, verbose_name='失败原因')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase')),
            ],
            options={
                'db_table': 'api_case_result',
            },
        ),
        migrations.AddField(
            model_name='apicasedetailed',
            name='api_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apiinfo'),
        ),
        migrations.AddField(
            model_name='apicasedetailed',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase'),
        ),
    ]
