# Generated by Django 3.0.5 on 2022-12-12 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzas', '0002_comment_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='Pizzas.Pizza'),
        ),
    ]
