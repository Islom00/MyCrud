# Generated by Django 3.2.5 on 2021-07-17 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_alter_bookmodel_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
