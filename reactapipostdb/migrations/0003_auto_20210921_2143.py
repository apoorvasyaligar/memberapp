# Generated by Django 3.2.7 on 2021-09-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reactapipostdb', '0002_infomodel_datetimeofupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infomodel',
            name='address1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='address2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='datacategories',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='dateofsignature',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='dob',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='email',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='optionalyourname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='phonenumber',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='infomodel',
            name='signatureurl',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
