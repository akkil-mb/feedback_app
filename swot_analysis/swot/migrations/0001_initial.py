# Generated by Django 5.0.3 on 2024-04-14 05:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataEntryPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(6, 'Team'), (5, 'Team Lead'), (4, 'Manager'), (3, 'HR'), (2, 'CEO'), (1, 'Super User')])),
                ('can_post', models.BooleanField(default=True)),
                ('can_view_role_1', models.BooleanField(default=False)),
                ('can_view_role_2', models.BooleanField(default=False)),
                ('can_view_role_3', models.BooleanField(default=False)),
                ('can_view_role_4', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SwotModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_role', models.IntegerField(editable=False)),
                ('full_name', models.CharField(default='', max_length=100)),
                ('team_name', models.CharField(default='', max_length=150)),
                ('designation', models.CharField(default='', max_length=150)),
                ('joined_on', models.DateField(auto_now=True)),
                ('strengths', models.CharField(max_length=1000)),
                ('weakness', models.CharField(max_length=1000)),
                ('opportunity', models.CharField(max_length=1000)),
                ('threats', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(6, 'Team'), (5, 'Team Lead'), (4, 'Manager'), (3, 'HR'), (2, 'CEO'), (1, 'Super User')])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
