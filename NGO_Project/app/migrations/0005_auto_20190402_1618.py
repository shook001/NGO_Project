# Generated by Django 2.1.7 on 2019-04-02 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190402_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Con', 'Conference'), ('Sem', 'Seminar'), ('Pres', 'Presentation')], max_length=4),
        ),
    ]
