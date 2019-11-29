import re #libreria de expresiones regulares

path = "Palabras.java"

try:
    archivo = open(path,'r')
except:
    print ("El archivo que intentaste abrir no existe")
    quit()

texto=""

for linea in archivo:
    texto += linea
print(texto)

#ACTIVIDADES UNIDAD 4
print("\t\t\tACTIVIDADES DE LA UNIDAD 4")
#Actividad 1
patron = r"\b[a-zA-Z]{3,7}\b [a-zA-Z]{1,}[0-9]*?\;"
result = re.findall(patron,texto)
#print ("\nVariables: ", result)
print ("\nVariables: ")
n = 0 
for i in result:
	pat = r"\b[a-zA-Z]{1,}[0-9]*?\;"
	x = re.findall(pat,i)
	n=n+1
	print("[",n,"] .- ", x, end=" \n")

#Actividad 2
patron = r"(\b[0-9]{1,}\.[0-9]{1,}\b|\b[0-9]{1,}\b)"
result = re.findall(patron,texto)
print ("\nEnteros y decimales: ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividad 3
patron = r"\b(\%|\*|\/|\+|\-)"
result = re.findall(patron,texto)
print ("\nOperadores aritméticos: ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividad 4
patron = r"(\>\=|\<\=|\=\=|\!\=|\>|\<)"
result = re.findall(patron,texto)
print ("\nOperadores relacionales: ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividad 5
patron = r"\b(import|public|static|void|for|while|int|float|String|boolean|return)\b"
result = re.findall(patron,texto)
print ("\nPalabras reservadas de JAVA: ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividades Unidad 5
print("\t\t\tACTIVIDADES DE LA UNIDAD 5")
#Actividad 1
patron = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][ |\S][\w|\d.\d]{1,}\;"
result = re.findall(patron,texto)
print ("\nOperaciones aritméticas básicas: ")
#[a-zA-Z]{1,}[\d\S|\d\s|\s|\S]{1,}\=[\S|\s][\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][ |\S][\w|\d.\d]{1,}\;
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividad 2
patron = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}\;"
result = re.findall(patron,texto)
print ("\nSentencia de asignación: ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")

#Actividad 3
patron = r"([\w|\d.\d]{1,}[\S|\s](\<|\>|\=\=|\<\=|\>\=|\!\=)[\s|\S][\w|\d.\d]{1,}[\;|\s])"
result = re.findall(patron,texto)
print ("\nExpresiones booleanas básicas: ")
#([\w|\d.\d]{1,}[\S|\s](\!\=|\>\=|\<\=|\=\=|\<|\>)[\s|\S][\w|\d.\d]{1,}[\;|\s])
for i in range(len(result)):
	for j in range(len(result[i])):
		if j==0:
			print([i+1], ".- ",result[i][j], end=" \n")

#Actividad 4
patron = r"[a-zA-Z]{1,}[\d|\s]{1,}\=[\s|\w|\d.\d]{1,}[\s|\S][\*|\/|\%|\+|\-][\s|\]\([\w|\d.\d]{1,}[\S|\s][\*|\/|\%|\+|\-][\S|\s][\w|\d.\d]{1,}[ \)|\S\)]\;"
result = re.findall(patron,texto)
print ("\nFormulas más complejas del tipo c = a op ( b op d): ")
for i in range(len(result)):
	print([i+1], ".- ",result[i], end=" \n")


#Actividad 5
patron = r"((\b(if)[\S|\s]\([\S|\s][\w|\d.\d]{1,}[\S|\s](\<|\>|\=\=|\<\=|\>\=|\!\=)[\S|\s][\w|\d.\d]{1,}\))|(\b(while)[\S|\s]\([\S|\s][\w|\d.\d]{1,}[\S|\s](\<|\>|\=\=|\<\=|\>\=|\!\=)[\S|\s][\w|\d.\d]{1,}\))|(\b(for)[\S|\s](int|)[\S|\s]\w{0,}[\s|\S]\=[\s|\S]\d{0,}\;[\S|\s]\w{0,}[\s|\S](\!\=|\>\=|\<\=|\=\=|\<|\>)[\s|\S]\d{0,}\;[\S|\s]\w{0,}\+\+[\S|\s]))"
#(\b(if)[\S|\s]\([\S|\s][\w|\d.\d]{1,}[\S|\s](\<|\>|\=\=|\<\=|\>\=|\!\=)[\S|\s][\w|\d.\d]{1,}\))
#(\b(while)[\S|\s]\([\S|\s][\w|\d.\d]{1,}[\S|\s](\<|\>|\=\=|\<\=|\>\=|\!\=)[\S|\s][\w|\d.\d]{1,}\))
#(\b(for)[\S|\s](int|)[\S|\s]\w{0,}[\s|\S]\=[\s|\S]\d{0,}\;[\S|\s]\w{0,}[\s|\S](\!\=|\>\=|\<\=|\=\=|\<|\>)[\s|\S]\d{0,}\;[\S|\s]\w{0,}\+\+[\S|\s])
result = re.findall(patron,texto)
print ("\nEl encabezado de estructura de control. if, while, for, etc.: ")
for i in range(len(result)):
	for j in range(len(result[i])):
		if j==0:
			print([i+1], ".- ",result[i][j], end=" \n")
