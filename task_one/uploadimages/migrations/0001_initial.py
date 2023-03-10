# Generated by Django 4.1.7 on 2023-03-11 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_images', models.ImageField(null=True, upload_to='')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('thumbnail_200', models.ImageField(blank=True, null=True, upload_to='')),
                ('thumbnail_400', models.ImageField(blank=True, null=True, upload_to='')),
                ('uploaded_by', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
