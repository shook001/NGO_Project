# Generated by Django 2.1.7 on 2019-04-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20190402_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sem', 'Seminar'), ('Con', 'Conference'), ('Pres', 'Presentation')], max_length=4),
        ),
        migrations.AlterField(
            model_name='regform',
            name='adultQty',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='regform',
            name='childQty',
            field=models.IntegerField(),
        ),
    ]
