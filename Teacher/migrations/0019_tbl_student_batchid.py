# Generated by Django 5.0.1 on 2024-04-07 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_tbl_questions'),
        ('Teacher', '0018_alter_tbl_section_section_qstn'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_student',
            name='batchid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_batch'),
        ),
    ]
