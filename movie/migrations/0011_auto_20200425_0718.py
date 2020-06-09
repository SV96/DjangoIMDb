# Generated by Django 3.0.4 on 2020-04-25 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_auto_20200425_0714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='banner',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_trailer',
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('action', 'ACTION'), ('comedy', 'COMEDY'), ('drama', 'DRAMA'), ('romance', 'ROMANCE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN')], max_length=20),
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RE', 'RECENTLY ADDED'), ('MW', 'MOSTLY WATCHED'), ('TR', 'TOP RATED')], max_length=2),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='type',
            field=models.CharField(choices=[('D', 'Downalod link'), ('W', 'Watch link')], max_length=1),
        ),
    ]