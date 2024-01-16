# Generated by Django 4.1.5 on 2023-10-13 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('auto_user', '0001_initial'),
        ('auto_ui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduledTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('task_name', models.CharField(max_length=64, verbose_name='任务名称')),
                ('type', models.SmallIntegerField(null=True, verbose_name='任务类型')),
                ('status', models.SmallIntegerField(null=True, verbose_name='任务状态')),
                ('executor_name',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user')),
            ],
            options={
                'db_table': 'scheduled_tasks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TimeTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, null=True, unique=True, verbose_name='定时策略名称')),
                ('trigger_type', models.CharField(max_length=64, null=True, verbose_name='触发器类型')),
                ('month', models.CharField(max_length=64, null=True, verbose_name='月')),
                ('day', models.CharField(max_length=64, null=True, verbose_name='天')),
                ('hour', models.CharField(max_length=64, null=True, verbose_name='小时')),
                ('minute', models.CharField(max_length=64, null=True, verbose_name='分钟')),
            ],
            options={
                'db_table': 'time_tasks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='类型')),
                ('case_name', models.CharField(max_length=64, verbose_name='用例名称')),
                ('run_state', models.SmallIntegerField(null=True, verbose_name='执行状态')),
                ('state', models.SmallIntegerField(null=True, verbose_name='测试结果')),
                ('project',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'test_report',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('environment', models.SmallIntegerField(verbose_name='环境备注')),
                ('test_type', models.SmallIntegerField(verbose_name='对应什么客户端')),
                ('name', models.CharField(max_length=64, verbose_name='被测试的对象')),
                ('value', models.CharField(max_length=1024, verbose_name='被测试的对象')),
                ('executor_name',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user')),
                ('project',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'test_obj',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TasksRunCaseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='类型')),
                ('case',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_ui.uicase')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='auto_system.scheduledtasks')),
            ],
            options={
                'db_table': 'tasks_run_case_list',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='scheduledtasks',
            name='test_obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='auto_system.testobject'),
        ),
        migrations.AddField(
            model_name='scheduledtasks',
            name='timing_strategy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='auto_system.timetasks'),
        ),
        migrations.CreateModel(
            name='NoticeConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='类型')),
                ('config', models.CharField(max_length=1028, null=True, verbose_name='通知配置')),
                ('state', models.SmallIntegerField(null=True, verbose_name='是否选中发送')),
                ('project',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
            ],
            options={
                'db_table': 'notice_config',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='数据库名称')),
                ('user', models.CharField(max_length=64, null=True, verbose_name='登录用户名')),
                ('password', models.CharField(max_length=64, null=True, verbose_name='登录密码')),
                ('host', models.CharField(max_length=64, null=True, verbose_name='数据库地址')),
                ('post', models.IntegerField(null=True, verbose_name='端口')),
                ('project',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               to='auto_system.testobject')),
            ],
            options={
                'db_table': 'data_base',
                'ordering': ['-id'],
            },
        ),
    ]