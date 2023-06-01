# Generated by Django 4.2.1 on 2023-06-01 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='articul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=10000)),
                ('detalle', models.CharField(max_length=200)),
                ('lista', models.CharField(max_length=100)),
                ('cod_lista', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]