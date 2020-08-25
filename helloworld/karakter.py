karakter = {'Programmering':12, 'Dansk':10, 'Kom/IT':7, 'Idehistorie':4, 'Psykologi':2, 'Teknik':0}

def udskrivEnKarakter(fag, bog):
    if fag in bog.keys():
        print('Karakter i {}: {}'.format(fag, bog[fag]))
    else:
        print('Fejl. Der findes ingen karakter for {} i den angivne karakterbog.'.format(fag))

udskrivEnKarakter('Programmering', karakter)
udskrivEnKarakter('Matematik', karakter)

def udskrivAlleKarakterer(k):
    for fag in k.keys():
        udskrivEnKarakter(fag, k)

udskrivAlleKarakterer(karakter)
