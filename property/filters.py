import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Property
        fields = ['name', 'place', 'category', 'price']
        order_by = ['-price', 'name']