# Generated by Django 2.2.6 on 2019-10-20 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_merge_20191019_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='certification',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
