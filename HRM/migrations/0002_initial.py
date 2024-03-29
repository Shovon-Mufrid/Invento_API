# Generated by Django 4.2.6 on 2023-10-16 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('HRM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='hrm_employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='designation',
            name='Department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM.department'),
        ),
        migrations.AddField(
            model_name='company',
            name='GroupOfCompany',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM.groupofcompany'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_attendance', to='HRM.employee'),
        ),
    ]
