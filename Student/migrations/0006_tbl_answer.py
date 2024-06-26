# Generated by Django 5.0.1 on 2024-04-05 05:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0017_tbl_questions'),
        ('Student', '0005_delete_tbl_answer'),
        ('Teacher', '0017_tbl_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.CharField(max_length=500)),
                ('answer_mark', models.IntegerField(null=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_questions')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Teacher.tbl_student')),
            ],
        ),
    ]
