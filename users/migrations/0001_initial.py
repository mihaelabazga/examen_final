# Generated by Django 2.2.6 on 2019-10-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('number_of_login', models.IntegerField()),
            ],
            options={
                'db_table': 'personmodel',
            },
        ),
    ]