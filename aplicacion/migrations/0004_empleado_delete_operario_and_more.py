# Generated by Django 4.2.3 on 2023-08-01 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alter_mantenimiento_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Operario',
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='planificado',
            field=models.CharField(max_length=10),
        ),
    ]