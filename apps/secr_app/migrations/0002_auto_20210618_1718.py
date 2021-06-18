# Generated by Django 3.1.7 on 2021-06-18 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '__first__'),
        ('secr_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='defendant',
            name='defendant_created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_create_defendant', to='users_app.user'),
        ),
    ]
