# Generated by Django 2.2.4 on 2024-06-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mm1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='num_class_in_week',
            field=models.IntegerField(default=0),
        ),
    ]
