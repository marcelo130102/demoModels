# Generated by Django 4.0.4 on 2022-11-29 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Examen_Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_fecha', models.DateTimeField()),
                ('curso', models.CharField(max_length=30)),
                ('evaluador', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('n_preguntas', models.IntegerField()),
                ('puntaje_total', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('salario', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_fecha', models.DateTimeField()),
                ('curso', models.CharField(max_length=30)),
                ('evaluador', models.CharField(max_length=50)),
                ('tema_proyecto', models.CharField(max_length=100)),
                ('n_grupos', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aula', models.CharField(max_length=2)),
                ('hora_entrada', models.TimeField()),
                ('profesor_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='myapp.profesor')),
            ],
        ),
        migrations.AddConstraint(
            model_name='profesor',
            constraint=models.UniqueConstraint(fields=('id', 'first_name', 'last_name'), name='primary_key_profesor'),
        ),
        migrations.AddField(
            model_name='alumno',
            name='idSalon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.salon'),
        ),
        migrations.CreateModel(
            name='OrderedAlum',
            fields=[
            ],
            options={
                'ordering': ['last_name'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.alumno',),
        ),
        migrations.CreateModel(
            name='OrderedNameProject',
            fields=[
            ],
            options={
                'ordering': ['tema_proyecto'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('myapp.proyecto',),
        ),
        migrations.AddConstraint(
            model_name='alumno',
            constraint=models.UniqueConstraint(fields=('id', 'first_name', 'last_name'), name='primary_key_alumno'),
        ),
    ]
