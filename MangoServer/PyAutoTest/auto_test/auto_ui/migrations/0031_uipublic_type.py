# Generated by Django 4.1.5 on 2024-02-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_ui', '0030_uieleresult_actual_uieleresult_expect'),
    ]

    operations = [
        migrations.AddField(
            model_name='uipublic',
            name='type',
            field=models.SmallIntegerField(null=True, verbose_name='自定义变量类型'),
        ),
    ]
