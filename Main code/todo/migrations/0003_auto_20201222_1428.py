# Generated by Django 3.1.4 on 2020-12-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201222_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='rate',
            field=models.CharField(blank=True, choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default=0, max_length=2, null=True),
        ),
    ]
