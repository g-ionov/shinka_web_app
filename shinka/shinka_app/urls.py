from django.contrib import admin
from django.urls import path, include
from .views import *



app_name = 'shinka_app'
urlpatterns = [
    path('wheels/', WheelsView.as_view()),
    path('wheels/create', WheelsCreateView.as_view()),
    path('wheels/supplies', WheelsSuppliesView.as_view()),
    path('wheels/supplies/create', WheelsSuppliesCreateView.as_view()),
    path('review/', ReviewView.as_view()),
    path('review/create', ReviewCreateView.as_view()),
    path('', WorkListView.as_view()),
    path('work/create', WorkCreateView.as_view()),
    path('work/detail/<int:pk>', WorkDetailView.as_view()),
    path('work/service/create', ServiceWorkCreateView.as_view()),
    path('stock/', StockTypeView.as_view()),
    path('stock/supplies', StockView.as_view()),
    path('stock/create', StockTypeCreateView.as_view()),
    path('stock/supplies/create', StockCreateView.as_view()),
    path('workers/positions/', PositionView.as_view()),
    path('workers/bonus/', BonusFineView.as_view()),
    path('workers/bonus/create', BonusFineCreateView.as_view()),
    path('client/detail/<int:pk>', ClientDetailView.as_view()),
    path('client/list', ClientView.as_view()),
    path('client/create', ClientCreateView.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('schedule/', ScheduleView.as_view()),
    path('schedule/create/', ScheduleCreateView.as_view()),
    path('schedule/detail/<int:pk>', ScheduleDetailView.as_view()),
]
