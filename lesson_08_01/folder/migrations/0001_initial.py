# Generated by Django 5.0 on 2024-02-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('species', models.CharField(blank=True, max_length=50, null=True)),
                ('health_status', models.CharField(choices=[('h', 'Здоровый'), ('s', 'Больной'), ('n', 'Не обследованный')], default='h', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Enclosure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.IntegerField()),
                ('animals', models.ManyToManyField(to='folder.animal')),
            ],
        ),
    ]
