import os
import hashlib as hs
from PySimpleGUI import (
    theme,
    Window,
    Button,
    Text,
    Combo,
    InputText,
    WIN_CLOSED,
)

def methodsHASH(paramSha, callDictId):
    dictSha = {
        'md5': hs.md5(callDictId),
        'sha1': hs.sha1(callDictId),
        'sha224': hs.sha224(callDictId),
        'sha256': hs.sha256(callDictId),
        'sha384': hs.sha384(callDictId),
        'sha512': hs.sha512(callDictId),
        'blake2b': hs.blake2b(callDictId),
        'blake2s': hs.blake2s(callDictId),
        'sha3_224': hs.sha3_224(callDictId),
        'sha3_256': hs.sha3_256(callDictId),
        'sha3_384': hs.sha3_384(callDictId),
        'sha3_512': hs.sha3_512(callDictId),
    }
    return dictSha[paramSha].hexdigest()


def hackSha(callDictId:str, paramSha:str, rutDict=None) -> list:
    if rutDict == None:
        rutDict = 'pass/dictpassword.txt'
    openDict = open(os.path.abspath(rutDict), 'r').readlines()
    return openDict[list(map(lambda iterDic: methodsHASH(paramSha, iterDic.replace('\n', '').encode('utf-8')), openDict)).index(callDictId)].replace('\n', '')


def layout() -> list:
    size = ()
    listSha = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512',
               'blake2b', 'blake2s', 'sha3_224', 'sha3_256', 'sha3_384', 'sha3_512']
    options = ['revelar', 'convertir']
    return [
        [Text('Encriptador')],
        [Combo(listSha, key='listsha'), Combo(options, key='options')],
        [Text('Introduce Tu string: '), InputText(key='stringuser')],
        [Text('Resultado es: '), InputText(key='stringresult')],
        [Text('Nombre Diccionario: '), InputText(key='abspath')],
        [Button('convertir')],
    ]


def init():
    theme('reddit')
    window = Window('CriptoHash', layout())
    while True:
        event, values = window.read()

        if event == 'convertir':
            listsha = values['listsha']
            stringuser = values['stringuser']
            options = values['options']
            abspath = values['abspath']

            if values['options'] == 'revelar':
                if abspath != '':
                    rutdict = f'pass/{abspath}.txt'
                else:
                    rutdict = None
                try:
                    resultDes = hackSha(stringuser, listsha, rutDict = rutdict)
                except ValueError as VL:
                    # print(VL)
                    resultDes = 'No Se Pudo Revelar'
                window['stringresult'].update(resultDes)

            elif values['options'] == 'convertir':
                resultConvert = methodsHASH(
                    listsha, stringuser.encode('utf-8'))
                window['stringresult'].update(resultConvert)

        if event == WIN_CLOSED:
            break

if __name__ == '__main__':
    init()
