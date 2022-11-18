# Generated by Django 3.2.15 on 2022-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=8)),
                ('reg_id', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
    ]
