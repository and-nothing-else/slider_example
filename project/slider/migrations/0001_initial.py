# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20150401_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name='name')),
            ],
            options={
                'verbose_name_plural': 'galleries',
                'verbose_name': 'gallery',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='title', blank=True, null=True)),
                ('file', sorl.thumbnail.fields.ImageField(verbose_name='file', upload_to='images')),
                ('gallery', models.ForeignKey(to='slider.Gallery')),
            ],
            options={
                'verbose_name_plural': 'photo',
                'verbose_name': 'photo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(serialize=False, to='cms.CMSPlugin', auto_created=True, parent_link=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name='title', blank=True, null=True)),
                ('description', djangocms_text_ckeditor.fields.HTMLField(verbose_name='description', blank=True, null=True)),
                ('gallery', models.ForeignKey(to='slider.Gallery', verbose_name='gallery', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
