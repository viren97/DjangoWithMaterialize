# Generated by Django 2.1.7 on 2019-03-13 19:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorial', '0003_auto_20190311_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 1, 28, 36, 261485), verbose_name='date published'),
        ),
    ]
