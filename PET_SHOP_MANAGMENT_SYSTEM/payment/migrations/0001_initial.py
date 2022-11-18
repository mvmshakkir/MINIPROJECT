# Generated by Django 3.2.15 on 2022-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('card_number', models.IntegerField()),
                ('cardholder_name', models.CharField(max_length=25)),
                ('cvv', models.IntegerField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
    ]