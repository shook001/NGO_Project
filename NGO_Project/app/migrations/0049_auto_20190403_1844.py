# Generated by Django 2.2 on 2019-04-03 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0048_auto_20190403_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Con', 'Conference'), ('Pres', 'Presentation'), ('Sem', 'Seminar')], max_length=4),
        ),
    ]