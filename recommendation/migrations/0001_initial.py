# Generated by Django 3.1.6 on 2021-09-25 20:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('relationship', models.CharField(choices=[('we work together in the same team or on the same project', 'We work together in the same team or on the same project'), ('blaise was under my responsability', 'Blaise was under my responsability'), ('i was under his responsability', 'I was under his responsability'), ('we work together inderectly', 'We work together inderectly'), ('i was his customer', 'I was his customer'), ('i heard about his skills', 'I heard about his skills')], max_length=200)),
                ('comment', models.TextField(blank=True, default=None, max_length=1000, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]