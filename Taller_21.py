"""
Metodos de los diccionarios:

- get()
  Busca un elemento a partir de su clave y si no lo encuentra devuelve un valor por defecto

- keys()
  Genera una lista en clave de los registros del diccionario:

- values()
  Genera una lista en valor de los registros del diccionario:

- items()
  Genera una lista en clave-valor de los registros del diccionario:


Eliminar datos:

- pop()
  Extrae un registro de un diccionario a partir de su clave y lo borra, acepta valor por defecto:

- También se puede eliminar así: del diccionario['Llave a eliminar']

- clear()
  Borra todos los registros de un diccionario:

- popitem()
  Elimina el últmo elemento de un diccionario

Insertar datos:

- setdefault():
  Sila llave está en el diccionario, devuelve el valor, si no crea el elemento del diccionario

 - Tambián se puede agregar así: diccionario['Llave_nueva'] = nuevo valor


"""

peet_list = [
  {
    'tipe': 'Gato',
    'name': 'Pelusa',
    'race': 'Persa',
    'sex': 'Hembra',
    'weight': 6,
    'age': 12,
    'height': 52
  },
  {
    'tipe': 'Perro',
    'name': 'Bruno',
    'race': 'Golden Retriever',
    'sex': 'Macho',
    'weight': 42,
    'age': 3,
    'height': 110
  },
  {
    'tipe': 'Perro',
    'name': 'Kyara',
    'race': 'Golden Retriever',
    'sex': 'Hembra',
    'weight': 46,
    'age': 10,
    'height': 84
  },
  {
    'tipe': 'Conejo',
    'name': 'Nieve',
    'race': 'Belier Holandes',
    'sex': 'Macho',
    'weight': 7,
    'age': 6,
    'height': 37
  },
  {
    'tipe': 'Perro',
    'name': 'Mila',
    'race': 'Pastor Collie',
    'sex': 'Hembra',
    'weight': 32,
    'age': 12,
    'height': 69
  },
  {
    'tipe': 'Gato',
    'name': 'Atena',
    'race': 'Siames',
    'sex': 'Hembra',
    'weight': 5,
    'age': 3,
    'height': 34
  }
]

football_teams = {
  'Real Madrid':{
    'Director':{
      'name': 'Carlo Ancelotti',
      'country': 'Italia',
      'age': 62,
      'height': 179
    },
    'players':{
      'Thibaut Courtois':{
        'position': 'Portero',
        'country': 'Belgica',
        'age': 30,
        'height': 200
      },
      'Andriy Lunin':{
        'position': 'Portero',
        'country': 'Ucrania',
        'age': 25,
        'height': 193
      },
      'Daniel Carvajal':{
        'position': 'Defensa',
        'country': 'España',
        'age': 30,
        'height': 173
      },
      'Eder Militao':{
        'position': 'Defensa',
        'country': 'Brasil',
        'age': 24,
        'height': 186
      },
      'David Alaba':{
        'position': 'Defensa',
        'country': 'Austria',
        'age': 29,
        'height': 180
      },
      'Jesus Vallejo':{
        'position': 'Defensa',
        'country': 'España',
        'age': 25,
        'height': 184
      },
      'Nacho fernandez':{
        'position': 'Defensa',
        'country': 'España',
        'age': 32,
        'height': 180
      },
      'Marcelo Vieira':{
        'position': 'Defensa',
        'country': 'Brasil',
        'age': 33,
        'height': 174
      },
      'Ferland Mendy':{
        'position': 'Defensa',
        'country': 'Francia',
        'age': 26,
        'height': 178
      },
      'Toni Kroos':{
        'position': 'Mediocampista',
        'country': 'Alemania',
        'age': 32,
        'height': 183
      },
      'Luka Modric':{
        'position': 'Mediocampista',
        'country': 'Croacia',
        'age': 36,
        'height': 172
      },
      'Carlos Casemiro':{
        'position': 'Mediocampista',
        'country': 'Brasil',
        'age': 29,
        'height': 185
      },
      'Federico Valverde':{
        'position': 'Mediocampista',
        'country': 'Uruguay',
        'age': 23,
        'height': 182
      },
      'Lucas Vazquez':{
        'position': 'Mediocampista',
        'country': 'España',
        'age': 30,
        'height': 173
      },
      'Daniel Ceballos':{
        'position': 'Mediocampista',
        'country': 'España',
        'age': 25,
        'height': 179
      },
      'Isco Suarez':{
        'position': 'Mediocampista',
        'country': 'España',
        'age': 29,
        'height': 176
      },
      'Eduardo Camavinga':{
        'position': 'Mediocampista',
        'country': 'Francia',
        'age': 19,
        'height': 182
      },
      'Eden Hazard':{
        'position': 'Delantero',
        'country': 'Alemania',
        'age': 31,
        'height': 175
      },
      'Karim Benzema':{
        'position': 'Delantero',
        'country': 'Francia',
        'age': 34,
        'height': 185
      },
      'Marco Asensio':{
        'position': 'Delantero',
        'country': 'España',
        'age': 26,
        'height': 180
      },
      'Luka Jovic':{
        'position': 'Delantero',
        'country': 'Serbia',
        'age': 24,
        'height': 182
      },
      'Gareth Bale':{
        'position': 'Delantero',
        'country': 'Gales',
        'age': 32,
        'height': 185
      },
      'Vinicius Jr':{
        'position': 'Delantero',
        'country': 'Brasil',
        'age': 21,
        'height': 176
      },
      'Rodrygo Goes':{
        'position': 'Delantero',
        'country': 'Brasil',
        'age': 21,
        'height': 174
      },
      'Mariano Diaz':{
        'position': 'Delantero',
        'country': 'España',
        'age': 28,
        'height': 180
      }
    }
  },
  'Manchester City':{
    'Drector':{
      'name': 'Josep Guardiola',
      'country': 'España',
      'age': 51,
      'height': 180
    },
    'players':{
      'Ederson':{
        'position': 'Portero',
        'country': 'Brasil',
        'age': 28,
        'height': 188
      },
      'Zack Steffen':{
        'position': 'Portero',
        'country': 'USA',
        'age': 26,
        'height': 191
      },
      'Kyle Walker':{
        'position': 'Defensa',
        'country': 'Inglaterra',
        'age': 31,
        'height': 178
      },
      'Ruben Diaz':{
        'position': 'Defensa',
        'country': 'Portugal',
        'age': 24,
        'height': 186
      },
      'John Stones':{
        'position': 'Defensa',
        'country': 'Inglaterra',
        'age': 27,
        'height': 188
      },
      'Nathan Ake':{
        'position': 'Defensa',
        'country': 'Holanda',
        'age': 26,
        'height': 180
      },
      'Oleksandr Zonchenko':{
        'position': 'Defensa',
        'country': 'Ucrania',
        'age': 25,
        'height': 175
      },
      'Aymeric Laporte':{
        'position': 'Defensa',
        'country': 'España',
        'age': 27,
        'height': 191
      },
      'Benjamin Mendy':{
        'position': 'Defensa',
        'country': 'Francia',
        'age': 27,
        'height': 185
      },
      'Joao Cancelo':{
        'position': 'Defensa',
        'country': 'Portugal',
        'age': 27,
        'height': 182
      },
      'Ilkay Gundogan':{
        'position': 'Mediocampista',
        'country': 'Alemania',
        'age': 31,
        'height': 180
      },
      'Jack Grealish':{
        'position': 'Mediocampista',
        'country': 'Inglaterra',
        'age': 26,
        'height': 175
      },
      'Rodri':{
        'position': 'Mediocampista',
        'country': 'España',
        'age': 25,
        'height': 191
      },
      'Kevin de Bruyne':{
        'position': 'Mediocampista',
        'country': 'Belgica',
        'age': 30,
        'height': 181
      },
      'Bernardo Silva':{
        'position': 'Mediocampista',
        'country': 'Portugal',
        'age': 27,
        'height': 173
      },
      'Fernandinho':{
        'position': 'Mediocampista',
        'country': 'Brasil',
        'age': 36,
        'height': 179
      },
      'Phil Foden':{
        'position': 'Mediocampista',
        'country': 'inglaterra',
        'age': 21,
        'height': 171
      },
      'Cole Palmer':{
        'position': 'Mediocampista',
        'country': 'Inglaterra',
        'age': 19,
        'height': 182
      },
      'Raheem Sterling':{
        'position': 'Delantero',
        'country': 'Inglaterra',
        'age': 27,
        'height': 170
      },
      'Gabriel Jesus':{
        'position': 'Delantero',
        'country': 'Brasil',
        'age': 24,
        'height': 175
      },
      'Ryad Mahrez':{
        'position': 'Delantero',
        'country': 'Argelia',
        'age': 30,
        'height': 179
      }
    }
  }
}