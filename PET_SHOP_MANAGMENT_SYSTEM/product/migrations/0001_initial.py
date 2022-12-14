# Generated by Django 3.2.15 on 2022-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=25)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('image', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
    ]
