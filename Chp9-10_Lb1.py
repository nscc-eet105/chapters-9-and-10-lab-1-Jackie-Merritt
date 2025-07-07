#Jackie-Merritt_Chp9-10-Lab1_7/6/2025

def main():
    print("Name Processor\n")
    name = inputing_name()
    proper = name.title()

    comma_index = name.find(',')

    if comma_index == -1:
        reverse(proper)
    else:
        keep(proper)

def inputing_name():
    while True:
        name = input('Enter your name: ')
        if ' ' in name:
            return name
        else:
            print('Please input first and last name.')


def reverse(proper):
    name_index = proper.split()
    print(f'{name_index[-1]}, {name_index[0]}')
    
    

def keep(proper):
    name_index = proper.split()
    print(f'{name_index[0]} {name_index[-1]}')

if __name__ == '__main__':
    main()
