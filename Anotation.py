from typing import Optional, Callable

def add(number: Optional[float], callback: Callable[[float, None], float]) -> float:
    """Производит арифметические действия с числами.
    Принимает число и функцию, выполняющую арифметическое действие."""
  
    return callback(number)


def adder20(number: Optional[float]) -> float:
    """Добавляет к аргументу 20."""
    return number + 20


def multiplier2(number: Optional[float]) -> float:
    """Умножает аргумент на 2."""
    return number * 2
