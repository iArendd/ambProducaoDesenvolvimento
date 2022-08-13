from decouple import config


'''Busca o arquivo .env, o primeiro parâmetro é a variável que estamos buscando, 
    o segundo parâmetro é o estado padrão dessa variável caso seja encontrado nada,
    o terceiro padâmetro é o tipo de dado que essa variável será considerada.'''
DEBUG = config("DEBUG", default="False", cast=bool)

print(type(DEBUG))


if(DEBUG):

    print('A variável DEBUG no .env é True')

