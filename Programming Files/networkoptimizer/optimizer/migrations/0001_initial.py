# Generated by Django 2.1.3 on 2019-03-28 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('must_exist', models.BooleanField()),
                ('must_remove', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_id', models.CharField(max_length=200)),
                ('provider_name', models.CharField(max_length=200)),
                ('cost', models.CharField(max_length=200)),
                ('quality', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(max_length=200)),
                ('quality', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='provider',
            name='search',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search', to='optimizer.Search'),
        ),
    ]
