# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-09 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scheduled_time', models.TimeField()),
                ('pickup_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, choices=[('Dr', 'Docteur')], max_length=30, null=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('parent_organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Organization')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='host',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Organization'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Host'),
        ),
    ]