# Generated by Django 2.2 on 2020-07-21 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0006_remove_db_tucao_ctime'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_tucao',
            name='ctime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
