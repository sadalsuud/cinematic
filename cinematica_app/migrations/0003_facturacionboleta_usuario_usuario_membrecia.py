# Generated by Django 4.0.6 on 2022-07-15 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinematica_app', '0002_remove_usuario_membrecia'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturacionboleta',
            name='usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='membrecia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='cinematica_app.membrecia'),
            preserve_default=False,
        ),
    ]