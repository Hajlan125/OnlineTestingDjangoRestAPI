# Generated by Django 3.2.8 on 2022-04-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answ_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('answ_text', models.TextField(db_column='answ_text', verbose_name='Вопрос')),
                ('is_correct', models.BooleanField(db_column='is_correct')),
            ],
            options={
                'db_table': 'answer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('q_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('q_title', models.TextField(db_column='q_title', verbose_name='Вопрос')),
                ('q_chance', models.IntegerField(db_column='q_chance', verbose_name='Шанс')),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('score_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('score_text', models.TextField(db_column='score_text', verbose_name='Оценка')),
            ],
            options={
                'db_table': 'score',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('test_name', models.TextField(db_column='test_name', verbose_name='Название')),
                ('test_create_date', models.DateTimeField(db_column='test_create_date', verbose_name='Дата создания теста')),
                ('test_subject', models.TextField(db_column='test_subject', verbose_name='Предмет')),
                ('is_tree', models.BooleanField(db_column='is_tree', default=False, verbose_name='Древовидность')),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestingSystem',
            fields=[
                ('ts_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ts_start_time', models.DateTimeField(db_column='ts_start_time', verbose_name='Дата начала')),
                ('ts_end_time', models.DateTimeField(db_column='ts_end_time', verbose_name='Дата окончания')),
                ('ts_count_right_answers', models.IntegerField(db_column='ts_count_right_answers', verbose_name='Количество правильных ответов')),
            ],
            options={
                'db_table': 'testing_system',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField(db_column='user_name', verbose_name='Имя')),
                ('user_type', models.TextField(db_column='user_type', verbose_name='Тип')),
                ('login', models.TextField(db_column='login', verbose_name='Логин')),
                ('password', models.TextField(db_column='password', verbose_name='Пароль')),
                ('create_test_permission', models.BooleanField(db_column='create_test_permission', verbose_name='Разрешение на создание теста')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]