# Generated by Django 5.0.1 on 2024-04-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0017_tbl_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_section',
            name='section_qstn',
            field=models.IntegerField(null=True),
        ),
    ]