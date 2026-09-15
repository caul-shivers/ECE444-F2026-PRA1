class Utils:

    def reversed(self, number: int) -> int:
        return int(str(number)[::-1])

    def formatter(self, number: int) -> tuple[str, str]:
        return bin(number), oct(number)