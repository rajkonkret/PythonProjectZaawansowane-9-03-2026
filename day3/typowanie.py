# użycie TypeDict

from typing import TypedDict, get_origin


class User(TypedDict):
    name: str
    age: int
    email: str


def print_user_info(user: User) -> None:
    print(f"Name: {user['name']}, Age: {user['age']}, e-mail: {user['email']}")


user_data = {'name': "Leon", 'age': 40, 'email': 'leonion@abc.pl'}
print_user_info(user_data)
# Name: Leon, Age: 40, e-mail: leonion@abc.pl

# zlożone aliasy typów
from typing import List, Tuple, Union

Coordinate = Tuple[float, float]
Path = List[Coordinate]
CoordinateError = Union[Coordinate, int]

def validate_coordinate(coord: CoordinateError) -> bool:
    if isinstance(coord, str):
        print(f"Error: {coord}")
        return False
    return True



example_path = [(0.0, 1.0), (2.5, 3.5), (4.0, -1.2), ("True", True)]
print(validate_coordinate(example_path[-1]))
print(validate_coordinate("invalidate coordinate"))

g = get_origin(Coordinate)
print(g)  # <class 'tuple'>


def validate_coordinate(coord: Coordinate) -> bool:
    if isinstance(coord, get_origin(Coordinate)):
        print(f"Error: {coord}")
        return False
    return True


example_path = [(0.0, 1.0), (2.5, 3.5), (4.0, -1.2), ("True", True)]
print(validate_coordinate(example_path[-1]))

# Protocol
from typing import Protocol


class Runner(Protocol):
    def run(self) -> str:
        ...

    def finish_time(self) -> float:
        ...


class Athlete:
    def run(self) -> str:
        return "Athlete is running"

    def finish_time(self):
        return 1.15


class Robot:
    def run(self) -> str:
        return "robot is running"

    def finish_time(self) -> float:
        return 1.12


def start_race(participiant: Runner) -> None:
    print(participiant.run())
    print(participiant.finish_time())


athlete = Athlete()
robot = Robot()
start_race(athlete)
start_race(robot)
# Athlete is running
# 1.15
# robot is running
# 1.12

# generic
from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()


stack = Stack[int]()
stack.push(10)
stack.push(12)
stack.push(8.8)
stack.push("abcz")
print(stack.pop())


# nowsze podejście
class Stack[V]:
    def __init__(self) -> None:
        self._container: list[V] = []

    def push(self, item: V) -> None:
        self._container.append(item)

    def pop(self) -> V:
        return self._container.pop()

stack = Stack[int]()
stack.push(10)
stack.push(12)
stack.push(8.8)
stack.push("abcz")
print(stack.pop())
from typing import Literal


def set_status(status: Literal['active', 'inactive', 'pending']) -> str:
    return f"Status to: {status}"


print(set_status('active'))  # Status to: active
print(set_status('destroy'))  # Status to: destroy
