# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('req_type', models.CharField(max_length=1, choices=[(b'P', b'Prerequisite'), (b'C', b'Corequisite')])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('req', models.ForeignKey(related_name='req', to='course.Course')),
                ('req_for', models.ForeignKey(related_name='req_for', to='course.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
