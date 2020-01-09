# Generated by Django 2.1 on 2020-01-08 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0004_user_evaluation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOVIE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_id', models.CharField(max_length=50)),
                ('titles', models.CharField(max_length=100)),
                ('release_time', models.CharField(max_length=50)),
                ('director', models.CharField(max_length=50)),
                ('times', models.CharField(max_length=50)),
                ('tags', models.CharField(max_length=200)),
                ('gerne', models.CharField(max_length=50)),
                ('score', models.CharField(max_length=40)),
                ('score_numbers', models.CharField(max_length=50)),
                ('comments_num', models.CharField(max_length=50)),
                ('five_stars', models.CharField(max_length=50)),
                ('four_stars', models.CharField(max_length=50)),
                ('three_stars', models.CharField(max_length=50)),
                ('two_stars', models.CharField(max_length=50)),
                ('one_star', models.CharField(max_length=50)),
                ('region', models.CharField(max_length=50)),
                ('jpg_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='user_evaluation',
            unique_together={('user_id', 'movie_id')},
        ),
    ]
