# Generated by Django 5.0.1 on 2024-04-07 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0010_remove_tbl_examstudent_exam_id_and_more'),
        ('Teacher', '0019_tbl_student_batchid'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_examstudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_mark', models.IntegerField()),
                ('exam_status', models.IntegerField(default=0)),
                ('exam_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.tbl_exam')),
                ('exstudent_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Teacher.tbl_student')),
            ],
        ),
    ]
