# Generated by Django 3.2 on 2021-05-16 01:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_auto_20210502_1506'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TblAlert',
        ),
        migrations.DeleteModel(
            name='TblDevice',
        ),
        migrations.DeleteModel(
            name='TblIncoming',
        ),
        migrations.DeleteModel(
            name='TblSubscription',
        ),
        migrations.DeleteModel(
            name='TblUser',
        ),
    ]
