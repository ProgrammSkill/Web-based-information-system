# Generated by Django 4.1.3 on 2022-11-16 21:48

import django.contrib.auth.models
import django.contrib.auth.validators
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
            name='AutoParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=20, verbose_name='Артикул')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50, verbose_name='Марка автозапчасти')),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(max_length=50, verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('мodel', models.CharField(max_length=50, verbose_name='Модель марки')),
            ],
        ),
        migrations.CreateModel(
            name='Streets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='Улица')),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Наименование организации')),
                ('INN', models.IntegerField(verbose_name='ИНН')),
                ('CIO', models.IntegerField(verbose_name='КПП')),
                ('FullNameManager', models.CharField(max_length=150, verbose_name='ФИО руководителя')),
                ('telephone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('email', models.CharField(max_length=30, verbose_name='Эл почта')),
            ],
        ),
        migrations.CreateModel(
            name='StoreDepartments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house', models.CharField(max_length=10, verbose_name='Дом')),
                ('telephone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('id_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.cities', verbose_name='Город')),
                ('id_street', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.streets', verbose_name='Улица')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('DateOfSale', models.DateField(verbose_name='Дата продажи')),
                ('id_autoParts', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.autoparts', verbose_name='Автозапчасть')),
                ('id_suppliers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.storedepartments', verbose_name='Отдел магазина')),
            ],
        ),
        migrations.CreateModel(
            name='BrandsAndModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_brand', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.brands', verbose_name='Марка автомобиля')),
                ('id_model', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.models', verbose_name='Модель')),
            ],
        ),
        migrations.CreateModel(
            name='AutoPartsInStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Наименование')),
                ('comment', models.TextField(verbose_name='Комментарий')),
                ('id_StoreDepartment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.autoparts', verbose_name='Автозапчасть')),
                ('id_brand_and_models', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.brandsandmodels', verbose_name='Автомобиль')),
                ('id_manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.manufacturers', verbose_name='Производитель')),
            ],
        ),
        migrations.AddField(
            model_name='autoparts',
            name='id_brand_and_models',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.brandsandmodels', verbose_name='Автомобиль'),
        ),
        migrations.AddField(
            model_name='autoparts',
            name='id_manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='autodocapp.manufacturers', verbose_name='Производитель'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('last_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
