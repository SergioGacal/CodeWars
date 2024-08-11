import math
#def square_or_square_root(arr):
from collections import Counter
#def scramble(s1, s2):
import datetime
# def check_coupon(entered_code, correct_code, current_date, expiration_date):

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

def goals(laLiga, copaDelRey, championsLeague):
    return laLiga + copaDelRey + championsLeague

def switch_it_up(number):
    numeros = {0: 'Zero', 1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8: 'Eight',9:'Nine'}
    return numeros[number]

def str_count(strng, letter):
    return strng.count(letter)

def rot13(message):
    rot13_reemplazo = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',     'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',    'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U',    'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C',    'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K','Y': 'L', 'Z': 'M'}
    respuesta = ''
    for letra in message:
        if letra in rot13_reemplazo:
            respuesta += rot13_reemplazo[letra]
        else:
            respuesta+=letra
    return respuesta

def pipe_fix(nums):
    resultado = []
    menor=min(nums)
    maximo=max(nums)
    for i in range(menor,maximo+1,1):
        resultado.append(i)
    return resultado

def sequence_sum(begin_number, end_number, step):
    if end_number < begin_number:
        return 0
    resultado = 0
    for i in range(begin_number,end_number+1,step):
        resultado+=i
    return resultado

def change_me(money): 
    acepto = {'£5': 500, '£2': 200, '£1' : 100, '50p':50 , '20p': 20}
    if money not in acepto:
        return money
    if money == '20p':
        return '10p 10p'
    cambio = acepto[money]
    p20 = cambio //20
    p10 = int((cambio - ((cambio //20)*20))/10)
    monedas = []
    monedas.extend(['20p']*p20)
    monedas.extend(['10p']*p10)
    return ' '.join(monedas)

def find_multiples(integer, limit):
    respuesta = []
    for i in range(0,limit,integer):
        respuesta.append(i)
    return respuesta

def find_multiples(integer, limit):
    print(limit%integer)
    respuesta = []
    if limit%integer == 0:
        for i in range(integer,limit+1,integer):
            respuesta.append(i)
    else:
        for i in range(integer,limit,integer):
            respuesta.append(i)
    return respuesta

def two_sum(numbers, target):
    x=0
    y=1
    while x < len(numbers)-1:
        while y < len(numbers):
            if numbers[x]+numbers[y] == target and x != y:
                return x, y
            y+=1
        y=1
        x+=1

def round_to_next5(n):
    while True:
        if n%5 ==0:
            return n
        n+=1

def sum_array(arr):
    if arr == [] or arr == None or len(arr)==1:
        return 0
    else:
        return sum(arr)-min(arr)-max(arr)

def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)

def problem(a):
    if type(a) == str:
        return 'Error'
    else:
        return a*50+6

def between(a,b):
    resultado = []
    for i in range(a,b+1):
        resultado.append(i)
    return resultado

def get_real_floor(n):
    if n==0:
        return 0
    elif n <0:
        return n
    elif n <13:
        return n-1
    else:
        return n-2

def sort_array(source_array):
    impares = list()
    for i in range(len(source_array)):
        if source_array[i]%2 != 0:
            impares.append(source_array[i])
    impares = sorted(impares)
    for i in range(len(source_array)):
        if source_array[i]%2 != 0:
            source_array[i] = impares.pop(0)
    return source_array

def sum_str(a, b):
    a = int(a) if len(a) >0 else 0
    b = int(b) if len(b) >0 else 0
    return str(a+b)

def plural(n):
    return n != 1

def get_char(c):
    return chr(c)

def remove_smallest(numbers):
    copia = numbers[:]
    if copia:
        menor= copia.index(min(copia))
        copia.pop(menor)
        return copia
    else:
        return []

def two_sort(array):
    ordenado = sorted(array)
    valor = ordenado[0]
    resultado = ''
    for l in valor:
        resultado += l + '***'
    return resultado[0:len(resultado)-3]

def unusual_five():
    a=len('abcde')
    return a

def gimme(input_array):
    menor=min(input_array)
    mayor=max(input_array)
    for i in input_array:
        if i < mayor and i > menor:
            respuesta = i
    return input_array.index(respuesta)

def duplicate_count(text):
    repetidas = []
    analizar = text.lower()
    for i in analizar:
        if analizar.count(i) > 1 and i not in repetidas:
            repetidas.append(i)
    return len(repetidas)

def add_five(num):
    total = num + 5
    return total

def reverse_letter(st):
    letras = 'abcdefghijklmnopqrstuvwxyz'
    respuesta = ''
    for i in range(len(st)):
        if st[i] in letras:
            respuesta = st[i]+respuesta
    return respuesta

def capitals(word):
    mayusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    respusta = []
    for i in range(len(word)):
        if word[i] in mayusculas:
            respusta.append(i)
    return respusta

def dir_reduc(arr):
    eliminables = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    resultado = []
    for i in arr:
        if resultado and resultado[-1] == eliminables.get(i):
            resultado.pop()
        else:
            resultado.append(i)
    return resultado

def dig_pow(n, p):
    t= str(n)
    resultado=0
    for i in range(len(t)):
        resultado+=int(t[i]) ** (p+i)
    if resultado%n ==0:
        return int(resultado/n)
    else:
        return -1

def better_than_average(class_points, your_points):
    if your_points > (sum(class_points)/len(class_points)):
        return True 
    else:
        return False

def accum(st):
    resultado = ''
    for i in range(len(st)):
        resultado += st[i].capitalize()+st[i].lower()*(i)+'-'
    return resultado[0:len(resultado)-1]

def factorial(n):
    if n <0 or n >12:
        raise ValueError('ValueError')
    else:
        resultado=1
        for i in range(1,n+1):
            resultado*=i
        return resultado

def DNA_strand(dna):
    valores = {'A':'T','C':'G','T':'A','G':'C'}
    respuesta = ''
    for v in dna:
        respuesta+= valores.get(v)
    return respuesta

def comp(array1, array2):
    if array1 == [] and array2 == []:
        return True
    if array1 is None or array2 is None or not array1 or not array2:
        return False
    array3 = []
    array4 = []
    for n in array1:
        if n < 0:
            array3.append(n*(-1))
        else:
            array3.append(n)
    for n in array2:
        array4.append(n)
    o1 = sorted(array3)
    o2 = sorted(array4)
    for i in range(len(o1)):
        if o1[i] ** 2 != o2[i]:
            return False
    return True

def chromosome_check(chromosome):
    if chromosome == 'XX':
        return 'Congratulations! You\'re going to have a daughter.'
    else:
        return 'Congratulations! You\'re going to have a son.'

def find_difference(a, b):
    return abs(a[0]*a[1]*a[2]-b[0]*b[1]*b[2])

def solve(s):
    mayusculas= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    minusculas= 'abcdefghijklmnopqrstuvwxyz'
    ma=mi=0
    for i in s:
        if i in mayusculas:
            ma+=1
        if i in minusculas:
            mi+=1
    if ma>mi:
        return s.upper()
    else:
        return s.lower()

def reverse_list(l):
    l2= []
    for i in l:
        l2.insert(0,i)
    return l2

def bouncing_ball(h, bounce, window):
    if h >0 and bounce >0 and bounce <1 and window <h:
        rebotes = -1
        while h > window:
            h*=bounce
            rebotes+=2
        return rebotes
    else:
        return -1

def find_nb(m):
    n = 0
    total = 0
    while total <m:
        valor=n*n*n
        total+=valor
        n+=1
    if total == m:
        return n-1
    else:
        return -1

def powers_of_two(n):
    respuesta = []
    for i in range(0,n+1):
        respuesta.append(2**i)
    return respuesta

def find_average(numbers):
    if not numbers:
        return 0
    else:
        return sum(numbers)/len(numbers)

def solution(number):
    if number<0:
        return 0
    else:
        suma=0
        for i in range(number):
            if i %3 ==0 or i %5 ==0:
                suma+=i
    return suma

def longest_consec(strarr, k):
    if k > len(strarr) or k < 1:
        return ''
    respuesta = ''
    maximo = 0
    for i in range(len(strarr) - k + 1):
        concatenado = ''.join(strarr[i:i + k])
        largo = len(concatenado)
        if largo > maximo:
            respuesta = concatenado
            maximo = largo
    return respuesta

def combat(health, damage):
    return health - damage if health - damage > 0 else 0

def wave(people):
    respuesta = []
    for i in range(len(people)):
        if people[i] != ' ':
            frase = people[:i] + people[i].upper() + people[i+1:]
            respuesta.append(frase)
    return respuesta

def other_angle(a, b):
    return 180-a-b

def spin_words(sentence):
    palabras = sentence.split(' ')
    respuesta = ''
    for i in range(len(palabras)):
        if len(palabras[i])>=5:
            respuesta+=' '+palabras[i][::-1]
        else:
            respuesta+=' '+(palabras[i])
    return respuesta[1:]

def multiply(a, b):
    return a * b

def digital_root(n):
    numero=str(n)
    while len(numero)!=1:
        total=0
        for n in numero:
            total+=int(n)
        numero=str(total)
    return int(numero)
    
def remove(s):
    return s[:-1] if s[len(s)-1:] == '!' else s

def is_divisible(n,x,y):
    return True if n % x ==0 and n%y ==0 else False

def count_bits(n):
    binario = bin(n)
    respuesta = 0
    for uno in binario:
        if uno == '1':
            respuesta+=1
    return respuesta

def find_outlier(integers):
    par = []
    inpar = []
    list(map(lambda x: par.append(x) if x%2==0 else inpar.append(x),integers))
    return par[0] if len(par)==1 else inpar[0]

def xo(s):
    return s.lower().count('x') == s.lower().count('o')

def maskify(cc):
    return '#'*(len(cc)-4)+cc[len(cc)-4:] if len(cc)>3 else cc

def to_camel_case(text):
    texto=''
    for t in text:
        if t == '-' or t == '_':
            texto+= ' '
        else:
            texto+= t
    cadena= texto.split(' ')
    texto = cadena[0]
    cadena.pop(0)
    for c in cadena:
        texto += c[0].upper() + c[1:len(c)]
    return texto

def narcissistic(value) :
    num_text = str(value)
    total = 0
    for num in num_text:
        total+=int(num)**len(num_text)
    return total == value

def longest(a1, a2):
    return ''.join(sorted(set(a1+a2)))

def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == 'needle':
            return f'found the needle at position {i}'

def remove_url_anchor(url):
    respuesta = ''
    for letra in url:
        if letra != '#':
            respuesta+=letra
        else:
            break
    return respuesta

def how_many_light_sabers_do_you_own(name=''):
    return 18 if name == 'Zach' else 0

def get_size(w,h,d):
    return [2*( w * h ) + 2 * (d * h) + 2 * (w * d), w * h * d]

def duty_free(price, discount, holiday_cost):
    return int(holiday_cost/(price*discount/100))

def multi_table(number):
    respuesta = ''
    for i in range (1,11):
        respuesta+=f'{i} * {number} = {i*number}\n'
    return respuesta[0:len(respuesta)-1]

def find_even_index(arr):
    total = sum(arr)
    izq = 0
    for i, num in enumerate(arr):
        total -= num
        if izq == total:
            return i
        izq += num
    return -1

def smash(words):
    frase=''
    for palabra in words:
        frase+=palabra+' '
    return frase[0:len(frase)-1]

def move_zeros(lst):
    respuesta = []
    print(type(lst),type(respuesta))
    ceros = 0
    for num in lst:
        if num == 0:
            ceros+=1
        else:
            respuesta.append(num)
    for i in range(ceros):
        respuesta.append(0)
    return respuesta

def min_wind_strength(strengths):
    if not strengths:
        return 0
    fuerza_necesaria = 0
    for i in range(1,len(strengths)+1):
        if i  < len(strengths):
            fuerza_necesaria = max(fuerza_necesaria, strengths[i-1] + 1)
            strengths[i] = max(strengths[i] - strengths[i-1], 0)
        else:
            fuerza_necesaria = max(fuerza_necesaria, strengths[i-1])
    return fuerza_necesaria

def solution(s):
    respuesta = []
    iteraciones = len(s)/2
    if len(s)%2 != 0:
        iteraciones +=1 
    for i in range(int(iteraciones)):
        if len(s[(i*2):(i*2+2)]) == 1:
            respuesta.append(s[(i*2):(i*2+2)]+'_')
        else:
            respuesta.append(s[(i*2):(i*2+2)])
    return respuesta

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'} # Para que no de error, lo levanta de from preloaded import MORSE_CODE
def decode_morse(morse_code):
    respuesta= ''
    morse_code = morse_code.strip()
    codigo = (morse_code.replace('   ','  ')).split(' ')
    for clave in codigo:
        respuesta += str(MORSE_CODE.get(clave))
    respuesta =respuesta.replace('None',' ')
    return(respuesta)

def pig_it(text):
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    respuesta = ''
    frase = text.split(' ')
    for palabra in frase:
        letra=palabra[0]
        if letra.lower() in letras:
            respuesta+= palabra[1:]+letra+'ay'+' '
        else:
            respuesta+= palabra
    return respuesta.strip()

def find_missing_letter(chars):
    letras = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    inicio = letras.index(chars[0])
    print('inicio', inicio)
    print('len',len(chars))
    print()
    for i in range(len(chars)):
        if chars[i] != letras[inicio+i]:
            return letras[inicio+i]

def make_readable(seconds):
    segundos= str(seconds%60)
    if len(segundos) == 1:
        segundos='0'+segundos
    minutos= int(seconds/60)
    if minutos >59:
        horas = int(minutos/60)
        minutos = str(minutos-(60*horas))
    else:
        horas = 0
    minutos=str(minutos)
    if len(minutos) == 1:
        minutos = '0'+minutos
    horas = str(horas)
    if len(horas) == 1:
        horas= '0'+ horas
    return f'{horas}:{minutos}:{segundos}'

def hero(bullets, dragons):
    return bullets/dragons >= 2

def rgb(r, g, b):
    if r <0:
        r =0
    if r>255:
        r=255
    if g <0:
        g=0
    if g >255:
        g=255
    if b<0:
        b=0
    if b>255:
        b=255
    return format(r, '02x').upper()+format(g, '02x').upper()+format(b, '02x').upper()

def divisors(integer):
    respuesta = []
    for i in range(2,integer):
        if integer%i ==0:
            respuesta.append(i)
    if respuesta == []:
        return f'{integer} is prime'
    return respuesta

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

def reverse_words(s):
    s = s.split(' ')
    r = ''
    for palabra in s:
        r = palabra+' '+r
    return r[:-1]

def array_plus_array(arr1,arr2):
    return sum(arr1+arr2)

def valid_braces(string):
    while '()' in string or '{}' in string or '[]' in string:
        string=string.replace('()','')
        string=string.replace('{}','')
        string=string.replace('[]','')
    return string ==''

def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def get_average(marks):
    return int(sum(marks)/(len(marks)))

def greet(name, owner):
    return 'Hello boss' if name == owner else 'Hello guest'

def is_anagram(test, original):
    return sorted(test.lower()) ==  sorted(original.lower())

def remove_exclamation_marks(s):
    remover = ['¡', '!']
    respuesta = ''
    for i in range(len(s)):
        print(s[i])
        if s[i] not in remover:
            respuesta+=s[i]
    return respuesta

def monkey_count(n):
    respuesta = []
    for i in range(1,n+1):
        respuesta.append(i)
    return respuesta

def update_light(current):
    cambios = {'green':'yellow','yellow':'red', 'red':'green'}
    return cambios.get(current)

def bonus_time(salary, bonus):
    if bonus:
        return f'${int(salary*10)}'
    else:
        return f'${int(salary)}'
    
    
def in_array(array1, array2):
    previa=set()
    for contenedor in array2:
        for contenido in array1:
            if contenido in contenedor:
                previa.add(contenido)
    respuesta = sorted(list(previa))
    return respuesta

def enough(cap, on, wait):
    if cap-on-wait>0:
        return 0
    else:
        return (cap-on-wait)*-1
    
def get_planet_name(id):
    planetas = {1:'Mercury', 2: 'Venus',3:'Earth',4: 'Mars',5:'Jupiter',6:'Saturn',7:'Uranus',8:'Neptune'}
    name = planetas.get(id)
    return name

def divisors(n):
    respuesta=0
    for i in range(n,0,-1):
        if n%i==0:
            respuesta+=1
    return respuesta

def zero(a=None): 
    return 0 if not a else a(0)
def one(a=None): 
    return 1 if not a else a(1)
def two(a=None):
    return 2 if not a else a(2)
def three(a=None):
    return 3 if not a else a(3)
def four(a=None):
    return 4 if not a else a(4)
def five(a=None):
    return 5 if not a else a(5)
def six(a=None):
    return 6 if not a else a(6)
def seven(a=None):
    return 7 if not a else a(7)
def eight(a=None):
    return 8 if not a else a(8)
def nine(a=None):
    return 9 if not a else a(9)
def plus(b):
    return lambda x:x+b
def minus(b):
    return lambda x:x-b
def times(b):
    return lambda x:x*b
def divided_by(b):
    return lambda x:int(x/b)

def dont_give_me_five(start,end):
    n=0
    for i in range(start,end+1):
        if '5' not in str(i):
            n+=1
    return n

def solution(n):
    num_text='0'*(4-len(str(n)))+str(n)
    miles=int(num_text[0])*'M'
    c = int(num_text[1])
    d = int(num_text[2])
    n = int(num_text[3])
    if c <4:
        centena=c*'C'
    elif c==4:
        centena='CD'
    else:
        centena='D'
        if c>5 and c<9:
            centena+=(c-5)*'C'
        elif c==9:
            centena='CM'
    if d <4:
        decena=d*'X'
    elif d==4:
        decena='XL'
    else:
        decena='L'
        if d>5 and d<9:
            decena+=(d-5)*'X'
        elif d==9:
            decena='XC'
    if n <4:
        numeral=n*'I'
    elif n==4:
        numeral='IV'
    else:
        numeral='V'
        if n>5 and n<9:
            numeral+=(n-5)*'I'
        elif n==9:
            numeral='IX'
    return miles+centena+decena+numeral

def include(arr, item):
    return item in arr

def nb_dig(n, d):
    respuesta=0
    for i in range(0,n+1):
        resultado=str(i**2)
        respuesta+=resultado.count(str(d))
    return respuesta

def generate_hashtag(s):
    hashtag= '#'
    frase=s.lower().split(' ')
    for palabra in frase:
        hashtag+=palabra.capitalize()
    if len(hashtag)>140 or not s:
        return False
    return hashtag

def stray(arr):
    for i in range(len(arr)):
        if arr.count(arr[i]) == 1:
            return arr[i]

def cakes(recipe, available):
    ingredientes=list(recipe.keys())
    tengo=list(available.keys())
    for necesito in ingredientes:
        if necesito not in tengo:
            return 0
    maximo=9999999
    for i in ingredientes:
        if maximo > int(available.get(i)/recipe.get(i)):
            maximo = int(available.get(i)/recipe.get(i))
    return maximo

def first_non_repeating_letter(s):
    for letra in s.lower():
        if s.lower().count(letra) == 1:
            return s[s.lower().index(letra)]
    return ''

def odd_count(n):
    return int(n/2)

def to_alternating_case(string):
    respuesta=''
    for letra in string:
        if letra.isupper():
            respuesta+=letra.lower()
        else:
            respuesta+=letra.upper()
    return respuesta

def order_weight(strng):
    if not strng:
        return ''
    lista=strng.split(' ')
    previa=[]
    for i in range(len(lista)):
        k=0
        for j in range(len(lista[i])):
            k+=int(lista[i][j])
        previa.append(k)
    sumas_unicas=[]
    for i in previa:
        if i not in sumas_unicas:
            sumas_unicas.append(i)
    sumas_unicas= sorted(sumas_unicas)
    resultado=''
    for valor_a_buscar in sumas_unicas:
        temporal = []
        for indice, valor in enumerate(previa):
            if valor == valor_a_buscar:
                temporal.append(lista[indice])
        temporal=sorted(temporal)
        for i in range(len(temporal)):
            resultado+=temporal[i]+' '
    return resultado[:-1]
    
def divisible_by(numbers, divisor):
    resultado = []
    for num in numbers:
        if num%divisor ==0:
            resultado.append(num)
    return resultado

def solution(roman : str) -> int:
    resultado=0
    equivalencia = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(roman)):
        if i == 0:
            resultado+= equivalencia.get(roman[i])
        else:
            if equivalencia.get(roman[i]) > equivalencia.get(roman[i-1]):
                resultado-=equivalencia.get(roman[i-1])
                resultado+=(equivalencia.get(roman[i])-equivalencia.get(roman[i-1]))
            else:
                resultado+=equivalencia.get(roman[i])
    return resultado

def format_duration(seconds):
    if seconds ==0:
        return 'now'
    anios= seconds//60//60//24//365
    if anios >0:
        seconds= seconds-(anios*31536000)
    dias = seconds//60//60//24
    if dias >0:
        seconds=seconds-(dias*86400)
    horas = seconds //60//60
    if horas >0:
        seconds=seconds-(horas*3600)
    minutos = seconds//60
    if minutos >0:
        seconds=seconds-(minutos*60)
    respuesta = ''
    
    if anios > 1:
        respuesta+= str(anios)+' years, '
    elif anios == 1:
        respuesta+= str(anios)+' year, '
    else:
        pass
    if dias > 1:
        respuesta+= str(dias)+' days, '
    elif dias == 1:
        respuesta+= str(dias)+' day, '
    else:
        pass
    if horas >1:
        respuesta+= str(horas)+' hours, '
    elif horas ==1:
        respuesta+= str(horas)+' hour, '
    else:
        pass
    if minutos >1:
        respuesta+= str(minutos)+' minutes, '
    elif minutos ==1:
        respuesta+= str(minutos)+' minute, '
    else:
        pass
    if seconds >1:
        respuesta+= str(seconds)+' seconds, '
    elif seconds ==1:
        respuesta+= str(seconds)+' second, '
    else:
        pass
    respuesta = respuesta[:-2]
    for i in range(len(respuesta),0,-1):
        if (respuesta[i-1]) == ',':
            respuesta=respuesta[0:i-1] +' and '+respuesta[i+1:]
            break
    return respuesta

def how_much_i_love_you(nb_petals):
    petalos= {0: "not at all", 1: "I love you", 2: "a little", 3: "a lot", 4: "passionately", 5: "madly"}
    return petalos.get(nb_petals%6)

def solution(args):
    respuesta = ''
    i = 0
    while i < len(args):
        start = i
        while i < len(args) - 1 and args[i] + 1 == args[i + 1]:
            i += 1
        end = i
        if end - start >= 2:
            respuesta += f'{args[start]}-{args[end]},'
        else:
            for j in range(start, end + 1):
                respuesta += f'{args[j]},'
        i += 1
    return respuesta[:-1]  # Elimina la última coma

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects > 4:
        return 90
    elif exam > 50 and projects >1 :
        return 75
    else:
        return 0

def sort_by_length(arr):
    final = len(arr)
    for i in range(final):
        for j in range(final - 1 - i):
            if len(arr[j]) > len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def move(position, roll):
    return position+(roll*2)

def square_or_square_root(arr):
    respuesta= []
    for num in arr:
        if math.sqrt(num) - int(math.sqrt(num)) == 0:
            respuesta.append(int(math.sqrt(num)))
        else:
            respuesta.append(num**2)
    return respuesta

def scramble(s1, s2):
    d1= Counter(s1)
    d2=Counter(s2)
    for clave, valor in d2.items():
        if not d1.get(clave):
            return False
        else:
            if valor > d1.get(clave) or d1.get(clave) is None:
                return False 
    return True

def calculate_years(principal, interest, tax, desired):
    years=0
    while principal < desired:
        gane=(principal*interest)*(1-tax)
        principal+=gane
        years+=1
    return years

def create_array(n):
    res=[]
    i=1
    while i<=n:
        res.append(i)
        i+=1
    return res

def break_chocolate(n, m):
    if n==0:
        return 0
    return n*m-1

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for palabra in geese:
        if palabra in birds:
            birds.remove(palabra)
    return birds

def stringy(size):
    if size%2==0:
        return '10'*int(size/2)
    else:
        return '10'*int(size/2)+'1'

def check_alive(health):
    return health >0

def fix_the_meerkat(arr):
    return [arr[2],arr[1],arr[0]]

def well(x):
    if 'good' not in x:
        return 'Fail!'
    if x.count('good') <= 2:
        return 'Publish!'
    else:
        return 'I smell a series!'

def shortcut( s ):
    vocales= 'aeiou'
    nvcls= ''
    for letra in s:
        if letra not in vocales:
            nvcls += letra
    return nvcls

def solution(a, b):
    largo_a = len(a)
    largo_b = len(b)
    if largo_a < largo_b:
        return a+b+a
    else:
        return b+a+b

def small_enough(array, limit):
    return max(array) <= limit

a = "code"
b = "wa.rs"
name = a + b

def name_shuffler(str_):
    separo = str_.split(' ')
    return separo[1]+' '+separo[0]

def nth_even(n):
    return (n*2)-2

def people_with_age_drink(age):
    if age <14:
        return 'drink toddy'
    elif age <18:
        return 'drink coke'
    elif age<21:
        return 'drink beer'
    else:
        return 'drink whisky'

def camel_case(s): # sería "PascalCase"
    respuesta = ''
    separo = s.lower().split(' ')
    for palabra in separo:
        respuesta += palabra.capitalize()
    return respuesta

def two_oldest_ages(ages):
    ordeno=sorted(ages,reverse=True)
    return sorted(ordeno[:2])

class Fighter(object):
        def __init__(self,name,health,damage_per_attack):
            self.name = name
            self.health = health
            self.damage_per_attack = damage_per_attack
        def __str__(self):
            return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)

def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        while True:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <=0:
                return fighter1.name
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <=0:
                return fighter2.name
    else:
        while True:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health <=0:
                return fighter2.name
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health <=0:
                return fighter1.name

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

def position(alphabet):
    letras= '-abcdefghijklmnopqrstuvwxyz'
    return 'Position of alphabet: '+ str(letras.index(alphabet))

def title_case(title, minor_words=''):
    separo = title.lower().split(' ')
    minor = minor_words.lower().split(' ')
    respuesta = ''
    for palabra in separo:
        if palabra not in minor:
            respuesta+= palabra.capitalize()+' '
        else:
            if respuesta == '':
                respuesta += palabra.capitalize()+' '
            else:
                respuesta+= palabra+' '
    return respuesta[:-1]

def add(a, b):
    return a+b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b
def mod(a, b):
    return a%b
def exponent(a, b):
    return a**b
def subt(a, b):
    return a-b

def xor(a,b):
    if (a== True and b== False):
        return True
    elif (a==True and b== True):
        return False
    elif (a==False and b==True):
        return True
    else:
        return False

def no_boring_zeros(num):
    if not num:
        return 0
    text=str(num)
    for i in range(len(text)):
        if ((text[len(text)-1])) == '0':
            text = text[0:len(text)-1]
        else:
            return int(text)

def score(dice):
    resultado=0
    if dice.count(1) == 5:
        resultado+=1200
    elif dice.count(1) == 4:
        resultado+=1100
    elif dice.count(1) == 3:
        resultado+=1000
    elif dice.count(1) >0:
        resultado+=100 * dice.count(1)
    if dice.count(5) == 5:
        resultado+=600
    elif dice.count(5) == 4:
        resultado+=550
    elif dice.count(5) == 3:
        resultado+=500
    elif dice.count(5) >0:
        resultado+=50 * dice.count(5)
    if dice.count(6) >= 3:
        resultado+=600
    if dice.count(4) >= 3:
        resultado+=400        
    if dice.count(3) >= 3:
        resultado+=300    
    if dice.count(2) >= 3:
        resultado+=200     
    return resultado

def merge_arrays(arr1, arr2):
    unir = set(arr1) | set(arr2)
    respuesta = list(unir)
    return sorted(respuesta)
    
def sp_eng(sentence): 
    return 'english' in sentence.lower()

def to_binary(n):
    if n == 0:
        return '0'
    binario = ''
    while n >0:
        resto = n%2
        binario = str(resto)+ binario
        n //= 2
    return int(binario)

def to_weird_case(words):
    frase = words.split(' ')
    respuesta = ''
    for palabra in frase:
        
        for i in range(len(palabra)):
            if i%2 == 0 :
                respuesta += palabra[i].upper()
            else:
                respuesta += palabra[i].lower()
        respuesta += ' '
    return respuesta [:-1]

def check_exam(arr1,arr2):
    resultado =0
    for i in range(len(arr1)):
        if arr2[i]:
            if arr1[i] == arr2[i]:
                resultado += 4
            else:
                resultado -= 1
    if resultado < 0:
        resultado = 0
    return resultado

def is_valid_IP(strng):
    if not strng:
        return False
    separo = strng.split('.')
    if len(separo) != 4:
        return False
    for num in separo:
        if not num.isdigit() or (num.startswith('0') and len(num) > 1):
            return False
        if not num.isdigit():
            return False
        n = int(num)
        if not(0 <= n <=255):
            return False
    return True

def capitalize_word (word):
    return word.capitalize()

def diamond(n):
    respuesta = ''
    if n <=0 or n%2 ==0:
        return None
    media = int(n-1)/2
    for i in range(int(media)):
        respuesta += ' '*(int(media)-i)+'*'*(2*i+1)+'\n'
    respuesta += '*'*n +'\n'
    for i in range(int(media)-1,-1,-1):
        respuesta += ' '*(int(media)-i)+'*'*(2*i+1)+'\n'
    return respuesta

def warn_the_sheep(queue):
    for i in range(len(queue),0,-1):
        if queue[len(queue)-1] == 'wolf':
            return 'Pls go away and stop eating my sheep'
        if queue[i-1] == 'wolf':
            return f'Oi! Sheep number {len(queue)-i}! You are about to be eaten by a wolf!'

def rev_rot(strng, sz):
    if sz > len(strng):
        return ''
    if sz <=0 or strng == '':
        return ''
    pedazos=int(len(strng))/sz
    respuesta=''
    for i in range(int(pedazos)):
        trozo=strng[i*sz:(i+1)*sz]
        resultado=0
        for dig in trozo:
            resultado+=int(dig)
        if resultado %2 == 0:
            for i in range(len(trozo),0,-1):
                respuesta+=trozo[i-1]
        else:
            respuesta+=trozo[1:len(trozo)]+trozo[0:1]
    return respuesta

def sq_in_rect(lng, wdth):
    mayor = max(lng,wdth)
    menor = min(lng,wdth)
    resultado = []
    if lng == wdth:
        return None
    while mayor != 1 or menor != 1:
        resultado.append(menor)
        temporal = [(mayor-menor),menor]
        menor = min(temporal)
        mayor = max(temporal)
        if menor == mayor:
            resultado.append(menor)
            break
    return resultado

def rain_amount(mm):
    if mm >= 40:
        return "Your plant has had more than enough water for today!"
    else:
        return f'You need to give your plant {40-mm}mm of water'

def find_glasses(lst):
    pares = {'dustO':'Odust', 'O':'O','OO':'OO'}
    for lente in lst:
        for i,(key, value) in enumerate(pares.items()):
            if key in lente and value in lente:
                evaluar = lente[lente.index(key):]
                if '-' in evaluar:
                    guiones = evaluar.count('-')
                    if str(key)+'-'*int(guiones)+str(value) in lente:
                        return lst.index(lente)
                    if lente.count(key) >1:
                        print(lente,'\n',key,value,'\n')
                        if 'OO-OO' in lente:
                            return lst.index(lente)

STRANGE_STRING = 'ß'

def search_names(logins):
    return list(filter(lambda x: any('_' in item for item in x), logins))

def mouth_size(animal): 
    if animal.lower() == 'alligator':
        return 'small'
    else:
        return 'wide'

def prime_factors(n):
    resultado = ''
    previa = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            n //= divisor
            previa.append(divisor)
        divisor += 1
        if divisor * divisor > n:
            if n > 1:
                previa.append(n)
            break
    agrupado = {elemento: previa.count(elemento) for elemento in previa}
    for clave, valor in agrupado.items():
        if valor >1:
            resultado += f'({clave}**{valor})'
        else:
            resultado += f'({clave})'
    return resultado

def reverse(st):
    return " ".join(st.split()[::-1])

def sum_digits(number):
    texto=str(number)
    total=0
    numeros = '1234567890'
    for letra in texto:
        if letra in numeros:
            total += int(letra)
    return total

def no_odds(values):
    respuesta = []
    for num in values:
        if num % 2 == 0:
            respuesta.append(num)
    return respuesta

def replace_exclamation(st):
    respuesta = ''
    vocales = 'aeiouAEIOU'
    for letra in st:
        if letra in vocales:
            respuesta += '!'
        else:
            respuesta += letra
    return respuesta

def combine_names(name,surname):
    return f'{name} {surname}'

def sum_mul(n, m):
    if n < 1 or m < 1 and n > m or not n and not m:
        return "INVALID"
    resultado = 0
    for i in range(m-n):
        if (n+i)%n == 0:
            resultado += (n+i)
    return resultado

def hex_to_dec(s):
    return int(s,16)

def angle(n):
    return 180*(n-2)

def add_length(str_):
    separo = str_.split(' ')
    respuesta = []
    for palabra in separo:
        respuesta.append(f'{palabra} {len(palabra)}')
    return respuesta

def snail(snail_map):
    if len(snail_map) == 1 and len(snail_map[0]) == 0:
        return []
    respuesta = []
    partida = {'fila':0,'columna':-1}
    sentido = 'der'
    filas=len(snail_map)
    columnas=len(snail_map)-1
    opciones = {
    'der': {'sig': 'aba', 'x': 1, 'y': 0,'resto':'fila', 'rango_j': filas },
    'aba': {'sig': 'izq', 'x': 0, 'y': 1,'resto':'columna', 'rango_j': columnas },
    'izq': {'sig': 'arr', 'x': -1, 'y': 0,'resto':'fila', 'rango_j': filas },
    'arr': {'sig': 'der', 'x': 0, 'y': -1,'resto':'columna', 'rango_j': columnas },
}
    for i in range(len(snail_map)*2-1):
        if sentido in ('der','izq'):
            for j in range(filas):
                partida['columna'] += opciones[sentido]['x']
                respuesta.append(snail_map[partida['fila']][partida['columna']])
        else:
            for j in range(columnas):
                partida['fila'] += opciones[sentido]['y']
                respuesta.append(snail_map[partida['fila']][partida['columna']])
        if opciones[sentido]['resto'] == 'fila':
            filas -= 1
        else:
            columnas -= 1
        sentido = opciones[sentido]['sig']
    return respuesta

def triple_trouble(one, two, three):
    return ''.join(map(lambda x: x[0]+x[1]+x[2],zip(one,two,three)))

def calculate_age(year_of_birth, current_year):
    if year_of_birth+1 == current_year:
        return 'You are 1 year old.'
    if year_of_birth < current_year:
        return f'You are {current_year - year_of_birth} years old.'
    elif year_of_birth == current_year:
        return 'You were born this very year!'
    elif year_of_birth == current_year+1:
        return 'You will be born in 1 year.'
    else:
        return f'You will be born in {year_of_birth - current_year} years.'

def zeros(n):
    res = 0
    if n == 0:
        return res
    for i in range(1,n):
        if int(n /5 ** i) != 0:
            res += int(n /5 ** i)
        else:
            return res

def perimeter(n):
    fibo_ant = 0
    fibo_act = 1
    fibo_sig = 1
    acumulado = 2
    for i in range(2,n+1):
        fibo_ant = fibo_act
        fibo_act = fibo_sig
        fibo_sig = fibo_ant + fibo_act
        acumulado += fibo_sig
    return acumulado *4

def bin_to_decimal(inp):
    return int(inp,2)

def mango(quantity, price):
    return (quantity-int(quantity/3))*price

def max_multiple(divisor, bound):
    for i in range(bound,0,-1):
        if i % divisor == 0:
            return i

def correct_tail(body, tail):
    return tail == body[-1]

def generate_range(start, stop, step):
    return list(range(start,stop+1,step))

def min_value(digits):
    return int(''.join(map(str, sorted(set(digits)))))

from datetime import datetime
def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if not entered_code or not correct_code or not current_date or not expiration_date:
        return False
    print(entered_code, correct_code, current_date, expiration_date)
    current_date_dt = datetime.strptime(current_date, '%B %d, %Y')
    expiration_date_dt = datetime.strptime(expiration_date, '%B %d, %Y')
    return entered_code == correct_code and current_date_dt <= expiration_date_dt

def array(string):
    items = string.split(',')
    if len(items) <= 2:
        return None
    middle_items = items[1:-1]
    result = ' '.join(middle_items)
    return result

def hello(name=''):
    if name:
        return 'Hello, ' + name.capitalize()+'!'
    else:
        return 'Hello, World!'

def how_many_dalmatians(n):
    if n <=10:
        return 'Hardly any'
    elif n <=50:
        return 'More than a handful!'
    elif n <=100:
        return "Woah that's a lot of dogs!"
    else:
        return '101 DALMATIONS!!!'

import re
def replace_dots(s):
    return re.sub(r'\.', '-', s)

def bumps(road):
    return 'Car Dead' if road.count('n') >15  else 'Woohoo!'

def list_squared(m, n):
    def es_cuadrado(n):
        return int(n ** 0.5) ** 2 == n
    respuesta = []
    suma=0
    for i in range(m,n+1):
        suma=0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                suma += j ** 2
                if j != i // j:
                    suma += (i // j) ** 2
        if es_cuadrado(suma):
            respuesta.append([i,suma])
    return respuesta

def distinct(seq):
    respuesta = []
    for num in seq:
        if num not in respuesta:
            respuesta.append(num)
    return respuesta

def greet(name):
    return f'Hello, {name} how are you doing today?'

def take(arr,n):
    return arr[0:n]

def weather_info (temp):
    c = (temp-32)*(5/9)
    return f'{c} is freezing temperature' if c < 0 else f'{c} is above freezing temperature'

def capitalize(s):
    a = b = ''
    for i in range(len(s)):
        if i % 2 == 0:
            a += s[i].upper()
            b += s[i].lower()
        else:
            a += s[i].lower()
            b += s[i].upper()
    return [a,b]

def multiplication_table(size):
    respuesta = []
    lista = list(range(1,size+1))
    print(lista)
    for i in range(size):
        nueva = list(map(lambda x: x *(i+1),lista))
        respuesta.append(nueva)
    return respuesta

def flip(d, a):
    return sorted(a) if d == 'R'  else  sorted(a,reverse=True)

def build_string(*args):
    return "I like {}!".format(", ".join(args))

codigo = {'a':'1','1':'a','e':'2','2':'e','i':'3','3':'i','o':'4','4':'o','u':'5','5':'u'}

def encode(st):
    respuesta = ''
    for letra in st:
        if letra in codigo:
            respuesta += codigo.get(letra)
        else:
            respuesta += letra
    return respuesta

def decode(st):
    respuesta = ''
    for letra in st:
        if letra in codigo:
            respuesta += codigo.get(letra)
        else:
            respuesta += letra
    return respuesta

def sum_of_minimums(numbers):
    return sum(map(lambda x : min(x),numbers))

def main(verb, noun):
    return f'{verb}{noun}'

def flatten_and_sort(array):
    respuesta = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            respuesta.append(array[i][j])
    return sorted(respuesta)

def say_hello(name, city, state):
    nombre = ''
    for n in name:
        nombre += n + ' '
    return f'Hello, {nombre[:-1]}! Welcome to {city}, {state}!'

def in_asc_order(arr):
    return arr == sorted(arr)

def find_average(nums):
    return sum(nums)/len(nums)

def seats_in_theater(tot_cols, tot_rows, col, row):
    return((tot_cols-col+1)*(tot_rows-row))

def solution(digits):
    respuesta= []
    for i in range(len(str(digits))-4):
        respuesta.append(str(digits)[i:i+5])
    return max(respuesta)

def multiple_of_index(arr):
    respuesta = []
    for i in range(len(arr)):
        if arr[i] == 0:
            respuesta.append(0)
        elif i > 0 and arr[i] % i == 0:
            respuesta.append(arr[i])
    return respuesta

def array_madness(a,b):
    return sum(list(map(lambda x : x ** 2 , a))) > sum(list(map(lambda x : x ** 3 , b)))

websites = []
for i in range(1000):
    websites.append('codewars')

def remainder(a,b):
    return None if min(a,b) == 0 else max(a,b) % min(a,b)

def row_weights(array):
    a = b = 0
    for i in range(len(array)):
        if i % 2 == 0:
            a += array[i]
        else:
            b += array[i]
    return (a,b)

def string_clean(s):
    n = '1234567890'
    r = ''
    for c in s:
        if c not in n:
            r += c
    return r

def parse(data):
    init = 0
    respuesta = []
    for i in range(len(data)):
        if data[i] == 'i':
            init += 1
            print(data[i], init)
        elif data[i] == 'd':
            init -= 1
            print(data[i])
        elif data[i] == 's':
            init = init ** 2
            print(data[i])
        elif data[i] == 'o':
            respuesta.append(init)
            print(data[i])
    return respuesta

def good_vs_evil(good, evil):
    bien = good.split(' ')
    mal = evil.split(' ')
    total_bien = int(bien[0])*1+int(bien[1])*2+int(bien[2])*3+int(bien[3])*3+int(bien[4])*4+int(bien[5])*10
    total_mal = int(mal[0])*1+int(mal[1])*2+int(mal[2])*2+int(mal[3])*2+int(mal[4])*3+int(mal[5])*5+int(mal[6])*10
    if total_bien > total_mal:
        return 'Battle Result: Good triumphs over Evil'
    elif total_bien < total_mal:
        return 'Battle Result: Evil eradicates all trace of Good'
    else:
        return 'Battle Result: No victor on this battle field'

def derive(coefficient, exponent): 
    return f'{coefficient * exponent}x^{exponent-1}'

def cube_checker(volume, side):
    return volume == side ** 3 and volume > 0 and side > 0

def cookie(x):
    if isinstance(x,str):
        return 'Who ate the last cookie? It was Zach!'
    elif type(x) is bool:
        return 'Who ate the last cookie? It was the dog!'
    else:
        return 'Who ate the last cookie? It was Monica!'
    
def multiply(n):
    return n * (5**int(len(str(n)))) if n>0 else n * (5**int(len(str(n*-1))))

def billboard(name, price=30):
    costo = 0
    for i in range(len(name)):
        costo += price
    return costo

def digits(n):
    return int(len(str(n)))

def even_numbers(arr,n):
    respuesta = []
    for i in range(len(arr)):
        print(i,arr[len(arr)-1-i])
        if arr[-i-1]%2 == 0:
            respuesta.insert(0,arr[len(arr)-1-i])
        if len(respuesta) == n:
            break
    return respuesta

def factorial(n):
    resultado = 1
    for i in range(n,0,-1):
        resultado *= i
    return resultado

def evaporator(content, evap_per_day, threshold):
    dias = 0
    resultado = 100
    evapapora = 1 - evap_per_day /100
    while resultado > threshold:
        resultado *= evapapora
        dias +=1
    return dias

def get_drink_by_profession(param):
    codigo = {"Jabroni":"Patron Tequila", "School Counselor":"Anything with Alcohol","Programmer":"Hipster Craft Beer","Bike Gang Member":"Moonshine","Politician":"Your tax dollars","Rapper":"Cristal"}
    return codigo.get(param.title() ,'Beer')

def stairs_in_20(stairs):
    return (sum(stairs[0])+sum(stairs[1])+sum(stairs[2])+sum(stairs[3])+sum(stairs[4])+sum(stairs[5])+sum(stairs[6]))*20

def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        shark_speed /= 2
    mi_tiempo = pontoon_distance / you_speed
    tiempo_tiburon = shark_distance / shark_speed
    return 'Alive!' if mi_tiempo < tiempo_tiburon else 'Shark Bait!'

import math
def calculate_tip(amount, rating):
    propina = {'terrible': 0, 'poor':5,'good':10,'great':15,'excellent':20}
    return math.ceil(amount * (propina.get(rating.lower())/100)) if rating.lower() in propina else 'Rating not recognised'

def is_vow(inp):
    return [chr(num) if num in {97, 101, 105, 111, 117} else num for num in inp]

def remove(st):
    while st[len(st)-1:len(st)] == '!':
        st = st[0:len(st)-1]
    return st

def adjacent_element_product(array):
    maximo = array[0] *array[1]
    for i in range(len(array)-1):
        if array[i]* array[i+1] > maximo:
            maximo = array[i]* array[i+1]
    return maximo

def sort_gift_code(code):
    return ''.join(sorted(code))

import re
regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,}$"

def check(a, x): 
    return x in a

def who_is_paying(name):
    return [name, name[:2]] if len(name)>2 else [name[:2]]

def is_leap_year(year):
    return year % 100 != 0 and year % 4 == 0 or year % 400 == 0

def format_money(amount):
    return '${:.2f}'.format(amount)

def is_digit(n):
    return n.isdigit() and len(n) == 1

def vowel_indices(word):
    respuesta = []
    for i in range(len(word)):
        if word[i] in 'aeiouAEIOUyY':
            respuesta.append(i+1)
    return respuesta

def filter_string(st):
    resultado = ''
    for a in st:
        if a in '1234567890':
            resultado += a
    return int(resultado)

def shorten_to_date(long_date):
    return long_date.split(",")[0]

def vert_mirror(strng):
    return '\n'.join([line[::-1] for line in strng.split('\n')])
def hor_mirror(strng):
    return '\n'.join(strng.split('\n')[::-1])
def oper(fct, s):
    return fct(s)

import re
def remove(st, n):
    return re.sub(r'!', '', st, n)

def generate_shape(n):
    rta=''
    for i in range(n):
        rta +='+'*n+'\n'
    return rta[:-1]

def gps(s, x):
    if len(x)<2:
        return 0
    a = x[1]-x[0]
    for i in range(len(x)-1):
        if a < x[i+1]-x[i]:
            a = x[i+1]-x[i]
    return int(a*3600 / s)

def remove_duplicate_words(s):
    separo = s.split(' ')
    respuesta = ''
    for palabra in separo:
        if palabra not in respuesta:
            respuesta += palabra + ' '
    return respuesta[:-1]

import re
def validate_code(code):
    return bool(re.match(r'^[123]', str(code)))

def quote(fighter):
    return "I'd like to take this chance to apologize.. To absolutely NOBODY!" if fighter.lower() == 'conor mcgregor' else "I am not impressed by your performance."

def duck_duck_goose(players, goose):
    return players[(goose - 1) % len(players)].name

def greet(name): 
    return f'Hello {name.capitalize()}!'

def _all(seq, fun): 
    return all(map(fun,seq))

def number_to_pwr(number, p): 
    resultado = 1
    for i in range(p):
        resultado *= number
    return resultado

def uefa_euro_2016(teams, scores):
    if scores[0]>scores[1]:
        return f'At match {teams[0]} - {teams[1]}, {teams[0]} won!' 
    elif scores[0]<scores[1]:
        return f'At match {teams[0]} - {teams[1]}, {teams[1]} won!'
    else:
        return f'At match {teams[0]} - {teams[1]}, teams played draw.'

def to_float_array(arr): 
    return list(map(float, arr))

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
     return int(((age_1**2+age_2**2+age_3**2+age_4**2+age_5**2+age_6**2+age_7**2+age_8**2)**0.5)/2)

def sum_of_differences(arr):
    if len(arr)<2:
        return 0
    nuevo = sorted(arr,reverse=True)
    resultado = 0
    for i in range(len(nuevo)-1):
        resultado += nuevo[i]-nuevo[i+1]
    return resultado

def show_sequence(n):
    if n > 0:
        resultado=0
        texto = ''
        for i in range(n+1):
            resultado += i
            texto += str(i) + '+'
        return texto[:-1] + ' = ' + str(resultado)
    elif n == 0:
        return '0=0'
    else:
        return f'{n}<0'

def spacify(string):
    respuesta = ''
    for letra in string:
        respuesta += letra + ' '
    return respuesta[:-1]

def usdcny(usd):
    return f'{(usd*6.75):.2f} Chinese Yuan'

websites.append('codewars')

def get_even_numbers(arr):
    return list(filter(lambda x: x%2 == 0,arr))

def max_rot(n):
    texto = str(n)
    parcial = [n]
    for i in range(len(texto)):
        texto = texto[:i] + texto[i+1:] + texto[i]
        parcial.append(int(texto))
    return max(parcial)

odds = lambda x: list(filter(lambda n: n % 2 != 0, x))

def folding(a, b):
    cuadrados = 0
    while a !=0 and b !=0:
        if a < b:
            a,b = b,a
        cuadrados += a // b
        a = a % b
    return cuadrados

def whatday(num):
    dias = {1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',7:'Saturday'}
    return dias.get(num) if num < 8 and num > 0 else 'Wrong, please enter a number between 1 and 7'

def square_area(A):
    return round((2 * A / math.pi) ** 2, 2)

def solution(arr_val, arr_unit) :
    peso = {'kg': 1,'g' : 0.001,'mg' : 1e-6,'μg' : 1e-9,'lb' : 0.453592}
    distancia = {'m' : 1,'cm' : .01,'mm' : .001,'μm' : 1e-6,'ft' : 0.3048}
    return 6.67e-11 * (arr_val[0] * peso[arr_unit[0]]) * (arr_val[1] * peso[arr_unit[1]]) / (arr_val[2] * distancia[arr_unit[2]])**2

def power_of_two(x):
    return x > 0 and (x & (x - 1)) == 0

def reverse(lst):
    result = list()
    while lst:
        result.append(lst.pop())
    return result
