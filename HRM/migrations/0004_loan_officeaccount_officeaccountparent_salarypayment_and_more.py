# Generated by Django 4.2.6 on 2023-10-19 11:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HRM', '0003_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanAmount', models.FloatField(blank=True, default=0.0, null=True)),
                ('loanType', models.CharField(blank=True, max_length=255, null=True)),
                ('loanPayableMonths', models.IntegerField(blank=True, default=0, null=True)),
                ('loanPayableAmount', models.FloatField(blank=True, default=0.0, null=True)),
                ('loanStatus', models.CharField(default='pending', max_length=255)),
                ('loanPaymentStatus', models.CharField(default='pending', max_length=255)),
                ('note', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_loan', to='HRM.employee')),
            ],
        ),
        migrations.CreateModel(
            name='OfficeAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('details', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('account_no', models.CharField(blank=True, max_length=255, null=True)),
                ('cash', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('txnCharge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OfficeAccountParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalaryPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paidAmount', models.FloatField(blank=True, default=0.0, null=True)),
                ('salaryMonth', models.IntegerField(blank=True, default=0, null=True)),
                ('salaryYear', models.IntegerField(blank=True, default=0, null=True)),
                ('paymentDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary_payment', to='HRM.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monthlySalary', models.FloatField(blank=True, default=0.0, null=True)),
                ('dailyAllowance', models.FloatField(blank=True, default=0.0, null=True)),
                ('incentive', models.FloatField(blank=True, default=0.0, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_salary', to='HRM.employee')),
            ],
        ),
        migrations.CreateModel(
            name='PaySlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaryMonth', models.IntegerField(blank=True, default=0, null=True)),
                ('salaryYear', models.IntegerField(blank=True, default=0, null=True)),
                ('publicHoliday', models.IntegerField(blank=True, default=0, null=True)),
                ('leave', models.IntegerField(blank=True, default=0, null=True)),
                ('present', models.IntegerField(blank=True, default=0, null=True)),
                ('absent', models.IntegerField(blank=True, default=0, null=True)),
                ('late', models.IntegerField(blank=True, default=0, null=True)),
                ('dayOverTime', models.IntegerField(blank=True, default=0, null=True)),
                ('nightOverTime', models.IntegerField(blank=True, default=0, null=True)),
                ('overtimeTotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('incentiveTotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('dailyAllowanceTotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('fine', models.FloatField(blank=True, default=0.0, null=True)),
                ('loan_adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('advance_adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('net_salary', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment', models.FloatField(blank=True, default=0.0, null=True)),
                ('due', models.FloatField(blank=True, default=0.0, null=True)),
                ('amount_1', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment_method_info_1', models.CharField(blank=True, max_length=255, null=True)),
                ('amount_2', models.FloatField(blank=True, default=0.0, null=True)),
                ('payment_method_info_2', models.CharField(blank=True, max_length=255, null=True)),
                ('paymentDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_payslip', to='HRM.employee')),
                ('payment_method_1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_payment_account1', to='HRM.officeaccount')),
                ('payment_method_2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employee_payment_account2', to='HRM.officeaccount')),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payslip_salary', to='HRM.salary')),
            ],
        ),
        migrations.AddField(
            model_name='officeaccount',
            name='accountparent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='HRM.officeaccountparent'),
        ),
        migrations.CreateModel(
            name='LoanPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paidAmount', models.FloatField(blank=True, default=0.0, null=True)),
                ('paymentDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee_loan_payment', to='HRM.employee')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_payment_loan', to='HRM.loan')),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='payment_method',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='loan_payment_method', to='HRM.officeaccount'),
        ),
    ]
