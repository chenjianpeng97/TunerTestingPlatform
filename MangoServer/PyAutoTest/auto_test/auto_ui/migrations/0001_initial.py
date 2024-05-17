# Generated by Django 4.1.5 on 2024-05-17 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UiCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='用例组名称')),
                ('case_flow', models.CharField(max_length=2000, null=True, verbose_name='步骤顺序')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('level', models.SmallIntegerField(null=True, verbose_name='用例级别')),
                ('front_custom', models.JSONField(null=True, verbose_name='前置自定义')),
                ('front_sql', models.JSONField(null=True, verbose_name='前置sql')),
                ('posterior_sql', models.JSONField(null=True, verbose_name='后置sql')),
                ('case_people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user', verbose_name='用例责任人')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.productmodule')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
            ],
            options={
                'db_table': 'ui_case',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiCaseResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('case_id', models.IntegerField(null=True, verbose_name='用例ID')),
                ('case_name', models.CharField(max_length=64, null=True, verbose_name='用例名称')),
                ('module_name', models.CharField(max_length=64, null=True, verbose_name='模块名称')),
                ('case_people', models.CharField(max_length=64, null=True, verbose_name='负责人名称')),
                ('test_obj', models.CharField(max_length=1024, null=True, verbose_name='测试环境')),
                ('case_cache_data', models.JSONField(null=True, verbose_name='用例缓存数据')),
                ('status', models.SmallIntegerField(null=True, verbose_name='用例测试结果')),
                ('error_message', models.TextField(null=True, verbose_name='错误提示')),
            ],
            options={
                'db_table': 'ui_case_result',
            },
        ),
        migrations.CreateModel(
            name='UiElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='元素名称')),
                ('exp', models.SmallIntegerField(verbose_name='元素表达式')),
                ('loc', models.CharField(max_length=1048, null=True, verbose_name='元素定位')),
                ('sleep', models.IntegerField(null=True, verbose_name='等待时间')),
                ('sub', models.IntegerField(null=True, verbose_name='下标')),
                ('is_iframe', models.SmallIntegerField(null=True, verbose_name='是否在iframe里面')),
            ],
            options={
                'db_table': 'ui_ele',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiEleResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('case_id', models.IntegerField(null=True, verbose_name='用例ID')),
                ('page_step_id', models.IntegerField(null=True, verbose_name='步骤id')),
                ('ele_name', models.CharField(max_length=64, null=True, verbose_name='元素名称')),
                ('ele_quantity', models.SmallIntegerField(null=True, verbose_name='元素个数')),
                ('status', models.SmallIntegerField(null=True, verbose_name='元素测试结果')),
                ('picture_path', models.CharField(max_length=1000, null=True, verbose_name='用例名称')),
                ('exp', models.SmallIntegerField(null=True, verbose_name='元素表达式')),
                ('loc', models.CharField(max_length=1048, null=True, verbose_name='元素定位')),
                ('sleep', models.IntegerField(null=True, verbose_name='等待时间')),
                ('sub', models.IntegerField(null=True, verbose_name='下标')),
                ('ope_type', models.CharField(max_length=1048, null=True, verbose_name='对该元素的操作类型')),
                ('ope_value', models.JSONField(max_length=1048, null=True, verbose_name='操作内容')),
                ('ass_type', models.CharField(max_length=1048, null=True, verbose_name='断言类型')),
                ('ass_value', models.JSONField(max_length=1048, null=True, verbose_name='操作内容')),
                ('error_message', models.CharField(max_length=2048, null=True, verbose_name='元素错误提示语')),
                ('expect', models.TextField(null=True, verbose_name='预期')),
                ('actual', models.TextField(null=True, verbose_name='实际')),
            ],
            options={
                'db_table': 'ui_ele_result',
            },
        ),
        migrations.CreateModel(
            name='UiPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_Time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='页面名称')),
                ('url', models.CharField(max_length=128, verbose_name='url')),
                ('type', models.SmallIntegerField(verbose_name='页面是什么端')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.productmodule')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
            ],
            options={
                'db_table': 'ui_page',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiPageSteps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='步骤名称')),
                ('run_flow', models.CharField(max_length=2000, null=True, verbose_name='步骤顺序')),
                ('type', models.SmallIntegerField(null=True, verbose_name='步骤类型')),
                ('module', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.productmodule')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipage')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
            ],
            options={
                'db_table': 'ui_page_steps',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiPageStepsResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('test_suite_id', models.BigIntegerField(null=True, verbose_name='测试套件id')),
                ('case_id', models.IntegerField(null=True, verbose_name='用例ID')),
                ('page_step_id', models.IntegerField(null=True, verbose_name='步骤id')),
                ('page_step_name', models.CharField(max_length=64, null=True, verbose_name='步骤名称')),
                ('status', models.SmallIntegerField(null=True, verbose_name='步骤测试结果')),
                ('error_message', models.TextField(null=True, verbose_name='错误提示')),
            ],
            options={
                'db_table': 'ui_page_steps_result',
            },
        ),
        migrations.CreateModel(
            name='UiPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='自定义变量类型')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('key', models.CharField(max_length=128, null=True, verbose_name='键')),
                ('value', models.CharField(max_length=2048, null=True, verbose_name='值')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
            ],
            options={
                'db_table': 'ui_public',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiPageStepsDetailed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('step_sort', models.IntegerField(null=True, verbose_name='顺序的排序')),
                ('ope_type', models.CharField(max_length=1048, null=True, verbose_name='对该元素的操作类型')),
                ('ope_value', models.JSONField(null=True, verbose_name='操作内容')),
                ('type', models.SmallIntegerField(null=True, verbose_name='操作类型')),
                ('ass_type', models.CharField(max_length=1048, null=True, verbose_name='断言类型')),
                ('ass_value', models.JSONField(null=True, verbose_name='操作内容')),
                ('key_list', models.JSONField(null=True, verbose_name='sql查询结果的key_list')),
                ('sql', models.CharField(max_length=1048, null=True, verbose_name='sql')),
                ('key', models.CharField(max_length=1048, null=True, verbose_name='key')),
                ('value', models.CharField(max_length=1048, null=True, verbose_name='value')),
                ('ele_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uielement')),
                ('page_step', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipagesteps')),
            ],
            options={
                'db_table': 'ui_page_steps_detailed',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='uielement',
            name='page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipage'),
        ),
        migrations.CreateModel(
            name='UiConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='什么客户端')),
                ('browser_port', models.CharField(max_length=64, null=True, verbose_name='web端口')),
                ('browser_path', models.CharField(max_length=1024, null=True, verbose_name='chrome路径')),
                ('browser_type', models.SmallIntegerField(null=True, verbose_name='浏览器类型')),
                ('equipment', models.CharField(max_length=64, null=True, verbose_name='安卓设备名称')),
                ('is_headless', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user')),
            ],
            options={
                'db_table': 'ui_config',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiCaseStepsDetailed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('case_sort', models.IntegerField(null=True, verbose_name='用例排序')),
                ('case_cache_data', models.JSONField(null=True, verbose_name='用例缓存数据')),
                ('case_cache_ass', models.JSONField(null=True, verbose_name='步骤缓存断言')),
                ('case_data', models.JSONField(null=True, verbose_name='用例步骤数据')),
                ('status', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('error_message', models.TextField(null=True, verbose_name='错误提示')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicase')),
                ('page_step', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipagesteps')),
            ],
            options={
                'db_table': 'ui_case_steps_detailed',
            },
        ),
    ]
