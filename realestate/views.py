from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from .serializers import RealEstateSerializer

from .models import RealEstate


class RealtorListView(ListAPIView):
    """
    This view is responsible for creating the List of all realestate products
    """
    permission_classes = (permissions.AllowAny,)
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer
    pagination_class = None


class RealtorView(RetrieveAPIView):
    """
    This view is responsible for single products view
    """
    queryset = RealEstate.objects.all()
    serializer_class = RealEstateSerializer


class TopSellerView(ListAPIView):
    """
    this view is responsible for Top Seller products view
    """
    permission_classes = (permissions.AllowAny,)
    queryset = RealEstate.objects.filter(top_seller=True)
    serializer_class = RealEstateSerializer
    pagination_class = None
