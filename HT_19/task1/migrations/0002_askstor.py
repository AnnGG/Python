# Generated by Django 4.0.1 on 2022-01-31 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Askstor',
            fields=[
                ('by', models.CharField(max_length=200)),
                ('descendants', models.IntegerField()),
                ('id_ask', models.IntegerField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('text', models.TextField()),
                ('time', models.IntegerField()),
                ('title', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
    ]
