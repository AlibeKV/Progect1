# Generated by Django 4.2.2 on 2023-10-04 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='событие', max_length=256, verbose_name='имя события')),
                ('description', models.TextField(blank=True, null=True, verbose_name='oписание события')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата события')),
                ('is_important', models.BooleanField(default=False, verbose_name='важность события')),
                ('image', models.ImageField(upload_to='event-image', verbose_name='фото события')),
            ],
            options={
                'verbose_name': 'сoбытия',
                'verbose_name_plural': 'событие',
            },
        ),
    ]