# Generated by Django 3.0.3 on 2020-07-15 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0007_delete_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='bookname',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='cover_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='languague',
            new_name='language',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='pages',
            new_name='page_count',
        ),
        migrations.RemoveField(
            model_name='book',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='book',
            name='condition',
            field=models.CharField(choices=[('Like New', 'Like New'), ('Used', 'Used'), ('Collectible', 'Collectible')], default='LikeNew', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_type',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Soft', 'Soft')], default='Hard', max_length=20),
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(default='', max_length=2000),
        ),
        migrations.AddField(
            model_name='book',
            name='gener',
            field=models.CharField(default='', max_length=100),
        ),
    ]
