# Generated by Django 3.0.8 on 2020-07-31 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('total_pages', models.IntegerField(null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('isbn', models.CharField(max_length=13, null=True)),
                ('published_date', models.DateField(null=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Authors')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Genres')),
                ('publisher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.Publishers')),
            ],
            options={
                'db_table': 'Books',
            },
        ),
    ]
