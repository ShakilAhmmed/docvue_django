# Generated by Django 2.2.2 on 2019-06-17 18:15

from django.db import migrations, models
import myfolder_section.validators


class Migration(migrations.Migration):

    dependencies = [
        ('myfolder_section', '0003_auto_20190612_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=120, unique=True, validators=[myfolder_section.validators.clean_project_name])),
                ('folder_description', models.TextField()),
                ('parent_folder', models.IntegerField()),
                ('created_by', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'my_folder',
            },
        ),
    ]
