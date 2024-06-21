#manipulacao de string (texto)

texto = """Os amigos do maestro querem que dificilmente se possa achar obra tão bem-acabada. 
Um ou outro admite certas rudezas e tais ou quais lacunas, mas com o andar da ópera é provável que estas 
sejam preenchidas ou explicadas, e aquelas desapareçam inteiramente, não se negando o maestro a emendar 
a obra onde achar que não responde de todo ao pensamento sublime do poeta. Já não dizem o mesmo os amigos deste. Juram 
que o libreto foi sacrificado, que a partitura corrompeu o sentido da letra, e, posto seja bonita em alguns lugares, e 
trabalhada com arte em outros, é absolutamente diversa e até contrária ao drama."""

#separando as frases dos texto
frases = texto.split(".")

#passando pelas frases
for frase in frases:
    #colocando todas as letras minisculas e procurando pela palavra amigo
    if "amigo" in frase.lower():
        print('amigo encontrando!')
    print("frase analisada:", frase)