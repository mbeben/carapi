# Generated by Django 3.2.5 on 2021-07-29 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.car', verbose_name='car'),
        ),
    ]
