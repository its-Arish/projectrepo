# Generated by Django 2.1 on 2021-03-04 05:39

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20210302_2055'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('spam', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spam_filtering',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.Listing'),
        ),
        migrations.AddField(
            model_name='spam_filtering',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='spam_filtering',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 4, 5, 39, 55, 810797), null=True),
        ),
    ]