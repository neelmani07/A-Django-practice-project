# Generated by Django 3.1.12 on 2021-08-26 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djAssignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compo',
            name='type_of_compo',
            field=models.CharField(choices=[('ic', 'icons'), ('im', 'image'), ('h', 'heading'), ('b', 'body'), ('l', 'link')], max_length=50),
        ),
    ]