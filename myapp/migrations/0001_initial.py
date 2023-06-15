# Generated by Django 4.2.1 on 2023-05-30 15:14

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin_user', models.BooleanField(default=False)),
                ('is_vendor', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('created_by', models.IntegerField(blank=True, default=None, null=True)),
                ('updated_by', models.IntegerField(blank=True, default=None, null=True)),
                ('user_type', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=255)),
                ('vendor_email', models.EmailField(max_length=254, unique=True)),
                ('vendor_address', models.CharField(max_length=255)),
                ('vendor_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('org_name', models.CharField(max_length=255)),
                ('GTS_no', models.CharField(max_length=50)),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=254, unique=True)),
                ('customer_address', models.CharField(max_length=255)),
                ('customer_phone', models.CharField(blank=True, max_length=20, null=True)),
                ('age', models.CharField(max_length=5)),
                ('gender', models.CharField(max_length=10)),
                ('occupation', models.CharField(max_length=50)),
                ('maried_status', models.CharField(max_length=10)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]