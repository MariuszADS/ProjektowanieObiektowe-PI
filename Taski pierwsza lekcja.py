# 🇦 Zadanie -- napisać "dataclass-ę", która będzie odpowiadała za "samochód"; 4 pola... (marka, model, data_produkcji, vin);
# 🇧 Napisać jakiś sensowny walidator do (A), czyli is_valid(c: Car) -> bool
# teraz piszemy "logger z buforowaniem" a przy wywołaniu metody log(msg) sam msg ma zostać zapisany do jakiejś wewnętrznej listy; i dopiero po wywołaniu metody flush() całość ma być drukowana na konsolę
# 🇨 Napisać klasę BufferedLogger, której konstuktor bierze dodatkowy parametr buffer_size_lines: int, i tworzy sobie wewnętrznie pole buffer: list[str]
# 🇩 Zaimplementować metodę log(msg:str), która zapisuje msg do wewnętrznego pola buffer (zwykle, przez append); odpowiednio sformatować zapisywaną linię, tak by miała postać f'timestamp] {msg}'
# 🇪 Zaimplementować metodę flush(), która wydrukuje po kolei (od najstarszych do najnowszych) wszystkie linie z wewnętrznego bufora, po czym opróżni ten bufor; sprawdzić działanie BufferedLogger
# 'a przy logowaniu (w pętli) tysiąca losowych liczb... (sprawdzić, że buforowany Logger nie będzie tracił czasu na każdej z linii tak jak zwykła metoda print)

from dataclasses import dataclass


@dataclass
class A:
    uid: int
    name: str


def is_valid(instance: A) -> bool:
    """
    Checks if the `instance` is fulfilling the requirements
    :param instance:
    :return: True if `instance` is OK
    """
    if (instance.uid == None or instance.uid < 0 or len(instance.name)==0):
        return False
    if (instance.name[0].isdigit()):
        return False
    return True


if __name__ == '__main__':
    # twrzymy "instancję" klasy
    a = A(10, 'abc')
    b = A(11, 'xxx')    #druga, niezależna instancja
    print(id(a))
    print(id(b))
    print(a)
    print(b)
    print(a.uid)
    print(f'instancja "a" jest valid? {is_valid(a)}')



# ========================================================



    class Logger:
        log_id: int  # pole / field

        def __init__(self, log_id: int):
            print('konstruktor działa')
            self.log_id = log_id

        def log_it(self, msg: str):
            # to jest "metoda (method)"
            print(f'Logger[{self.log_id}]: {msg}')


    if __name__ == '__main__':
        ll = Logger(log_id=17)
        ll.log_it('Komunikat')
        l7 = Logger(7)
        l7.log_it('Komunikat')
