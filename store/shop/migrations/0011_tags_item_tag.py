# Generated by Django 4.1.3 on 2023-04-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_orderdata_city_alter_orderdata_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(to='shop.tags'),
        ),
    ]
