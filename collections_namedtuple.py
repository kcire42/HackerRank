from collections import namedtuple



def collections_namedtuple(trys:int):
    fields = input().split()
    total = 0
    for intent in range(trys):
        students = namedtuple('student',fields)
        field1,field2,field3,field4 = input().split()
        student = students(field1,field2,field3,field4)
        total += int(student.MARKS)
    print(total/trys)

        





if __name__ == "__main__":
    trys = int(input())
    collections_namedtuple(trys)