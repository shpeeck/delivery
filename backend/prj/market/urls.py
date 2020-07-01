from django.urls import path, include
from market.views.auth import AuthViews, hello


urlpatterns = [
    path('hello', hello),
    path('userlogin', AuthViews.as_view())
]

        