# Generated by Django 2.2.3 on 2019-07-06 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190703_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramuser',
            name='chat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.TelegramChat'),
        ),
    ]
