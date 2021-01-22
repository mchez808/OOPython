from dataclasses import dataclass


# "The "frozen" parameter makes the class immutable
@dataclass(frozen=True)  
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval


if __name__ == "__main__":
    obj = ImmutableClass()
    print(obj.value1)

    # attempting to change the value of an immutable class throws an exception
    # obj.value1 = "NEW value"

    # even functions within the class can't change anything
    # obj.somefunc(20)      # throws an exception
