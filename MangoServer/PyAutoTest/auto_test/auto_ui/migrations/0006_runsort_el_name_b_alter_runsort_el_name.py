# Generated by Django 4.1.5 on 2023-05-20 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_ui', '0005_alter_runsort_ass_type_alter_runsort_ope_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='runsort',
            name='el_name_b',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='related_UiElement_b', to='auto_ui.uielement'),
        ),
        migrations.AlterField(
            model_name='runsort',
            name='el_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    related_name='related_UiElement_a', to='auto_ui.uielement'),
        ),
    ]
