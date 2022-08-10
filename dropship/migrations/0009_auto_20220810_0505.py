# Generated by Django 2.2.4 on 2022-08-10 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropship', '0008_auto_20220809_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='issue',
            old_name='labels_list',
            new_name='labels',
        ),
        migrations.RenameField(
            model_name='issue',
            old_name='watchers_list',
            new_name='watchers',
        ),
        migrations.RemoveField(
            model_name='issue',
            name='reporter',
        ),
        migrations.AddField(
            model_name='issue',
            name='reportee',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportee', to='dropship.Member'),
        ),
    ]
