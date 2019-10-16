# Generated by Django 2.2.6 on 2019-10-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(db_index=True, max_length=64, verbose_name='Key')),
                ('value', models.CharField(blank=True, max_length=512, verbose_name='Value')),
                ('type', models.CharField(blank=True, choices=[('str', 'string'), ('int', 'integer'), ('float', 'float')], default='str', max_length=8, verbose_name='Type')),
                ('enabled', models.BooleanField(default=True, verbose_name='Enabled')),
                ('comment', models.TextField(blank=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]