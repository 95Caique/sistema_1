# Generated by Django 5.1.6 on 2025-02-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servidor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servidor',
            name='cidade',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='servidor',
            name='lotacao',
            field=models.CharField(default='', max_length=100),
        ),
    ]
