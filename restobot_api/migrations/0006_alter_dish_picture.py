# Generated by Django 4.2.3 on 2023-08-05 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restobot_api', '0005_alter_dish_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='picture',
            field=models.ImageField(default='No_image.jpg', upload_to='dish_pictures/'),
        ),
    ]