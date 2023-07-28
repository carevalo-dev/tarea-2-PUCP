class alumnos:
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombreAlumno = nombre
        self.apellidoAlumno = apellido
        self.edadAlumno = edad
        self.notaAlumno = ''
        self.nacionalidadAlumno = nacionalidad

    def leerNota(self, nota):
        print("La nota del alumno es: ", nota)

    def registrarNota(self, nota):
        self.notaAlumno = nota


if __name__ == '__main__':

    notasAlumnos = []
    comandoSistema = ["R", "C", "P", "S", "X"]
    print("Bienvenido al registro de notas de alumnos")
    while True:
        comandoUsuario = input("Ingrese el comando: ")
        if comandoUsuario in comandoSistema:
            if comandoUsuario == "R":
                print("Registrar alumno")
                nombre = input("Ingrese el nombre del alumno: ")
                apellido = input("Ingrese el apellido del alumno: ")
                edad = input("Ingrese la edad del alumno: ")
                nacionalidad = input("Ingrese la nacionalidad del alumno: ")
                objAlumno = alumnos(nombre, apellido, edad, nacionalidad)
                notasAlumnos.append(objAlumno)
                print("Alumno registrado correctamente")
            elif comandoUsuario == "C":
                print("Calificar alumno")
                for alumno in notasAlumnos:
                    if alumno.notaAlumno == '':
                        nota = input(f"Alumno {alumno.nombreAlumno} {alumno.apellidoAlumno} ingrese la nota: ")
                        while True:
                            if nota.isnumeric() and int(nota) >= 0 and int(nota) <= 20:
                                alumno.registrarNota(nota)
                                break
                            else:
                                print("Nota no valida")
                                nota = input(f"Alumno {alumno.nombreAlumno} {alumno.apellidoAlumno} ingrese la nota: ")
            elif comandoUsuario == "P":
                print("Promedio de notas de alumnos")
                sumaNotas = 0
                cantidadAlumnos = len(notasAlumnos)
                for alumno in notasAlumnos:
                    sumaNotas = sumaNotas + int(alumno.notaAlumno)
                    promedio = sumaNotas / cantidadAlumnos
                print(f"El promedio de notas para {cantidadAlumnos} es: {promedio}")
            elif comandoUsuario == "S":
                print("Suma de Notas de alumnos")
                sumaNotas = 0
                cantidadAlumnos = len(notasAlumnos)
                for alumno in notasAlumnos:
                    sumaNotas = sumaNotas + int(alumno.notaAlumno)
                print(f"La suma de notas para {cantidadAlumnos} es: {sumaNotas}")
            elif comandoUsuario == "X":
                print("Salir del programa")
                break
        else:
            print("Comando no valido")
