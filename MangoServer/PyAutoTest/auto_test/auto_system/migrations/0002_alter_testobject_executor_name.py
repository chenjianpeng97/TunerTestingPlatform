# Generated by Django 4.1.5 on 2023-05-04 09:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('auto_user', '0002_user_mailbox'),
        ('auto_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testobject',
            name='executor_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auto_user.user'),
        ),
    ]
