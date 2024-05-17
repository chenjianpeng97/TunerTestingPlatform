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
            name='CacheData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('describe', models.CharField(max_length=1024, null=True, verbose_name='描述')),
                ('key', models.CharField(max_length=128, verbose_name='key')),
                ('value', models.TextField(null=True, verbose_name='value')),
                ('value_type', models.SmallIntegerField(null=True, verbose_name='value的类型枚举')),
                ('case_type', models.SmallIntegerField(null=True, verbose_name='用例类型')),
                ('case_id', models.SmallIntegerField(null=True, verbose_name='绑定的用例ID')),
            ],
            options={
                'db_table': 'cache_data',
            },
        ),
        migrations.CreateModel(
            name='ScheduledTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('name', models.CharField(max_length=64, verbose_name='任务名称')),
                ('case_executor', models.JSONField(null=True, verbose_name='用例执行人')),
                ('type', models.SmallIntegerField(null=True, verbose_name='任务类型')),
                ('status', models.SmallIntegerField(null=True, verbose_name='任务状态')),
                ('is_notice', models.SmallIntegerField(null=True, verbose_name='是否发送通知')),
                ('case_people', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user', verbose_name='用例责任人')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.testobject')),
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
                ('day_of_week', models.CharField(max_length=64, null=True, verbose_name='周')),
                ('hour', models.CharField(max_length=64, null=True, verbose_name='小时')),
                ('minute', models.CharField(max_length=64, null=True, verbose_name='分钟')),
            ],
            options={
                'db_table': 'time_tasks',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestSuiteReport',
            fields=[
                ('id', models.BigIntegerField(editable=False, primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='类型')),
                ('error_message', models.TextField(null=True, verbose_name='错误提示')),
                ('run_status', models.SmallIntegerField(null=True, verbose_name='执行状态')),
                ('status', models.SmallIntegerField(null=True, verbose_name='测试结果')),
                ('case_list', models.JSONField(null=True, verbose_name='测试套包含的用例列表')),
                ('is_notice', models.SmallIntegerField(null=True, verbose_name='是否发送通知')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
                ('test_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.testobject')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user', verbose_name='用例责任人')),
            ],
            options={
                'db_table': 'test_suite_report',
                'ordering': ['-create_time'],
            },
        ),
        migrations.CreateModel(
            name='TasksRunCaseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('case', models.SmallIntegerField(null=True, verbose_name='api_case_id')),
                ('sort', models.SmallIntegerField(null=True, verbose_name='api_case_id')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.scheduledtasks')),
                ('test_object', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.testobject')),
            ],
            options={
                'db_table': 'tasks_run_case_list',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='scheduledtasks',
            name='timing_strategy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_system.timetasks'),
        ),
        migrations.CreateModel(
            name='NoticeConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('type', models.SmallIntegerField(null=True, verbose_name='类型')),
                ('config', models.CharField(max_length=1028, null=True, verbose_name='通知配置')),
                ('status', models.SmallIntegerField(null=True, verbose_name='是否选中发送')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.project')),
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
                ('port', models.IntegerField(null=True, verbose_name='端口')),
                ('project_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.projectproduct')),
                ('test_obj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.testobject')),
            ],
            options={
                'db_table': 'data_base',
                'ordering': ['-id'],
            },
        ),
    ]
