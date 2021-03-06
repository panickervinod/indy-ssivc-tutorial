# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 16:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IssuerService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('issuerOrgTLA', models.CharField(max_length=255)),
                ('issuerOrgURL', models.CharField(blank=True, max_length=255, null=True)),
                ('DID', models.CharField(max_length=255)),
                ('effectiveDate', models.DateField(default=django.utils.timezone.now)),
                ('endDate', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ISSUER_SERVICE',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('code', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'PERMISSION',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'ROLE',
            },
        ),
        migrations.CreateModel(
            name='RolePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('permissionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RolePermissionpermissionId', to='api.Permission')),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='RolePermissionroleId', to='api.Role')),
            ],
            options={
                'db_table': 'ROLE_PERMISSION',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('givenName', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=150, null=True)),
                ('userId', models.CharField(blank=True, max_length=500, null=True)),
                ('guid', models.CharField(blank=True, max_length=100, null=True)),
                ('authorizationDirectory', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'USER',
            },
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CREATE_TIMESTAMP', models.DateTimeField(auto_now_add=True, null=True)),
                ('UPDATE_TIMESTAMP', models.DateTimeField(auto_now=True, null=True)),
                ('roleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserRoleroleId', to='api.Role')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UserRoleuserId', to='api.User')),
            ],
            options={
                'db_table': 'USER_ROLE',
            },
        ),
        migrations.RemoveField(
            model_name='issuerorg',
            name='jurisdictionId',
        ),
        migrations.RenameField(
            model_name='inactiveclaimreason',
            old_name='expirationDate',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='expirationDate',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='volocationtype',
            old_name='expirationDate',
            new_name='endDate',
        ),
        migrations.RenameField(
            model_name='votype',
            old_name='expirationDate',
            new_name='endDate',
        ),
        migrations.RemoveField(
            model_name='verifiedorg',
            name='orgType',
        ),
        migrations.RemoveField(
            model_name='verifiedorg',
            name='primaryLocation',
        ),
        migrations.AddField(
            model_name='verifiedorg',
            name='orgTypeId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='VerifiedOrgorgTypeId', to='api.VOType'),
        ),
        migrations.AddField(
            model_name='voclaimtype',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='voclaimtype',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='vodoingbusinessas',
            name='verifiedOrgId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='VODoingBusinessAsverifiedOrgId', to='api.VerifiedOrg'),
        ),
        migrations.AddField(
            model_name='volocation',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='volocation',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='volocation',
            name='verifiedOrgId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='VOLocationverifiedOrgId', to='api.VerifiedOrg'),
        ),
        migrations.AlterField(
            model_name='inactiveclaimreason',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='jurisdiction',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='verifiedorg',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='voclaim',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='voclaim',
            name='endDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voclaimtype',
            name='issuerOrgId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VOClaimTypeissuerOrgId', to='api.IssuerService'),
        ),
        migrations.AlterField(
            model_name='vodoingbusinessas',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='volocationtype',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='votype',
            name='effectiveDate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='IssuerOrg',
        ),
        migrations.AddField(
            model_name='issuerservice',
            name='jurisdictionId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='IssuerServicejurisdictionId', to='api.Jurisdiction'),
        ),
    ]
