# Generated by Django 3.2.15 on 2022-10-25 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetOrder',
            fields=[
                ('petorder_id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('reg_id', models.IntegerField()),
            ],
            options={
                'db_table': 'pet_order',
                'managed': False,
            },
        ),
    ]
