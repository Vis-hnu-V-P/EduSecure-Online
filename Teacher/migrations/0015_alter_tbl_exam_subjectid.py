# Generated by Django 5.0.1 on 2024-03-11 06:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_delete_tbl_examquestions'),
        ('Teacher', '0014_tbl_exam_batchid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_exam',
            name='subjectid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_subject'),
        ),
    ]