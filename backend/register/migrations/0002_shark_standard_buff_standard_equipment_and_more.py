# Generated by Django 4.1.7 on 2023-02-18 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack', models.IntegerField()),
                ('deffence', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('hp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='standard_buff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buff_name', models.CharField(max_length=30)),
                ('attack', models.IntegerField()),
                ('deffence', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='standard_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=30)),
                ('attack', models.IntegerField()),
                ('deffence', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='registered_user',
            name='IP_address',
            field=models.GenericIPAddressField(),
        ),
        migrations.CreateModel(
            name='available_equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affect_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.shark')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.registered_user')),
                ('standard_equipment_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.standard_equipment')),
            ],
        ),
        migrations.CreateModel(
            name='available_buff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('affect_on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.shark')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.registered_user')),
                ('standard_buff_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.standard_buff')),
            ],
        ),
    ]
