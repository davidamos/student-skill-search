# Generated by Django 2.1.7 on 2019-03-04 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_merge_20190304_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_start_time',
            field=models.TimeField(),
        ),
    ]
