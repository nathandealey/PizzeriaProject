# Generated by Django 3.0.5 on 2022-12-12 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzas', '0003_auto_20221212_0512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('pizza_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pizzas.Pizza')),
            ],
        ),
    ]
