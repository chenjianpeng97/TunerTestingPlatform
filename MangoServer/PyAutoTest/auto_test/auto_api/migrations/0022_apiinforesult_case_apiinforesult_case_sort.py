# Generated by Django 4.1.5 on 2024-01-24 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_api', '0021_apicase_test_suite_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiinforesult',
            name='case',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_api.apicase'),
        ),
        migrations.AddField(
            model_name='apiinforesult',
            name='case_sort',
            field=models.IntegerField(null=True, verbose_name='用例排序'),
        ),
    ]
