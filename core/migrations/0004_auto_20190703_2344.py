# Generated by Django 2.2.3 on 2019-07-03 23:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190703_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rcuser',
            name='telegram_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TelegramUser'),
        ),
    ]