class Persona:
    def __init__(self, edad, nacionalidad, civil):
        self.edad = edad
        self.nacinalidad = nacionalidad
        self.civil = civil
    
pedro_sanchez = Persona(45, "Español", "Soltero")
print(pedro_sanchez.edad)
persona = Persona(0,"","")
persona.edad = int(input("Cual es la edad del usuario"))
persona.nacinalidad = input("Cual es la Nacinalidad del usuario")
persona.civil = input("Cual es la Estado Civil del usuario")

print(f'''
Los datos del usuario son: 
      
      Tiene {persona.edad} años 
      De nacinalidad {persona.nacinalidad} 
      Y estado civil {persona.civil}
''')
