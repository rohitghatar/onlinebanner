# Generated by Django 4.2.4 on 2023-12-25 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bannerapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banners_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(upload_to='banners_image')),
                ('pub_name', models.CharField(max_length=20)),
                ('banner_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('price', models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='banners',
        ),
    ]
