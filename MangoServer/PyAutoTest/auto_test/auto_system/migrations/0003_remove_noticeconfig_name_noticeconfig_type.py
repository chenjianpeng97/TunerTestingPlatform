# Generated by Django 4.1.5 on 2023-05-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_system', '0002_alter_testobject_executor_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticeconfig',
            name='name',
        ),
        migrations.AddField(
            model_name='noticeconfig',
            name='type',
            field=models.SmallIntegerField(null=True, verbose_name='是否选中发送'),
        ),
    ]