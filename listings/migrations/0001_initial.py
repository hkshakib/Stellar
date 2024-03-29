# Generated by Django 4.2.1 on 2023-05-28 09:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realestate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True)),
                ('sale_type', models.CharField(choices=[('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='For Sale', max_length=50)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('home_type', models.CharField(choices=[('House', 'House'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse')], default='House', max_length=50)),
                ('sqft', models.IntegerField()),
                ('open_house', models.BooleanField(default=False)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.listing')),
            ],
        ),
        migrations.AddField(
            model_name='listing',
            name='photos',
            field=models.ManyToManyField(related_name='listing_photos', to='listings.photo'),
        ),
        migrations.AddField(
            model_name='listing',
            name='realtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realestate.realestate'),
        ),
    ]
