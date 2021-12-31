from pokedex import dex

def main():
    print('Welcome to your Pokedex')
    print('=======================')

    while(True):
        var = input('\nWhich pokemon do you need info on? ')
        if var == '0':
            break
        dex(var.lower())
    
    print('\nThank You for using the Pokedex!\nGoodbye!')
    print('=======================\n')

if __name__ ==  "__main__":
    main()