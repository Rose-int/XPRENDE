# Generated by Django 4.2.16 on 2024-10-01 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductGroup',
            fields=[
                ('code', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitMeasurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('trademark', models.CharField(blank=True, max_length=40)),
                ('model', models.CharField(blank=True, max_length=40)),
                ('price', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('minimum_stock', models.DecimalField(decimal_places=5, default=0, max_digits=15)),
                ('active', models.BooleanField(default=True)),
                ('product_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.productgroup')),
                ('unit_measurement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_app.unitmeasurement')),
            ],
        ),
    ]
