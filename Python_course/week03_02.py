import csv
import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count, body_whl='', extra=''):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = "car"


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl, passenger_seats_count = '', extra=''):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        if body_whl:
            self.body_length = float(body_whl.split('x')[0])
            self.body_width = float(body_whl.split('x')[1])
            self.body_height = float(body_whl.split('x')[2])
        else:
            self.body_length = 0
            self.body_width = 0
            self.body_height = 0
        self.car_type = "truck"

    def get_body_volume(self):
        return self.body_length*self.body_width*self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra, passenger_seats_count = '', body_whl=''):
        super().__init__(brand=brand, photo_file_name=photo_file_name, carrying=carrying)
        self.extra = extra
        self.car_type = "spec_machine"


cars_choices = {
    'car': Car,
    'truck': Truck,
    'spec_machine': SpecMachine
}


def caller(params):
    try:
        if params[0] not in cars_choices:
            raise ValueError
    except IndexError:
        raise ValueError
    else:
        try:
            return cars_choices[params[0]](brand=params[1], passenger_seats_count=params[2], photo_file_name=params[3],
                                           body_whl=params[4], carrying=params[5], extra=params[6])
        except IndexError:
            raise ValueError


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                car_list.append(caller(row))
            except ValueError:
                continue
    return car_list


if __name__ == "__main__":
    print(get_car_list('coursera_week3_cars.csv'))
