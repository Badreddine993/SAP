from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('income.urls')),
    path('', include('expenses.urls')),
    path('auth/', include('authentication.urls')),
    path('preferences/', include('userpreferences.urls')),
    path('', include('chatbot.urls')),
    path('',include('Maintenance.urls')),

]