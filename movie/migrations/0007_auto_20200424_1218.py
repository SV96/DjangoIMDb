# Generated by Django 3.0.4 on 2020-04-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200424_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN')], max_length=20),
        ),
    ]