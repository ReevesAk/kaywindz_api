# Generated by Django 4.0.3 on 2022-03-09 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_rename_petdetails_petdetail_alter_sex_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sex',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='petdetail',
            name='pet',
        ),
        migrations.AddField(
            model_name='petdetail',
            name='pet',
            field=models.ManyToManyField(to='pet.pet'),
        ),
    ]
