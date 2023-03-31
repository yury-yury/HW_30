# Generated by Django 4.1.7 on 2023-03-30 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0003_alter_user_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='author.location'),
        ),
    ]
