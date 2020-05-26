# Generated by Django 2.2 on 2020-05-26 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('gift_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='example.GiftList')),
            ],
        ),
    ]
