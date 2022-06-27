# Generated by Django 4.0.4 on 2022-06-27 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regionName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='YearTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('win', models.FloatField(null=True)),
                ('spr', models.FloatField(null=True)),
                ('sum', models.FloatField(null=True)),
                ('aut', models.FloatField(null=True)),
                ('ann', models.FloatField(null=True)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yeartemperature', to='core.parameter')),
            ],
        ),
        migrations.AddField(
            model_name='parameter',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameter', to='core.region'),
        ),
        migrations.CreateModel(
            name='MonthTemperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('temperature', models.FloatField(null=True)),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='monthtemperature', to='core.yeartemperature')),
            ],
        ),
    ]
