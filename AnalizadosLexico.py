import re
import html

tokens = [
    ('Llave abrir', r'\{'),
    ('Llave cerrar', r'\}'),
    ('Dos puntos', r'\:'),
    ('Corchete abrir', r'\['),
    ('Corchete cerrar', r'\]'),
    ('Coma', r'\,'),
    ('Parentesis abrir', r'\('),        # Paréntesis abrir
    ('Parentesis cerrar', r'\)'),       # Paréntesis cerrar
    ('Igual', r'\='), 
    ('Punto y Coma', r'\;'),
    ('Cadena', r'\".*?\"'),
    ('Guion', r'\-'),
    ('Asterisco', r'\*'),
    ('Diagonal', r'\/'),
    ('Comillas arriba', r'\“'),
    ('Comillas abajo', r'\”'),
    ('Comillas normales', r'\"'),
    ('Signo de dollar', r'\$'),
    ('Comillas_simples', r"'"),
    ('Cadena', r'[a-zA-ZáéíóúÁÉÍÓÚüÜ_][a-zA-ZáéíóúÁÉÍÓÚüÜ0-9_]*'),  # Identificadores
    ('Espacios', r'\s+')
]

def analizador_lexico(datos):
    global lista_tokens_no_validos
    global lista_tokens_validos
    lista_tokens_validos = []
    lista_tokens_no_validos = []
    num_linea = 1
    num_columna = 1

    while datos:
        token_encontrado = False

        for token_nom, patron_exp in tokens:
            patron = re.compile(patron_exp)
            coincidencia = patron.match(datos)

            if coincidencia:
                valor = coincidencia.group(0)
                if token_nom != 'Espacios':
                    lista_tokens_validos.append((token_nom, valor, num_linea, num_columna))
                token_encontrado = True
                datos = datos[len(valor):]
                num_columna += len(valor)
                break

        if not token_encontrado:
            lista_tokens_no_validos.append(('Caracter no valido', datos[0], num_linea, num_columna))
            datos = datos[1:]
            num_columna += 1

        if datos and datos[0] == '\n':
            num_linea += 1
            num_columna = 1
            datos = datos[1:]

    return lista_tokens_validos, lista_tokens_no_validos


tabla_html = ''
tabla_html_novalidos = ''

def generar_tabla_html():
    global tabla_html, tabla_html_novalidos
    tabla_html = '<div style="margin: 0 auto; width: fit-content;">\n'
    tabla_html += '<div style="text-align: center;"><h2>Tabla de Tokens Válidos</h2></div>\n'
    tabla_html += '<table border="1">\n'
    tabla_html += '<tr><th>Token</th><th>Lexema</th><th>Número de línea</th><th>Número de columna</th></tr>\n'

    tabla_html_novalidos = '<div style="margin: 0 auto; width: fit-content;">\n'
    tabla_html_novalidos += '<div style="text-align: center;"><h2>Tabla de Caracteres No Válidos</h2></div>\n'
    tabla_html_novalidos += '<table border="1">\n'
    tabla_html_novalidos += '<tr><th>Carácter</th><th>Número de línea</th><th>Número de columna</th></tr>\n'

    for token in lista_tokens_validos:
        tabla_html += f'<tr><td>{token[0]}</td><td>{token[1]}</td><td>{token[2]}</td><td>{token[3]}</td></tr>\n'

    for token_no_v in lista_tokens_no_validos:
        tabla_html_novalidos += f'<tr><td>{token_no_v[1]}</td><td>{token_no_v[2]}</td><td>{token_no_v[3]}</td></tr>\n'

    tabla_html += '</table>\n</div>\n'
    tabla_html_novalidos += '</table>\n</div>\n'
    return tabla_html, tabla_html_novalidos

def generar_archivo_html():
    global tabla_html, tabla_html_novalidos
    with open("C:/Users/danis/OneDrive/Documents/Quinto Semestre/LFP/[LFP]Proyecto2/tabla_tokens.html", "w") as archivo:
        archivo.write("<!DOCTYPE html>\n")
        archivo.write("<html>\n<head>\n<title>Tabla de Tokens</title>\n</head>\n<body>\n")
        archivo.write(tabla_html)
        archivo.write(tabla_html_novalidos)
        archivo.write("\n</body>\n</html>")