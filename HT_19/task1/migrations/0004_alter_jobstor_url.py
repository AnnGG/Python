# Generated by Django 4.0.1 on 2022-02-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0003_jobstor_newstor_showstor_delete_askstoris'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobstor',
            name='url',
            field=models.CharField(max_length=250),
        ),
    ]
