# Generated by Django 4.2 on 2023-04-08 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.FloatField(),
        ),
    ]
