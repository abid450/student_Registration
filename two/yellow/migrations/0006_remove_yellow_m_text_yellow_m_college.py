# Generated by Django 5.0 on 2024-07-05 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellow', '0005_alter_yellow_m_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yellow_m',
            name='Text',
        ),
        migrations.AddField(
            model_name='yellow_m',
            name='College',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
