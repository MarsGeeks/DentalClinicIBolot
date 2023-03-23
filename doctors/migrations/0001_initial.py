# Generated by Django 4.1.7 on 2023-03-21 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Destinationnames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imag', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=50, verbose_name='Названия направлений')),
            ],
            options={
                'verbose_name': 'Названия направления',
                'verbose_name_plural': 'Названия направлений',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='user.jpg', upload_to='')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('datetime', models.DateField(verbose_name='Дата рождения')),
                ('education', models.TextField(null=True, verbose_name='Образование')),
                ('experience', models.IntegerField(verbose_name='Стаж работы')),
            ],
            options={
                'verbose_name': 'Информация о докторе',
                'verbose_name_plural': 'Добавить доктора',
            },
        ),
        migrations.CreateModel(
            name='Money',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField(verbose_name='Стоимость')),
            ],
            options={
                'verbose_name': 'Стоимость',
                'verbose_name_plural': 'Стоимости',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.CharField(max_length=50, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('names', models.CharField(max_length=50, null=True, verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Услуги',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=255, verbose_name='Описание праблемы')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.destinationnames')),
                ('doctor', models.ManyToManyField(to='doctors.doctor', verbose_name='Доктора которых можно записаться')),
                ('money', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.money', verbose_name='Цены')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255, verbose_name='Tекст')),
                ('created_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='doctor_reviews', to='doctors.doctor', verbose_name='Выберите доктора')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.post', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='destinationnames',
            name='services',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.services'),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+996', max_length=13, region=None, verbose_name='Номер телефона')),
                ('date', models.DateField(verbose_name='Назначить Дату')),
                ('time', models.CharField(choices=[('8', '08:00-09:20'), ('9', '09:30-10:50'), ('14', '14:00-15:20'), ('15', '15:30-16:50'), ('17', '17:00-18:20'), ('18', '18:30-20:00')], max_length=2, verbose_name='Выбрать Время')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor', verbose_name='Выбрать Врача')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.service', verbose_name='Выбрать Услугу')),
            ],
            options={
                'verbose_name': 'Запись на Прием',
                'verbose_name_plural': 'Запись на прием',
            },
        ),
    ]
