import csv
from datetime import date
from django.template.defaultfilters import slugify
import decimal

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                # TODO: Добавьте сохранение модели
                id = int(line[0])
                name = line[1]
                image = line[2]
                str_price = line[3]
                price = decimal.Decimal(str_price)
                r_date = line[4].split('-')
                release_date = date(int(r_date[0]), int(r_date[1]), int(r_date[2]))
                lte_exists = bool(line[5])
                slug = slugify(name)
                phone = Phone(id=id, name=name, price=price, image=image, release_date=release_date,
                              lte_exists=lte_exists, slug=slug)
                phone.save()
