from typing import List


class Car:
    """
    Базовый класс, описывающий автомобиль.
    """

    def __init__(self, brand: str, model: str, max_speed: int) -> None:
        """
        Конструктор базового класса.

        Args:
            brand (str): марка автомобиля
            model (str): модель автомобиля
            max_speed (int): максимальная скорость
        """
        self.brand: str = brand
        self.model: str = model
        self.max_speed: int = max_speed

        # защищённый атрибут
        # хранит список пройденных расстояний
        # инкапсуляция нужна, чтобы ограничить прямое изменение извне
        self._trip_history: List[int] = []

        # приватный атрибут — используется только внутри класса
        self.__vehicle_id: int = id(self)

    def add_trip(self, distance: int) -> None:
        """
        Добавить поездку в историю автомобиля.

        Args:
            distance (int): расстояние поездки в километрах
        """
        self._trip_history.append(distance)

    def calculate_range(self) -> int:
        """
        Рассчитать примерный запас хода автомобиля.

        Returns:
            int: запас хода в километрах
        """
        return 500

    def __str__(self) -> str:
        """
        Человекочитаемое представление автомобиля.
        """
        return f"{self.brand} {self.model}, max speed: {self.max_speed} km/h"

    def __repr__(self) -> str:
        """
        Официальное представление объекта.
        """
        return (
            f"Car(brand={self.brand!r}, model={self.model!r}, "
            f"max_speed={self.max_speed!r})"
        )


class Truck(Car):
    """
    Дочерний класс, представляющий грузовой автомобиль.
    """

    def __init__(
        self,
        brand: str,
        model: str,
        max_speed: int,
        cargo_capacity: int
    ) -> None:
        """
        Конструктор класса Truck.

        Args:
            brand (str): марка автомобиля
            model (str): модель автомобиля
            max_speed (int): максимальная скорость
            cargo_capacity (int): грузоподъёмность (кг)
        """
        super().__init__(brand, model, max_speed)
        self.cargo_capacity: int = cargo_capacity

    def calculate_range(self) -> int:
        """
        Переопределённый метод расчёта запаса хода.

        Причина перегрузки:
        грузовые автомобили расходуют больше топлива
        из-за большого веса и перевозимого груза.

        Returns:
            int: запас хода грузовика
        """
        return 350

    def load_cargo(self, weight: int) -> str:
        """
        Загрузить груз в автомобиль.

        Args:
            weight (int): вес груза

        Returns:
            str: результат загрузки
        """
        if weight > self.cargo_capacity:
            return "Cargo exceeds truck capacity."
        return f"Loaded {weight} kg of cargo."

    def __str__(self) -> str:
        return (
            f"Truck {self.brand} {self.model}, "
            f"capacity: {self.cargo_capacity} kg"
        )

    def __repr__(self) -> str:
        return (
            f"Truck(brand={self.brand!r}, model={self.model!r}, "
            f"max_speed={self.max_speed!r}, cargo_capacity={self.cargo_capacity!r})"
        )


class ElectricCar(Car):
    """
    Дочерний класс, представляющий электрический автомобиль.
    """

    def __init__(
        self,
        brand: str,
        model: str,
        max_speed: int,
        battery_capacity: int
    ) -> None:
        """
        Конструктор класса ElectricCar.

        Args:
            brand (str): марка автомобиля
            model (str): модель автомобиля
            max_speed (int): максимальная скорость
            battery_capacity (int): ёмкость батареи (кВт·ч)
        """
        super().__init__(brand, model, max_speed)
        self.battery_capacity: int = battery_capacity

    def calculate_range(self) -> int:
        """
        Переопределённый метод расчёта запаса хода.

        Причина перегрузки:
        для электромобилей запас хода зависит от
        ёмкости батареи, а не от топлива.

        Returns:
            int: запас хода электромобиля
        """
        return self.battery_capacity * 6

    def charge(self) -> str:
        """
        Зарядить батарею автомобиля.

        Returns:
            str: сообщение о зарядке
        """
        return "Battery is charging."

    def __str__(self) -> str:
        return (
            f"Electric car {self.brand} {self.model}, "
            f"battery: {self.battery_capacity} kWh"
        )

    def __repr__(self) -> str:
        return (
            f"ElectricCar(brand={self.brand!r}, model={self.model!r}, "
            f"max_speed={self.max_speed!r}, battery_capacity={self.battery_capacity!r})"
        )


if __name__ == "__main__":
    # Write your solution here

    truck = Truck("Volvo", "FH16", 120, 20000)
    electric = ElectricCar("Tesla", "Model 3", 225, 75)

    truck.add_trip(200)
    electric.add_trip(150)

    print(truck)
    print(repr(truck))
    print("Truck range:", truck.calculate_range())
    print(truck.load_cargo(15000))

    print()

    print(electric)
    print(repr(electric))
    print("Electric car range:", electric.calculate_range())
    print(electric.charge())