# Generated by Django 3.1.3 on 2022-11-08 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0003_auto_20221106_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson'),
            preserve_default=False,
        ),
    ]
