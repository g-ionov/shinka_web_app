from django.contrib import admin
from .models import *

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'car_model', 'vehicle_num')
    list_display_links = ('id', 'brand', 'car_model')
    search_fields = ('brand', 'car_model', 'vehicle_num')
    list_filter = ('brand', 'car_model')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'patronymic', 'phoneNumber', 'finding_from', 'updated_at', 'created_at')
    list_display_links = ('id', 'surname', 'name', 'patronymic')
    search_fields = ('surname', 'name', 'patronymic', 'phoneNumber')

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_of_work', 'date_of_work', 'approximate_begin_time', 'real_begin_time', 'end_time', 'extra_price', 'comment', 'main_worker', 'client', 'car', 'updated_at', 'created_at')
    list_display_links = ('id', 'type_of_work', 'client', 'car')
    search_fields = ('id', 'type_of_work', 'date_of_work', 'main_worker', 'client', 'car')
    list_filter = ('type_of_work', 'main_worker')

class WorkerAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic', 'phoneNumber', 'position', 'updated_at', 'created_at')
    list_display_links = ('surname', 'name', 'patronymic')
    search_fields = ('surname', 'name', 'patronymic', 'phoneNumber')
    list_filter = ('position',)

class WorkerScheduleAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'attendance', 'hours', 'place')
    list_display_links = ('worker', 'date')
    search_fields = ('worker', 'date', 'attendance')
    list_filter = ('attendance', 'date')
    list_editable = ('attendance',)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'updated_at', 'created_at')
    list_display_links = ('name', 'price')
    search_fields = ('name', 'price')

class PositionChangeAdmin(admin.ModelAdmin):
    list_display = ('worker', 'new_position', 'created_at')
    list_display_links = ('worker', 'new_position')
    search_fields = ('worker', 'new_position')
    list_filter = ('new_position',)

class BonusFineAdmin(admin.ModelAdmin):
    list_display = ('worker', 'date', 'price', 'comment')
    list_display_links = ('worker', 'date')
    search_fields = ('worker', 'date')
    list_filter = ('worker',)

class ServiceListAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    list_display_links = ('name', 'price')
    search_fields = ('name',)

class ServiceWorkAdmin(admin.ModelAdmin):
    list_display = ('work', 'service', 'quantity')
    list_display_links = ('work', 'service')
    search_fields = ('work', 'service')
    list_filter = ('service',)

class StockTypeAdmin(admin.ModelAdmin):
    list_display = ('item_type', 'name', 'default_price', 'sale_price')
    list_display_links = ('item_type', 'name')
    search_fields = ('item_type', 'name')
    list_filter = ('item_type',)

# class StockWorkAdmin(admin.ModelAdmin):
#     list_display = ('work', 'stock', 'quantity')
#     list_display_links = ('work', 'stock')
#     search_fields = ('work', 'stock')
#     list_filter = ('stock',)

class StockAdmin(admin.ModelAdmin):
    list_display = ('stock_type', 'wheels', 'date', 'number')
    list_display_links = ('stock_type', 'wheels', 'date')
    search_fields = ('stock_type', 'date')
    list_filter = ('stock_type',)

class WheelsAdmin(admin.ModelAdmin):
    list_display = ('type', 'brand', 'model_name', 'diameter', 'width', 'profile', 'run_flat', 'marking_c', 'grade', 'winter', 'status')
    list_display_links = ('model_name',)
    search_fields = ('model_name', 'diameter', 'width', 'profile', 'run_flat', 'marking_c', 'grade', 'winter')
    list_filter = ('winter', 'grade', 'run_flat', 'marking_c')
    list_editable = ('run_flat', 'marking_c', 'winter', 'grade')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('work', 'grade', 'comment', 'created_at', 'updated_at')
    list_display_links = ('work',)
    search_fields = ('work',)
    list_filter = ('grade',)


admin.site.register(Car, CarAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Work, WorkAdmin)
# admin.site.register(Schedule)
admin.site.register(Worker, WorkerAdmin)
admin.site.register(WorkerSchedule, WorkerScheduleAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(PositionChange, PositionChangeAdmin)
admin.site.register(BonusFine, BonusFineAdmin)
admin.site.register(ServiceList, ServiceListAdmin)
admin.site.register(ServiceWork, ServiceWorkAdmin)
admin.site.register(StockType, StockTypeAdmin)
# admin.site.register(StockWork, StockWorkAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Wheels, WheelsAdmin)

