# Generated by Django 2.1.7 on 2019-04-02 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('description', models.TextField(max_length=255)),
                ('category', models.CharField(choices=[('Pres', 'Presentation'), ('Sem', 'Seminar'), ('Con', 'Conference')], max_length=4)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('e_start_time', models.DateTimeField()),
                ('e_end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('registrants', models.BooleanField()),
                ('e_image', models.ImageField(upload_to='')),
                ('e_adult_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('e_child_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]