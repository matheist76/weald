# Generated by Django 4.0.4 on 2022-06-11 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('template', models.CharField(max_length=30)),
            ],
        ),
    ]
