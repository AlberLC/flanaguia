## Variables, tipos, entrada/salida

### Ideas:

- Pedir por consola nombre de fruta y precio por kilo. Luego preguntar cuantos kilos por fruta y al final imprimir coste total.

<br>

### Ejercicios:

1. Pedir por consola cuánto cuesta y cuánto pesa una caja vacía, así como cuánto cuesta y pesa una muñeca. Luego pedir por consola cuántas muñecas hay por caja y cuántas cajas hay. Imprimir en la consola el coste y peso totales.

    <details>
    <summary>Solución</summary>

    ```python
    doll_price = float(input('Precio de una muñeca: '))
    doll_weight = float(input('Peso de una muñeca: '))
    box_price = float(input('Precio de una caja: '))
    box_weight = float(input('Peso de una caja: '))
    doll_number = int(input('¿Cuántas muñecas hay por caja?: '))
    box_number = int(input('¿Cuántas cajas hay?: '))

    boxes_price = box_number * box_price
    boxes_weight = box_number * box_weight

    dolls_price_per_box = doll_number * doll_price
    dolls_weight_per_bax = doll_number * doll_weight

    print()
    print(f'Coste total: {boxes_price + box_number * dolls_price_per_box} €')
    print(f'Peso total: {boxes_weight + box_number * dolls_weight_per_bax} g')
    ```

    </details>

<br>

2. Comprobar si una palabra recibida por consola es un **palíndromo** e imprimir el **[booleano](README.md#11-tipos-más-usados)** resultante **sin usar [sentencias condicionales](README.md#4-condicionales)**. Un **palíndromo** es un texto que se lee igual de izquierda a derecha que de derecha a izquierda. Por ejemplo:

    - `hola` ➡️ `False`
    - `ojos` ➡️ `False`
    - `ojo` ➡️ `True`
    - `abcba` ➡️ `True`
    - `rallar` ➡️ `True`
    - `reconocer` ➡️ `True`

    <br>

    <details>
    <summary>Solución</summary>

    ```python
    text = input('Introduce una palabra: ')
    print(text == text[::-1])
    ```

    </details>

<br>

3. Pedir por consola un texto e imprimir el número de caracteres que contiene **sin usar [bucles](README.md#5-bucles)**.

    <details>
    <summary>Solución</summary>

    ```python
    text = input('Introduce un texto: ')
    print(len(text))
    ```

    </details>

<br>

4. Pedir por consola un texto e imprimir el número de caracteres **distintos** que contiene **sin usar [bucles](README.md#5-bucles)**.

    <details>
    <summary>Solución</summary>

    ```python
    text = input('Introduce un texto: ')
    print(len(set(text)))
    ```

    </details>

<br>

## Condicionales

### Ideas:

- Calculadora

<br>

### Ejercicios:

1. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de una entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años (inclusive) debe pagar 5 € y si es mayor de 18 años, 10 €.

    <details>
    <summary>Solución</summary>

    ```python
    age = int(input('Edad: '))

    if age < 4:
        price = 0
    elif age <= 18:
        price = 5
    else:
        price = 10

    print(f"Precio de la entrada: {f'{price} €.' if price else '¡gratis!'}")
    ```

    </details>

<br>

2. Pedir por consola un año e imprimir si es bisiesto o no.

    <details>
    <summary>Solución</summary>

    ```python
    year = int(input('Año: '))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('Es bisiesto.')
    else:
        print('No es bisiesto.')
    ```

    </details>

<br>

3. Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por consola el grupo que le corresponde.

    <details>
    <summary>Solución</summary>

    ```python
    name_first_letter = input('Introduce tu nombre: ')[0].upper()
    sex = input('Introduce tu sexo (M/F): ').upper()

    if sex == 'F' and name_first_letter < 'M' or sex == 'M' and name_first_letter > 'M':
        print('Grupo A.')
    else:
        print('Grupo B.')
    ```

    </details>

<br>

4. Escribir un programa que reciba tu fecha de nacimiento por consola con un formato como `12/05/97` o `12/05/1997` y que imprima por consola cuantos años cumplirás el año 2023. Hay que tener en cuenta que el año puede darse en dos dígitos o en cuatro.

    <details>
    <summary>Solución</summary>

    a)
    ```python
    date = input('Fecha de nacimiento: ')
    year = int(date.split('/')[-1])

    if year < 1000:
        if year >= 23:
            year += 1900
        else:
            year += 2000

    print(f'Este año cumples {2023 - year} años.')
    ```
    b)
    ```python
    import datetime

    date = input('Fecha de nacimiento: ')

    try:
        year = datetime.datetime.strptime(date, '%d/%m/%y').year
    except ValueError:
        year = datetime.datetime.strptime(date, '%d/%m/%Y').year

    print(f'Este año cumples {2023 - year} años.')
    ```

    </details>

<br>

## Bucles

### Ideas:

- Iterar cadena o colecciones y contar o imprimir.
- Pedir contraseña hasta que sea la correcta.
- Añadir palabras a una lista hasta "fin" e imprimirla.
- Sumar números de una lista.
- Máximo/mínimo manualmente.
- Convertir una lista de números a sus cuadrados.
- Números impares hasta x.
- Número es primo/números primos hasta x.
- Programa que traduzca palabras del siguiente texto. Se introduce por teclado `<palabra>,<traducción>` hasta "fin". Texto:

```
Keith recently came back from a trip to Chicago, Illinois. This midwestern metropolis is found along the shore of Lake Michigan. During his visit, Keith spent a lot of time exploring the city to visit important landmarks and monuments.
```

- Iterar diccionario de datos de alumnos y actualizar estado según nota.
- Matrices. Imprimir la diagonal. Hacer producto vectorial, etc.

<br>

### Ejercicios:

1. Escribir por consola la tabla de multiplicar del número que se pida por consola.

    <details>
    <summary>Solución</summary>

    ```python
    number = int(input('Tabla del: '))
    for i in range(1, 11):
        print(f'{number} * {i} = {number * i}')
    ```

    </details>

<br>

2. Pedir por consola un número cuyos dígitos vamos a iterar para imprimir, según el valor de cada uno de ellos, una barra de progreso con los caracteres █ y ▒. Por ejemplo, si tuviéramos el número `41752`, iteraríamos cada dígito (empezando por el `4`), entonces imprimiríamos por consola `4 `████▒▒▒▒▒. Luego en la siguiente fila imprimiríamos `1 `█▒▒▒▒▒▒▒▒ y así sucesivamente hasta `2 `██▒▒▒▒▒▒▒.

    <details>
    <summary>Solución</summary>

    ```python
    CHARACTER_ON = '█'
    CHARACTER_OFF = '▒'
    
    number = input('Introduce un número: ')    
    
    for digit in number:
        print(f'{digit} {CHARACTER_ON * int(digit)}{CHARACTER_OFF * (9 - int(digit))}')
    ```

    </details>

<br>

3. Usando como base el ejercicio anterior: pedir por consola otro número. Si este número es mayor que `0`, las barras de progreso se imprimirán en orden ascendente, si es menor que `0`, en orden descendente, y si es igual a `0`, en orden de aparición (como en el ejercicio anterior).

    <details>
    <summary>Solución</summary>

    ```python
    CHARACTER_ON = '█'
    CHARACTER_OFF = '▒'
    
    number = input('Introduce un número: ')
    order = int(input('Introduce el orden: '))
    
    if order < 0:
        digits = sorted(number, reverse=True)
    elif order == 0:
        digits = number
    else:
        digits = sorted(number)
    
    for digit in digits:
        print(f'{digit} {CHARACTER_ON * int(digit)}{CHARACTER_OFF * (9 - int(digit))}')
    ```

    </details>

<br>

4. Pedir por consola la longitud de un lado de un triángulo e imprimir uno siguiendo el formato dado a continuación. Por ejemplo, para longitud 5:

    ```
    1 
    3 1 
    5 3 1 
    7 5 3 1 
    9 7 5 3 1 
    ```

    <details>
    <summary>Solución</summary>

    ```python
    height = int(input('Introduce la altura del triángulo: '))
    
    for i in range(1, height * 2, 2):
        for j in range(i, 0, -2):
            print(j, end=' ')
        print()
    ```

    </details>

<br>

5. Pedir por consola la longitud de un lado de un rombo e imprimir uno siguiendo el formato dado a continuación. Por ejemplo: para longitud 4:

    ```
       *
      ***
     *****
    *******
     *****
      ***
       *
    ```

    <details>
    <summary>Solución</summary>

    ```python
    length = int(input('Introduce la longitud del lado del rombo: '))
    
    for i in range(-length + 1, length):
        print(f"{' ' * (abs(i))}{'*' * ((length - abs(i)) * 2 - 1)}")
    ```

    </details>

<br>

6. Pedir por consola el número de niveles (altura) del [triángulo de Pascal o de Tartaglia](https://es.wikipedia.org/wiki/Tri%C3%A1ngulo_de_Pascal) e imprimirlo por consola. Por ejemplo:

    - Para altura 0:

        ```
        ```

    - Para altura 1:

        ```
        1 
        ```

    - Para altura 2:

        ```
         1 
        1 1 
        ```

    - Para altura 5:

        ```
            1 
           1 1 
          1 2 1 
         1 3 3 1 
        1 4 6 4 1 
        ```

    <details>
    <summary>Solución</summary>

    a)
    ```python
    length = int(input('Introduce la altura del triángulo: '))
    
    last_row = [0, 1]
    for i in range(length):
        print(' ' * (length - i - 1), end='')
    
        row = [0]
        for j in range(i + 1):
            number = last_row[j] + last_row[j + 1]
            print(number, end=' ')
            row.append(number)
        row.append(0)
        print()
    
        last_row = row
    ```
    b)
    ```python
    length = int(input('Introduce la altura del triángulo: '))
    
    if length > 0:
        print(f"{' ' * (length - 1)}1")
    
    last_row = []
    for i in range(1, length):
        print(f"{' ' * (length - i - 1)}1", end=' ')
    
        row = [1]
        for j in range(i - 1):
            number = last_row[j] + last_row[j + 1]
            print(number, end=' ')
            row.append(number)
        print(1)
        row.append(1)
    
        last_row = row
    ```
    c)
    ```python
    import math
    
    length = int(input('Introduce la altura del triángulo: '))
    
    for i in range(length):
        print(' ' * (length - i - 1), end='')
    
        for j in range(i + 1):
            print(int(math.factorial(i) / (math.factorial(j) * math.factorial(i - j))), end=' ')
        print()
    ```

    </details>

<br>

7. Pedir por consola un texto e imprimir el número de caracteres **distintos** que contiene **usando [bucles](README.md#5-bucles)** y **sin usar [conjuntos](README.md#16-conjuntos)**.

    <details>
    <summary>Solución</summary>

    ```python
    text = input('Introduce un texto: ')
    characters = []
    for character in text:
        if character not in characters:
            characters.append(character)
    
    print(len(characters))
    ```

    </details>

<br>

8. Comprobar si dos palabras recibidas por consola son **anagramas** entre sí e imprimir el **[booleano](README.md#11-tipos-más-usados)** resultante. Una palabra se considera **anagrama** de otra si contienen los mismos caracteres sin importar el orden. Por ejemplo:

    - `hola`, `adios` ➡️ `False`
    - `urnas`, `runa` ➡️ `False`
    - `urnas`, `runas` ➡️ `True`

    <br>

    <details>
    <summary>Solución</summary>

    ```python
    word_1 = input('Introduce la primera palabra: ')
    word_2 = input('Introduce la segunda palabra: ')
    print(sorted(word_1) == sorted(word_2))
    ```

    </details>

<br>

9. A continuación se mostrarán unos fragmentos de código que crean listas. El objetivo de este ejercicio es convertir cada caso en una [lista por comprensión](README.md#51-listas-por-comprensión) que sea equivalente.

    1. <br>

        ```python
        numbers = []
        for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            numbers.append(number * 2)
        ```

        <details>
        <summary>Solución</summary>

        ```python
        [number * 2 for number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]
        ```

        </details>

    2. <br>

        ```python
        numbers = []
        for number in range(10):
            if number % 3 == 0:
                numbers.append(number)
        ```

        <details>
        <summary>Solución</summary>

        ```python
        [number for number in range(10) if number % 3 == 0]
        ```

        </details>

    3. <br>

        ```python
        words = []
        for word in ['Lorem', 'IPSUM', 'DoLoR', 'sit', 'aMeT']:
            words.append(word.lower())
        ```

        <details>
        <summary>Solución</summary>

        ```python
        [word.lower() for word in ['Lorem', 'IPSUM', 'DoLoR', 'sit', 'aMeT']]
        ```

        </details>

    4. <br>

        ```python
        words = []
        for word in 'lorem ipsum dolor sit amet'.split():
            if word[0] in {'a', 'e', 'i', 'o', 'u'}:
                words.append(word.upper())
        ```

        <details>
        <summary>Solución</summary>

        ```python
        [word.upper() for word in 'lorem ipsum dolor sit amet'.split() if word[0] in {'a', 'e', 'i', 'o', 'u'}]
        ```

        </details>

    5. <br>

        ```python
        characters = []
        for character in 'Lorem IPSUM DoLoR sit aMeT':
            if character.isupper():
                characters.append('🔼')
            else:
                characters.append('🔽')
        ```

        <details>
        <summary>Solución</summary>

        ```python
        ['🔼' if character.isupper() else '🔽' for character in 'Lorem IPSUM DoLoR sit aMeT']
        ```

        </details>

    6. <br>

        ```python
        elements = []
        for i in range(10):
            if 2 <= i < 4:
                elements.append('---')
            else:
                elements.append(i)
        ```

        <details>
        <summary>Solución</summary>

        ```python
        ['---' if 2 <= i < 4 else i for i in range(10)]
        ```

        </details>

    7. <br>

        ```python
        elements = []
        for i in [0, 1, 'two', 'three', 4, 5]:
            if isinstance(i, int):
                elements.append(i % 2 == 0)
        ```

        <details>
        <summary>Solución</summary>

        ```python
        [i % 2 == 0 for i in [0, 1, 'two', 'three', 4, 5] if isinstance(i, int)]
        ```

        </details>

    8. <br>

        ```python
        elements = []
        for i, element in enumerate([0, 1, 'two', 'three', 4, 5]):
            if i < 4:
                continue
        
            if element % 4 == 0:
                elements.append('✅')
            else:
                elements.append('❌')
        ```

        <details>
        <summary>Solución</summary>

        ```python
        ['✅' if element % 4 == 0 else '❌' for i, element in enumerate([0, 1, 'two', 'three', 4, 5]) if i >= 4]
        ```

        </details>

<br>

10. Programar un juego de piedra, papel y tijeras en el que se pide tu jugada por consola y se genera la jugada de la ia de manera aleatoria. Mientras el usuario proporcione una entrada por consola que no sea "piedra", "papel" o "tijeras" se debe repetir la petición por consola. Al obtener la respuesta se imprimirá por consola que opción escogió la ia y el resultado de la ronda. El juego continuará para siempre.

    <details>
    <summary>Solución</summary>

    ```python
    import random
    
    options = ('piedra', 'papel', 'tijeras')
    
    while True:
        human_play = input('Elige tu jugada (piedra/papel/tijeras): ')
        if human_play not in options:
            continue
    
        ai_play = random.choice(options)
    
        if human_play == ai_play:
            print(f'La IA eligió {ai_play}. Empate.')
        elif options[(options.index(human_play) + 1) % 3] == ai_play:
            print(f'La IA eligió {ai_play}. Perdiste.')
        else:
            print(f'La IA eligió {ai_play}. ¡Ganaste!')
    ```

    </details>

<br>

11. Escribir un programa que reciba tu fecha de nacimiento por consola con un formato como `18/6/97` o `18/6/1997` (teniendo en cuenta que el año puede darse en dos o cuatro dígitos) y que imprima por consola una línea por año cumplido hasta 2023, inclusive. Por ejemplo, para `18/6/1997`:

    ```
    El 18 de junio de 1998 cumpliste 1 año.
    El 18 de junio de 1999 cumpliste 2 años.
    ...
    ```

    Nótese que cuando se cumple 1 año se indica en singular y, para más años, en plural. Además sustituimos el número de mes por su nombre.

    <details>
    <summary>Solución</summary>

    a)
    ```python
    date = input('Fecha de nacimiento: ')
    day, month, first_year = (int(number) for number in date.split('/'))
    
    if first_year < 1000:
        if first_year >= 23:
            first_year += 1900
        else:
            first_year += 2000
    
    month_names = [
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre'
    ]
    
    for i, year in enumerate(range(first_year + 1, 2024), start=1):
        print(f"El {day} de {month_names[month - 1]} de {year} cumpliste {i} año{'' if i == 1 else 's'}.")
    ```
    b)
    ```python
    import datetime
    
    date = input('Fecha de nacimiento: ')
    day, month, first_year = (int(number) for number in date.split('/'))
    
    try:
        first_year = datetime.datetime.strptime(date, '%d/%m/%y').year
    except ValueError:
        first_year = datetime.datetime.strptime(date, '%d/%m/%Y').year
    
    month_names = [
        'enero',
        'febrero',
        'marzo',
        'abril',
        'mayo',
        'junio',
        'julio',
        'agosto',
        'septiembre',
        'octubre',
        'noviembre',
        'diciembre'
    ]
    
    for i, year in enumerate(range(first_year + 1, 2024), start=1):
        print(f"El {day} de {month_names[month - 1]} de {year} cumpliste {i} año{'' if i == 1 else 's'}.")
    ```

    </details>

<br>

12. Escribir un programa que pida por consola nombres de asignaturas continuamente hasta que se introduzca `fin`. Luego el programa preguntará la nota para cada asignatura y terminará imprimiendo las asignaturas que queden suspensas siguiendo el siguiente formato: `Asignaturas suspensas: Lengua, Matemáticas y Física.`

    <details>
    <summary>Solución</summary>

    ```python
    subject = input('Introduce una asignatura ("fin" para terminar): ')
    subjects = []
    while subject != 'fin':
        subjects.append(subject)
        subject = input('Introduce una asignatura ("fin" para terminar): ')
    
    failed_subjects = []
    for subject in subjects:
        grade = float(input(f'Introduce la nota de {subject}: '))
        if grade < 5:
            failed_subjects.append(subject)
    
    if len(failed_subjects) > 1:
        print(f"Asignaturas suspensas: {', '.join(failed_subjects[:-1])} y {failed_subjects[-1]}.")
    else:
        print(f'Asignaturas suspensas: {failed_subjects[0]}.')
    ```

    </details>

<br>

13. Hacer un programa que imprima por consola el número de veces que aparece cada palabra en el siguiente texto:

    ```
    Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.
    ```

    <details>
    <summary>Solución</summary>

    a)
    ```python
    text = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
    
    word_occurrences = {}
    
    for word in text.split():
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1
    
    print(word_occurrences)
    ```
    b)
    ```python
    from collections import defaultdict
    
    text = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
    
    word_occurrences = defaultdict(int)
    
    for word in text.split():
        word_occurrences[word] += 1
    
    print(word_occurrences)
    ```
    c)
    ```python
    from collections import Counter
    
    text = 'Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem Ipsum.'
    
    print(Counter(text.split()))
    ```

    </details>

<br>

14. En una tienda de deportes ha habido un lote de pelotas descoloridas que se tienen que vender con descuento. Crear un programa que pida por consola el precio de una pelota y su descuento para el lote descolorido. Luego pedir por consola el número de pelotas normales y descoloridas que hay en la tienda. Mientras queden pelotas en la tienda: preguntar por consola si quiere comprar una pelota normal o una descolorida e imprimir por consola lo que le va a costar al cliente (y la pelota contará ya como vendida).

    <details>
    <summary>Solución</summary>

    ```python
    ball_price = float(input('Precio de una pelota: '))
    discount = float(input('% de descuento para pelota descolorida: '))
    normal_balls = int(input('Nº de pelotas normales: '))
    colorless_balls = int(input('Nº de pelotas descoloridas: '))

    discounted_price = ball_price * discount / 100

    while normal_balls or colorless_balls:
        option = input('¿Quieres una pelota normal o descolorida? (N/D): ')

        if option.upper() == 'N':
            if normal_balls:
                print(f'Te va a costar {ball_price} €')
                normal_balls -= 1
                print(f'Quedan {normal_balls} pelotas normales.')
            else:
                print('No quedan pelotas normales.')
        elif option.upper() == 'D':
            if colorless_balls:
                print(f'Te va a costar {discounted_price} €')
                colorless_balls -= 1
                print(f'Quedan {colorless_balls} pelotas descoloridas.')
            else:
                print('No quedan pelotas descoloridas.')
    ```

    </details>

<br>

## Funciones

### Ideas:

- Filtrar los números de una lista que son múltiplos de 2 y, luego, los que son múltiplos de 3.
- Módulo de un vector.
- Suma de vetores.
- Área de un círculo y otra el volúmen de un cilindro usando la anterior.

<br>

### Ejercicios:

1. Sea una función `sum_numbers` que sume una lista de números enteros y devuelva el resultado:

    ```python
    def sum_numbers(numbers: list[int]) -> int:
        ...
    
    
    assert sum_numbers([1]) == 1
    assert sum_numbers([0, 1, 2, 3, 4, 5]) == 15
    assert sum_numbers([5, 1, 85, 21, 5, 1, 252, 15, 1, 0, 56]) == 442
    assert sum_numbers([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -165, -1]) == 374
    assert sum_numbers([]) == 0
    
    print('OK')
    ```
   
    Rellenar el código donde `...` para que, al ejecutarlo, no se produzca ningún error y se imprima `OK` por consola.
    
    > `assert` es una sentencia que comprueba la veracidad de lo que haya a la derecha. Si es `True` no hace nada, pero si es `False` lanza una [excepción](README.md#7-excepciones).

    <details>
    <summary>Solución</summary>

    a)
    ```python
    def sum_numbers(numbers: list[int]) -> int:
        total = 0
        for number in numbers:
            total += number
    
        return total
    
    
    assert sum_numbers([1]) == 1
    assert sum_numbers([0, 1, 2, 3, 4, 5]) == 15
    assert sum_numbers([5, 1, 85, 21, 5, 1, 252, 15, 1, 0, 56]) == 442
    assert sum_numbers([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -165, -1]) == 374
    assert sum_numbers([]) == 0
    
    print('OK')
    ```
    b)
    > Usando la [función integrada](https://docs.python.org/3/library/functions.html) `sum()`:

    ```python
    def sum_numbers(numbers: list[int]) -> int:
        return sum(numbers)
    
    
    assert sum_numbers([1]) == 1
    assert sum_numbers([0, 1, 2, 3, 4, 5]) == 15
    assert sum_numbers([5, 1, 85, 21, 5, 1, 252, 15, 1, 0, 56]) == 442
    assert sum_numbers([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -165, -1]) == 374
    assert sum_numbers([]) == 0
    
    print('OK')
    ```

    </details>

<br>

2. Crear una función que devuelva la media de una lista de números enteros. Para ello rellenar el siguiente código donde `...` y ejecutarlo sin errores:

    ```python
    ...
    
    
    assert average([0, 1]) == 0.5
    assert average([1, 3]) == 2
    assert average([1, 1, 1, 2, 2, 2]) == 1.5
    assert average([1, 2, 3, 4, 5, 6, 7]) == 4
    assert average([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -1]) == 49
    
    print('OK')
    ```

    <details>
    <summary>Solución</summary>

    a)
    ```python
    def average(numbers: list[int]) -> float:
        return sum(numbers) / len(numbers)
    
    
    assert average([0, 1]) == 0.5
    assert average([1, 3]) == 2
    assert average([1, 1, 1, 2, 2, 2]) == 1.5
    assert average([1, 2, 3, 4, 5, 6, 7]) == 4
    assert average([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -1]) == 49
    
    print('OK')
    ```
    b)
    ```python
    import statistics
    
    
    def average(numbers: list[int]) -> float:
        return statistics.mean(numbers)
    
    
    assert average([0, 1]) == 0.5
    assert average([1, 3]) == 2
    assert average([1, 1, 1, 2, 2, 2]) == 1.5
    assert average([1, 2, 3, 4, 5, 6, 7]) == 4
    assert average([99, -2, 651, -215, -5, 15, -2, -5, -5, 9, -1]) == 49
    
    print('OK')
    ```

    </details>

<br>

3. Crear una función que multiplique dos números enteros y devuelva el resultado **sin usar el operador `*` ni otras funciones ya existentes en el lenguaje**. Para ello rellenar el siguiente código donde `...` y ejecutarlo sin errores:

    ```python
    ...
    
    
    assert multiply(1, 0) == 0
    assert multiply(1, 5) == 5
    assert multiply(2, 3) == 6
    assert multiply(4, 6) == 24
    assert multiply(9, 9) == 81
    assert multiply(156, 748) == 116688
    
    print('OK')
    ```

    <details>
    <summary>Solución</summary>

    a)
    ```python
    def multiply(a: int, b: int) -> int:
        result = 0
        for _ in range(b):
            result += a
    
        return result
    
    
    assert multiply(1, 0) == 0
    assert multiply(1, 5) == 5
    assert multiply(2, 3) == 6
    assert multiply(4, 6) == 24
    assert multiply(9, 9) == 81
    assert multiply(156, 748) == 116688
    
    print('OK')
    ```

    </details>

<br>

4. Crear una función que calcule la potencia de dos números enteros y devuelva el resultado **sin usar el operador `*` ni el `**` ni otras funciones ya existentes en el lenguaje**. Para ello rellenar el siguiente código donde `...` y ejecutarlo sin errores:

    ```python
    ...
    
    
    assert power(1, 0) == 1
    assert power(1, 5) == 1
    assert power(2, 3) == 8
    assert power(4, 6) == 4096
    assert power(9, 9) == 387420489
    assert power(156, 748) == 286549443351127940912310344045265379399803458435563791862649509231216879586336194220793821017373647185528398137999718912683128795377832303403490201379359728778963725712702463720899321651446986307432812286112922967228580960214040125458695767296293492756095590796296252772591364291990138982325685743548631279104099327229955069543312383943928569589500428240235864193352231896378085487701206310482438629978196570600669696176974867295927957162771499932719963782638405872941627163945392132697296159548444339186032772019071612508373347184386809719130025733501976239325432083270617606124112480291078628881717726173272160235619918748740934426750510852059921564202650490333472044279349258704176344258614157450959649432290412661948873317244678184320775559997651598349552153798297229315952888067156171478848685229875195340084118982746553371195570217565399222912887319714437063923000301169199431174634221186253813327520958521863464388914428822386196528155397135516468634450866394412866963150900511750867881496922423196459731944557792051780869298758423806545140278667826504433395868108990488815000032551672311460007973246010385852170542062600416835177910004633677354230797418744082051322584486841250399669246233133287810006784316971050988939252097351751754453069226094037483479404065220228309524776165493035610689065099827326914471595115782429383596669980591989328083380710996308171307342231329766100047312986412629944411588282939893313052319942829030706584636734295943711749021207252714951142354676931287445776741682610756756409826172383898461966942453065292464871485995092675008017851221446856996710750853618091265093397903433961824210436455077318230016
    
    print('OK')
    ```

    <details>
    <summary>Solución</summary>

    a)
    ```python
    def multiply(a: int, b: int) -> int:
        result = 0
        for _ in range(b):
            result += a
    
        return result
    
    
    def power(a: int, b: int) -> int:
        result = 1
        for _ in range(b):
            result *= a
    
        return result
    
    
    assert power(1, 0) == 1
    assert power(1, 5) == 1
    assert power(2, 3) == 8
    assert power(4, 6) == 4096
    assert power(9, 9) == 387420489
    assert power(156, 748) == 286549443351127940912310344045265379399803458435563791862649509231216879586336194220793821017373647185528398137999718912683128795377832303403490201379359728778963725712702463720899321651446986307432812286112922967228580960214040125458695767296293492756095590796296252772591364291990138982325685743548631279104099327229955069543312383943928569589500428240235864193352231896378085487701206310482438629978196570600669696176974867295927957162771499932719963782638405872941627163945392132697296159548444339186032772019071612508373347184386809719130025733501976239325432083270617606124112480291078628881717726173272160235619918748740934426750510852059921564202650490333472044279349258704176344258614157450959649432290412661948873317244678184320775559997651598349552153798297229315952888067156171478848685229875195340084118982746553371195570217565399222912887319714437063923000301169199431174634221186253813327520958521863464388914428822386196528155397135516468634450866394412866963150900511750867881496922423196459731944557792051780869298758423806545140278667826504433395868108990488815000032551672311460007973246010385852170542062600416835177910004633677354230797418744082051322584486841250399669246233133287810006784316971050988939252097351751754453069226094037483479404065220228309524776165493035610689065099827326914471595115782429383596669980591989328083380710996308171307342231329766100047312986412629944411588282939893313052319942829030706584636734295943711749021207252714951142354676931287445776741682610756756409826172383898461966942453065292464871485995092675008017851221446856996710750853618091265093397903433961824210436455077318230016
    
    print('OK')
    ```

    </details>

<br>

5. Crear una función que devuelva el factorial de un número dado como argumento **usando [bucles](README.md#5-bucles)**. El factorial de 0 es 1. Y el factorial de un número negativo debe [lanzar](README.md#71-lanzamiento-de-excepciones) un `ValueError`.

    <details>
    <summary>Solución</summary>

    a)
    ```python
    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError
    
        result = 1
        while number > 1:
            result *= number
            number -= 1
    
        return result
    
    
    print(factorial(4))
    print(factorial(-1))
    ```
    b)
    ```python
    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError
    
        result = 1
        for i in range(2, number + 1):
            result *= i
    
        return result
    
    
    print(factorial(4))
    print(factorial(-1))
    ```

    </details>

<br>

6. Crear una función que devuelva el factorial de un número dado como argumento **sin usar [bucles](README.md#5-bucles)**. El factorial de 0 es 1. Y el factorial de un número negativo debe [lanzar](README.md#71-lanzamiento-de-excepciones) un `ValueError`.

    <details>
    <summary>Solución</summary>

    ```python
    def factorial(number: int) -> int:
        if number < 0:
            raise ValueError
        if number <= 1:
            return 1
    
        return number * factorial(number - 1)
    
    
    print(factorial(7))
    print(factorial(-1))
    ```

    </details>

<br>

7. Crear una función que aplane una lista (u otro iterable). Una lista puede tener otras listas y demás estructuras como tuplas, conjuntos, etc., por lo tanto, aplanar una lista consiste en conseguir como resultado otra con los elementos que contenía originalmente más aquellos contenidos en esas estructuras o colecciones internas. Por ejemplo:

    - `[0, 1, 2, [3, 4, 5]]` ➡️ `[0, 1, 2, 3, 4, 5]`
    - `[{'hello', 'bye'}, 45, 'text']` ➡️ `['hello', 'bye', 45, 'text']`
    - `[[0], [[[1]]], 2]` ➡️ `[0, 1, 2]`
    - `(0, [1], (2, ('three', [4.0, {'five'}])))` ➡️ `[0, 1, 2, 'three', 4.0, 'five']`
    - `range(6)` ➡️ `[0, 1, 2, 3, 4, 5]`

    La función puede recibir como argumento cualquier iterable, no solo listas, pero el resultado devuelto siempre será una lista.

    <details>
    <summary>Solución</summary>

    ```python
    from collections.abc import Iterable
    
    
    def flatten(elements: Iterable) -> list:
        new_elements = []
    
        for element in elements:
            if isinstance(element, Iterable) and not isinstance(element, str):
                new_elements += flatten(element)
            else:
                new_elements.append(element)
    
        return new_elements
    
    
    print(flatten([0, 1, 2, [3, 4, 5]]))
    print(flatten([{'hello', 'bye'}, 45, 'text']))
    print(flatten([0, 1, 2, [3, 4, 5]]))
    print(flatten((0, [1], (2, ('three', [4.0, {'five'}])))))
    print(flatten(range(6)))
    ```

    </details>

<br>

8. Crear una función que imprima por consola los `n` primeros números de la sucesión de Fibonacci separados por el separador dado por argumento. Esta sucesión es la siguiente: `0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...`. Los dos primeros números son `0` y `1` y cada número posterior es el resultado de la suma de los dos anteriores. Entonces:

    - `fibonacci_sequence(0, ', ')` ➡️
    - `fibonacci_sequence(1, ', ')` ➡️ `0`
    - `fibonacci_sequence(3, ', ')` ➡️ `0, 1, 1`
    - `fibonacci_sequence(5, ' - ')` ➡️ `0 - 1 - 1 - 2 - 3`
    - `fibonacci_sequence(11, ' | ')` ➡️ `0 | 1 | 1 | 2 | 3 | 5 | 8 | 13 | 21 | 34 | 55`

    La sucesión de Fibonacci para `n` negativo debe [lanzar](README.md#71-lanzamiento-de-excepciones) un `ValueError`.

   > La función `join()` de las cadenas nos puede ayudar en este ejercicio:
   > ```python
    > >>> ', '.join(['one', 'two', 'three', 'four'])
    > 'one, two, three, four'
    > >>> '-YEAH-'.join(['one', 'two', 'three', 'four'])
    > 'one-YEAH-two-YEAH-three-YEAH-four'
    > ```

    <details>
    <summary>Solución</summary>

    ```python
    def fibonacci(number: int) -> int:
        if number == 0:
            return 0
        if number == 1:
            return 1
    
        return fibonacci(number - 2) + fibonacci(number - 1)
    
    
    def fibonacci_sequence(n: int, separator: str) -> None:
        if n < 0:
            raise ValueError
    
        print(separator.join(str(fibonacci(i)) for i in range(n)))
    
    
    fibonacci_sequence(0, ', ')
    fibonacci_sequence(1, ', ')
    fibonacci_sequence(3, ', ')
    fibonacci_sequence(5, ' - ')
    fibonacci_sequence(11, ' | ')
    fibonacci_sequence(-1, ' | ')
    ```

    </details>

<br>

9. Crear dos funciones que simulen el [cifrado césar](https://es.wikipedia.org/wiki/Cifrado_C%C3%A9sar) y posterior descifrado de un mensaje. Este cifrado consiste básicamente en cambiar cada símbolo de un texto por otro que le sigue a cierta distancia en el alfabeto. Por ejemplo, si ciframos el texto `'abc'` con un desplazamiento `1`:

    `encode('abc', 1)` ➡️ `'bcd'`

    Si lo ciframos con desplazamiento `2`:

    `encode('abc', 2)` ➡️ `'cde'`

    En el ejercicio vamos a usar únicamente los [caracteres ascii](https://elcodigoascii.com.ar/)   imprimibles (del 32 al 126) como alfabeto, es decir, del `' '` al `'~'`, así que los textos cifrados van a contener solamente carácteres dentro de ese rango.

    Teniendo esto en cuenta: desarrollar dos funciones que reciban dos argumentos, el texto y el desplazamiento, de forma que siempre se cumpla:

    `decode(encode(text, offset), offset) == text` ➡️ `True`

    <details>
    <summary>Solución</summary>

    ```python
    FIRST_CHARACTER_INDEX = 32
    ALPHABET_LENGHT = 95
    
    
    def encode(text: str, offset: int) -> str:
        new_characters = [
            chr(ord(character) - FIRST_CHARACTER_INDEX + offset % ALPHABET_LENGHT + FIRST_CHARACTER_INDEX)
            for character in text
        ]
        return ''.join(new_characters)
    
    
    def decode(text: str, offset: int) -> str:
        new_characters = [
            chr(ord(character) - FIRST_CHARACTER_INDEX - offset % ALPHABET_LENGHT + FIRST_CHARACTER_INDEX)
            for character in text
        ]
        return ''.join(new_characters)
    
    
    offset = 12
    text = 'asdASD0123456789!"·!"·"$%&/()=?¿¡\'09876.,:;-_´`+çÇ^¨*{}[]@#54321 sdfklwd'
    print(decode(encode(text, offset), offset) == text)
    ```

    </details>

<br>

10. Sustituir los `...` de los comentarios del siguiente códido por `local` o `global` según el ámbito del nombre/recurso usado:

    > Para este ejercicio es necesario entender el capítulo [6.3. Ámbitos](README.md#63-ámbitos) de la teoría.

    ```python
    n = 45
    word = 'house'
    
    
    def aaa(text, n):
        print(f'--- {text} ---')  # text ➡️ ...
        print(n * 2)  # n ➡️ ...
    
    
    def bbb(f, numbers):
        word = 'car'
        aaa(word, n)  # aaa ➡️ ... # word ➡️ ... # n ➡️ ...
        for number in numbers:  # numbers ➡️ ...
            print(number)  # number ➡️ ...
        f()  # f ➡️ ...
        ccc()  # ccc ➡️ ...
    
    
    def ccc():
        def ddd():
            print(n)  # n ➡️ ...
    
        ddd()  # ddd ➡️ ...
    
    
    aaa(word, n)  # aaa ➡️ ... # word ➡️ ... # n ➡️ ...
    bbb(ccc, [1, 2, 3])  # bbb ➡️ ... # ccc ➡️ ...
    ```

    <details>
    <summary>Solución</summary>

    ```python
    n = 45
    word = 'house'
    
    
    def aaa(text, n):
        print(f'--- {text} ---')  # text ➡️ local
        print(n * 2)  # n ➡️ local
    
    
    def bbb(f, numbers):
        word = 'car'
        aaa(word, n)  # aaa ➡️ global # word ➡️ local # n ➡️ global
        for number in numbers:  # numbers ➡️ local
            print(number)  # number ➡️ local
        f()  # f ➡️ local
        ccc()  # ccc ➡️ global
    
    
    def ccc():
        def ddd():
            print(n)  # n ➡️ global
    
        ddd()  # ddd ➡️ local
    
    
    aaa(word, n)  # aaa ➡️ global # word ➡️ global # n ➡️ global
    bbb(ccc, [1, 2, 3])  # bbb ➡️ global # ccc ➡️ global
    ```

    </details>

<br>

11. Ejercicio `time_it()`.

    > Para este ejercicio es necesario haber hecho y entendido el ejercicio anterior.

    > Si se complica este ejercicio: revisar los capítulos de la teoría de [funciones](README.md#índice).

    1. Se proporcionará código que contiene dos funciones:`function_1()` y `time_it()`.

        - `function_1()` está ya hecha y se encarga de generar una espera aleatoria entre 1 y 3 segundos.
        - `time_it()` hay que completarla y tiene que servir para calcular cuanto tarda cualquier función en ejecutarse usando la función `perf_counter()` del módulo `time`.

        Objetivo: completar el código donde `...` de forma que se imprima por consola cuantos segundos ha tardado `function_1()` en ejecutarse **sin usar `function_1()` globalmente dentro de `time_it`**.

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def time_it(...) -> None:
            ...
        
        
        time_it(...)
        ```

        <details>
        <summary>Solución</summary>

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def time_it(function: Callable) -> None:
            start = time.perf_counter()
            function()
            print(f'Ha tardado {time.perf_counter() - start} segundos.')
        
        
        time_it(function_1)
        ```

        </details>

    2. `function_1()` ha evolucionado a `function_2()`. Ahora, además, devuelve la suma de tres números enteros recibidos por parámetro.

        Objetivo: completar el siguiente código donde `...` de forma que se imprima por consola cuantos segundos ha tardado `function_2()` en ejecutarse y el resultado de la suma (de ahí el `print()` añadido en la última línea) **sin usar `function_2()` globalmente dentro de `time_it`**.

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def time_it(...) -> int:
            ...
        
        
        print(time_it(...))
        ```

        <details>
        <summary>Solución</summary>

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def time_it(function: Callable, a: int, b: int, c: int) -> int:
            start = time.perf_counter()
        
            value = function(a, b, c)
            print(f'Ha tardado {time.perf_counter() - start} segundos.')
            return value
        
        
        print(time_it(function_2, 5, 2, 7))
        ```

        </details>

    3. Ahora tenemos todas las funciones anteriores más `function_3()`. Esta genera una espera aleatoria y devuelve la cadena de texto resultante de multiplicar una cadena por un número (ambos recibidos por parámetro).

        Objetivo: completar el siguiente código donde `...` de forma que se imprima por consola cuantos segundos han tardado `function_1()`, `function_2()` y `function_3()` en ejecutarse y sus resultados.

        ```python
        import random
        import time
        from collections.abc import Callable
        from typing import Any
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def function_3(text: str, n: int) -> str:
            time.sleep(random.randint(1, 3))
        
            return text * n
        
        
        def time_it(...) -> Any:
            ...
        
        
        time_it(function_1)
        print(time_it(function_2, 5, 2, 7))
        print(time_it(function_3, 'hola', 3))
        ```

        <details>
        <summary>Solución</summary>

        ```python
        import random
        import time
        from collections.abc import Callable
        from typing import Any
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def function_3(text: str, n: int) -> str:
            time.sleep(random.randint(1, 3))
        
            return text * n
        
        
        def time_it(function: Callable, *args: Any) -> Any:
            start = time.perf_counter()
        
            value = function(*args)
            print(f'Ha tardado {time.perf_counter() - start} segundos.')
            return value
        
        
        time_it(function_1)
        print(time_it(function_2, 5, 2, 7))
        print(time_it(function_3, 'hola', 3))
        ```

        </details>

    4. Por último: completar donde `...` para conseguir la misma salida del ejercicio anterior con la cabecera de `time_it()` ya definida como sigue:

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def function_3(text: str, n: int) -> str:
            time.sleep(random.randint(1, 3))
        
            return text * n
        
        
        def time_it(function: Callable) -> str:
            ...
        
        
        time_it(...)
        print(time_it(...))
        print(time_it(...))
        ```

        <details>
        <summary>Solución</summary>

        ```python
        import random
        import time
        from collections.abc import Callable
        
        
        def function_1() -> None:
            time.sleep(random.randint(1, 3))
        
        
        def function_2(a: int, b: int, c: int) -> int:
            time.sleep(random.randint(1, 3))
        
            return a + b + c
        
        
        def function_3(text: str, n: int) -> str:
            time.sleep(random.randint(1, 3))
        
            return text * n
        
        
        def time_it(function: Callable) -> str:
            start = time.perf_counter()
        
            value = function()
            print(f'Ha tardado {time.perf_counter() - start} segundos.')
            return value
        
        
        time_it(function_1)
        print(time_it(lambda: function_2(5, 2, 7)))
        print(time_it(lambda: function_3('hola', 3)))
        ```

        </details>

<br>

12. Sea el siguiente código:

    ```python
    from collections.abc import Callable
    from typing import Any
    
    
    def process(numbers: list, something: Callable[[int], Any]) -> None:
        print([something(number) for number in numbers])
    
    
    numbers_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ...
    ```
    
    Completar `...` **sin usar `print()`** y ejecutar para que en la consola salga:

    ```
    [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
    [False, True, False, True, False, True, False, True, False, True, False]
    ['Suspenso', 'Suspenso', 'Suspenso', 'Suspenso', 'Suspenso', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado']
    ```

    <details>
    <summary>Solución</summary>

    ```python
    from collections.abc import Callable
    from typing import Any
    
    
    def process(numbers: list[int], something: Callable[[int], Any]) -> None:
        print([something(number) for number in numbers])
    
    
    numbers_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    process(numbers_, lambda number: number * 3)
    process(numbers_, lambda number: number % 2 == 0)
    process(numbers_, lambda number: 'Aprobado' if number >= 5 else 'Suspenso')
    ```

    </details>

<br>

13. Sea:

    ```python
    elements = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven')]   
    ```

    Ordenar `elements` por el **segundo elemento** de cada tupla **descendentemente** usando la [función integrada](https://docs.python.org/3/library/functions.html) `sorted()` (y sus parámetros `key` y `reverse`) y mostrar el resultado por consola.

    > `key` espera una función para ordenar los elementos de forma que devuelva el valor a comparar.

    <details>
    <summary>Solución</summary>

    ```python
    elements = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'), (6, 'six'), (7, 'seven')]
    
    print(sorted(elements, key=lambda item: item[1], reverse=True))
    ```

    </details>

<br>

14. Filtrado de archivos.

    En el siguiente grupo de ejercicios vamos a utilizar varias técnicas para navegar por los archivos de nuestro ordenador. Vamos a usar diversos recursos de la biblioteca [pathlib](https://docs.python.org/3/library/pathlib.html) (`import pathlib`), que viene ya instalada con el lenguaje, para iterar los archivos como objetos `Path`.

    1. Crear una función:
        - Que tenga dos parámetros: la ruta (`str`) donde se encuentran los archivos y una extensión (`str`) para filtrar aquellos que la tengan (por ejemplo: `.jpg`)
        - Que devuelva la lista de archivos (`list[Path]`) en ese directorio que tengan dicha extensión.
        - Sin buscar recursivamente en subdirectorios.
        - Sin usar [listas por comprensión](README.md#51-listas-por-comprensión).

       Probar la función pidiendo por consola la ruta y la extensión e imprimir cada ruta con el número correspondiente tal que:
        ```
        1. <ruta>
        2. <ruta>
        3. <ruta>
        ...
        ```

        <details>
        <summary>Solución</summary>

        ```python
        import pathlib
        
        
        def filter_files(path: str, extension: str) -> list[pathlib.Path]:
            files = []
            for path in pathlib.Path(path).iterdir():
                if path.suffix == extension:
                    files.append(path)
        
            return files
        
        
        path_ = input('Ruta: ')
        extension_ = input('Extensión: ')
        
        for i, path_ in enumerate(filter_files(path_, extension_), start=1):
            print(f'{i}. {path_}')
        ```

       > Alternativamente se podrían importar los recursos así: `from pathlib import Path`. De esta manera usaríamos `Path` directamente en vez de `pathlib.Path`. Es preferencia personal elegir que método resulta más descriptivo y cómodo pero ten en cuenta que, cuando se usan muchas bibliotecas, ayuda mucho importar sólo el módulo y luego acceder al recurso excplícitamente como se hace en la solución para saber de donde vienen las cosas.

        </details>

    2. En el ejercicio anterior creamos una lista con todas las rutas `Path` de los archivos que cumplen nuestro filtro. Imaginemos que nuestro directorio contiene millones de archivos: estamos guardando en memoria un objeto `Path` por cada uno de ellos y, como es lógico, eso es bastante problemático. En los casos donde tengamos que procesar muchos elementos y no necesitemos que persistan en el tiempo o no sea posible por las limitaciones de memoria del ordenador tendremos que usar [iteradores](README.md#52-iteradores).

       Con eso en mente: arreglar la función del ejercicio anterior manteniendo los requisitos (menos el valor de retorno `list[Path]`).

        <details>
        <summary>Solución</summary>

        ```python
        import pathlib
        from collections.abc import Iterator
        
        
        def filter_files(path: str, extension: str) -> Iterator[pathlib.Path]:
            for path in pathlib.Path(path).iterdir():
                if path.suffix == extension:
                    yield path
        
        
        path_ = input('Ruta: ')
        extension_ = input('Extensión: ')
        
        for i, path_ in enumerate(filter_files(path_, extension_), start=1):
            print(f'{i}. {path_}')
        ```

       > Alternativamente, en la función generadora se podria declarar este tipo de retorno: ` -> Generator[Path, None, None]:`. Más información en la [documentación](https://docs.python.org/3/library/typing.html#typing.Generator).

        </details>

    3. Olvidemos los iteradores. Volvamos a hacer el ejercicio inicial, pero con [listas por comprensión](README.md#51-listas-por-comprensión) (prohibido usar `append()`).

        <details>
        <summary>Solución</summary>

        ```python
        import pathlib
        
        
        def filter_files(path: str, extension: str) -> list[pathlib.Path]:
            return [path for path in pathlib.Path(path).iterdir() if path.suffix == extension]
        
        
        path_ = input('Ruta: ')
        extension_ = input('Extensión: ')
        
        for i, path_ in enumerate(filter_files(path_, extension_), start=1):
            print(f'{i}. {path_}')
        ```

        </details>

    4. Ahora, en vez de una lista por comprensión, usar un [generador con paréntesis](README.md#521-generadores) (no debería ocupar ni una línea más ni menos que el ejercicio anterior).

        <details>
        <summary>Solución</summary>

        ```python
        import pathlib
        from collections.abc import Iterator
        
        
        def filter_files(path: str, extension: str) -> Iterator[pathlib.Path]:
            return (path for path in pathlib.Path(path).iterdir() if path.suffix == extension)
        
        
        path_ = input('Ruta: ')
        extension_ = input('Extensión: ')
        
        for i, path_ in enumerate(filter_files(path_, extension_), start=1):
            print(f'{i}. {path_}')
        ```

        </details>

    5. Envolver el `for` con el `print(...)` que ponemos al final para probar nuestra función en otra, de forma que reciba los `Path` por parámetro.

        <details>
        <summary>Solución</summary>

        ```python
        import pathlib
        from collections.abc import Iterable, Iterator
        
        
        def filter_files(path: str, extension: str) -> Iterator[pathlib.Path]:
            return (path for path in pathlib.Path(path).iterdir() if path.suffix == extension)
        
        
        def print_files(paths: Iterable[pathlib]) -> None:
            for i, path in enumerate(paths, start=1):
                print(f'{i}. {path}')
        
        
        path_ = input('Ruta: ')
        extension_ = input('Extensión: ')
        print_files(filter_files(path_, extension_))
        ```

       > Es recomdable declarar los tipos de los parámetros lo más ampliamente posible. En nuestro caso vamos a iterar los `Path`, no necesitamos que sea específicamente una lista, un conjunto, un generador, etc., con que sea iterable nos vale. Así hacemos nuestra función más flexible.

        </details>

    6. Por último, queremos poder filtrar los archivos siguiendo otros criterios, añadir flexibilidad al filtro de forma que, desde fuera, se pueda definir que archivos queremos, es decir, el usuario final de la función deberá poder trabajar directamente con los `Path` para poder definir filtros como:

        - Archivos que comiencen por mayúsculas.
        - Archivos cuya primera letra esté entra la `a` y la `g`.
        - Archivos que pesen más de 1 MB.
        - Archivos cuya extensión esté en `{'.png', .flv' .mp4'}`
        - Cualquier combinación de todas las reglas anteriores.
        - Cualquier cosa que se le ocurra a quien quiera usar la función y que pueda hacer con los objetos `Path`.

       Por lo tanto el filtro debe ser recibido por parámetro.

       Objetivo: alterar el programa anterior de forma que la función no reciba una extensión por parámetro, sino que reciba "algo" que se pueda aplicar dentro del generador para filtrar los `Path` que nos interesan.

       Probar los siguientes filtros:

        - Archivos que contienen la letra `e` en su nombre y tienen un número impar de letras.
        - Archivos `.jpg` o `.png` que pesan menos de 1 MB.
        - Archivos sin extensión (no directorios).
        - Archivos que se modificaron hace menos de un año.

        <br>

        <details>
        <summary>Solución</summary>

        ```python
        import datetime
        import pathlib
        from collections.abc import Callable, Iterable, Iterator
        
        
        def filter_files(path: str, filter_: Callable[[pathlib.Path], bool]) -> Iterator[pathlib.Path]:
            return (path for path in pathlib.Path(path).iterdir() if filter_(path))
        
        
        def print_files(paths: Iterable[pathlib]) -> None:
            for i, path in enumerate(paths, start=1):
                print(f'{i}. {path}')
        
        
        path_ = input('Ruta: ')
        print_files(filter_files(path_, lambda path: 'e' in path.name and len(path.name) % 2 != 0))
        print()
        print_files(filter_files(path_, lambda path: path.suffix in {'.jpg', '.png'} and path.stat().st_size < 1_000_000))
        print()
        print_files(filter_files(path_, lambda path: not path.suffix and path.is_file()))
        print()
        minimum_date = datetime.datetime.now() - datetime.timedelta(days=365)
        print_files(filter_files(path_, lambda path: minimum_date < datetime.datetime.fromtimestamp(path.stat().st_mtime)))
        ```

        </details>

<br>

15. ☠️ Crear un gestor de clientes por consola.

    > Para este ejercicio es recomendable saber utilizar [excepciones](README.md#7-excepciones).

    - ▶️ Inicio.
        - Cada cliente se va a gestionar como un diccionario `{'id': <value>, 'name': <value>, 'age': <value>}`.
        - Los clientes se van a almacenar en una lista global `clients`, es decir, `clients: list[dict] = []` .
        - Cuando se inicie por primera vez se imprimirá lo siguiente:

            ```
            Bienvenido al gestor de clientes.
            
            ----- Menú -----
            1. ➕ Añadir cliente.
            2. 🔎 Buscar clientes.
            3. 🔄️ Actualizar cliente.
            4. 🗑️ Eliminar cliente.
            5. 🏃🏻 Salir.
             
            > 
            ```

        - La flecha `>` de abajo es el `input()` para elegir la opción del menú.
        - Si se introduce una opción inválida se imprimirá otra vez el menú y se volverá a pedir la opción.

    - ➕ Añadir cliente.

        - Una vez introducida la opción `1` el programa pedirá un nombre y una edad.
            - El nombre puede ser cualquier texto.
            - La edad tiene que ser un número entero mayor que 0. Si el valor introducido no es válido se repetirá la petición de la edad.
        - Cada cliente tendrá un id generado incrementalmente por el programa. Dicho id será el número que sigue al máximo de todos los ids de los clientes existentes en ese momento.
        - Finalmente se almacenará el cliente, se enviará un mensaje y se preguntará si quiere añadir otro:

            ```
            > 1
            Nombre: Juan
            Edad: 22
            Cliente añadido exitosamente.
            
            ¿Añadir otro? (s/n): 
            ```

            - Si la opción introducida es distinta de `s` o `n` se repetirá la pregunta.
            - Si la opción introducida es `s` se repetirá la petición de datos para un nuevo cliente.
            - Si la opción introducida es `n` se volverá al menú.

    - 🔎 Buscar clientes.

        - Una vez introducida la opción `2` se imprimirá lo siguiente:

            ```
            > 2
            🔎🔎🔎 Búsqueda de clientes 🔎🔎🔎
            ▫️Los filtros se separan por ";".
            ▫️"exit" para salir.
            
            --- Tipos de filtros ---
            id:<id>
            name:<name part>
            age:<age>
            min:<id|name|age>
            max:<id|name|age>
            
            > 
            ```

        - Como indica el texto, el programa podrá filtrar clientes mediante unos filtros que se pedirán por consola siguiendo el formato indicado.
        - Si se introduce `exit` en vez de un filtro, se volverá al menú principal.
        - Ejemplos de filtros:
            - `id:2` ➡️ clientes cuyo id sea 2.
            - `name:Juan` ➡️ clientes cuyo nombre contenga "Juan".
            - `name:a` ➡️ clientes cuyo nombre contenga "a".
            - `age:22` ➡️ clientes cuya edad sea 22.
            - `min:id` ➡️ el cliente de menor id.
            - `max:age` ➡️ el cliente de mayor edad.
            - `name:an;age:22;max:id` ➡️ el cliente cuyo nombre contenga "a", cuya edad sea 22 y cuyo id sea el mayor.
        - Si no se proporciona un filtro o es inválido no se aplicará ningún filtro.
        - Cada vez que se introduzcan los filtros se imprimirán por consola los clientes filtrados y se volverá a pedir otro filtro.
            - Por ejemplo, tenemos los siguientes clientes almacenados:

                ```
                [
                    {'id': 1, 'name': 'Juan', 'age': 22},
                    {'id': 2, 'name': 'María', 'age': 43},
                    {'id': 3, 'name': 'Alberto', 'age': 35},
                    {'id': 4, 'name': 'Ana', 'age': 22}
                ]
                ```
            
            - Si se envía un filtro vacío o inválido:

                ```
                > 
                {'id': 1, 'name': 'Juan', 'age': 22}
                {'id': 2, 'name': 'María', 'age': 43}
                {'id': 3, 'name': 'Alberto', 'age': 35}
                {'id': 4, 'name': 'Ana', 'age': 22}
                ```
            
            - Otros ejemplos de filtros:

                ```
                > id:2
                {'id': 2, 'name': 'María', 'age': 43}
                ```

                ```
                > name:Juan
                {'id': 1, 'name': 'Juan', 'age': 22}
                ```

                ```
                > name:a
                {'id': 1, 'name': 'Juan', 'age': 22}
                {'id': 2, 'name': 'María', 'age': 43}
                {'id': 4, 'name': 'Ana', 'age': 22}
                ```

                ```
                > age:22
                {'id': 1, 'name': 'Juan', 'age': 22}
                {'id': 4, 'name': 'Ana', 'age': 22}
                ```

                ```
                > min:id
                {'id': 1, 'name': 'Juan', 'age': 22}
                ```

                ```
                > max:age
                {'id': 2, 'name': 'María', 'age': 43}
                ```

                ```
                > name:a;age:22;max:id
                {'id': 4, 'name': 'Ana', 'age': 22}
                ```

    - 🔄️ Actualizar cliente.

        - Una vez introducida la opción `3` el programa pedirá un id.
            - Si el valor introducido no es un número entero se repetirá la petición.
        - Si el id introducido no existe se enviará un mensaje y se esperará a que el usuario esté listo para volver al menú mediante otro `input()`:

            ```
            > 3
            Id: 345
            Cliente no encontrado.
            
            Presione ENTER para volver al menú...
            ```

        - Si el id existe: como cuando añadimos un cliente, se pedirán nombre y edad.
            - El nombre puede ser cualquier texto.
            - La edad tiene que ser un número entero mayor que 0. Si el valor introducido no es válido se repetirá la petición de la edad.
        - Una vez introducidos los datos correctamente se actualizarán los datos el cliente, se enviará un mensaje de éxito y se esperará a que el usuario esté listo para volver al menú mediante otro `input()`:

            ```
            > 3
            Id: 2
            Nombre: Alberto
            Edad: 35
            Cliente actualizado exitosamente.
                
            Presione ENTER para volver al menú...
            ```

    - 🗑️ Eliminar cliente.

        - Una vez introducida la opción `4` el programa pedirá un id.
            - Si el valor introducido no es un número entero se repetirá la petición.
        - Si el id introducido no existe se enviará un mensaje y se esperará a que el usuario esté listo para volver al menú mediante otro `input()`:

            ```
            > 4
            Id: 345
            Cliente no encontrado.
            
            Presione ENTER para volver al menú...
            ```

        - Si el id existe: se eliminará el cliente, se enviará un mensaje de éxito y se esperará a que el usuario esté listo para volver al menú mediante otro `input()`:

            ```
            > 4
            Id: 2
            Cliente eliminado exitosamente.
            
            Presione ENTER para volver al menú...
            ```

    - 🏃🏻 Salir.

        - Al introducir la opción `5` se terminará el programa.

    <br>

    <details>
    <summary>Solución</summary>

    ```python
    from collections.abc import Collection
    
    
    def add_client() -> None:
        id_ = max((client['id'] for client in clients), default=0)
    
        option = None
        while option != 'n':
            id_ += 1
            name = input('Nombre: ')
            age = age_input('Edad: ')
    
            clients.append({'id': id_, 'name': name, 'age': age})
            print('Cliente añadido exitosamente.\n')
            option = options_input('¿Añadir otro? (s/n): ', {'s', 'n'})
    
    
    def age_input(prompt: str) -> int:
        while True:
            try:
                age = int(input(prompt))
            except ValueError:
                pass
            else:
                if age > 0:
                    return age
    
    
    def client_index_by_id(id_: int) -> int | None:
        for i, client in enumerate(clients):
            if client['id'] == id_:
                return i
    
    
    def delete_client() -> None:
        id_ = int_input('Id: ')
        index = client_index_by_id(id_)
        if index is None:
            print('Cliente no encontrado.')
        else:
            del clients[index]
            print('Cliente eliminado exitosamente.')
    
        input('\nPresione ENTER para volver al menú...')
    
    
    def int_input(prompt: str) -> int:
        while True:
            try:
                option = int(input(prompt))
            except ValueError:
                pass
            else:
                return option
    
    
    def options_input(prompt: str, options: Collection[str]) -> str:
        option = None
        while option not in options:
            option = input(prompt)
    
        return option
    
    
    def search_clients() -> None:
        def search_clients_(filters: list[str]):
            filtered_clients = clients.copy()
            for filter_ in filters:
                filter_parts = filter_.split(':')
    
                match filter_parts:
                    case 'id' | 'age' as key, value:
                        try:
                            value = int(value)
                        except ValueError:
                            pass
                        else:
                            filtered_clients = [client for client in filtered_clients if client[key] == value]
                    case 'name', name:
                        filtered_clients = [client for client in filtered_clients if name in client['name']]
                    case 'min', 'id' | 'name' | 'age' as key if filtered_clients:
                        filtered_clients = [min(filtered_clients, key=lambda client: client[key])]
                    case 'max', 'id' | 'name' | 'age' as key if filtered_clients:
                        filtered_clients = [max(filtered_clients, key=lambda client: client[key])]
    
            for client in filtered_clients:
                print(client)
            print()
    
        print('🔎🔎🔎 Búsqueda de clientes 🔎🔎🔎\n'
              '▫️Los filtros se separan por ";".\n'
              '▫️"exit" para salir.\n'
              '\n--- Tipos de filtros ---\n'
              'id:<id>\n'
              'name:<name part>\n'
              'age:<age>\n'
              'min:<id|name|age>\n'
              'max:<id|name|age>\n')
    
        option = input('> ')
        while option != 'exit':
            search_clients_(option.split(';'))
            option = input('> ')
    
    
    def update_client() -> None:
        id_ = int_input('Id: ')
        index = client_index_by_id(id_)
        if index is None:
            print('Cliente no encontrado.')
        else:
            name = input('Nombre: ')
            age = age_input('Edad: ')
            clients[index]['name'] = name
            clients[index]['age'] = age
            print('Cliente actualizado exitosamente.')
    
        input('\nPresione ENTER para volver al menú...')
    
    
    clients: list[dict] = []
    print('Bienvenido al gestor de clientes.')
    
    while True:
        print(f'\n----- Menú -----\n'
              f'1. ➕ Añadir cliente.\n'
              f'2. 🔎 Buscar clientes.\n'
              f'3. 🔄️ Actualizar cliente.\n'
              f'4. 🗑️ Eliminar cliente.\n'
              f'5. 🏃🏻 Salir.\n')
    
        match input('> '):
            case '1':
                add_client()
            case '2':
                search_clients()
            case '3':
                update_client()
            case '4':
                delete_client()
            case '5':
                break
    ```

    </details>

<br>

## Clases

### Ejercicios:

1. ☠️ Vehículos.

    Construir con clases el siguiente escenario:

    1. Utilizar anotaciones de tipos para los parámetros de los métodos y para los valores de retorno.
    2. Una clase `Person`:
        1. Atributo `name` que siempre tiene que tener la primera en mayúscula y el resto en minúscula aunque el usuario introduzca el nombre mal.
        2. Atributo `age`.
        3. Sobrecargar los métodos necesarios para imprimir bonitos los objetos de la clase por consola en todo momento.
    3. Clases `Vehicle`, `Car` y `Train`:
        1. Usar clases abstractas si es necesario.
        2. Las 3 clases tienen que tener estos atributos:
            1. `max_passenger`: número máximo de pasajeros.
            2. `plate`: matrícula de tipo **cadena (`str`)** que, por defecto, si no se introduce nada va a ser un número entre 1111 y 9999 almacenado como texto (es el único parámetro con valor por defecto del ejercicio).
            3. `_passengers`: un **conjunto** de pasajeros que inicialmente está vacío y no debe nunca sobrepasar el límite. No se puede acceder a este atributo desde fuera de la clase.
        3. La clase `Car` tiene, además, los atributos `doors`, `airbags` y `wheel_drive`. Este último es el tipo de tracción y solo tiene dos opciones: front y rear (delantera y trasera).
        4. La clase `Train` tiene, además, un atributo `wagons`.
        5. Un propiedad `passengers` para acceder a `_passengers`.
        6. El resultado de sumar dos vehículos con `+` es un nuevo vehículo con los **atributos del primero** y **los pasajeros de ambos**. Los dos vehículos originales se vaciarán de pasajeros.
        7. `len()` devolverá el número de pasajeros.
        8. Sobrecargar `__iter__` para hacer la clase iterable de forma que se iteren sobre los pasajeros y, estos, sean devueltos uno a uno.
        9. Sobrecargar los métodos necesarios para imprimir bonitos los objetos de la clase por consola en todo momento.
        10. Un método `add_passenger()` que reciba un pasajero por parámetro y lo añada, si puede. Si no, tiene que lanzar un `ValueError`.
        11. Un método `first_passenger()` que reciba una función de un parámetro y devuelva un booleano. `first_passenger()` tiene que devolver el primer pasajero que la cumpla con la función recibida.
        12. Un método `empty()` que vacíe el conjunto de los pasajeros y los devuelva hacia fuera de la función.
        13. Un método `remove_passenger()` que reciba un pasajero por parámetro y lo descarte del conjunto. Si no está no da error.
        14. Un método `remove_passenger_by_name()` que reciba por parámetro un nombre de un posible pasajero y lo elimine sin dar error.
    4. Crear un vehículo cualquiera, intentar añadirle más personas del máximo, controlar el error e imprimir algo por consola indicando que se ha controlado con éxito.

    <br>

    <details>
    <summary>Solución</summary>

    ```python
    from __future__ import annotations
    
    """
    ⬆️
    In some future version this import will not be necessary. This is needed for now to be able to use a class as a type hint within
    itself (before it was defined):
    
    class Vehicle:
        ...                           ⬇️
        def __add__(self, other) -> Vehicle:
            ...
    
    If not, they can be indicated with quotes:
    
    class Vehicle:
        ...                            ⬇️
        def __add__(self, other) -> 'Vehicle':
            ...   
    """
    
    import random
    from abc import ABC, abstractmethod
    from collections.abc import Callable
    from enum import Enum, auto
    from typing import Iterator
    
    
    class WheelDrive(Enum):
        FRONT = auto()
        REAR = auto()
    
    
    class Person:
        def __init__(self, name: str, age: int) -> None:
            self.name = name.capitalize()
            self.age = age
    
        def __repr__(self) -> str:
            return f'{self.name} ({self.age})'
    
    
    class Vehicle(ABC):
        @abstractmethod
        def __init__(self, max_passengers: int, plate: str = None) -> None:
            self.max_passengers = max_passengers
            self.plate = plate if plate else str(random.randint(1111, 9999))
            self._passengers = set()
    
        def __add__(self, other) -> Vehicle:
            new_vehicle = type(self)(**{k: v for k, v in vars(self).items() if k not in ('plate', '_passengers')})
            for passenger in self.empty() | other.empty():
                new_vehicle.add_passenger(passenger)
    
            return new_vehicle
    
        def __iter__(self) -> Iterator[Person]:
            yield from self.passengers
    
        def __len__(self) -> int:
            return len(self.passengers)
    
        def __str__(self) -> str:
            return f'{type(self).__name__} ({self.plate}). Passengers: {self.passengers}'
    
        def add_passenger(self, passenger: Person) -> None:
            if len(self.passengers) >= self.max_passengers:
                raise ValueError('Full vehicle')
    
            self._passengers.add(passenger)
    
        def first_passenger(self, condition: Callable) -> Person:
            return next(passenger for passenger in self.passengers if condition(passenger))
    
        def empty(self) -> set[Person]:
            passengers = self.passengers.copy()
            self._passengers.clear()
            return passengers
    
        @property
        def passengers(self) -> set[Person]:
            return self._passengers
    
        def remove_passenger(self, passenger: Person) -> None:
            self._passengers.discard(passenger)
    
        def remove_passenger_by_name(self, name: str) -> None:
            try:
                self.remove_passenger(self.first_passenger(lambda passenger: passenger.name.lower() == name.lower()))
            except StopIteration:
                pass
    
    
    class Car(Vehicle):
        def __init__(self, doors: int, airbags: int, wheel_drive: WheelDrive, max_passengers: int, plate: str = None) -> None:
            super().__init__(max_passengers, plate)
            self.doors = doors
            self.airbags = airbags
            self.wheel_drive = wheel_drive
    
    
    class Train(Vehicle):
        def __init__(self, wagons: int, max_passengers: int, plate: str = None) -> None:
            super().__init__(max_passengers, plate)
            self.wagons = wagons
    
    
    jorge = Person('Jorge', 24)
    victoria = Person('Victoria', 21)
    javier = Person('Javier', 77)
    elena = Person('Elena', 42)
    
    car = Car(5, 2, WheelDrive.FRONT, 3)
    
    car.add_passenger(jorge)
    car.add_passenger(victoria)
    car.add_passenger(javier)
    
    try:
        car.add_passenger(elena)
    except ValueError:
        print('ValueError controlado con éxito.')
    ```

    </details>

<br>

## Estructuras de datos

### Ejercicios:

1. ☠️ Lista enlazada.

    Crear una lista enlazada con clases:

    1. Llamar a la clase `LinkedList`.
    2. Utilizar anotaciones de tipos para los parámetros de los métodos y para los valores de retorno.
    3. Sobrecargar los métodos necesarios para imprimir bonitas las listas listas enlazadas según el siguiente formato:
        1. Lista vacía: `<>`
        2. Lista con un elemento `'a'`: `<'a'>`
        3. Lista con los elementos `1`, `2`, `3` y `'hello'`: `<1, 2, 3, 'hello'>`.
    4. Sobrecargar el método necesario para hacer la clase iterable.
    5. Sobrecargar el método necesario para que la [función integrada](https://docs.python.org/3/library/functions.html) `len()` devuelva el número de elementos que contiene la lista enlazada.
    6. Método `add(...)` para añadir elementos a la lista.
    7. Método `get(...)` para obtener el elemento en una posición concreta. Lanza un `IndexError` si el índice dado por argumento es menor que 0 o mayor que el número de elementos contenidos en la lista.
    8. Método `delete(...)` para eliminar el elemento en una posición concreta. Lanza un `IndexError` si el índice dado por argumento es menor que 0 o mayor que el número de elementos contenidos en la lista.
    9. Método `insert(...)` para insertar un elemento en una posición concreta. No lanza excepciones. Si el índice es menor que 0 se inserta al inicio y, si es mayor que el número de elementos, se inserta al final.
    10. Método `clear(...)` para vaciar la lista enlazada.

    <br>

    Puedes servirte de la siguiente función para ejecutar pruebas. Si esta función imprime en la consola `OK`, el ejercicio estará realizado con éxito:

    ```python
    def run_tests() -> None:
        ll = LinkedList()
        assert str(ll) == '<>'
        assert len(ll) == 0
    
        ll.add(1)
        assert str(ll) == '<1>'
        ll.add(2)
        assert str(ll) == '<1, 2>'
        ll.add(3)
        assert str(ll) == '<1, 2, 3>'
        assert len(ll) == 3
    
        assert 1 in ll
        assert 2 in ll
        assert 3 in ll
        assert 4 not in ll
    
        try:
            ll.delete(-1)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.delete(3)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.delete(24)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        ll.delete(2)
        assert str(ll) == '<1, 2>'
        assert len(ll) == 2
    
        ll.add('aasdasd')
        assert str(ll) == '<1, 2, aasdasd>'
    
        assert ll.get(1) == 2
        assert ll.get(2) == 'aasdasd'
        try:
            ll.get(-1)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.get(3)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.get(24)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
    
        ll.add(('5', 5))
        assert str(ll) == "<1, 2, aasdasd, ('5', 5)>"
        assert len(ll) == 4
        ll.delete(1)
        assert str(ll) == "<1, aasdasd, ('5', 5)>"
        ll.delete(0)
        assert str(ll) == "<aasdasd, ('5', 5)>"
        ll.delete(0)
        assert str(ll) == "<('5', 5)>"
        assert len(ll) == 1
        ll.delete(0)
        assert str(ll) == '<>'
        assert len(ll) == 0
        ll.clear()
        assert str(ll) == '<>'
        assert len(ll) == 0
        ll.add(5)
        ll.add(5)
        ll.add(5)
        assert str(ll) == '<5, 5, 5>'
        assert len(ll) == 3
        ll.clear()
        assert str(ll) == '<>'
        assert len(ll) == 0
    
        ll.insert(-1, 'a')
        assert str(ll) == '<a>'
        assert len(ll) == 1
        ll.clear()
        assert len(ll) == 0
        ll.insert(24, 'b')
        assert str(ll) == '<b>'
        assert len(ll) == 1
        ll.clear()
        ll.insert(0, 'c')
        assert str(ll) == '<c>'
        assert len(ll) == 1
        ll.clear()
        ll.add('hola')
        ll.insert(-1, 'x')
        assert str(ll) == '<x, hola>'
        assert len(ll) == 2
        ll.delete(0)
        ll.insert(24, 'y')
        assert str(ll) == '<hola, y>'
        assert len(ll) == 2
        ll.delete(1)
        ll.insert(0, 'z')
        assert str(ll) == '<z, hola>'
        assert len(ll) == 2
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.insert(2, 'adios')
        assert str(ll) == '<z, hola, adios, 1, 2, 3>'
        assert len(ll) == 6
        ll.insert(len(ll), 'ultimo')
        ll.insert(len(ll) - 1, 'penultimo')
        ll.insert(len(ll) - 2, 'antepenultimo')
        assert str(ll) == '<z, hola, adios, 1, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 9
        ll.insert(4, {1, 2})
        assert str(ll) == '<z, hola, adios, 1, {1, 2}, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 10
        ll.insert(1, range(5))
        assert str(ll) == '<z, range(0, 5), hola, adios, 1, {1, 2}, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 11
    
        print('OK')
    ```

    <details>
    <summary>Solución</summary>

    ```python
    from typing import Any, Iterator
    
    
    class Node:
        def __init__(self, value) -> None:
            self.value: Any = value
            self.next: Node | None = None
    
    
    class LinkedList:
        def __init__(self) -> None:
            self.root: Node | None = None
            self.last: Node | None = self.root
            self._length = 0
    
        def __iter__(self) -> Iterator[Node]:
            node = self.root
            while node:
                yield node.value
                node = node.next
    
        def __len__(self) -> int:
            return self._length
    
        def __str__(self) -> str:
            return f"<{', '.join(str(value) for value in self)}>"
    
        def _get_node(self, index: int) -> Node:
            if index >= self._length:
                return self.last
    
            node = self.root
            for _ in range(index):
                node = node.next
            return node
    
        def add(self, value: Any) -> None:
            if self.last is None:
                self.root = Node(value)
                self.last = self.root
            else:
                self.last.next = Node(value)
                self.last = self.last.next
            self._length += 1
    
        def clear(self) -> None:
            self.root = None
            self.last = self.root
            self._length = 0
    
        def delete(self, index: int) -> None:
            if not 0 <= index < self._length:
                raise IndexError
    
            if index == 0:
                try:
                    self.root = self.root.next
                except AttributeError:
                    self.root = None
                    self.last = self.root
                self._length -= 1
            else:
                previous_node = self._get_node(index - 1)
                if previous_node.next and previous_node.next.next:
                    previous_node.next = previous_node.next.next
                else:
                    previous_node.next = None
                    self.last = previous_node
                self._length -= 1
    
        def get(self, index: int) -> Any:
            if not 0 < index < self._length:
                raise IndexError
    
            return self._get_node(index).value
    
        def insert(self, index: int, value: Any) -> None:
            if self._length == 0:
                self.add(value)
            else:
                if index <= 0:
                    node = Node(value)
                    node.next = self.root
                    self.root = node
                else:
                    node = self._get_node(index - 1)
                    next_node = node.next
                    node.next = Node(value)
                    node.next.next = next_node
                self._length += 1
    
    
    def run_tests() -> None:
        ll = LinkedList()
        assert str(ll) == '<>'
        assert len(ll) == 0
    
        ll.add(1)
        assert str(ll) == '<1>'
        ll.add(2)
        assert str(ll) == '<1, 2>'
        ll.add(3)
        assert str(ll) == '<1, 2, 3>'
        assert len(ll) == 3
    
        assert 1 in ll
        assert 2 in ll
        assert 3 in ll
        assert 4 not in ll
    
        try:
            ll.delete(-1)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.delete(3)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.delete(24)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        ll.delete(2)
        assert str(ll) == '<1, 2>'
        assert len(ll) == 2
    
        ll.add('aasdasd')
        assert str(ll) == '<1, 2, aasdasd>'
    
        assert ll.get(1) == 2
        assert ll.get(2) == 'aasdasd'
        try:
            ll.get(-1)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.get(3)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
        try:
            ll.get(24)
        except IndexError:
            pass
        else:
            raise Exception('No lanza IndexError')
    
        ll.add(('5', 5))
        assert str(ll) == "<1, 2, aasdasd, ('5', 5)>"
        assert len(ll) == 4
        ll.delete(1)
        assert str(ll) == "<1, aasdasd, ('5', 5)>"
        ll.delete(0)
        assert str(ll) == "<aasdasd, ('5', 5)>"
        ll.delete(0)
        assert str(ll) == "<('5', 5)>"
        assert len(ll) == 1
        ll.delete(0)
        assert str(ll) == '<>'
        assert len(ll) == 0
        ll.clear()
        assert str(ll) == '<>'
        assert len(ll) == 0
        ll.add(5)
        ll.add(5)
        ll.add(5)
        assert str(ll) == '<5, 5, 5>'
        assert len(ll) == 3
        ll.clear()
        assert str(ll) == '<>'
        assert len(ll) == 0
    
        ll.insert(-1, 'a')
        assert str(ll) == '<a>'
        assert len(ll) == 1
        ll.clear()
        assert len(ll) == 0
        ll.insert(24, 'b')
        assert str(ll) == '<b>'
        assert len(ll) == 1
        ll.clear()
        ll.insert(0, 'c')
        assert str(ll) == '<c>'
        assert len(ll) == 1
        ll.clear()
        ll.add('hola')
        ll.insert(-1, 'x')
        assert str(ll) == '<x, hola>'
        assert len(ll) == 2
        ll.delete(0)
        ll.insert(24, 'y')
        assert str(ll) == '<hola, y>'
        assert len(ll) == 2
        ll.delete(1)
        ll.insert(0, 'z')
        assert str(ll) == '<z, hola>'
        assert len(ll) == 2
        ll.add(1)
        ll.add(2)
        ll.add(3)
        ll.insert(2, 'adios')
        assert str(ll) == '<z, hola, adios, 1, 2, 3>'
        assert len(ll) == 6
        ll.insert(len(ll), 'ultimo')
        ll.insert(len(ll) - 1, 'penultimo')
        ll.insert(len(ll) - 2, 'antepenultimo')
        assert str(ll) == '<z, hola, adios, 1, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 9
        ll.insert(4, {1, 2})
        assert str(ll) == '<z, hola, adios, 1, {1, 2}, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 10
        ll.insert(1, range(5))
        assert str(ll) == '<z, range(0, 5), hola, adios, 1, {1, 2}, 2, 3, antepenultimo, penultimo, ultimo>'
        assert len(ll) == 11
    
        print('OK')
    
    
    run_tests()
    ```

    </details>

<br>

## Algoritmos avanzados

### Ejercicios:

1. ☠️☠️☠️ Rascacielos.

    Este ejercicio se basa en el famoso juego de los rascacielos. Este juego tipo puzle tiene similitudes con el sudoku a la hora de colocar los rascacielos en cada celda pero también juega con la perspectiva, es decir, es importante tener en cuenta la cantidad de rascacielos que se pueden ver desde cada lado del tablero.

    La siguiente imagen muestra el inicio del juego, el tablero sin resolver:

   ![skyscraper.png](md_images/skyscraper.png)

    En este caso la partida es de `4x4` pero podría tener cualquier tamaño `nxn`. Al ser de tamaño `4`, los rascacielos que podremos colocar tendrán una altura entre `1` y `4` (inclusive).

    No podremos colocar dos rascacielos de la misma altura en una misma fila o columna.

    Los números que aparecen fuera del tablero indican el número de rascacielos que se verían desde esa posición. Vamos a ver la solución de este tablero para tenerlo más claro:

   ![skyscraper_solution.png](md_images/skyscraper_solution.png)

    Los rascacielos altos tapan a los más bajos cuando los miramos desde cierto lado.

    Fijémonos en la tercera columna: como arriba tiene un `4` (el número fuera del tablero), eso significa que en esa columna, desde arriba hacia abajo, se pueden ver todos los rascacielos desde altura `1` hasta `4`, o sea, cuatro rascacielos. Y si miramos en el número de abajo de la misma columna nos daremos cuenta de que es un `1`, porque solo podríamos ver un rascacielos, el de altura `4`, tapando los de altura `3`, `2` y `1`.

    Entonces, cumpliendo las reglas indicadas en el exterior de tablero y teniendo en cuenta que no se pueden colocar dos rascacielos de misma altura en una misma fila o columna: crear una función `skyscrapers(...)` que reciba las reglas de cada lado del tablero de cualquier tamaño `nxn` en el orden **arriba**, **abajo**, **izquierda** y **derecha** mediante cuatro listas como argumentos y que devuelva una lista de listas representando el tablero resuelto relleno con los números que simbolizan los rascacielos de altura `1` hasta `n`. En el caso de no existir solución posible al tablero con las reglas propuestas, la función debe devolver `None`.

    Con el tablero del ejemplo sería así:

    `skyscrapers([3, 2, 4, 1], [2, 2, 1, 2], [3, 2, 1, 3], [1, 3, 3, 2])` ➡️ `[[2, 3, 1, 4], [3, 4, 2, 1], [4, 1, 3, 2], [1, 2, 4, 3]]`

    Si cambiáramos en las reglas el primer `3` por un `2`, la partida no tendría solución, entonces:

    `skyscrapers([2, 2, 4, 1], [2, 2, 1, 2], [3, 2, 1, 3], [1, 3, 3, 2])` ➡️ `None`

    <br>

    A continuación se proporcionará una función que ejecuta casos de pruebas para tableros desde tamaño `1x1` hasta `6x6`. Está ofuscada para evitar confusiones y sacar ideas involuntariamente para el ejercicio. Si esta función imprime en la consola `OK`, el ejercicio estará realizado con éxito:

    ```python
    def run_tests() -> None:
        def _1(_11, _1001, _1100101, _0011):
            def _10(_00011):
                _0101011 = range
                _010111 = reversed
    
                def _10101(_1011001):
                    _101 = 0
                    _111000 = 0
                    for _10110 in _1011001:
                        if _10110 > _101:
                            _111000 += 1
                            _101 = _10110
                    return _111000
    
                _010101 = enumerate
                _000101 = len
                for _01100, _01 in _010101(_00011):
                    for _1011, _00011110 in _010101(_01):
                        _11110 = 0
                        for _111 in _0101011(_000101(_00011)):
                            if _111 != _1011 and _00011[_01100][_111] == _00011110 or _111 != _01100 and _00011[_111][_1011] == _00011110:
                                _11110 = 1
                                break
                        _11000 = [_000[_1011] for _000 in _00011]
                        _011001 = ((0 in _11000 or _10101(_11000) == _11[_1011] and _10101(_010111(_11000)) == _1001[_1011]) and
                                   (0 in _00011[_01100] or _10101(_00011[_01100]) == _1100101[_01100] and _10101(_010111(_00011[_01100])) == _0011[_01100]))
                        if _11110 or not _011001:
                            return 0
                return 1
    
            if (_0111000 := skyscrapers(_11, _1001, _1100101, _0011)) is None:
                raise ValueError(f'skyscrapers returns None with rules {_11} {_1001} {_1100101} {_0011}')
            assert _10(_0111000)
    
        _1([1], [1], [1], [1])
        assert skyscrapers([1], [1], [2], [1]) is None
        _1([2, 1], [1, 2], [2, 1], [1, 2])
        assert skyscrapers([2, 1], [1, 2], [1, 2], [2, 1]) is None
        _1([3, 2, 4, 1], [2, 2, 1, 2], [3, 2, 1, 3], [1, 3, 3, 2])
        assert skyscrapers([3, 2, 4, 1], [2, 2, 2, 2], [3, 2, 1, 3], [1, 3, 3, 2]) is None
        _1([3, 2, 1, 2, 3], [1, 2, 3, 3, 2], [3, 2, 2, 3, 1], [3, 4, 2, 1, 3])
        assert skyscrapers([3, 1, 1, 2, 3], [1, 1, 3, 3, 2], [3, 2, 2, 3, 1], [3, 4, 2, 1, 3]) is None
        _1([3, 2, 3, 1, 2, 3], [3, 1, 2, 3, 4, 3], [3, 3, 1, 2, 3, 2], [2, 2, 3, 1, 4, 5])
        assert skyscrapers([3, 2, 3, 1, 2, 3], [3, 1, 2, 3, 4, 3], [2, 3, 5, 2, 3, 2], [2, 2, 3, 1, 4, 5]) is None
        
        print('OK')
    ```

    <details>
    <summary>Solución</summary>

    ```python
    from collections.abc import Iterable


    def calculate_solution(
        row_index: int,
        column_index: int,
        up_rules: list[int],
        down_rules: list[int],
        left_rules: list[int],
        right_rules: list[int],
        board: list[list[int]]
    ) -> bool:
        if not (position := next_available_position(row_index, column_index, board)):
            return True
    
        row_index, column_index = position
    
        for i in range(1, len(board) + 1):
            board[row_index][column_index] = i
            if (
                not number_in_cross(i, row_index, column_index, board)
                and
                check_rules(row_index, column_index, up_rules, down_rules, left_rules, right_rules, board)
                and
                calculate_solution(row_index, column_index, up_rules, down_rules, left_rules, right_rules, board)
            ):
                return True
    
        board[row_index][column_index] = 0
        return False
    
    
    def check_rules(
        row_index: int,
        column_index: int,
        up_rules: list[int],
        down_rules: list[int],
        left_rules: list[int],
        right_rules: list[int],
        board: list[list[int]]
    ) -> bool:
        column = get_column(column_index, board)
        return (
            (
                0 in column
                or
                n_sees(column) == up_rules[column_index]
                and
                n_sees(reversed(column)) == down_rules[column_index]
            )
            and
            (
                0 in board[row_index]
                or
                n_sees(board[row_index]) == left_rules[row_index]
                and
                n_sees(reversed(board[row_index])) == right_rules[row_index]
            )
        )
    
    
    def get_column(column_index: int, board: list[list[int]]) -> list[int]:
        return [row[column_index] for row in board]
    
    
    def fill_column_decrement(column_index: int, board: list[list[int]]) -> None:
        for i, row in enumerate(board):
            row[column_index] = len(board) - i
    
    
    def fill_column_increment(column_index: int, board: list[list[int]]) -> None:
        for i, row in enumerate(board, start=1):
            row[column_index] = i
    
    
    def n_sees(numbers: Iterable[int]) -> int:
        max_ = 0
        n_sees_ = 0
        for number in numbers:
            if number > max_:
                n_sees_ += 1
                max_ = number
    
        return n_sees_
    
    
    def next_available_position(row_index: int, column_index: int, board: list[list[int]]) -> tuple[int, int] | None:
        i = row_index
        j = column_index
        while i < len(board):
            while j < len(board):
                if not board[i][j]:
                    return i, j
                j += 1
            i += 1
            j = 0
    
    
    def number_in_cross(number: int, row_index: int, column_index: int, board: list[list[int]]) -> bool:
        for i in range(len(board)):
            if i != column_index and board[row_index][i] == number or i != row_index and board[i][column_index] == number:
                return True
    
        return False
    
    
    def put_init_values(up_rules, down_rules, left_rules, right_rules, board) -> None:
        for i in range(len(board)):
            if up_rules[i] == 1:
                board[0][i] = len(board)
            if up_rules[i] == len(board):
                fill_column_increment(i, board)
            if down_rules[i] == 1:
                board[len(board) - 1][i] = len(board)
            if down_rules[i] == len(board):
                fill_column_decrement(i, board)
            if left_rules[i] == 1:
                board[i][0] = len(board)
            if left_rules[i] == len(board):
                board[i] = list(range(1, len(board) + 1))
            if right_rules[i] == 1:
                board[i][len(board) - 1] = len(board)
            if right_rules[i] == len(board):
                board[i] = list(range(len(board), 0, -1))
    
    
    def skyscrapers(
        up_rules: list[int],
        down_rules: list[int],
        left_rules: list[int],
        right_rules: list[int]
    ) -> list[list[int]] | None:
        board = [[0] * len(up_rules) for _ in range(len(up_rules))]
    
        put_init_values(up_rules, down_rules, left_rules, right_rules, board)
    
        if (
            valid_board(up_rules, down_rules, left_rules, right_rules, board)
            and
            calculate_solution(0, 0, up_rules, down_rules, left_rules, right_rules, board)
        ):
            return board
    
    
    def valid_board(
        up_rules: list[int],
        down_rules: list[int],
        left_rules: list[int],
        right_rules: list[int],
        board: list[list[int]]
    ) -> bool:
        for i, row in enumerate(board):
            for j, number in enumerate(row):
                if (
                    number
                    and
                    (
                        number_in_cross(number, i, j, board)
                        or
                        not check_rules(i, j, up_rules, down_rules, left_rules, right_rules, board)
                    )
                ):
                    return False
    
        return True
    
    
    def run_tests() -> None:
        def _1(_11, _1001, _1100101, _0011):
            def _10(_00011):
                _0101011 = range
                _010111 = reversed
    
                def _10101(_1011001):
                    _101 = 0
                    _111000 = 0
                    for _10110 in _1011001:
                        if _10110 > _101:
                            _111000 += 1
                            _101 = _10110
                    return _111000
    
                _010101 = enumerate
                _000101 = len
                for _01100, _01 in _010101(_00011):
                    for _1011, _00011110 in _010101(_01):
                        _11110 = 0
                        for _111 in _0101011(_000101(_00011)):
                            if _111 != _1011 and _00011[_01100][_111] == _00011110 or _111 != _01100 and _00011[_111][_1011] == _00011110:
                                _11110 = 1
                                break
                        _11000 = [_000[_1011] for _000 in _00011]
                        _011001 = ((0 in _11000 or _10101(_11000) == _11[_1011] and _10101(_010111(_11000)) == _1001[_1011]) and
                                   (0 in _00011[_01100] or _10101(_00011[_01100]) == _1100101[_01100] and _10101(_010111(_00011[_01100])) == _0011[_01100]))
                        if _11110 or not _011001:
                            return 0
                return 1
    
            if (_0111000 := skyscrapers(_11, _1001, _1100101, _0011)) is None:
                raise ValueError(f'skyscrapers returns None with rules {_11} {_1001} {_1100101} {_0011}')
            assert _10(_0111000)
    
        _1([1], [1], [1], [1])
        assert skyscrapers([1], [1], [2], [1]) is None
        _1([2, 1], [1, 2], [2, 1], [1, 2])
        assert skyscrapers([2, 1], [1, 2], [1, 2], [2, 1]) is None
        _1([3, 2, 4, 1], [2, 2, 1, 2], [3, 2, 1, 3], [1, 3, 3, 2])
        assert skyscrapers([3, 2, 4, 1], [2, 2, 2, 2], [3, 2, 1, 3], [1, 3, 3, 2]) is None
        _1([3, 2, 1, 2, 3], [1, 2, 3, 3, 2], [3, 2, 2, 3, 1], [3, 4, 2, 1, 3])
        assert skyscrapers([3, 1, 1, 2, 3], [1, 1, 3, 3, 2], [3, 2, 2, 3, 1], [3, 4, 2, 1, 3]) is None
        _1([3, 2, 3, 1, 2, 3], [3, 1, 2, 3, 4, 3], [3, 3, 1, 2, 3, 2], [2, 2, 3, 1, 4, 5])
        assert skyscrapers([3, 2, 3, 1, 2, 3], [3, 1, 2, 3, 4, 3], [2, 3, 5, 2, 3, 2], [2, 2, 3, 1, 4, 5]) is None
    
        print('OK')
    
    
    run_tests()
    ```

    </details>
