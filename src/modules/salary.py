class Salary:
    """Класс для абстракции 'Заработная плата'"""
    __from: int
    __to: int
    __currency: str
    __slots__ = ('__from', '__to', '__currency')

    def __init__(self, salary: tuple):
        self.__from = salary[0] if salary and salary[0] else 0
        self.__to = salary[1] if salary and salary[1] else 0
        self.__currency = salary[2] if salary and salary[2] else 'RUR'

    def get_from(self) -> int:
        return self.__from

    def get_to(self) -> int:
        return self.__to

    @property
    def currency(self) -> str:
        return self.__currency

    @property
    def salary(self) -> tuple[int, int, str | None]:
        return self.__from, self.__to, self.__currency
