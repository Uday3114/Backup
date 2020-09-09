# Generated by Django 3.1 on 2020-09-09 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadingImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'verbose_name': 'UploadingImage',
                'verbose_name_plural': 'UploadingImages',
            },
        ),
    ]
