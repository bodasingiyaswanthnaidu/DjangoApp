# Generated by Django 3.2 on 2021-05-08 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0008_alter_cartitem_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]