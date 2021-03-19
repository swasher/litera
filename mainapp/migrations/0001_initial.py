# Generated by Django 3.0.7 on 2020-06-22 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Font',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fontSubfamily', models.CharField(help_text='Подсемейство', max_length=150)),
                ('fullName', models.CharField(help_text='Полное название шрифта', max_length=150)),
                ('designer', models.CharField(help_text='Дизайнер', max_length=150)),
                ('designerURL', models.CharField(help_text='URL дизайнера', max_length=150)),
                ('manufacturer', models.CharField(help_text='Изготовитель', max_length=150)),
                ('manufacturerURL', models.CharField(help_text='URL поставщика', max_length=150)),
                ('trademark', models.CharField(help_text='Торговая марка', max_length=150)),
                ('licenseURL', models.CharField(help_text='URL лицензии', max_length=150)),
                ('postScriptName', models.CharField(help_text='PostScript название', max_length=150)),
                ('uniqueID', models.CharField(help_text='Идентификатор', max_length=150)),
                ('version', models.CharField(help_text='Версия', max_length=150)),
                ('copyright', models.CharField(help_text='Copyright', max_length=150)),
                ('free', models.BooleanField(default=False)),
                ('fontfile', models.FileField(upload_to='fonts/')),
                ('fontFamily', models.ForeignKey(help_text='Семейство', on_delete=django.db.models.deletion.CASCADE, to='mainapp.Family')),
            ],
        ),
    ]