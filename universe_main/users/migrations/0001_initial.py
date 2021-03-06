# Generated by Django 3.2 on 2021-04-25 18:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('surname', models.CharField(blank=True, max_length=255, null=True, verbose_name='Surname')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Birth date')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='users/avatars/', verbose_name='Avatar')),
                ('about_me', models.CharField(blank=True, max_length=1000, null=True, verbose_name='About me')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=10)),
            ],
        ),
    ]
