from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Property
from django.views.generic.edit import FormMixin
from .forms import PropertyBookForm
from .filters import PropertyFilter
from django_filters.views import FilterView

# Create your views here.

class PropertyList(FilterView):
    model = Property
    paginate_by = 2
    
    filterset_class = PropertyFilter
    template_name = 'property/property_list.html'


class PropertyDetail(FormMixin,DetailView):
    model = Property
    form_class = PropertyBookForm
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category=self.object.category)[:3]
        return context
      
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            myForm = form.save(commit=False)
            myForm.property = self.get_object()
            myForm.user = request.user
            myForm.save()
            return redirect('/')
        
            
    
    