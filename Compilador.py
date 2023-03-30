ERR = -1  # valor que indica un error en la matriz de transiciones o en la entrada.
ACP = 99 #valor que indica que se ha alcanzado un estado de aceptación.
idx = 0 #índice que se utiliza para recorrer la entrada.
cERR = False # variable booleana que se utiliza para indicar si ha ocurrido un error durante el análisis léxico.
tok = ''# variable que se utiliza para almacenar el tipo de token encontrado.
lex = ''  #  variable que se utiliza para almacenar el lexema encontrado.
bPrinc = False # variable booleana que se utiliza para indicar si se está analizando el programa principal.
ren = 1 # variable que se utiliza para almacenar el número de línea actual.
colu = 0  # variable que se utiliza para almacenar el número de columna actual.
pTipos = []

cTipo = ["E=E", "A=A", "R=R", "L=L", "R=E",
        "E+E", "E+R", "R+E", "R+R", "A+A",
        "E-E", "E-R", "R-E", "R-R",
        "E*E", "E*R", "R*E", "R*R",
        "E/E", "E/R", "R/E", "R/R",
        "E\37E", "-E", "-R",
        "LyL", "LoL", "noL",
        "E>E", "R>E", "E>R", "R>R",
        "E<E", "R<E", "E<R", "R<R",
        "E>=E", "R>=E", "E>=R", "R>=R",
        "E<=E", "R<=E", "E<=R", "R<=R",
        "E<>E", "R<>E", "E<>R", "R<>R", "A<>A",
        "E==E", "R==E", "E==R", "R==R", "A==A"
]

tipoR = ["",  "",  "",  "",  "",
        "E", "R", "R", "R", "A",
        "E", "R", "R", "R",
        "E", "R", "R", "R",
        "R", "R", "R", "R",
                                          "E", "E", "R",
                                          "L", "L", "L",
                                          "L", "L", "L", "L",
                                          "L", "L", "L", "L",
                                          "L", "L", "L", "L",
                                          "L", "L", "L", "L",
                                          "L", "L", "L", "L", "L",
                                          "L", "L", "L", "L", "L"
]

def buscaTipo(cadt):
    for i in range(55):
        if cTipo[i]==cadt: return i
    return -1


class objPrgm():
    def __init__(self, nom, cls, tip, dim1, dim2, apv) -> None:
        self.nombre = nom
        self.clase = cls
        self.tipo = tip
        self.dim1 = dim1
        self.dim2 = dim2
        self.apv = apv

class TabSimb():
    arreglo = []
    def inserSimbolo(self, nom, cls, tip, dim1, dim2, apv):
        obj = objPrgm(nom, cls, tip, dim1, dim2, apv)
        self.arreglo.append( obj )

    def buscaSimbolo(self, ide):
        for x in self.arreglo:
            if x.nom == ide: return x
        return None
    
    def grabaTabla(self, archSal):
        with open(archSal, 'r') as aSal:
            if aSal == None: return 

        with open(archSal, 'w') as aSal:
            for x in tabSimb:
                aSal.write(x.nom +',' + x.clas + ',' + x.tip + ',' + \
                           x.dim1 + ','+ x.dim2 + ',#')
            aSal.close()
        return

class codigo():
    def __init__(self, mnem, dir1, dir2):
        self.mnemo = mnem
        self.dir1 = dir1
        self.dir2 = dir2
linCod = 1    
class Programa():
    cod = []
    def insCodigo(self, mnemo, dir1, dir2):
        global linCod
        x = codigo(mnemo, dir1, dir2)
        self.cod[linCod] = x
        linCod = linCod + 1


tabSimb = TabSimb()  

prgmCod = Programa()

pilaTipos = []

def erra(terr, desc):
    #imprimir un mensaje de error en la salida estándar, indicando el tipo de error y la posición en la que se ha producido. 
    #La función actualiza las variables globales ren y colu, y establece la variable booleana cERR en True para indicar que se ha producido un error durante el análisis léxico.
    global ren, colu
    global cERR
    print('['+str(ren)+']'+'['+str(colu)+']', terr, desc)
    cERR = True

matran=[
    #let  dig  del  opa   <    >    =    .   "
    [1,   2,   6,   5,    10,  8,   7,  ERR, 12], #0
    [1,   1,   ACP, ACP, ACP, ACP, ACP, ACP,ACP], #1
    [ACP, 2,   ACP, ACP, ACP, ACP, ACP,  3, ACP], #2
    [ERR, 4,   ERR, ERR, ERR, ERR, ERR, ERR,ERR], #3
    [ACP, 4,   ACP, ACP, ACP, ACP, ACP, ACP,ACP], #4
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,ACP], #5
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,ACP], #6
    [ACP, ACP, ACP, ACP, ACP, ACP,  9,  ACP,ACP], #7
    [ACP, ACP, ACP, ACP, ACP, ACP,  9,  ACP,ACP], #8
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,ACP], #9
    [ACP, ACP, ACP, ACP, ACP, 11,    9, ACP,ACP], #10
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,ACP], #11
    [12,   12,  12,  12,  12,  12,  12,  12, 13], #12
    [ACP, ACP, ACP, ACP, ACP, ACP, ACP, ACP,ACP]  #13
]

tipo = ['nulo', 'entero', 'decimal', 'palabra', 'logico'] # lista de strings que contiene los tipos de datos que puede manejar el lenguaje.
opl = ['no', 'y', 'o'] #lista de strings que contiene los operadores lógicos que puede manejar el lenguaje.
ctl= ['verdadero', 'falso'] # lista de strings que contiene las constantes lógicas que puede manejar el lenguaje.
key= ['constante', 'desde', 'si', 'hasta', 'mientras', 'entero', 'decimal', 'regresa', 'hacer',
      'palabra', 'logico', 'nulo', 'sino', 'incr' 'imprime', 'imprimenl', 'lee', 'repite', 'que'] # lista de strings que contiene las palabras clave del lenguaje.
opar=['+', '-', '*', '/', '%', '^'] #lista de strings que contiene los operadores aritméticos que puede manejar el lenguaje.
deli=[';', ',', '(',')', '{', '}', '[', ']', ':'] # lista de strings que contiene los delimitadores que puede manejar el lenguaje.
delu=[' ', '\t', '\n']# lista de strings que contiene los caracteres especiales que se pueden ignorar durante el análisis léxico.
opRl = ['<', '>', '<=', '>=', '<>']  #lista de strings que contiene los operadores relacionales que puede manejar el lenguaje.
tkCts = ['Ent', 'Dec', 'CtA', 'CtL'] # lista de strings que contiene los tokens correspondientes a las constantes enteras, decimales, caracteres y lógicas.
entrada = ''
def colCar(x):
    # se encarga de asignar un valor numérico a cada símbolo del alfabeto del lenguaje. 
    # Este valor se utiliza como índice en la matriz de transiciones para determinar el siguiente estado. Si el símbolo no pertenece al alfabeto del lenguaje se genera un error léxico.
    if x == '_' or x.isalpha(): return 0 
    if x.isdigit(): return 1
    if x in deli: return 2
    if x in opar: return 3
    if x == '<': return 4   
    if x == '>': return 5   
    if x == '=': return 6   
    if x == '.': return 7
    if x == '"': return 8
    if x == '/' : return 13
    if x in delu: return 15
    erra('Error Lexico', x + ' simbolo no valido en Alfabeto')
    return ERR


def scanner():
    # es la que se encarga de analizar la entrada y generar los tokens correspondientes. Para esto, se recorre la entrada caracter por caracter y se va consultando la matriz de transiciones para determinar el siguiente estado. 
    # Si se llega a un estado de aceptación, se genera el token correspondiente y se guarda el lexema en la variable lex. Si se llega a un estado de error, se genera un mensaje de error y se marca la variable cERR como verdadera.
    global entrada, ERR, ACP, idx, ren, colu
    estado = 0
    lexema = ''
    c = ''
    col = 0
    while idx < len(entrada) and \
          estado != ERR and estado != ACP: 
          c = entrada[idx]
          idx = idx + 1
          if c == '\n':
              colu = 0
              ren = ren + 1

          col = colCar(c)
          if estado == 0 and col == 15: 
            continue;
          if col >= 0 and col <= 8 or col == 15:
            if col == 15 and estado != 12: 
                estado = ACP
            if col >=0 and col <= 8:
                estado = matran[estado][col]
            if estado != ERR and estado != ACP and col != 15 or col == 15 and estado == 12:
                estA = estado
                lexema = lexema + c
            
            if c != '\n': colu = colu + 1

    if estado != ACP and estado != ERR: estA = estado;
    token = 'Ntk'
    if estado == ACP and col != 15: 
        idx = idx - 1
        colu = colu - 1

    if estado != ERR and estado != ACP:
        estA = estado

    if lexema in key: token = 'Res'
    elif lexema in opl: token = 'OpL'
    elif lexema in ctl: token = 'CtL'
    else: token = 'Ide'

    if estA == 2: token = 'Ent'
    elif estA == 4: token = 'Dec'
    elif estA == 5: token = 'OpA'
    elif estA == 6: token = 'Del'
    elif estA == 7: token = 'OpS'
    elif estA in [8, 9 , 10 , 11]: token = 'OpR'
    elif estA == 13: token = 'CtA'

    if token == 'Ntk':
        print('estA=', estA, 'estado=', estado)


    return token, lexema

def cte():
    global tok, lex, prgmCod 
    if not(tok in tkCts):
        erra('Error de sintaxis', 'se esperaba Cte y llego '+ lex)
    else:
        if tok == 'CtA' or tok == 'Ent' or tok == 'Dec':
           prgmCod.insCodigo('LIT', lex, '0')
        if tok == 'CtL':
            if lex == 'verdadero':
                prgmCod.insCodigo('LIT', 'V', '0')
            elif lex == 'falso':
                prgmCod.insCodigo('LIT', 'F', '0') 


def termino():
    global lex, tok
    if lex != '(' and tok != 'Ide' and tok != 'CtA' and \
        tok != 'CtL' and tok != 'Ent' and 'Dec':
        tok, lex = scanner()
    if lex == '(':
        tok, lex = scanner()
        expr()
        if lex != ')':
            erra('Error de Sintaxis', 'se espera cerrar ) y llego '+ lex)
    elif tok == 'Ide':
        nomIde = lex
        tok, lex = scanner()
        if lex == '[': 
            tok, lex = scanner()
            expr()
            if lex != ']':
                erra('Error Sintaxis', 'se esperaba cerrar ] y llego '+lex)
        elif lex == '(': pass
        oIde = tabSimb.buscaSimbolo(nomIde)
        if oIde != None:
            pilaTipos.append(oIde.tip)
        else:
            erra("Error de Semantica", 'Identificador no declarado '+ nomIde) 
            pilaTipos('I')
    elif tok == 'CtL' or tok == 'CtA' or tok == 'Dec' or tok == 'Ent': 
        cte()
    if lex != ')':  
        tok, lex = scanner()

def signo():
    global lex, tok
    if lex == '-':
        tok, lex = scanner()
    termino()


def expo():
    global tok, lex
    opr = '^'
    while opr == '^':
        signo()
        opr = lex


def multi():
    global tok, lex
    opr = '*'
    while opr == '*' or opr == '/' or opr == '%':
        expo()
        opr = lex

def suma():
    global tok, lex
    opr = '+'
    while opr == '+' or opr == '-':
        multi()
        opr = lex

def oprel():
    global tok, lex
    opr = '<'
    while opr in opRl:
        suma()
        opr = lex

def opno(): 
    global lex, tok
    if lex == 'no':
        tok, lex = scanner()
    oprel()

def opy():
    global tok, lex
    opr = 'y'
    while opr == 'y':
        opno()
        opr = lex

def expr():
    global tok, lex
    opr = 'o'
    while opr == 'o':
        opy()
        opr = lex

def coment():
    global tok, lex
    opr = '/'
    if opr == '/':
        while lex != "":
            pass



def constVars():
        global entrada, idx, tok, lex
        tok, lex = scanner()

def params(): 
    global entrada, lex, tok
    tok, lex = scanner()
    if tok != 'tipo':
        erra("Error de sintaxis", "Se espera una variable y se recibio " + tok+ lex)
    
   


def gpoExp():
    global tok, lex, prgmCod
    if lex != ')':
        deli=','
        while deli == ',':
            if lex == ',': 
                tok, lex = scanner()
            expr()
            deli = lex
            #if deli == ',': 
                #genCod(linea, 'OPR 0, 20)


def leer(): pass

def imprime(): 
    global tok, lex, prgmCod
    tok, lex = scanner()
    if lex != '(':
        erra('Error de Sintaxis', 'se esperaba abrir ( y llego '+ lex)
    tok, lex = scanner()
    if lex != ')': gpoExp()
    if lex != ')': tok, lex = scanner()
    if lex != ')':
        erra('Error de Sintaxis', 'se esperaba cerrar ) y llego '+ lex)
    prgmCod.insCodigo('OPR', '0', '20')

def imprimenl(): 
    global tok, lex, prgmCod 
    tok, lex = scanner()
    if lex != '(':
        erra('Error de Sintaxis', 'se esperaba abrir ( y llego '+ lex)
    tok, lex = scanner()
    if lex != ')': gpoExp()
    if lex != ')': tok, lex = scanner()
    if lex != ')':
        erra('Error de Sintaxis', 'se esperaba cerrar ) y llego '+ lex)
    prgmCod.insCodigo('OPR', '0', '21')


def desde():
    global tok, lex
    tok, lex = scanner()
    if lex != '(':
        erra('Error de Sintaxis', 'se esperaba abrir ( y llego '+ lex)
    tok, lex = scanner()
    if lex != ')': params()
    if lex != ')': tok, lex = scanner()
    if lex != ')':
        erra('Error de Sintaxis', 'se esperaba cerrar ) y llego '+ lex)
    tok,lex = scanner()    
    if lex != '{':
        erra('Error de Sintaxis', 'se esperaba abrir { y llego '+ lex)
    tok,lex = scanner()
    if lex != '}': blkcmd()
    print("si pase el desde")
    print('Mi estado del lex y del tok es' + lex, tok) 


def mientras(): 
    global tok, lex
    tok, lex = scanner()
    if lex != '(':
        erra('Error de Sintaxis', 'se esperaba abrir ( y llego '+ lex)
    tok, lex = scanner()
    if lex != ')': params()
    if lex != ')': tok, lex = scanner()
    if lex != ')':
        erra('Error de Sintaxis', 'se esperaba cerrar ) y llego '+ lex)
    tok,lex = scanner()    
    if lex != '{':
        erra('Error de Sintaxis', 'se esperaba abrir { y llego '+ lex)
    
    #entrada de parametros
    tok,lex = scanner()
    if lex != '}': blkcmd() #funcion que llama a los parametros
    print("si pase el mientras")
    print('Mi estado del lex y del tok es' + lex, tok) 

def si(): 
    global tok, lex
    tok, lex = scanner()
    if lex != '(':
        erra('Error de Sintaxis', 'se esperaba abrir ( y llego '+ lex)
    tok, lex = scanner()
    if lex != ')': gpoExp()
    if lex != ')': tok, lex = scanner()
    if lex != ')':
        erra('Error de Sintaxis', 'se esperaba cerrar ) y llego '+ lex)
    tok,lex = scanner()    
    if lex != '{':
        erra('Error de Sintaxis', 'se esperaba abrir { y llego '+ lex)
    tok,lex = scanner()
    if lex != '}': blkcmd()
    print("si pase el if")
    print('Mi estado del lex y del tok es' + lex, tok)

def repite(): pass

def lmp(): pass

def regresa(): pass

def asigLfunc(): pass

def comando(): 
    global tok, lex
    if tok == 'Ide': asigLfunc()
    if lex == 'lee': leer()
    elif lex == 'imprime': imprime()
    elif lex == 'imprimenl': imprimenl()
    elif lex == 'desde': desde()
    elif lex == 'mientras': mientras()
    elif lex == 'si': si()
    elif lex == 'repite': repite()
    elif lex == 'lmp': lmp()
    elif lex == 'regresa': regresa()
    else: erra('Error de Sintaxis', 'comando no definido '+ lex)
    tok, lex = scanner()

def blkcmd():
    global lex, tok
    tok, lex = scanner()
    if lex != ';' and lex != '{': 
        comando()
        tok, lex = scanner()
        if lex != ';': erra('Error de Sintaxis', 'se esperaba ; y llego '+lex)
    elif lex == '{':
        estatutos()
        if lex != '}': erra('Error de Sintaxis', 'se esperaba cerrar block \"}\" y llego '+ lex)

def estatutos(): 
    global tok, lex
    cbk = '{'
    while cbk != '}':
        if lex != ';': comando()
        if lex != ';': erra('Error de Sintaxis', 'se esperaba ; y llego '+lex)
        tok, lex = scanner()
        cbk = lex

def blkFunc():
    global lex, tok
    if lex != '{': erra('Error de Sintaxis', 'se esperaba abrir \"{\" y llego '+lex)
    tok, lex = scanner()
    if lex != '}': estatutos()
    if lex != '}':erra('Error de Sintaxis', 'se esperaba cerrar \"}\" y llego '+lex)



def funcs():
        global entrada, idx, tok, lex, tipo, bPrinc
        if not(lex in tipo):
            erra('Error Sintactico', 'Se esperaba tipo' + str(tipo))
        tok, lex = scanner()
        if tok != 'Ide': erra('Error Sintaxis', 'Se esperaba Nombre Funcion y llego ' + lex)
        if bPrinc: erra('Error de Semantica', 'la Funcion Principal ya esta definida') 
        if lex == 'principal': bPrinc = True
        tok, lex = scanner()      
        if lex != '(': erra('Error de Sintaxis', 'se esperaba parentisis abierto \"(\" y llego '+ lex) 
        tok, lex = scanner()      
        if lex != ')': params()
        if lex != ')': erra('Error de Sintaxis', 'se esperaba parentisis cerrado \")\"')
        tok, lex = scanner()
        blkFunc()

def comment():
    global entrada, idx, tok, lex, tipo
    if not(lex in tipo):
        tok, lex = scanner()
        if lex == '/':
            tok, lex = scanner()
            if lex != '/':
                erra("Error de sintaxis", "No es comentario puede ser division")
            elif lex == '/':
                tok = "Ide"
                print("Soy comentario y mi tok es" + tok)
                #iterando para ver si sirve
                entrada = lex
                while (entrada != ' '):
                    tok = "Ide"
                print(lex)
                
                
                


def prgm():
    while len(entrada) > 0 and  idx < len(entrada):
        comment()
        constVars()
        funcs()

def parser():
    global entrada, idx, tok, lex
    prgm()

if __name__ == '__main__':
    arche = input('Archivo (.icc) [.]=salir: ')
    if arche == '.': exit()
    archivo = open(arche, 'r')
    #se carag archivo en entrada
    entrada = ''
    for linea in archivo:
        entrada += linea
        
    print(entrada)
    parser()
    if not(cERR): print('Programa COMPILO con EXITO') 