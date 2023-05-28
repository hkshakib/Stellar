from django.db import models
from django.utils.timezone import now
from realestate.models import RealEstate


class Listing(models.Model):
    FOR_SALE = 'For Sale'
    FOR_RENT = 'For Rent'
    SALE_CHOICES = [
        (FOR_SALE, 'For Sale'),
        (FOR_RENT, 'For Rent')
    ]

    HOUSE = 'House'
    CONDO = 'Condo'
    TOWNHOUSE = 'Townhouse'
    HOME_CHOICES = [
        (HOUSE, 'House'),
        (CONDO, 'Condo'),
        (TOWNHOUSE, 'Townhouse')
    ]

    realtor = models.ForeignKey(RealEstate, on_delete=models.DO_NOTHING)
    slug = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    sale_type = models.CharField(max_length=50, choices=SALE_CHOICES, default=FOR_SALE)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    home_type = models.CharField(max_length=50, choices=HOME_CHOICES, default=HOUSE)
    sqft = models.IntegerField()
    open_house = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=now, blank=True)
    photos = models.ManyToManyField('Photo', related_name='listing_photos')

    def __str__(self):
        return self.title


class Photo(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')

    def __str__(self):
        return f"Photo for {self.listing.title}"
