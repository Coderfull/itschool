# Generated by Django 4.0.4 on 2023-11-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_myuser_fan_remove_myuser_gruhi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yunalishlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
