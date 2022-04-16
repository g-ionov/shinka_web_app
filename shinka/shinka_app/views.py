from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions
from django.db.models import Sum, Q
from .serializers import *

class ReviewView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAdminUser]

class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class WorkListView(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkListSerializer
    permission_classes = [permissions.IsAdminUser]

class WorkCreateView(generics.CreateAPIView):
    serializer_class = WorkCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class WorkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return WorkDetailGetSerializer
        else:
            return WorkDetailSerializer

    permission_classes = [permissions.IsAdminUser]

class ServiceWorkCreateView(generics.CreateAPIView):
    serializer_class = ServiceWorkCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class StockTypeView(generics.ListAPIView):
    queryset = StockType.objects.annotate(Sum('stock__number')).filter(stock__number__sum__gt=0).order_by()
    serializer_class = StockTypeSerializer
    permission_classes = [permissions.IsAdminUser]

class StockTypeCreateView(generics.CreateAPIView):
    serializer_class = StockTypeSerializer
    permission_classes = [permissions.IsAdminUser]

class StockView(generics.ListAPIView):
    queryset = Stock.objects.filter(stock_type__isnull=False)
    serializer_class = StockSerializer
    permission_classes = [permissions.IsAdminUser]

class StockCreateView(generics.CreateAPIView):
    serializer_class = StockCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class WheelsView(generics.ListAPIView):
    queryset = Wheels.objects.annotate(Sum('stock__number')).filter(stock__number__sum__gt=0).order_by()
    serializer_class = WheelsSerializer
    permission_classes = [permissions.IsAdminUser]

class WheelsCreateView(generics.CreateAPIView):
    serializer_class = WheelsCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class WheelsSuppliesView(generics.ListAPIView):
    serializer_class = WheelsSuppliesSerializer
    queryset = Stock.objects.filter(wheels__isnull=False)
    permission_classes = [permissions.IsAdminUser]

class WheelsSuppliesCreateView(generics.CreateAPIView):
    serializer_class = WheelsSuppliesCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class PositionView(generics.ListAPIView):
    queryset = PositionChange.objects.select_related('new_position').select_related('worker').all()
    serializer_class = PositionSerializer
    permission_classes = [permissions.IsAdminUser]

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ClientDetailSerializer
        else:
            return ClientDetailPostSerializer

    queryset = Client.objects.prefetch_related('car')
    permission_classes = [permissions.IsAdminUser]

class ClientView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]

class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser]

class BonusFineView(generics.ListAPIView):
    queryset = BonusFine.objects.prefetch_related('worker').all()
    serializer_class = BonusFineSerializer
    permission_classes = [permissions.IsAdminUser]

class BonusFineCreateView(generics.CreateAPIView):
    serializer_class = BonusFineCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class ScheduleView(generics.ListAPIView):
    queryset = WorkerSchedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [permissions.IsAdminUser]

class ScheduleCreateView(generics.CreateAPIView):
    serializer_class = ScheduleCreateSerializer
    permission_classes = [permissions.IsAdminUser]

class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScheduleCreateSerializer
    queryset = WorkerSchedule.objects.all()
    permission_classes = [permissions.IsAdminUser]
