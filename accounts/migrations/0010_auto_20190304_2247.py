# Generated by Django 2.1 on 2019-03-04 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20190304_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_days',
            field=models.CharField(max_length=100),
        ),
    ]
