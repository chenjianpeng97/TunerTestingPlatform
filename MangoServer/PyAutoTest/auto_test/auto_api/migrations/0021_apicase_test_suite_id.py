# Generated by Django 4.1.5 on 2024-01-24 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_api', '0020_apicaseresult_apiinforesult_delete_apiresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='apicase',
            name='test_suite_id',
            field=models.BigIntegerField(null=True, verbose_name='测试套件id'),
        ),
    ]
