# Generated by Django 2.0.3 on 2018-04-06 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('external_url', models.CharField(blank=True, max_length=70, null=True)),
                ('url', models.CharField(max_length=50)),
                ('mbid', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=40)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('followers', models.IntegerField(blank=True, null=True)),
                ('mbid', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('summary', models.CharField(blank=True, max_length=800, null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
                ('wiki_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('external_url', models.CharField(blank=True, max_length=70, null=True)),
                ('popularity', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(max_length=50)),
                ('mbid', models.CharField(editable=False, max_length=30, primary_key=True, serialize=False)),
                ('artist', models.ManyToManyField(to='info.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='UserTrackHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('played_on', models.DateTimeField(auto_now_add=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_track_history', related_query_name='user_track_history', to='info.Track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_history', related_query_name='track_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='gag',
            field=models.ManyToManyField(related_name='tags', related_query_name='tags', to='info.Tag'),
        ),
    ]
