# Generated by Django 3.1.6 on 2021-09-28 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='relationship',
            field=models.CharField(choices=[('we work together in the same team or on the same project', 'We work together in the same team or on the same project'), ('blaise was under my responsability', 'Blaise was under my responsability'), ('we work together inderectly', 'We work together inderectly'), ('i was his customer', 'I was his customer'), ('i heard about his skills', 'I heard about his skills')], max_length=200),
        ),
    ]