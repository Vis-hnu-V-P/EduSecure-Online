# Generated by Django 5.0.1 on 2024-04-07 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0009_tbl_answer_tbl_examstudent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_examstudent',
            name='exam_id',
        ),
        migrations.RemoveField(
            model_name='tbl_examstudent',
            name='exstudent_id',
        ),
        migrations.DeleteModel(
            name='tbl_answer',
        ),
        migrations.DeleteModel(
            name='tbl_examstudent',
        ),
    ]
