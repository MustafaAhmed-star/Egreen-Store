from django.shortcuts import render
from django.views import generic
from .models import Product,Review,ProductImages,Brand 

class ProductList(generic.ListView):
    model = Product
    
class ProductDetail(generic.DetailView):
    model = Product
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product =self.get_object())
        context["images"] =  ProductImages.objects.filter(product =self.get_object())
        context["related"] =  Product.objects.filter(brand =self.get_object().brand)[:5]
        return context        
        
        
class BrandList(generic.ListView):
    model = Brand
    
class BrandDetail(generic.DetailView):
    model = Brand