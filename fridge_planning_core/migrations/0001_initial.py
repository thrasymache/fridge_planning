# Generated by Django 3.0.1 on 2019-12-25 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foodstuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('foodstuff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fridge_planning_core.Foodstuff')),
                ('fridge', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fridge_planning_core.Fridge')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fridge_planning_core.Recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('foodstuff', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fridge_planning_core.Foodstuff')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fridge_planning_core.Recipe')),
            ],
        ),
    ]
