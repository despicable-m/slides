# Generated by Django 3.1 on 2020-12-01 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0023_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_name',
            field=models.CharField(default='something.jpg', max_length=10000),
        ),
    ]
