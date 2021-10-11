# Generated by Django 3.2.8 on 2021-10-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vue_app', '0005_rename_created_at_employees_dateofjoining'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('TweetId', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500)),
                ('Description', models.CharField(max_length=500)),
                ('DateOfJoining', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
    ]
