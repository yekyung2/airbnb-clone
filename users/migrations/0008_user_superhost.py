# Generated by Django 2.2.5 on 2020-11-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20201102_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False),
        ),
    ]
