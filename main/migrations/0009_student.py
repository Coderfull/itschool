# Generated by Django 4.0.4 on 2023-11-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_yunalishlar_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ismi', models.CharField(max_length=50)),
                ('familya', models.CharField(max_length=50)),
                ('yunalish', models.CharField(max_length=50)),
                ('vaqt', models.CharField(max_length=50)),
                ('kun', models.CharField(max_length=50)),
                ('telefon', models.CharField(max_length=50)),
            ],
        ),
    ]
