# Generated by Django 3.0.4 on 2020-04-24 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200424_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=20),
        ),
    ]
