
import time

list_of_names:list = [
    'Yana Lily',
    'Savio Dada',
    'Jane Mama',
]


def main():
    for name in list_of_names:
        for i in range(len(name)+1):
            print( f'{name[:i]}')
            time.sleep( 1 )

if __name__ == '__main__':
    main()
    
