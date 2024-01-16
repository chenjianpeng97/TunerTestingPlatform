# Generated by Django 4.1.5 on 2023-11-23 10:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_user', '0004_alter_projectmodule_superior_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='selected_environment',
            field=models.SmallIntegerField(null=True, verbose_name='选中的环境ID'),
        ),
        migrations.AddField(
            model_name='user',
            name='selected_project',
            field=models.SmallIntegerField(null=True, verbose_name='选中的项目ID'),
        ),
    ]