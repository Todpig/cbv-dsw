# Generated by Django 4.2.7 on 2023-11-23 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospedagem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='apartamento',
            field=models.IntegerField(null=True),
        ),
    ]
