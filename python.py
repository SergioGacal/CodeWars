def create_phone_number(n):
    if len(n) != 10:
        return "Error"
    numero_telefono =''.join(map(str, n))
    numero_formateado = '({}) {}-{}'.format(numero_telefono[:3], numero_telefono[3:6], numero_telefono[6:])
    
    return numero_formateado

def lovefunc( flower1, flower2 ):
    total = flower1 + flower2
    return total %2 != 0

def make_negative( number ):
    if number <=0:
        return number
    else:
        return -number

def summation(num):
    return sum(range(1, num + 1))

def zero_fuel(distance_to_pump, mpg, fuel_left):
        return mpg * fuel_left >= distance_to_pump

def century(year):
    if year % 100 ==0:
        return year // 100
    else: 
        return year // 100 + 1

def square_sum(numbers):
    resultado = 0
    for i in range(len(numbers)):
        resultado += (numbers[i] ** 2)
    return resultado

def solution(string):
    return string[::-1]

def fake_bin(x):
    y=""
    for a in x:
        if int(a) <5:
            y+="0"
        else:
            y+="1"
    return y

def sum_mix(arr):
    suma=0
    for a in arr:
        suma+=(int(a))
    return suma

def solution(text, ending):
    return text.endswith(ending)

def sum_array(a):
    return (sum(a))

def positive_sum(arr):
    snp=0
    for s in arr:
        if s >=0:
            snp +=s
    return snp

def basic_op(operator, value1, value2):
    resultado =0
    if operator == '+':
        resultado = value1+value2
    elif operator == '-':
        resultado = value1 - value2
    elif operator == '*':
        resultado = value1 * value2
    elif operator == '/':
        resultado = value1 / value2
    return resultado

def maps(a):
    return list(map(lambda x: x * 2, a))

def to_jaden_case(string):
    separo = string.split()
    mayuscula = [palabra.capitalize() for palabra in separo]
    return ' '.join(mayuscula)

def opposite(number):
  return -number

def no_space(x):
    resultado = ""
    for c in x:
        if c !=" ":
            resultado += c
    return resultado

def odd_or_even(arr):
    sum_of_elements = sum(arr)
    if sum_of_elements % 2 == 0:
        return "even"
    else:
        return "odd"

def add_binary(a,b):
    binario = bin(a+b)
    return binario[2:]

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0]+numbers[1]

def find_smallest_int(arr):
    arr.sort()
    return arr[0]

def grow(arr):
    res = 1
    for i in arr:
        res *=  i
    return res

def simple_multiplication(number) :
    if number % 2 == 1:
        return number * 9
    else:
        return number * 8

def greet():
    return "hello world!"

def square_digits(num):
    acum = ''
    txt = str(num)
    for i in txt:
        n=int(i)
        n=n*n
        acum += str(n)
    return int(acum)

def boolean_to_string(b):
    if b:
        return 'True'
    else:
        return 'False'

def dna_to_rna(dna):
    cad =''
    for i in dna:
        if i == 'T':
           cad += 'U'
        else:
            cad += i
    return cad

def is_isogram(string):
    mayus = string.upper()
    orden = ''.join(sorted(mayus))
    anterior = ''
    sum = 0
    for i in orden:
        if i != anterior:
            sum += 0
        else:
            sum += 1
        anterior = i
    if sum != 0:
        return False
    else:
        return True

def open_or_senior(data):
    output = []
    for i in data:
        categoria = ''
        if i[0] < 55:
            categoria = 'Open'
        else:
            if i[1] > 7:
                categoria = 'Senior'
            else:
                categoria = 'Open'
        output.append(categoria)
    return output

def high_and_low(numbers):
    elementos = numbers.split()
    min=elementos[0]
    max=elementos[0]
    for i in elementos:
        if int(i) < int(min):
            min = i
        if int(i) > int(max):
            max = i
    numbers = str(max)+ " " + str(min)
    return numbers

def binary_array_to_number(arr):
    binario=''
    for i in arr:
        binario += str(i)
    entero = int(binario,2)
    return entero

def repeat_str(repeat, string):
    texto = f'{string}'* int(repeat)
    return texto

def disemvowel(string_):
    vocales= 'aeiouAEIOU'
    for v in vocales:
        while (string_.count(v)) > 0:
            posborrar = string_.index(v)
            string_ = string_[:posborrar] +string_[posborrar+1:]
    return string_

def is_square(n):
    c=0
    resultado=False
    while c*c <= n:
        if c*c == n:
            resultado=True
        c=c+1
    return resultado

def count_sheeps(sheep):
    return sheep.count(True)

def count_by(x, n):
    valor=0
    resultado=[]
    for i in range(1,n+1):
        resultado.append(i*x)
    return resultado

def reverse_seq(n):
    resultado= []
    for i in range(n,0,-1):
        resultado.append(i)
    return resultado

def string_to_number(s):
    convierto= int(s)
    return convierto

def descending_order(num):
    t=str(num)
    r=''
    for i in range(9,-1,-1):
        q = t.count(str(i))
        r=r+str(i)*q
    return int(r)

def is_valid_walk(walk):
    if len(walk) == 10:
        n=walk.count('n')
        s=walk.count('s')
        e=walk.count('e')
        w=walk.count('w')
        if n-s == 0 and e-w ==0:
            return True
        else:
            return False
    return False

def find_it(seq):
    for i in seq:
        if seq.count(i)%2 != 0:
            return i

def tribonacci(signature, n):
    resultado=[]
    if n == 0:
        pass
    elif n == 1:
        resultado.append(signature[0])
    elif n == 2:
        resultado.append(signature[0])
        resultado.append(signature[1])
    else:
        e = len(signature)
        iteraciones=n-e
        resultado.append(signature[0])
        resultado.append(signature[1])
        resultado.append(signature[2])
        for i in range(1,n-2,1):
            resultado.append(resultado[i-1]+resultado[i]+resultado[i+1] )
    return resultado

def friend(x):
    nuevo =[]
    for i in x:
        print(len(i))
        if len(i) == 4:
            nuevo.append(i)
    return nuevo

def find_next_square(sq):
    raiz = 0
    while raiz * raiz < sq:
        raiz +=1
    if raiz * raiz == sq:
        raiz = raiz+1
        return raiz * raiz
    else:
        return -1

def remove_char(s):
    return s[1:len(s)-1]

def persistence(n):
    t=str(n)
    c=0
    while len(str(t)) !=1:
        c+=1
        resultado=1
        for i in t:
            resultado *= int(i)
        t = str(resultado)
    return c

def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 =='rock' and p2 == 'scissors' or p1 == 'scissors' and p2 == 'paper' or p1 == 'paper' and p2 == 'rock':
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'

def make_upper_case(s):
    return s.upper()

def expanded_form(num):
    txt=str(num)
    ceros=txt.count('0')
    salida=''
    contador=0
    for i in txt:
        contador+=1
        if i != '0' and salida =='':
            salida = str(i) + '0'*(len(txt)-contador)
        elif i != '0':
            salida = salida + ' + ' + str(i) + '0'*(len(txt)-contador)
    return salida

def count_sheep(n):
    salida=''
    for i in range(0,n,1):
        salida += f'{i+1} sheep...'
    return salida

def array_diff(a, b):
    for i in b:
        for j in range(0,a.count(i)):
            a.remove(i)
    return a

def get_grade(s1, s2, s3):
    promedio=(s1+s2+s3)/3
    if promedio >= 90:
        return 'A'
    elif promedio >= 80:
        return 'B'
    elif promedio >= 70:
        return 'C'
    elif promedio >= 60:
        return 'D'
    else:
        return "F"

def get_sum(a,b):
    mi=min(a,b)
    ma=max(a,b)
    if mi == ma:
        return mi
    else:
        suma=0
        for i in range(mi,ma+1,1):
            suma+=i
        return suma

def count_positives_sum_negatives(arr):
    positivo = 0
    negativo = 0
    resultado = []
    if arr == []:
        return resultado
    for i in arr:
        if i > 0:
            positivo += 1
        elif i < 0:
            negativo += i
    resultado.append(positivo)
    resultado.append(negativo)
    return resultado

def even_or_odd(number):
    if number %2 !=0:
        return 'Odd'
    else:
        return 'Even'

def digitize(n):
    txt=str(n)
    salida=[]
    for a in txt:
        salida.insert(0,int(a))
    return salida

def bmi(weight, height):
    mc=weight/(height*height)
    if mc <= 18.5:
        return 'Underweight'
    elif mc <= 25:
        return 'Normal'
    elif mc <= 30:
        return 'Overweight'
    elif mc > 30:
        return 'Obese'

def area_or_perimeter(l , w):
    if l == w:
        return l*w
    else:
        return 2*l+2*w

def double_integer(i):
    return 2*i

def min_max(lst):
    rta=[]
    mi = min(lst)
    ma = max(lst)
    rta.append(mi)
    rta.append(ma)
    return rta


def rental_car_cost(d):
    if d >=7:
        return (d*40)-50
    elif d >=3:
        return (d*40)-20
    else:
        return d*40

def tower_builder(n_floors):
    espacio = ' '
    asterisco = '*'
    respuesta = []
    ancho = n_floors + (n_floors-1)
    for i in range(n_floors,0,-1):
        variable=i-1
        espaciosPiso=(ancho-((i+(variable))))/2
        respuesta.insert(0,str(espacio)*int(espaciosPiso) + asterisco*(i+(variable))+str(espacio)*int(espaciosPiso))
    return respuesta

def quarter_of(month):
    if month <4:
        return 1
    elif month <7:
        return 2
    elif month <10:
        return 3
    else:
        return 4

def count(s):
    r ={}
    for i in s:
        if i not in r:
            r[i] = s.count(i)
    return r

def paperwork(n, m):
    if n <= 0 or m <= 0:
        return 0
    else:
        return n*m

def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    else:
        return False

def count_smileys(arr):
    respuesta = 0
    for i in arr:
        if len(i) == 2:
            if (i[0] == ':' or i[0] == ';') and (i[1] == ')' or i[1] == 'D'):
                respuesta += 1
        elif len(i) == 3:
            if (i[0] == ':' or i[0] == ';') and (i[1] == '-' or i[1] == '~') and (i[2] == ')' or i[2] == 'D'):
                respuesta += 1
    return respuesta

def are_you_playing_banjo(name):
    if name[0] == 'r' or name[0]== 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
    return name

def alphabet_position(text):
    salida= ''
    for i in text:
        if i == 'a' or i == 'A':
            salida = salida + " " + "1"
        elif i == 'b' or i == "B":
            salida = salida + " " + "2"
        elif i == 'c' or i == "C":
            salida = salida + " " + "3"
        elif i == 'd' or i == "D":
            salida = salida + " " + "4"    
        elif i == 'e' or i == "E":
            salida = salida + " " + "5"    
        elif i == 'f' or i == "F":
            salida = salida + " " + "6"
        elif i == 'g' or i == "G":
            salida = salida + " " + "7"
        elif i == 'h' or i == "H":
            salida = salida + " " + "8"
        elif i == 'i' or i == "I":
            salida = salida + " " + "9"
        elif i == 'j' or i == "J":
            salida = salida + " " + "10"
        elif i == 'k' or i == "K":
            salida = salida + " " + "11"
        elif i == 'l' or i == "L":
            salida = salida + " " + "12"
        elif i == 'm' or i == "M":
            salida = salida + " " + "13"
        elif i == 'n' or i == "N":
            salida = salida + " " + "14"
        elif i == 'o' or i == "O":
            salida = salida + " " + "15"
        elif i == 'p' or i == "P":
            salida = salida + " " + "16"
        elif i == 'q' or i == "Q":
            salida = salida + " " + "17"
        elif i == 'r' or i == "R":
            salida = salida + " " + "18"
        elif i == 's' or i == "S":
            salida = salida + " " + "19"
        elif i == 't' or i == "T":
            salida = salida + " " + "20"
        elif i == 'u' or i == "U":
            salida = salida + " " + "21"
        elif i == 'v' or i == "V":
            salida = salida + " " + "22"
        elif i == 'w' or i == "W":
            salida = salida + " " + "23"
        elif i == 'x' or i == "X":
            salida = salida + " " + "24"
        elif i == 'y' or i == "Y":
            salida = salida + " " + "25"
        elif i == 'z' or i == "Z":
            salida = salida + " " + "26"
    salida = salida[1:]
    return salida

def cockroach_speed(s):
    return int(s*1000)//36

def queue_time(customers, n):
    cajas = []
    turno = 0
    for i in range(1,n+1):
        cajas.append(0)
    while turno != len(customers):
        cajas[cajas.index(min(cajas))]+=customers[turno]
        customers[turno]
        turno+=1
    return max(cajas)

def feast(beast, dish):
    if beast[len(beast)-1:] == dish[len(dish)-1] and beast[0] == dish[0]:
        return True
    else:
        return False

def solution(s):
    salida=''
    for letra in s:
        if letra.isupper():
            salida += f' '+letra
        else:
            salida += letra
    return salida

def number_to_string(num):
    return str(num)

def is_pangram(s):
    mi=s.lower()
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for letra in letras:
        if letra not in mi:
            return False
    return True

def unique_in_order(sequence):
    letras = []
    resultado = []
    for i in sequence:
        letras.append(i)
    for i in range(len(letras)):
        actual = letras[i]
        if i > 0:
            anterior = letras[i - 1]
        else:
            anterior = None
        if i < len(letras) - 1:
            posterior = letras[i + 1]
        else:
            posterior = None
        if actual != posterior:
            resultado.append(actual)
    return resultado

def max_sequence(arr):
    maximo = maximo_acumulado = inicio = fin = reinicio = 0
    for i in range(len(arr)):
        maximo_acumulado += arr[i]
        if maximo_acumulado < 0:
            maximo_acumulado = 0
            reinicio = i + 1
        if maximo < maximo_acumulado:
            maximo = maximo_acumulado
            inicio = reinicio
            fin = i + 1
    return maximo

def series_sum(n):
    if n == 0:
        return "0.00"
    total = 0
    for i in range(n):
        total += 1 / (3 * i + 1)
    return "{:.2f}".format(total)

def hoop_count(n):
    if n >=10:
        return 'Great, now move on to tricks'
    else:
        return 'Keep at it until you get it'

def high(x):
    minusculas = x.lower()
    separo = minusculas.split(' ')
    letras = 'abcdefghijklmnopqrstuvwxyz'
    nummax=0
    respuesta=''
    for i in range(len(separo)):
        suma=0
        for j in range(len(separo[i])):
            suma+= letras.index(separo[i][j])+1
        if suma >nummax:
            nummax=suma
            respuesta=separo[i]
    return respuesta

def invert(lst):
    rta = []
    for n in lst:
        rta.append(-n)
    return rta

def domain_name(url):
    try:
        posicionBarra = url.index('//')
        try:
            posicionWWW = url.index('www')+4
            buscarPunto = url.index('.')+1
            texto = url[buscarPunto:]
            buscarPunto2 = texto.index('.')
            resultado = texto[:buscarPunto2]
        except ValueError:
            texto = url[posicionBarra+2:]
            buscarPunto = texto.index(".")
            resultado = url[posicionBarra+2:buscarPunto+posicionBarra+2]
    except ValueError:
        try:
            posicionWWW = url.index('www')+4
            buscarPunto = url[4:].index('.')
            resultado = url[posicionWWW:posicionWWW+buscarPunto]
        except ValueError:
            buscarPunto = url.index('.')
            resultado = url[:buscarPunto]
    return resultado

def duplicate_encode(word):
    resultado = ''
    word = word.lower()
    for w in word:
        print(w)
        if word.count(w) == 1:
            resultado += '('
        else:
            resultado += ')'
    return resultado

def double_char(s):
    resultado = ''
    for letra in s:
        resultado += f'{letra}{letra}'
    return resultado

def first_non_consecutive(arr):
    anterior = arr[0]-1
    for i in range(len(arr)):
        if anterior +1 != arr[i]:
            return arr[i]
        anterior=arr[i]

def get_age(age):
    return int(age[0])

def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    resultado= []
    for i in range(a,b+1):
        acumulado=0
        textoI=str(i)
        for j in range(len(textoI)):
            acumulado+=int(textoI[j])**(j+1)
        if acumulado == i:
            resultado.append(i)
    return resultado

def is_triangle(a, b, c):
    if a<1 or b<1 or c <1:
        return False
    else:
        maximo=max(a,b,c)
        suma=(a+b+c)
        sinMaximo = suma-maximo
        if maximo >= sinMaximo:
            return False
        else:
            return True

def number(lines):
    salida = []
    for i in range(len(lines)):
        salida.append (f'{i+1}: {lines[i]}')
    return salida

def nb_year(p0, percent, aug, p):
    resultado = 0
    while p0 < p:
        p0 = p0 + int(p0 * (percent / 100)) + aug
        resultado += 1
    return resultado

def string_to_array(s):
    rta= []
    separo= s.split(" ")
    for i in range(len(separo)):
        rta.append(separo[i])
    return rta

def points(games):
    puntaje=0
    for i in range(len(games)):
        print(games[i])
        if games[i][0] > games[i][2]:
            puntaje+=3
        elif games[i][0] == games[i][2]:
            puntaje+=1
    return puntaje

def order(sentence):
    separo = sentence.split(" ")
    resultado = []
    final=''
    for i in range(len(separo)):
        for j in range(len(separo[i])):
            if separo[i][j].isdigit():
                resultado.append(f'{separo[i][j]}{separo[i]}')
    resultado=sorted(resultado)
    for i in range(len(resultado)):
        final+= f'{resultado[i][1:]} '
    final = final[:-1]
    return final

def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False

def abbrev_name(name):
    separo=name.split(" ")
    rta=''
    for i in range(len(separo)):
        rta += f'{separo[i][:1].upper()}.'
    rta=rta[:3]
    return rta

def human_years_cat_years_dog_years(human_years):
    res= []
    if human_years ==1:
        res = [1, 15, 15]
    elif human_years ==2:
        res = [2, 24, 24]
    else:
        res = [human_years, (human_years-2)*4+24, (human_years-2)*5+24]
    return(res)

def is_even(n): 
    # your code here
    if n%2 ==0:
        return True
    else:
        return False

def get_middle(s):
    if len(s)%2 ==0:
        return (s[int((len(s)/2)-1):int((len(s)/2)+1)])
    else:
        return (s[int((len(s)/2))])

def greet(language):
    base= [ ("english", "Welcome"), ("czech", "Vitejte"), ("danish", "Velkomst"), ("dutch", "Welkom"), ("estonian", "Tere tulemast"), ("finnish", "Tervetuloa"), ("flemish", "Welgekomen"), ("french", "Bienvenue"), ("german", "Willkommen"), ("irish", "Failte"), ("italian", "Benvenuto"), ("latvian", "Gaidits"), ("lithuanian", "Laukiamas"), ("polish", "Witamy"), ("spanish", "Bienvenido"), ("swedish", "Valkommen"), ("welsh", "Croeso")]
    def busca_lenguaje(base,language):
        for entrada in base:
            if entrada[0] == language:
                return entrada[1]
        return 'Welcome'
    return busca_lenguaje(base, language)

def get_volume_of_cuboid(length, width, height):
    return (length * width * height)

def reverse_words(text):
    separo= text.split(' ')
    junto = ''
    for i in range(len(separo)):
        junto+= separo[i][::-1]+' '
    junto=junto[0:len(junto)-1]
    return junto

def validate_pin(pin):
    if pin.isdigit() and len(pin) == 4 or pin.isdigit() and len(pin) == 6:
        return True
    else:
        return False

def remove_every_other(my_list):
    lista = []
    for i in range(len(my_list)):
        if ((i+1)%2) !=0:
            lista.append(my_list[i])
    return lista

def likes(names):
    if len(names) == 0:
        return 'no one likes this'
    elif len(names) == 1:
        return f'{names[0]} likes this'
    elif len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'

def get_count(sentence):
    vocales=['a','e','i','o','u']
    cantidad=0
    for v in vocales:
        cantidad += sentence.count(v)
    return cantidad

def delete_nth(order,max_e):
    salida=[]
    for i in range(len(order)):
        if order[i] in salida:
            if salida.count(order[i]) < max_e:
                salida.append(order[i])
        else:
            salida.append(order[i])
    return salida

def number(bus_stops):
    pasajeros=0
    for i in range(len(bus_stops)):
        pasajeros+=bus_stops[i][0]
        pasajeros-=bus_stops[i][1]
    return pasajeros

def printer_error(s):
    ok = 'abcdefghijklm'
    errores=0
    for i in range(len(s)):
        if s[i] not in ok:
            errores+=1
    return f'{errores}/{str(len(s))}'

def is_palindrome(s):
    palindrom = True
    for i in range(len(s)):
        if  s[i].lower() != s[len(s)-(i+1)].lower():
            palindrom = False
    return palindrom

def sale_hotdogs(n):
    if n < 5:
        return n * 100
    elif n >= 5 and n < 10:
        return n * 95
    else:
        return n * 90

def correct(s):
    salida = ''
    for i in range(len(s)):
        if s[i] == '0':
            salida += 'o'
        elif s[i] == '1':
            salida += 'i'            
        elif s[i] == '5':
            salida += 's'
        else:
            salida += s[i]
    return salida.upper()

def arithmetic(a, b, operator):
    if operator == 'add':
        return a+b
    elif operator == 'subtract':
        return a-b
    elif operator == 'multiply':
        return a*b
    else:
        return a/b

def expression_matter(a, b, c):
    return max((a + b) * c, a + (b * c), (a * b) + c, a * (b + c),(a * b) * c, a * (b * c), (a * b) * c, a * (b * c),(a + b) + c, a + (b + c), (a + b) + c, a + (b + c))

def square(n):
    return n*n

def bool_to_word(boolean):
    return 'Yes' if boolean == True else 'No'

def increment_string(strng):
    num_texto = ''
    for i in range(len(strng)):
        if str(strng[len(strng)-(i+1):len(strng)-i]).isdigit():
            num_texto=str(strng[len(strng)-(i+1):len(strng)-i])+num_texto
        else:
            break
    if len(num_texto) == 0:
        return strng + '1'
    else:
        return strng[:len(strng)-(len(num_texto))] +'0' *int((len(num_texto) - len(str(int(num_texto)+1)))) + str(int(num_texto)+1)

def past(h, m, s):
    return s*1000+m*60*1000+h*60*60*1000

def filter_list(l):
    resultado = []
    def es_numero(n):
        return isinstance(n,(int,float))
    for e in l:
        if es_numero(e):
            resultado.append(e)
    return resultado

def row_sum_odd_numbers(n):
    return n**3

def say_hello(name):
    return 'Hello, ' + name 
   
def is_uppercase(inp):
    for i in range(len(inp)):
        if str(inp[i]) != str(inp[i]).upper():
            return False
    return True

def encrypt(text, n):
    if n <1:
        return text
    if text == '':
        return ''
    elif text == None:
        return None
    parcial = ''
    for i in range(n):
        for j in range(1,len(text),2):
            parcial+=text[j]
        for j in range(0,len(text),2):
            parcial+=text[j]
        text = parcial
        parcial=''
    return text

def decrypt(encrypted_text, n):
    if n <1:
        return encrypted_text
    if encrypted_text == '':
        return ''
    elif encrypted_text == None:
        return None
    rearmo = ''
    for i in range(n):
        for j in range(int(len(encrypted_text)/2)):
            rearmo+=(encrypted_text[int(len(encrypted_text)/2)+j])
            rearmo+=(encrypted_text[0+j])
        if len(encrypted_text)%2 != 0:
            rearmo += encrypted_text[len(encrypted_text)-1]
        encrypted_text = rearmo
        rearmo = ''
    return encrypted_text

def find_short(s):
    resultado = 1000
    a = s.split(" ")
    for i in range(len(a)):
        if len(a[i]) < resultado:
            resultado = len(a[i])
    return resultado

def litres(time):
    return int(time *0.5)

def get_pins(observed):
    resultados = []
    opciones = {0: 80, 1:124, 2: 1235, 3: 236, 4:1457, 5:24568, 6:3569,7:478,8:57890, 9:689}
    combinaciones = []
    for i in range(len(observed)):
        combinaciones.append(str(opciones.get(int(observed[i]))))
    def iterar_combinaciones(combinaciones, resultado_parcial=""):
        if not combinaciones:
            resultados.append(resultado_parcial)
        else:
            primera_combinacion = combinaciones[0]
            for elemento in primera_combinacion:
                iterar_combinaciones(combinaciones[1:], resultado_parcial + elemento)
    iterar_combinaciones(combinaciones)
    return resultados

def find_uniq(arr):
    frecuencia = {}
    for elemento in arr:
        if elemento in frecuencia:
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    
    for elemento, contador in frecuencia.items():
        if contador == 1:
            return elemento
    return None

def twice_as_old(dad_years_old, son_years_old):
    if dad_years_old - 2*(son_years_old) <= 0:
        return (dad_years_old - 2*(son_years_old))*(-1)
    else:
        return dad_years_old - 2*(son_years_old)

def solution(nums):
    if nums:
        return sorted(nums)
    else:
        return []

def product_fib(_prod):
    fib = 0
    fib1 = 1
    while True:
        if fib * fib1 == _prod:
            return [fib, fib1, True]
        elif fib * fib1 > _prod:
            return [fib, fib1, False]
        else:
            next = fib+fib1
            fib = fib1
            fib1 = next
