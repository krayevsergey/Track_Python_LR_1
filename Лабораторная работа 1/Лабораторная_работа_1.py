import doctest
from typing import Optional, List


class Smartphone:
    """
    Класс, представляющий смартфон.
    """

    def __init__(self, brand: str, model: str, battery_capacity_mah: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Бренд смартфона
        :param model: Модель смартфона
        :param battery_capacity_mah: Емкость батареи в мАч

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 3349)
        >>> phone.brand
        'Apple'
        >>> phone.model
        'iPhone 15'
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if len(brand.strip()) == 0:
            raise ValueError("Бренд не может быть пустой строкой")
        self.brand = brand.strip()

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if len(model.strip()) == 0:
            raise ValueError("Модель не может быть пустой строкой")
        self.model = model.strip()

        if not isinstance(battery_capacity_mah, int):
            raise TypeError("Емкость батареи должна быть целым числом")
        if battery_capacity_mah <= 0:
            raise ValueError("Емкость батареи должна быть положительным числом")
        self.battery_capacity_mah = battery_capacity_mah

        self._current_battery_level = 100  # в процентах
        self._is_powered_on = False

    def power_on(self) -> None:
        """
        Включение смартфона.

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S23", 3900)
        >>> phone.power_on()
        """
        if self._current_battery_level <= 0:
            raise ValueError("Недостаточно заряда для включения")
        self._is_powered_on = True

    def power_off(self) -> None:
        """
        Выключение смартфона.

        Примеры:
        >>> phone = Smartphone("Xiaomi", "Redmi Note 12", 5000)
        >>> phone.power_on()
        >>> phone.power_off()
        """
        self._is_powered_on = False

    def charge(self, minutes: int) -> int:
        """
        Зарядка смартфона.

        :param minutes: Количество минут зарядки
        :return: Текущий уровень заряда в процентах после зарядки

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 8", 4575)
        >>> phone._current_battery_level = 50  # Устанавливаем уровень заряда для теста
        >>> phone.charge(30)
        80
        """
        if not isinstance(minutes, int):
            raise TypeError("Время зарядки должно быть целым числом")
        if minutes <= 0:
            raise ValueError("Время зарядки должно быть положительным числом")

        # Заглушка для реализации
        ...
        # Предположим, что 1 минута заряжает на 1%
        charge_per_minute = 1
        new_level = self._current_battery_level + (minutes * charge_per_minute)
        self._current_battery_level = min(100, new_level)
        return self._current_battery_level


class Book:
    """
    Класс, представляющий книгу.
    """

    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param page_count: Количество страниц

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.title
        'Мастер и Маргарита'
        >>> book.author
        'Михаил Булгаков'
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if len(title.strip()) == 0:
            raise ValueError("Название книги не может быть пустой строкой")
        self.title = title.strip()

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        if len(author.strip()) == 0:
            raise ValueError("Автор книги не может быть пустой строкой")
        self.author = author.strip()

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_count = page_count

        self._current_page = 1
        self._is_opened = False

    def open_book(self) -> None:
        """
        Открытие книги.

        Примеры:
        >>> book = Book("Преступление и наказание", "Фёдор Достоевский", 672)
        >>> book.open_book()
        """
        self._is_opened = True

    def close_book(self) -> None:
        """
        Закрытие книги.

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        >>> book.open_book()
        >>> book.close_book()
        """
        self._is_opened = False

    def turn_page(self, pages: int = 1) -> int:
        """
        Перелистывание страниц книги.

        :param pages: Количество страниц для перелистывания (по умолчанию 1)
        :return: Номер текущей страницы после перелистывания

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.open_book()
        >>> book.turn_page(5)
        6
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")

        # Заглушка для реализации
        ...
        self._current_page = min(self._current_page + pages, self.page_count)
        return self._current_page


class BankAccount:
    """
    Класс, представляющий банковский счет.
    """

    def __init__(self, account_number: str, owner_name: str, initial_balance: float = 0.0):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер счета
        :param owner_name: Имя владельца счета
        :param initial_balance: Начальный баланс (по умолчанию 0.0)

        Примеры:
        >>> account = BankAccount("40817810099910004312", "Иванов Иван Иванович", 1000.0)
        >>> account.account_number
        '40817810099910004312'
        >>> account.owner_name
        'Иванов Иван Иванович'
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if len(account_number.strip()) < 10:
            raise ValueError("Номер счета должен содержать не менее 10 символов")
        self.account_number = account_number.strip()

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(owner_name.strip()) == 0:
            raise ValueError("Имя владельца не может быть пустой строкой")
        self.owner_name = owner_name.strip()

        if not isinstance(initial_balance, (int, float)):
            raise TypeError("Начальный баланс должен быть числом")
        if initial_balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")
        self._balance = float(initial_balance)
        self._transaction_history = []

    def deposit(self, amount: float) -> float:
        """
        Внесение денег на счет.

        :param amount: Сумма для внесения
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004313", "Петров Петр Петрович", 500.0)
        >>> account.deposit(1000.0)
        1500.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")

        # Заглушка для реализации
        ...
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004314", "Сидоров Сидор Сидорович", 2000.0)
        >>> account.withdraw(500.0)
        1500.0
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма должна быть положительным числом")

        # Заглушка для реализации
        ...
        self._balance -= amount  # ИСПРАВЛЕНО: вычитаем сумму
        return self._balance

    def get_balance(self) -> float:
        """
        Получение текущего баланса счета.

        :return: Текущий баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910004315", "Смирнов Алексей", 750.0)
        >>> account.get_balance()
        750.0
        """
        return self._balance


if __name__ == "__main__":
    # Запуск doctest для проверки примеров в документации
    doctest.testmod(verbose=True)

    # Демонстрация работы классов
    print("\n" + "=" * 50)
    print("Демонстрация работы классов:\n")

    # 1. Смартфон
    print("1. Класс Smartphone:")
    phone = Smartphone("Apple", "iPhone 15 Pro", 3274)
    print(f"   Создан: {phone.brand} {phone.model}")
    print(f"   Емкость батареи: {phone.battery_capacity_mah} мАч")

    # 2. Книга
    print("\n2. Класс Book:")
    book = Book("Гарри Поттер и философский камень", "Джоан Роулинг", 432)
    print(f"   Создана: '{book.title}'")
    print(f"   Автор: {book.author}")
    print(f"   Страниц: {book.page_count}")

    # 3. Банковский счет
    print("\n3. Класс BankAccount:")
    account = BankAccount("40817810099910001234", "Кузнецов Дмитрий", 15000.0)
    print(f"   Счет: {account.account_number}")
    print(f"   Владелец: {account.owner_name}")
    print(f"   Баланс: {account.get_balance()} руб.")

    print("\n" + "=" * 50)
    print("Все классы созданы успешно!")