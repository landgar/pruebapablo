# clase
import math as m


class Persona():
    # atributos
    nombre = "Carlos"
    apellido = "Vergara"
    sexo = "Masculino"
    edad = 30
    pasosAcumulados=0

    # metodos
    def hablar(self, mensaje):
        return mensaje

    def darunpaso(self):
        """
        Suma un paso a los pasos acumulados
        :return: no devuelve nada
        """
        self.pasosAcumulados += m.pi

###########################


# objeto
persona = Persona()

persona.darunpaso()
persona.darunpaso()
persona.darunpaso()
persona.darunpaso()
persona.darunpaso()

print(persona.pasosAcumulados)

