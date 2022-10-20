# class A:
#
#     def __init__(self, name):
#         self.name = name
#
#     def salut(self):
#         print(f'Hello {self.name}!')
#
#
#
# class B(A):
#
#     def change_name(self, new_name: str):
#         self.name = new_name
#
#     def salut(self):
#         #super().salut()
#         print(f'hello {self.name}!')
#
#
# def name_in_caps(instancja:A) -> str:
#     return str(instancja.name).lower()
#
#
#
#
# a = A('kadabra')
# print(a.name)
#
# b = A('abra')
# print(b.name)
# b.salut()
#
# xx = B('xin')
# xx.salut()
#
# xx.change_name('liaoning')
# xx.salut()
#
# print(name_in_caps(a))
# print(name_in_caps(b))
