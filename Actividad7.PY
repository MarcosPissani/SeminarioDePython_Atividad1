import random
# Preguntas para el juego
questions = ("¿Qué función se usa para obtener la longitud de una cadena en Python?","¿Cuál de las siguientes opciones es un número entero en Python?","¿Cómo se solicita entrada del usuario en Python?","¿Cuál de las siguientes expresiones es un comentario válido en Python?","¿Cuál es el operador de comparación para verificar si dos valores son iguales?",)
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [("size()", "len()", "length()", "count()"),("3.14", "'42'", "10", "True"),("input()", "scan()", "read()", "ask()"),("// Esto es un comentario", "/* Esto es un comentario */","-- Esto es un comentario","# Esto es un comentario",),("=", "==", "!=", "==="),] # Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
numero_de_preguntas = 1
valido = True
puntos = 0
6. 
7. 
1. 
2. 
3. 
# El usuario deberá contestar 3 preguntas
 # Se selecciona tres pregunta aleatoria
questions_to_ask = random.sample(list(zip(questions,answers, correct_answers_index)), k=3)
 # Se muestra la pregunta y las respuestas posibles
for question,answer,correct_answers in questions_to_ask:
     if(valido):
         print(question)
         for i in range(4):
             print(f"{i + 1}, {answer[i]}")
# El usuario tiene 2 intentos para responder correctamente
         for intento in range(2):
             user_answer = int(input("Respuesta: "))-1
# Se verifica si la respuesta es correcta

             if user_answer < 0 or user_answer >= 4 :
                 print("respuesta no valida")
                 valido = False
                 break
             else:
                 if (user_answer == correct_answers):
                     print("¡Correcto!")
                     puntos += 1
                     break
                 else:
                     print("respuesta no valida")
                     puntos -= 0.5
 # Si el usuario no responde correctamente después de 2 intentos,
 # se muestra la respuesta correcta 
             print("Incorrecto. La respuesta correcta es la opcion :")
             print(correct_answers)
 # Se imprime un blanco al final de la pregunta
     numero_de_preguntas += 1
print("la cantidad de puntos obtenidos en el juego es de  : ", puntos)