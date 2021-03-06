# Generated by Django 2.1.15 on 2022-05-16 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asociaciones',
            fields=[
                ('asociacionesid', models.AutoField(db_column='AsociacionesID', primary_key=True, serialize=False)),
                ('dpto', models.IntegerField(db_column='Dpto')),
                ('ctacontable', models.FloatField(db_column='CtaContable')),
                ('ctapresupuestaria', models.CharField(blank=True, db_column='CtaPresupuestaria', max_length=255, null=True)),
                ('descripcionctapresu', models.CharField(blank=True, db_column='DescripcionCtaPresu', max_length=255, null=True)),
                ('a', models.IntegerField(blank=True, db_column='A', null=True)),
                ('b', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Asociaciones',
                'managed': False,
            },
        ),
    ]
