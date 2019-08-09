# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-09 17:14
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='\u0410\u0442\u044b')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'Category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f\u043b\u0430\u0440',
            },
        ),
        migrations.CreateModel(
            name='Fon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to=b'ofonde/', verbose_name='\u041b\u043e\u0433\u043e')),
                ('ofonde_fon', models.ImageField(upload_to=b'slider/', verbose_name='\u0444\u043e\u043d\u0434')),
                ('video', models.ImageField(upload_to=b'ofonde/', verbose_name='\u0412\u0438\u0434\u0435\u043e')),
                ('foto', models.ImageField(upload_to=b'ofonde/', verbose_name='\u0424\u043e\u0442\u043e\u0433\u0430\u043b\u0430\u0440\u0435\u044f')),
                ('media', models.ImageField(upload_to=b'ofonde/', verbose_name='\u041c\u0435\u0434\u0438\u0430')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0424\u043e\u043d',
                'verbose_name_plural': '\u0424\u043e\u043d\u044b',
            },
        ),
        migrations.CreateModel(
            name='Fondjonundo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u0410\u0442\u044b')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='\u0411\u0430\u0433\u044b\u0442\u0442\u0430\u0440')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': '\u0424\u043e\u043d\u0434',
                'verbose_name': '\u0424\u043e\u043d\u0434\u0434\u0443\u043d \u0430\u0447\u044b\u043a\u0442\u0430\u043c\u0430\u0441\u044b',
                'verbose_name_plural': '\u0424\u043e\u043d\u0434\u0434\u0443\u043d \u0430\u0447\u044b\u043a\u0442\u0430\u043c\u0430\u0441\u044b',
            },
        ),
        migrations.CreateModel(
            name='Kairymduuluk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bilim_aluu', models.IntegerField(default=0, verbose_name='\u0411\u0438\u043b\u0438\u043c \u0430\u043b\u0443\u0443\u0433\u0430')),
                ('kurbandyk', models.IntegerField(default=0, verbose_name='\u041a\u0443\u0440\u0431\u0430\u043d\u0434\u044b\u043a\u043a\u0430')),
                ('muktaj', models.IntegerField(default=0, verbose_name='\u041c\u0443\u043a\u0442\u0430\u0436\u0434\u0430\u0440\u0433\u0430')),
                ('suu_chygaruu', models.IntegerField(default=0, verbose_name='\u0421\u0443\u0443 \u0447\u044b\u0433\u0430\u0440\u0443\u0443\u0433\u0430')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041c\u0430\u0430\u043b\u044b\u043c\u0430\u0442')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u041a\u0430\u0439\u0440\u044b\u043c\u0434\u0443\u0443\u043b\u0443\u043a',
                'verbose_name_plural': '\u041a\u0430\u0439\u0440\u044b\u043c\u0434\u0443\u0443\u043b\u0443\u043a',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=80, null=True, verbose_name='\u0410\u0442\u044b')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': '\u0422\u0438\u043b',
                'verbose_name': '\u0422\u0438\u043b',
                'verbose_name_plural': '\u0422\u0438\u043b\u0434\u0435\u0440',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, verbose_name='\u041c\u0430\u043a\u0430\u043b\u0430\u043d\u044b\u043d \u0430\u0442\u0430\u043b\u044b\u0448\u044b')),
                ('slug', models.CharField(blank=True, max_length=200, verbose_name='\u0422\u0440\u0430\u043d\u0441\u043b\u0438\u0442')),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'news/', verbose_name='\u0421\u04af\u0440\u04e9\u0442')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='\u041c\u0430\u0430\u043b\u044b\u043c\u0430\u0442')),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u0414\u0430\u0442\u0430')),
                ('author', models.CharField(blank=True, max_length=200, null=True, verbose_name='\u041c\u0430\u043a\u0430\u043b\u0430\u043d\u044b\u043d \u0430\u0432\u0442\u043e\u0440\u0443')),
                ('is_public', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='\u0422\u0438\u043b\u0438')),
                ('user_rection', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0416\u0430\u04a3\u044b\u043b\u044b\u043a',
                'verbose_name_plural': '\u0416\u0430\u04a3\u044b\u043b\u044b\u043a\u0442\u0430\u0440',
            },
        ),
        migrations.CreateModel(
            name='OFonde',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='\u0410\u0442\u044b')),
                ('phone', models.CharField(db_index=True, max_length=150, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d')),
                ('email', models.EmailField(max_length=254, verbose_name='\u0415\u043c\u0435\u0439\u043b')),
                ('adres', models.CharField(db_index=True, max_length=200, verbose_name='\u0414\u0430\u0440\u0435\u043a')),
                ('karta', models.CharField(max_length=400, verbose_name='\u041a\u0430\u0440\u0442\u0430')),
                ('facebook', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0424\u0435\u0439\u0441\u0431\u0443\u043a')),
                ('instagram', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u0418\u043d\u0441\u0442\u0430\u0433\u0440\u0430\u043c')),
                ('youtube', models.CharField(blank=True, max_length=250, null=True, verbose_name='\u042e\u0442\u0443\u0431')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='\u0422\u0438\u043b\u0438')),
            ],
            options={
                'ordering': ['-id'],
                'verbose_name': '\u0424\u043e\u043d\u0434 \u0436\u04e9\u043d\u04af\u043d\u0434\u04e9',
                'verbose_name_plural': '\u0424\u043e\u043d\u0434 \u0436\u04e9\u043d\u04af\u043d\u0434\u04e9',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fon', models.ImageField(upload_to=b'slider/', verbose_name='\u0421\u043b\u0430\u0439\u0434\u0435\u0440\u0434\u0438\u043d \u0441\u04af\u0440\u04e9\u0442\u04af')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='\u0422\u0438\u043b\u0438')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u0435\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='kairymduuluk',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='\u0422\u0438\u043b\u0438'),
        ),
        migrations.AddField(
            model_name='fondjonundo',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Language', verbose_name='\u0422\u0438\u043b\u0438'),
        ),
    ]