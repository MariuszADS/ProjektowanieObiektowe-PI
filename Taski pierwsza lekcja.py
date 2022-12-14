# 馃嚘 Zadanie -- napisa膰 "dataclass-臋", kt贸ra b臋dzie odpowiada艂a za "samoch贸d"; 4 pola... (marka, model, data_produkcji, vin);
# 馃嚙 Napisa膰 jaki艣 sensowny walidator do (A), czyli is_valid(c: Car) -> bool
# teraz piszemy "logger z buforowaniem" a przy wywo艂aniu metody log(msg) sam msg ma zosta膰 zapisany do jakiej艣 wewn臋trznej listy; i dopiero po wywo艂aniu metody flush() ca艂o艣膰 ma by膰 drukowana na konsol臋
# 馃嚚 Napisa膰 klas臋 BufferedLogger, kt贸rej konstuktor bierze dodatkowy parametr buffer_size_lines: int, i tworzy sobie wewn臋trznie pole buffer: list[str]
# 馃嚛 Zaimplementowa膰 metod臋 log(msg:str), kt贸ra zapisuje msg do wewn臋trznego pola buffer (zwykle, przez append); odpowiednio sformatowa膰 zapisywan膮 lini臋, tak by mia艂a posta膰 f'timestamp] {msg}'
# 馃嚜 Zaimplementowa膰 metod臋 flush(), kt贸ra wydrukuje po kolei (od najstarszych do najnowszych) wszystkie linie z wewn臋trznego bufora, po czym opr贸偶ni ten bufor; sprawdzi膰 dzia艂anie BufferedLogger
# 'a przy logowaniu (w p臋tli) tysi膮ca losowych liczb... (sprawdzi膰, 偶e buforowany Logger nie b臋dzie traci艂 czasu na ka偶dej z linii tak jak zwyk艂a metoda print)

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
    # twrzymy "instancj臋" klasy
    a = A(10, 'abc')
    b = A(11, 'xxx')    #druga, niezale偶na instancja
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
            print('konstruktor dzia艂a')
            self.log_id = log_id

        def log_it(self, msg: str):
            # to jest "metoda (method)"
            print(f'Logger[{self.log_id}]: {msg}')


    if __name__ == '__main__':
        ll = Logger(log_id=17)
        ll.log_it('Komunikat')
        l7 = Logger(7)
        l7.log_it('Komunikat')
