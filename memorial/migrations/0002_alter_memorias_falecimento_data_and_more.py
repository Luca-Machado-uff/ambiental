# Generated by Django 4.2.2 on 2023-06-17 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memorias',
            name='falecimento_data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='memorias',
            name='nascimento_data',
            field=models.DateField(blank=True, null=True),
        ),
    ]