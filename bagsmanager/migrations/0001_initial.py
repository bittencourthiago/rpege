# Generated by Django 2.2.9 on 2022-01-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('value', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('quantity', models.IntegerField(verbose_name='Quantidade')),
            ],
        ),
    ]
