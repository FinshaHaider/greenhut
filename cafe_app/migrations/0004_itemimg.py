# Generated by Django 5.0.2 on 2024-07-26 04:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe_app.menu')),
            ],
        ),
    ]
