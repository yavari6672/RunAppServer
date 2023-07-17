# Generated by Django 4.2.2 on 2023-06-29 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ip_address', models.CharField(max_length=17)),
                ('description', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=27)),
                ('port', models.IntegerField()),
                ('description', models.CharField(max_length=300, null=True)),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.server')),
            ],
        ),
    ]
