# Generated by Django 2.2.14 on 2020-07-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20200712_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]