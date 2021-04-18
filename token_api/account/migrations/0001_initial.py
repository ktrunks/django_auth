# Generated by Django 2.0 on 2019-11-04 18:12

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid
from .models import User

class Migration(migrations.Migration):

    initial = True

    def seed_data(apps, schema_editor):
        user = User(name='admin',
                          email='admin@gmail.com',
                          is_staff=True,
                          is_superuser=True,
                          phone='987654321',
                          gender='Male'
                        )
        user.set_password('Admin@123')
        user.save()

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(5000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(db_index=True, max_length=128, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('address', models.TextField(default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'G-store',
            },
        ),
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mobile', models.BigIntegerField(unique=True, validators=[django.core.validators.MinValueValidator(5000000000), django.core.validators.MaxValueValidator(9999999999)])),
                ('name', models.CharField(default=False, max_length=65)),
                ('email', models.EmailField(db_index=True, max_length=128, unique=True)),
                ('address', models.TextField(blank=True, default='')),
                ('current_ctc', models.IntegerField(default=0)),
                ('expected_ctc', models.IntegerField(default=0)),
                ('notice_days', models.IntegerField(default=0)),
                ('is_already_on_notice', models.BooleanField(default=False)),
                ('experience', models.FloatField(default=0)),
                ('tech_skills', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('preferable_locations', jsonfield.fields.JSONField(blank=True, default={}, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
