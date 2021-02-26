from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from myrestaurants.models import Restaurant, Dish
from myrestaurants.forms import RestaurantForm, DishForm
from myrestaurants.views import RestaurantCreate, DishCreate, RestaurantDetail, review, \
    LoginRequiredCheckIsOwnerUpdateView

app_name = "myrestaurants"

urlpatterns = [
    # List latest 5 restaurants: /myrestaurants/
    url(r'^$', ListView.as_view(queryset=Restaurant.objects.filter(date__lte=timezone.now()).order_by('-date')[:5],
    context_object_name='latest_restaurant_list', template_name='myrestaurants/restaurant_list.html'), name='restaurant_list'),

    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^restaurants/(?P<pk>\d+)/$', RestaurantDetail.as_view(), name='restaurant_detail'),

    # Restaurant dish details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^restaurants/(?P<pkr>\d+)/dishes/(?P<pk>\d+)/$',
    DetailView.as_view(model=Dish, template_name='myrestaurants/dish_detail.html'), name='dish_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$', RestaurantCreate.as_view(), name='restaurant_create'),

    # Edit restaurant details, ex.: /myrestaurants/restaurants/1/edit/
    url(r'^restaurants/(?P<pk>\d+)/edit/$',
    LoginRequiredCheckIsOwnerUpdateView.as_view(model=Restaurant, form_class=RestaurantForm),
    name='restaurant_edit'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/dishes/create/$', DishCreate.as_view(), name='dish_create'),

    # Create a restaurant review, ex.: /myrestaurants/restaurants/1/reviews/create/
    url(r'^restaurants/(?P<pk>\d+)/reviews/create/$', review, name='review_create'),
]