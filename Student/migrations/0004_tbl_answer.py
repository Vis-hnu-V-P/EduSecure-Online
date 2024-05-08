# Generated by Django 5.0.1 on 2024-04-02 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0015_delete_tbl_examquestions'),
        ('Student', '0003_delete_tbl_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_content', models.CharField(max_length=500)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_questions')),
            ],
        ),
    ]
