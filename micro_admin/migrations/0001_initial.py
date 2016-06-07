# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 07:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('user_roles', models.CharField(choices=[('BranchManager', 'BranchManager'), ('LoanOfficer', 'LoanOfficer'), ('Cashier', 'Cashier')], max_length=20)),
                ('date_of_birth', models.DateField(default='2000-01-01', null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('district', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('area', models.CharField(max_length=150, null=True)),
                ('mobile', models.CharField(default='0', max_length=10, null=True)),
                ('pincode', models.CharField(default='', max_length=10, null=True)),
            ],
            options={
                'permissions': (('branch_manager', 'Can manage all accounts under his/her branch.'),),
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('opening_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('phone_number', models.BigIntegerField()),
                ('pincode', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('account_number', models.CharField(max_length=50, unique=True)),
                ('date_of_birth', models.DateField()),
                ('blood_group', models.CharField(default=True, max_length=10, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('client_role', models.CharField(choices=[('FirstLeader', 'FirstLeader'), ('SecondLeader', 'SecondLeader'), ('GroupMember', 'GroupMember')], max_length=20)),
                ('occupation', models.CharField(max_length=200)),
                ('annual_income', models.BigIntegerField()),
                ('joined_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=150)),
                ('mobile', models.CharField(default=True, max_length=20, null=True)),
                ('pincode', models.CharField(default=True, max_length=20, null=True)),
                ('photo', models.ImageField(null=True, upload_to='static/images/users')),
                ('signature', models.ImageField(null=True, upload_to='static/images/signatures')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(default='UnAssigned', max_length=50, null=True)),
                ('sharecapital_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('entrancefee_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('membershipfee_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('bookfee_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('insurance_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FixedDeposits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposited_date', models.DateField()),
                ('status', models.CharField(choices=[('Opened', 'Opened'), ('Closed', 'Closed')], max_length=20)),
                ('fixed_deposit_number', models.CharField(max_length=50, unique=True)),
                ('fixed_deposit_amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('fixed_deposit_period', models.IntegerField()),
                ('fixed_deposit_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nominee_firstname', models.CharField(max_length=50)),
                ('nominee_lastname', models.CharField(max_length=50)),
                ('nominee_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('relationship_with_nominee', models.CharField(max_length=50)),
                ('nominee_date_of_birth', models.DateField()),
                ('nominee_occupation', models.CharField(max_length=50)),
                ('nominee_photo', models.ImageField(upload_to='static/images/users')),
                ('nominee_signature', models.ImageField(upload_to='static/images/signatures')),
                ('fixed_deposit_interest', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('maturity_amount', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('account_number', models.CharField(max_length=50, unique=True)),
                ('activation_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(default='UnAssigned', max_length=50)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch')),
                ('clients', models.ManyToManyField(blank=True, to='micro_admin.Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_created_by', to=settings.AUTH_USER_MODEL)),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMeetings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_date', models.DateField()),
                ('meeting_time', models.CharField(max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Group')),
            ],
        ),
        migrations.CreateModel(
            name='LoanAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50, unique=True)),
                ('interest_type', models.CharField(choices=[('Flat', 'Flat'), ('Declining', 'Declining')], max_length=20)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Withdrawn', 'Withdrawn'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Closed', 'Closed')], max_length=20)),
                ('opening_date', models.DateField(auto_now_add=True)),
                ('approved_date', models.DateField(blank=True, null=True)),
                ('loan_issued_date', models.DateField(blank=True, null=True)),
                ('closed_date', models.DateField(blank=True, null=True)),
                ('loan_amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('loan_repayment_period', models.IntegerField()),
                ('loan_repayment_every', models.IntegerField()),
                ('loan_repayment_amount', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('total_loan_amount_repaid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('loanpurpose_description', models.TextField()),
                ('annual_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('interest_charged', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_interest_repaid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_loan_paid', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_loan_balance', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('loanprocessingfee_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('no_of_repayments_completed', models.IntegerField(default=0)),
                ('principle_repayment', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Group')),
                ('loan_issued_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_issued_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('voucher_number', models.CharField(max_length=50, unique=True)),
                ('payment_type', models.CharField(choices=[('Loans', 'Loans'), ('TravellingAllowance', 'TravellingAllowance'), ('Paymentofsalary', 'Paymentofsalary'), ('PrintingCharges', 'PrintingCharges'), ('StationaryCharges', 'StationaryCharges'), ('OtherCharges', 'OtherCharges'), ('SavingsWithdrawal', 'SavingsWithdrawal'), ('FixedWithdrawal', 'FixedWithdrawal'), ('RecurringWithdrawal', 'RecurringWithdrawal')], max_length=25)),
                ('amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('interest', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('total_amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('totalamount_in_words', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Group')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Receipts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('receipt_number', models.CharField(max_length=50, unique=True)),
                ('sharecapital_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('entrancefee_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('membershipfee_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('bookfee_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('loanprocessingfee_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('savingsdeposit_thrift_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('fixeddeposit_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('recurringdeposit_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('loanprinciple_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('loaninterest_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('insurance_amount', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('savings_balance_atinstant', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('demand_loanprinciple_amount_atinstant', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('demand_loaninterest_amount_atinstant', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('principle_loan_balance_atinstant', models.DecimalField(blank=True, decimal_places=6, default=0, max_digits=19, null=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
                ('group', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Group')),
                ('group_loan_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_loan_account', to='micro_admin.LoanAccount')),
                ('member_loan_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.LoanAccount')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecurringDeposits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposited_date', models.DateField()),
                ('reccuring_deposit_number', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('Opened', 'Opened'), ('Closed', 'Closed')], max_length=20)),
                ('recurring_deposit_amount', models.DecimalField(decimal_places=6, max_digits=19)),
                ('recurring_deposit_period', models.IntegerField()),
                ('recurring_deposit_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('nominee_firstname', models.CharField(max_length=50)),
                ('nominee_lastname', models.CharField(max_length=50)),
                ('nominee_gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('relationship_with_nominee', models.CharField(max_length=50)),
                ('nominee_date_of_birth', models.DateField()),
                ('nominee_occupation', models.CharField(max_length=50)),
                ('nominee_photo', models.ImageField(upload_to='static/images/users')),
                ('nominee_signature', models.ImageField(upload_to='static/images/signatures')),
                ('recurring_deposit_interest', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('maturity_amount', models.DecimalField(blank=True, decimal_places=6, max_digits=19, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
            ],
        ),
        migrations.CreateModel(
            name='SavingsAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('Applied', 'Applied'), ('Withdrawn', 'Withdrawn'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Closed', 'Closed')], max_length=20)),
                ('opening_date', models.DateField()),
                ('min_required_balance', models.DecimalField(decimal_places=2, max_digits=5)),
                ('savings_balance', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('annual_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_deposits', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('total_withdrawals', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('fixeddeposit_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('fixeddepositperiod', models.IntegerField(blank=True, null=True)),
                ('recurringdeposit_amount', models.DecimalField(decimal_places=6, default=0, max_digits=19)),
                ('recurringdepositperiod', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Client')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Group')),
            ],
        ),
        migrations.AddField(
            model_name='centers',
            name='groups',
            field=models.ManyToManyField(blank=True, to='micro_admin.Group'),
        ),
        migrations.AddField(
            model_name='user',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='micro_admin.Branch'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='user_permissions', to='auth.Permission'),
        ),
    ]
