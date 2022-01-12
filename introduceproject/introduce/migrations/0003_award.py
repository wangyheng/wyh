# Generated by Django 4.0.1 on 2022-01-10 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('introduce', '0002_test_alter_category_options_alter_post_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=500, null=True, verbose_name='荣誉描述')),
                ('photo', models.ImageField(blank=True, upload_to='Award/', verbose_name='荣誉照片')),
            ],
            options={
                'verbose_name': '获奖和荣誉',
                'verbose_name_plural': '获奖和荣誉',
            },
        ),
    ]