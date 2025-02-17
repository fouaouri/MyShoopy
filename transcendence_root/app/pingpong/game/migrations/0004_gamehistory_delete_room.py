# Generated by Django 5.1.3 on 2024-12-31 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_room_ball_position_room_ball_velocity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_name', models.CharField(max_length=100)),
                ('player2_name', models.CharField(max_length=100)),
                ('score_player1', models.IntegerField(default=0)),
                ('score_player2', models.IntegerField(default=0)),
                ('winner', models.CharField(max_length=100)),
                ('date_played', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]
