# Generated by Django 4.1 on 2022-08-27 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bazar', '0004_alter_evento_options_alter_item_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='evento',
            field=models.ManyToManyField(related_name='evento', to='Bazar.evento'),
        ),
    ]