# Generated by Django 4.1.5 on 2024-02-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0029_uicase_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='uieleresult',
            name='actual',
            field=models.TextField(null=True, verbose_name='实际'),
        ),
        migrations.AddField(
            model_name='uieleresult',
            name='expect',
            field=models.TextField(null=True, verbose_name='预期'),
        ),
    ]
