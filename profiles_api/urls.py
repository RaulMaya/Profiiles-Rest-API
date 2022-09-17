from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile-viewset', views.UserProfileViewSet) #If you provide the queryset, Django will extract the name from the model

urlpatterns=[
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]