# Generated by Django 4.1.7 on 2023-02-19 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_shark_standard_buff_standard_equipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registered_user',
            name='IP_address',
        ),
        migrations.CreateModel(
            name='attack_action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.standard_buff')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.standard_equipment')),
                ('shark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.shark')),
            ],
        ),
    ]
