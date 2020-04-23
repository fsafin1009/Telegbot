# Generated by Django 3.0.5 on 2020-04-23 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegbot', '0002_auto_20200423_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(default='Sample content', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='city',
            field=models.CharField(max_length=128, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='player',
            name='mobil_phone',
            field=models.CharField(max_length=20, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='player',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=128, verbose_name='Team'),
        ),
        migrations.AlterField(
            model_name='player_response',
            name='message',
            field=models.CharField(max_length=150, verbose_name='Response'),
        ),
        migrations.AlterField(
            model_name='player_response',
            name='player_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegbot.Player', verbose_name='Player name'),
        ),
        migrations.AlterField(
            model_name='player_response',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telegbot.Question', verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]