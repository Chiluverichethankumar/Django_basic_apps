# Generated by Django 4.2.21 on 2025-05-26 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_alter_student_id_alter_todoitem_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
