# Generated by Django 3.1.12 on 2021-08-25 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djAssignment', '0004_pagecompomap_time_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='component',
        ),
        migrations.RemoveField(
            model_name='pagecompomap',
            name='compo',
        ),
        migrations.RemoveField(
            model_name='pagecompomap',
            name='page',
        ),
        migrations.DeleteModel(
            name='Compo',
        ),
        migrations.DeleteModel(
            name='Page',
        ),
        migrations.DeleteModel(
            name='PageCompoMap',
        ),
    ]
