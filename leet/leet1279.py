class TrafficLight:
    def __init__(self):
        self.roadA = 1

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        if self.roadA != roadId:
            turnGreen()
            self.roadA = roadId

        crossCar()

# Better solution

import threading


class TrafficLightBetter:
    def __init__(self):
        self.roadA = 1
        self.light_mutex = threading.Lock()

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        with threading.Lock():
            if roadId == self.roadA:
                crossCar()
            else:
                self.roadA = roadId
                turnGreen()
                crossCar()


import threading


class TrafficLightSemaphore:
    def __init__(self):
        self.ls = threading.Semaphore(1)
        self.id = 1

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        self.ls.acquire()
        if self.id != roadId:
            turnGreen()
            self.id = roadId

        crossCar()
        self.ls.release()

# O(1) solution but much clearer on methods

import threading

class TrafficLight:
    def __init__(self):
        self.lightA = 1
        self.lightB = 0
        self.lightLock = threading.Semaphore(1)

    def carArrived(
            self,
            carId: int,  # ID of the car
            roadId: int,  # ID of the road the car travels on. Can be 1 (road A) or 2 (road B)
            direction: int,  # Direction of the car
            turnGreen: 'Callable[[], None]',  # Use turnGreen() to turn light to green on current road
            crossCar: 'Callable[[], None]'  # Use crossCar() to make car cross the intersection
    ) -> None:
        if roadId == 1:
            self.crossA(crossCar, turnGreen)
        if roadId == 2:
            self.crossB(crossCar, turnGreen)

    def crossA(self, crossCar: 'Callable[[], None]', turnGreen: 'Callable[[], None]'):
        self.lightLock.acquire()
        if self.lightA == 1:
            crossCar()
        elif self.lightA == 0:
            turnGreen()
            self.lightA = 1
            self.lightB = 0
            crossCar()
        self.lightLock.release()

    def crossB(self, crossCar: 'Callable[[], None]', turnGreen: 'Callable[[], None]'):
        self.lightLock.acquire()
        if self.lightB == 1:
            crossCar()
        elif self.lightB == 0:
            turnGreen()
            self.lightB = 1
            self.lightA = 0
            crossCar()
        self.lightLock.release()

