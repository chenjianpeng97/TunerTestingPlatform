# Generated by Django 4.1.5 on 2023-11-20 05:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0021_uieleresult_msg'),
    ]

    operations = [
        migrations.AddField(
            model_name='uielement',
            name='is_iframe',
            field=models.SmallIntegerField(default=0, verbose_name='是否在iframe里面'),
            preserve_default=False,
        ),
    ]