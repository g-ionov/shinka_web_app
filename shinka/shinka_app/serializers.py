from rest_framework import serializers
from .models import *
from drf_writable_nested import WritableNestedModelSerializer
from phonenumber_field.modelfields import PhoneNumberField

class ClientWithCarSerializer(serializers.ModelSerializer):
    car = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ('pk', 'surname', 'name', 'patronymic', 'phoneNumber', 'car')

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('brand', 'car_model', 'vehicle_num')

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('surname', 'name', 'patronymic', 'phoneNumber', 'finding_from')

class WorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work
        fields = ('type_of_work', 'date_of_work', 'approximate_begin_time', 'real_begin_time', 'end_time', 'extra_price', 'comment', 'main_worker', 'client', 'car')

class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('surname', 'name', 'patronymic', 'phoneNumber', 'position',)
# Сериализатор с ФИО рабочего
class LocalWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ('surname', 'name', 'patronymic')


class PositionSerializer(serializers.ModelSerializer):
    new_position = serializers.SlugRelatedField('name', read_only=True)
    worker = LocalWorkerSerializer()
    created_at = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = PositionChange
        fields = ('worker', 'new_position', 'created_at')

class PositionChangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionChange
        fields = ('worker', 'new_position', 'created_at')

class ServicelistSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceList
        fields = ('name', 'price')

class ServiceWorkSerializer(serializers.ModelSerializer):

    service = ServicelistSerializer()

    class Meta:
        model = ServiceWork
        fields = ('service', 'quantity')

class ServiceWorkCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceWork
        fields = ('work', 'service', 'quantity')

class StockTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockType
        fields = ('item_type', 'name', 'default_price', 'sale_price')

class StockSerializer(serializers.ModelSerializer):

    date = serializers.DateField(format='%d-%m-%Y')
    stock_type = StockTypeSerializer(many=True)

    class Meta:
        model = Stock
        fields = ('stock_type', 'date', 'number')

class StockCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        exclude = ('id', 'date', 'wheels')

# class StockWorkSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = StockWork
#         fields = ('work', 'stock', 'quantity')

class WheelsSerializer(serializers.ModelSerializer):
    class LocalStockSerializer(serializers.ModelSerializer):
        class Meta:
            model = Stock
            fields = ('number', )

    stock_set = LocalStockSerializer(many=True) #Подсчет количества колёс на складе

    class Meta:
        model = Wheels
        fields = ('type', 'brand', 'model_name', 'diameter', 'width', 'profile', 'run_flat', 'marking_c', 'grade', 'winter', 'stock_set')
        depth = 1

class WheelsCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Wheels
        exclude = ('id', )

class WheelsSuppliesSerializer(serializers.ModelSerializer):
    class LocalWheelsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Wheels
            fields = ('type', 'brand', 'model_name', 'diameter', 'width', 'profile', 'run_flat', 'marking_c', 'grade', 'winter')

    date = serializers.DateField(format='%d-%m-%Y')
    wheels = LocalWheelsSerializer()

    class Meta:
        model = Stock
        fields = ('wheels', 'date', 'number')

class WheelsSuppliesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        exclude = ('id', 'date', 'stock_type')

class ReviewSerializer(serializers.ModelSerializer):

    class LocalWorkSerializer(serializers.ModelSerializer):
        class LocalClientSerializer(serializers.ModelSerializer):
            class Meta:
                model = Client
                fields = ('surname', 'name', 'patronymic')
        main_worker = serializers.StringRelatedField()
        client = LocalClientSerializer(read_only=True)

        class Meta:
            model = Work
            fields = ('client', 'date_of_work', 'main_worker')

    work = LocalWorkSerializer()

    class Meta:
        model = Review
        fields = ('work', 'grade', 'comment')

class ReviewCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        exclude = ('created_at', 'updated_at')

class WorkListSerializer(serializers.ModelSerializer):

    car = CarSerializer()
    service = ServiceWorkSerializer(many=True)

    class Meta:
        model = Work
        fields = ('car', 'type_of_work', 'date_of_work', 'approximate_begin_time', 'real_begin_time', 'end_time', 'service', 'extra_price')
        depth = 2

class WorkCreateSerializer(serializers.ModelSerializer):

    class LocalCarSerializer(serializers.Serializer):
        brand = serializers.CharField(label='Марка', max_length=150)
        car_model = serializers.CharField(label='Модель', max_length=200)
        vehicle_num = serializers.CharField(label='Гос номер', max_length=12)


    car = LocalCarSerializer()

    def create(self, validated_data):
        car_data = validated_data.pop('car')
        if Car.objects.filter(vehicle_num=list(list(car_data.items())[2])[1]).exists():
            car_queryset_data = Car.objects.get(vehicle_num=list(list(car_data.items())[2])[1])
            work = Work.objects.create(car=car_queryset_data, **validated_data)
        else:
            car = Car.objects.create(**car_data)
            work = Work.objects.create(car=car, **validated_data)
        return work

    class Meta:
        model = Work
        fields = ('car', 'date_of_work', 'approximate_begin_time')

class LocalWheelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheels
        fields = ('type', 'brand', 'model_name')

class WorkDetailSerializer(WritableNestedModelSerializer ,serializers.ModelSerializer):

    class LocalClientSerializer(serializers.Serializer):
        surname = serializers.CharField(label='Фамилия', max_length=100)
        name = serializers.CharField(label='Имя', max_length=100)
        patronymic = serializers.CharField(allow_blank=True, allow_null=True, label='Отчество', max_length=100, required=False)
        phoneNumber = serializers.CharField(allow_blank=True, allow_null=True, label='Номер телефона', max_length=128, required=False)
        finding_from = serializers.CharField(allow_blank=True, allow_null=True, label='Откуда нашли', required=False,  style={'base_template': 'textarea.html'})

    class LocalServiceWorkSerializer(serializers.Serializer):
        service = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=ServiceList.objects.all(), required=False)
        quantity = serializers.IntegerField(allow_null=True, label='Количество оказанных услуг', max_value=2147483647, min_value=-2147483648, required=False)

    car = CarSerializer(read_only=True)
    client = LocalClientSerializer()
    date_of_work = serializers.DateField(read_only=True)
    approximate_begin_time = serializers.TimeField(read_only=True)
    service = LocalServiceWorkSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        client_data = validated_data.pop('client')
        stock_data = list(validated_data.pop('stock'))
        service_data = validated_data.get('service')
        service_list = []
        print(service_data)
        # Создание нового клиента или присвоение данной работе существующего
        if client_data:
            if Client.objects.filter(phoneNumber=(list(list(client_data.items())[3])[1])).exists():
                client = Client.objects.get(phoneNumber=list(list(client_data.items())[3])[1])

            else:
                client = Client.objects.create(**client_data)
            client.car.add(instance.car)
            instance.client = client
        # Создание новых записей об услугах и их связывание с работой
        if service_data:
            for service in service_data:
                service_id = int((list(service.items())[0][1]).pk)
                if not ServiceWork.objects.filter(work=instance.pk, service=service_id).exists():
                    ServiceWork.objects.create(**service, work_id=instance.pk)
                service_list.append(ServiceWork.objects.get(work=instance.pk, service=service_id))
            instance.service.set(service_list)
        instance.main_worker = validated_data.get('main_worker', instance.main_worker)
        instance.type_of_work = validated_data.get('type_of_work', instance.type_of_work)
        instance.date_of_work = validated_data.get('date_of_work', instance.date_of_work)
        instance.approximate_begin_time = validated_data.get('approximate_begin_time', instance.approximate_begin_time)
        instance.real_begin_time = validated_data.get('real_begin_time', instance.real_begin_time)
        instance.end_time = validated_data.get('end_time', instance.end_time)
        instance.stock.set(stock_data)
        instance.wheels.set(validated_data.get('wheels'))
        instance.extra_price = validated_data.get('extra_price', instance.extra_price)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

    class Meta:
        model = Work
        fields = ('car', 'client', 'main_worker', 'type_of_work', 'date_of_work', 'approximate_begin_time', 'real_begin_time', 'end_time', 'stock', 'wheels', 'service', 'extra_price', 'comment')

class WorkDetailGetSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only=True)
    client = ClientSerializer()
    date_of_work = serializers.DateField(read_only=True)
    approximate_begin_time = serializers.TimeField(read_only=True)
    service = ServiceWorkSerializer(many=True, read_only=True)
    wheels = LocalWheelsSerializer(many=True)

    class Meta:
        model = Work
        fields = ('car', 'client', 'main_worker', 'type_of_work', 'date_of_work', 'approximate_begin_time', 'real_begin_time', 'end_time', 'stock', 'wheels', 'service', 'extra_price', 'comment')


class ScheduleSerializer(serializers.ModelSerializer):

    worker = LocalWorkerSerializer()

    class Meta:
        model = WorkerSchedule
        fields = ('worker', 'place', 'date', 'hours', 'attendance')

class ScheduleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerSchedule
        fields = ('worker', 'place', 'date', 'hours', 'attendance')

class ClientDetailSerializer(serializers.ModelSerializer):
    car = CarSerializer(many=True)

    class Meta:
        model = Client
        fields = ('surname', 'name', 'patronymic', 'phoneNumber','finding_from', 'car')

class ClientDetailPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('phoneNumber', 'car')

class BonusFineSerializer(serializers.ModelSerializer):

    worker = LocalWorkerSerializer()
    date = serializers.DateTimeField(format='%d-%m-%Y')

    class Meta:
        model = BonusFine
        fields = ('worker', 'date', 'price', 'comment')

class BonusFineCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BonusFine
        fields = ('worker', 'price', 'comment')
