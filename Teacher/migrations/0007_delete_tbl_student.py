# Generated by Django 5.0.1 on 2024-03-09 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0006_remove_tbl_student_student_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_student',
        ),
    ]
