# Generated by Django 3.1.7 on 2021-06-16 23:33

import apps.users_app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name1', models.CharField(max_length=45)),
                ('first_name2', models.CharField(max_length=45)),
                ('last_name1', models.CharField(max_length=45)),
                ('last_name2', models.CharField(max_length=45)),
                ('rut', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30, validators=[apps.users_app.models.validarEmail])),
                ('password', models.CharField(max_length=100, validators=[apps.users_app.models.ValidarLongitudPassword])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name1', models.CharField(max_length=45)),
                ('first_name2', models.CharField(max_length=45)),
                ('last_name1', models.CharField(max_length=45)),
                ('last_name2', models.CharField(max_length=45)),
                ('rut', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30, validators=[apps.users_app.models.validarEmail])),
                ('password', models.CharField(max_length=100, validators=[apps.users_app.models.ValidarLongitudPassword])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_type', to='users_app.usertype')),
                ('users_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administrator_create', to='users_app.administrator')),
            ],
        ),
    ]