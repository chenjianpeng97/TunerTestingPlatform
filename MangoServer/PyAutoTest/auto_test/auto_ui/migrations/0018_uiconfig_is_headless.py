# Generated by Django 4.1.5 on 2023-11-10 03:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0017_uicasestepsdetailed_case_cache_ass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='uiconfig',
            name='is_headless',
            field=models.SmallIntegerField(null=True, verbose_name='状态'),
        ),
    ]
