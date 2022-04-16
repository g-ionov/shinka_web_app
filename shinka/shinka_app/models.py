from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ServiceList(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название услуги')
    price = models.IntegerField(verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return '%s %s' % (self.name, self.price)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['name']

class ServiceWork(models.Model):
    quantity = models.IntegerField(verbose_name='Количество оказанных услуг', default=1)
    work = models.ForeignKey('Work', on_delete=models.CASCADE, verbose_name='Работа', related_name='service')
    service = models.ForeignKey('ServiceList', on_delete=models.CASCADE, verbose_name='Услуга', related_name='work')

    def __str__(self):
        return '%s %s, %s' % (self.work, self.service, self.quantity)

    class Meta:
        verbose_name = 'Услуги в работе'
        verbose_name_plural = 'Услуги в работе'
        ordering = ['work']

class StockType(models.Model):
    item_type = models.CharField(max_length=150, verbose_name='Тип')
    name = models.CharField(max_length=150, verbose_name='Название')
    default_price = models.IntegerField(verbose_name='Закупочная цена')
    sale_price = models.IntegerField(verbose_name='Стоимость продажи', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.item_type, self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'
        ordering = ['name']

# class StockWork(models.Model):
#     quantity = models.IntegerField(verbose_name='Количество товара для услуги', default=1, null=True, blank=True)
#     work = models.ForeignKey('Work', on_delete=models.PROTECT, verbose_name='Работа')
#     stock = models.ForeignKey('StockType', on_delete=models.PROTECT, verbose_name='Товар', null=True, blank=True)
#
#     def __str__(self):
#         return '%s %s %s' % (self.work, self.stock, self.quantity)
#
#     class Meta:
#         verbose_name = 'Товары для работы'
#         verbose_name_plural = 'Товары для работы'
#         ordering = ['work']

class Car(models.Model):
    brand = models.CharField(max_length=150, verbose_name='Марка')
    car_model = models.CharField(max_length=200, verbose_name='Модель')
    vehicle_num = models.CharField(max_length=12, verbose_name='Гос номер', unique=True)

    def __str__(self):
        return '%s %s %s' %(self.brand, self.car_model, self.vehicle_num)

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        ordering = ['brand']

class Client(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    phoneNumber = PhoneNumberField(unique=True, null=True, blank=True, verbose_name='Номер телефона')
    finding_from = models.TextField(verbose_name='Откуда нашли', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    car = models.ManyToManyField(Car)

    def __str__(self):
        return '%s %s %s' %(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
        ordering = ['surname']

class Review(models.Model):
    grade = models.FloatField(verbose_name='Оценка')
    comment = models.TextField(verbose_name='Комментарий к оценке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    work = models.ForeignKey('Work', on_delete=models.PROTECT, verbose_name='Работа')
    # client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент')

    def __str__(self):
        return '%s %s' %(self.grade, self.work)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['created_at']

class Work(models.Model):
    type_of_work = models.BooleanField(verbose_name='Прибытие на обслуживание', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания заяви')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления заявки')
    date_of_work = models.DateField(verbose_name='Дата проведения работы')
    approximate_begin_time = models.TimeField(verbose_name='Предположительное время начала работы')
    real_begin_time = models.TimeField(verbose_name='Реальное время начала работы', null=True, blank=True)
    end_time = models.TimeField(verbose_name='Время окончания работы', null=True, blank=True)
    extra_price = models.FloatField(verbose_name='Дополнительная стоимость', null=True, blank=True)
    comment = models.TextField(verbose_name='Комментарий к работе', null=True, blank=True)
    main_worker = models.ForeignKey('Worker', on_delete=models.PROTECT, verbose_name='Главный рабочий', null=True, blank=True)
    client = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name='Клиент', null=True, blank=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE, verbose_name='Машина')
    stock = models.ManyToManyField(StockType, blank=True, null=True)
    wheels = models.ManyToManyField('Wheels', verbose_name='Колеса/Шины', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' %(self.date_of_work, self.client, self.car)

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'
        ordering = ['approximate_begin_time']

# class Schedule(models.Model):
#     date_of_work = models.DateField(verbose_name='Дата работы')
#
#     def __str__(self):
#         return '%s' %(self.date_of_work)
#
#     class Meta:
#         verbose_name = 'Расписание'
#         verbose_name_plural = 'Расписание'
#         ordering = ['date_of_work']

class Worker(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    phoneNumber = PhoneNumberField(unique = True, null = False, blank = False, verbose_name='Номер телефона')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return '%s %s %s' %(self.surname, self.name, self.patronymic)

    class Meta:
        verbose_name = 'Рабочий'
        verbose_name_plural = 'Рабочие'
        ordering = ['surname']

class WorkerSchedule(models.Model):
    attendance = models.BooleanField(verbose_name='Выход на работу')
    hours = models.IntegerField(verbose_name='Количество часов')
    place = models.BooleanField(verbose_name='Главная точка шиномонтажа')
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, verbose_name='Рабочий')
    date = models.DateField(verbose_name='Дата работы')

    def __str__(self):
        return '%s %s' % (self.worker, self.schedule)

    class Meta:
        verbose_name = 'График'
        verbose_name_plural = 'График'

class Position(models.Model):
    name = models.CharField(max_length=100, verbose_name='Должность')
    price = models.IntegerField(verbose_name='Ставка (р/час)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ['name']

class PositionChange(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время смены должности')
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, verbose_name='рабочий')
    new_position = models.ForeignKey('Position', on_delete=models.PROTECT, verbose_name='Должность')

    def __str__(self):
        return '%s %s' % (self.worker, self.new_position)

    class Meta:
        verbose_name = 'Смена должности'
        verbose_name_plural = 'Смены должностей'
        ordering = ['created_at']

class BonusFine(models.Model):
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время назначения премии/штрафа')
    price = models.IntegerField(verbose_name='Стоимость', default=0)
    comment = models.TextField(verbose_name='Коммментарий к шрафу/премии', null=True)
    worker = models.ForeignKey('Worker', on_delete=models.PROTECT, verbose_name='Рабочий')

    def __str__(self):
        return '%s %s %s' %(self.worker, self.price, self.date)

    class Meta:
        verbose_name = 'Штраф/премия'
        verbose_name_plural = 'Штрафы/премии'
        ordering = ['date']

class Stock(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name='Дата операции')
    number = models.IntegerField(verbose_name='Количество')
    stock_type = models.ForeignKey('StockType', related_name='stock', on_delete=models.CASCADE, verbose_name='Товар', null=True, blank=True)
    wheels = models.ForeignKey('Wheels', on_delete=models.CASCADE, verbose_name='Шина', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.stock_type, self.date, self.number)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склад'
        ordering = ['date']

class Wheels(models.Model):
    type = models.CharField(max_length=6, verbose_name='Тип')
    brand = models.CharField(max_length=150, verbose_name='Марка')
    model_name = models.CharField(max_length=150, verbose_name='Модель')
    diameter = models.IntegerField(verbose_name='Диаметр')
    width = models.IntegerField(verbose_name='Ширина')
    profile = models.IntegerField(verbose_name='Профиль')
    run_flat = models.BooleanField(verbose_name='Run flat')
    marking_c = models.BooleanField(verbose_name='Маркировка С')
    status = models.CharField(max_length=150, verbose_name='Статус')
    winter = models.BooleanField(verbose_name='Зима')
    grade = models.FloatField(verbose_name='Оценка')
    # work = models.ManyToManyField('Work', related_name='wheels', verbose_name='Работа', null=True, blank=True)
    default_price = models.IntegerField(verbose_name='Закупочная цена')
    sale_price = models.IntegerField(verbose_name='Стоимость продажи')


    def __str__(self):
        return '%s %s %s %s' % (self.type, self.brand, self.model_name, self.grade)

    class Meta:
        verbose_name = 'Шина/Колесо'
        verbose_name_plural = 'Шины/Колеса'
        ordering = ['model_name']

