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
            name='UiCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='用例名称')),
                ('run_flow', models.CharField(max_length=2000, null=True, verbose_name='执行顺序的展示')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('case_type', models.SmallIntegerField(null=True, verbose_name='用例的类型')),
                ('type', models.SmallIntegerField(null=True, verbose_name='用例的类型')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'ui_case',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiCaseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='用例组名称')),
                ('case_id', models.CharField(max_length=1048, null=True, verbose_name='存放组内所有用例ID')),
                ('case_name', models.CharField(max_length=1048, null=True, verbose_name='存放组内所有用例名称')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('case_people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_case_people', to='auto_user.user', verbose_name='用例责任人')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.testobject')),
                ('time_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.timetasks')),
                ('timing_actuator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_timing_actuator', to='auto_user.user', verbose_name='定时执行的设备')),
            ],
            options={
                'db_table': 'ui_case_group',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('ele_name', models.CharField(max_length=1048, null=True, verbose_name='元素名称')),
                ('existence', models.SmallIntegerField(null=True, verbose_name='元素执行的情况')),
                ('picture', models.CharField(max_length=1048, null=True, verbose_name='图片路径或名称')),
                ('msg', models.CharField(max_length=1048, null=True, verbose_name='失败提示日志')),
                ('state', models.SmallIntegerField(null=True, verbose_name='结果')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicase')),
                ('case_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicasegroup')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.testobject')),
            ],
            options={
                'db_table': 'ui_result',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiPublic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='公共类型')),
                ('name', models.CharField(max_length=64, verbose_name='名称')),
                ('key', models.CharField(max_length=128, null=True, verbose_name='键')),
                ('value', models.CharField(max_length=2048, null=True, verbose_name='值')),
                ('state', models.SmallIntegerField(null=True, verbose_name='状态')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'ui_public',
                'ordering': ['-id'],
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
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'ui_page',
                'ordering': ['-id'],
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
                ('loc', models.CharField(max_length=1048, verbose_name='元素定位')),
                ('sleep', models.IntegerField(null=True, verbose_name='等待时间')),
                ('sub', models.IntegerField(null=True, verbose_name='下标')),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipage')),
            ],
            options={
                'db_table': 'ui_ele',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='UiConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('local_port', models.CharField(max_length=64, null=True, verbose_name='web端口')),
                ('browser_path', models.CharField(max_length=1024, null=True, verbose_name='chrome路径')),
                ('equipment', models.CharField(max_length=64, null=True, verbose_name='安卓设备名称')),
                ('package', models.CharField(max_length=64, null=True, verbose_name='app包名称')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user')),
            ],
            options={
                'db_table': 'ui_config',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='RunSort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('ope_type', models.CharField(max_length=1048, null=True, verbose_name='对该元素的操作类型')),
                ('ass_type', models.CharField(max_length=1048, null=True, verbose_name='断言类型')),
                ('ope_value', models.CharField(max_length=1048, null=True, verbose_name='操作内容')),
                ('ope_value_key', models.CharField(max_length=64, null=True, verbose_name='输入内容的key，用来保存变量')),
                ('ass_value', models.CharField(max_length=1048, null=True, verbose_name='操作内容')),
                ('run_sort', models.IntegerField(null=True, verbose_name='执行顺序的展示')),
                ('case', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicase')),
                ('el_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_UiElement_a', to='auto_ui.uielement')),
                ('el_name_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_UiElement_b', to='auto_ui.uielement')),
                ('el_page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uipage')),
            ],
            options={
                'db_table': 'ui_run_sort',
                'ordering': ['-id'],
            },
        ),
    ]
