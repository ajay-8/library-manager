# Generated by Django 5.0.4 on 2024-04-20 12:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('publication_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('quantity_in_stock', models.PositiveIntegerField()),
                ('author', models.ManyToManyField(related_name='authors_book', to='library.author')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='biography',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author_biography', to='library.book'),
        ),
        migrations.CreateModel(
            name='BookCheckoutInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(blank=True, null=True)),
                ('is_returned', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
            ],
        ),
    ]
