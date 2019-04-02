# Generated by Django 2.2 on 2019-04-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_merge_20190402_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('Sem', 'Seminar'), ('Pres', 'Presentation'), ('Con', 'Conference')], max_length=4),
        ),
        migrations.AlterField(
            model_name='regform',
            name='adultQty',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='regform',
            name='childQty',
            field=models.CharField(max_length=2),
        ),
    ]
