# Generated by Django 4.2.7 on 2023-11-18 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.TextField(null=True)),
                ('data', models.TextField(null=True)),
            ],
        ),
    ]
