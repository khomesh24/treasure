# Generated by Django 2.0 on 2017-12-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treasurelist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='treasure',
        ),
    ]
