# Generated by Django 2.2 on 2019-04-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20190402_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Con', 'Conference'), ('Sem', 'Seminar'), ('Pres', 'Presentation')], max_length=4),
        ),
    ]