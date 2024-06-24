katz_deli = []

def line(queue):
    if len(queue) == 0:
        print('The line is currently empty.')
    else:
        counter = 1
        lst = []
        for person in queue:
            lst.append(f'{counter}. {person}')
            counter += 1
        print('The line is currently: ' + ' '.join(lst))

def take_a_number(katz_deli, new_person):
    print(f'Welcome, {new_person}. You are number {len(katz_deli) + 1} in line.')
    katz_deli.append(new_person)

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print('There is nobody waiting to be served!')
    else:
        print('Currently serving ' + katz_deli[0] + '.')
        del katz_deli[0]