bd = {}

class Menu:
    def main(self,BD):
        print('Menu\n------')
        self.preguntar()
    
    def preguntar(self):
        while True:
            try:
                print('1- Registrarse\n2- Leer Base de datos\n3- Loguearse\n4- Salir')
                opcion = int(input("Elija una opcion: "))
                if opcion == 1:
                    self.registro(bd)
                elif opcion == 2:
                    self.leer(bd)
                elif opcion == 3:
                    self.login(bd)
                elif opcion == 4:
                    print("Hasta Pronto!!")
                    exit()
            except ValueError:
                print("Ingrese caracter valido")

    def registro(self,BD):
        usuario = input('Ingrese un nombre de usuario: ')
        while usuario in BD:
            print('El usuario ya existe.')
            usuario = input('Ingrese un nuevo usuario: ')
        else:
            password = input('Ingrese una contraseña: ')
        BD[usuario] = password
        print('Usuario registrado')

    def leer(self,BD):
        for usuario, password in BD.items():
            print(f'Usuario: {usuario}  Contraseña: {password}')

    def login(self,BD):
        for i in range(3):
            user = input('Ingrese su usuario: ')
            password = input('Ingrese la contraseña: ')
            if user in BD and password == BD[user]:
                print('Te has logueado correctamente')
                exit()
            else:
                print('Usuario o contraseña incorrectos')
        else:
            print('Ha agotado sus intentos')

if __name__ == '__main__':
    menu = Menu()
    menu.main(bd)