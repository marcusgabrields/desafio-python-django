# Generated by Django 3.1.3 on 2020-11-07 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phone',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', related_query_name='phone', to='profiles.profile', verbose_name='profile'),
        ),
    ]