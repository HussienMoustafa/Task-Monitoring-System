# Generated by Django 3.1.4 on 2020-12-24 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20201224_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='rate',
            field=models.IntegerField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, null=True),
        ),
    ]
