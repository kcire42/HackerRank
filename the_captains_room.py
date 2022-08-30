from collections import Counter



def the_captains_room(group_size:int, crew:list)->int:
    counter_rooms = Counter(crew)
    #print(counter_rooms)
    print(min(counter_rooms,key = counter_rooms.get))


if __name__ == '__main__':
    group_size = int(input())
    crew = list(map(int,input().split()))
    capitan = the_captains_room(group_size,crew)

