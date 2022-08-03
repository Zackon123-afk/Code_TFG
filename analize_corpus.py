import spacy
import string
import nltk
from nltk import word_tokenize, TweetTokenizer
import unicodedata

#CARGAR FITXEROS Y LIBRERIAS

SPECIAL_CHARS = ['#','%','$','&','/','º','ª','¨','^','*','<','¨','{','}','>','(',')','€','=']
FINAL_MARKS = ['.','?','!']
EMOTICONOS = ['😀','😁','😂','🤣','😬','😃','😄','😊','😉','😚','😙','😗','😘','😜','😡','😠','😖','🙁',
            '☹','😱','😭','😵','🤢','🤮','😴','💩','😈','👿','👍','👎','👏','🖕','🐷','🐽','🗡','⚔','🔪',
            '🔫','💣','⚰','❤️','🧡','💛','💚','💙','💜','🖤','❣','💕','💞','💓','💗','💖','💘','💝','💟']
ONOMATOPEYAS = ['jaja','jeje','jiji','haha','hehe','ja ja','ha ha','ñaca','triqui']
INTERJECCIONES = ['ah', 'eh', 'oh', 'uh', 'uf', 'ay', 'uy']
INTERPELACIONES = ['oye','escucha','mira']
DIMINUTIVOS = ['ete','eta','ito','ita','ico','ica','illo','illa','in','ina','uelo','uela','infra','micro','sub']
AUGMENTATIVOS = ['azo','aza','on','ona','ote','ota','al','udo','uda']
PEYORATIVOS = ['ato','ata','ajo','aja','astro','astra','acho','acha','ato','ata','ejo','eja','ango','anga','engo','enga',
            'ales','alla','astro','astra','orrio','orria','orro','orra','uco','uca','ucho','ucha','uzo','uza','zuelo','uelo']
SUPERLATIVOS = ['ismo','isma','errimo','errima','archi','hiper','infra','macro','mega','super','supra','ultra']
ADVERBIOS_CANT = ['demasiado','apenas','bastante','casi','justo','mitad','mucho','muy','nada','poco','solo','tan','tanto','todo']
ADVERBIOS_NEG = ['no','nunca','ni','tampoco','jamas']
ADVERBIOS_DUD = ['quiza','quizas','probablemente','puede','posiblemente','acaso']
ADJETIVOS_CANT = ['mucho','poco','bastante','demasiado','suficiente','extremado','excesivo','absoluto','aproximado']

insu_f = open('insultos.txt','r')
temp = insu_f.read()
insultos = temp.split(sep=',')

pri_pers_f = open('1era_persona.txt','r')
temp = pri_pers_f.read()
ending_in_first_person = temp.split(sep=',')

seg_pers_f = open('2nda_persona.txt','r')
temp = seg_pers_f.read()
ending_in_second_person = temp.split(sep=',')

subj_f = open('subjuntivo.txt','r')
temp = subj_f.read()
ending_in_subj = temp.split(sep=',')

indi_f = open('indicativo.txt','r')
temp = indi_f.read()
ending_in_indi = temp.split(sep=',')

pret_f = open('preterito.txt','r')
temp = pret_f.read()
ending_in_pret = temp.split(sep=',')

futu_f = open('futuro.txt','r')
temp = futu_f.read()
ending_in_futu = temp.split(sep=',')

pres_f = open('presente.txt','r')
temp = pres_f.read()
ending_in_pres = temp.split(sep=',')

impe_f = open('imperativo.txt','r')
temp = impe_f.read()
ending_in_impe = temp.split(sep=',')

cond_f = open('condicional.txt','r')
temp = cond_f.read()
ending_in_cond = temp.split(sep=',')

pri_pers_f.close()
seg_pers_f.close()
subj_f.close()
indi_f.close()
pret_f.close()
futu_f.close()
pres_f.close()
impe_f.close()
cond_f.close()
insu_f.close()

tweet_tokenizer = TweetTokenizer()

nlp = spacy.load('es_core_news_sm')

nltk.download('stopwords', quiet=True)

##CARACTERES Y SIGNOS

#CARACTERES ESPECIALES

#Tratar cada caracter especial (Aux)
def checkSpecialChar(char):
    if char in SPECIAL_CHARS:
        return 1
    else:
        return 0
        

#Contador de menciones
def contMencion(stringToCheck):
    sum = 0
    string_to_analize = tweet_tokenizer.tokenize(stringToCheck)
    for i in string_to_analize: 
        if i[0] == '@':
            sum += 1
    return sum

#Contador unico de menciones
def contUnicMencion(stringToCheck) :
    list_specialchars = dict([])
    for i in stringToCheck:
        if i[0] == '@':
            if ( list_specialchars.get(i) == None ):
                list_specialchars[i] = 1
            else:
                list_specialchars[i] = int(list_specialchars[i]) + 1
    return list_specialchars

#Contador de palabras con @ en medio
def contPalabrasConArrDentro(stringToCheck) :
    sum = 0
    string_to_analize = stringToCheck.split(" ")
    for i in string_to_analize: 
        if i[0] != '@' and i.__contains__('@'):
            sum += 1
    return sum

#Contador de caracteres especiales
def contCaracspecial(stringToCheck) :
    sum = 0
    for i in stringToCheck:
        sum += checkSpecialChar(i)
    return sum

#Contador individual de caracteres especiales
def contUnicCaracspecial(stringToCheck) :
    list_specialchars = dict([])
    for i in stringToCheck:
        if checkSpecialChar(i):
            if ( list_specialchars.get(i) == None ):
                list_specialchars[i] = 1
            else:
                list_specialchars[i] = int(list_specialchars[i]) + 1
    return list_specialchars

#SIGNOS DE PUNTUACION

#Contador de signos de puntuacion
def contSignosPunt(stringtoCheck) :
    sum = 0
    for i in stringtoCheck:
        if i in string.punctuation:
            sum += 1
    return sum

#Contador de cada signo de puntuacion
def contUnicSignosPunt(stringtoCheck):
    list_sign = dict([])
    for i in stringtoCheck:
        if i in string.punctuation:
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#MAYUSCULAS

#Contar porcentaje de caracteres en mayusculas
def contCaracMayusculas(stringtoCheck):
    sum = 0
    i = 1
    stringGo = stringtoCheck.replace(" ","")
    while i < len(stringGo):
        if (stringGo[i].isupper()) and (stringGo[i-1] not in FINAL_MARKS):
            sum += 1
        i += 1
    return round((sum/len(stringGo))*100,3)

#Contar caracteres unicos en mayusculas
def contCaracUnicMayuscula(stringtoCheck):
    list_letr = dict([])
    i = 1
    stringGo = stringtoCheck.replace(" ","")
    while i < len(stringGo):
        if (stringGo[i].isupper()) and (stringGo[i-1] not in FINAL_MARKS):
            if ( list_letr.get(stringGo[i]) == None ):
                list_letr[stringGo[i]] = 1
            else:
                list_letr[stringGo[i]] = int(list_letr[stringGo[i]]) + 1
        i += 1
    return(list_letr)

#LETRAS REPETIDAS

#Contador de letras repetidas
def contLetrRepetidas(stringToCheck):
    sum = 0
    temp = ""
    for i in stringToCheck:
        if i == temp:
            sum += 1
        else:
            temp = i
    return sum

#Contador de letras unicas repetidas
def contLetrUnicRepetidas(stringtoCheck):
    list_letr = dict([])
    temp = ""
    for i in stringtoCheck:
        if i == temp:
            if ( list_letr.get(i) == None ):
                list_letr[i] = 1
            else:
                list_letr[i] = int(list_letr[i]) + 1
        else:
            temp = i
    return(list_letr)

#PARENTESIS

#Contador de parentesis

def contParentesis(stringToCheck):
    sum = 0
    cont1= 0
    cont2 = 0
    for i in stringToCheck:
        if i == "(":
            cont1 += 1
        elif i == ")":
            cont2 += 1

    if cont1 >= cont2:
        sum = cont2
    else:
        sum = cont1
    
    return sum

#EMOTICONOS

#Contador de emoticonos 
def contEmojis(stringToCheck):
    sum = 0
    for i in stringToCheck:
        if i in EMOTICONOS:
            sum += 1
    return sum

#ONOMATOPEYAS

#Contador de onomatopeyas
def contOnomato(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in ONOMATOPEYAS):
            sum += 1
    return sum

#Contador unico de onomatopeyas
def contUnicOnomato(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in ONOMATOPEYAS):
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

# INTERJECCIONES

#Contador de interjecciones
def contInterj(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in INTERJECCIONES):
            sum += 1
    return sum

#Contador unico de interjecciones
def contUnicInterj(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in INTERJECCIONES):
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

# INTERPELACIONES

#Contador de interpelaciones
def contInterpelac(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in INTERPELACIONES):
            sum += 1
    return sum

#Contador unico de interpelaciones
def contUnicInterpelac(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if any((w in i) or (i in w) for w in INTERPELACIONES):
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

## MORFOLOGICOS

#DIMINUTIVOS

#Contador de diminutivos
def contDiminutiv(stringToCheck):
    sum = 0
    doc = nlp(stringToCheck)
    for token in doc:
        if 'ADJ' == token.pos_ or 'NOUN' == token.pos_:
            if any (str(token).endswith(w) for w in DIMINUTIVOS):
                sum += 1
    return sum

#Contador unico de diminutivos
def contUnicDiminutiv(stringtoCheck):
    list_sign = dict([])
    doc = nlp(stringtoCheck)
    for token in doc:
        if 'ADJ' == token.pos_ or 'NOUN' == token.pos_:
            if any (str(token).endswith(w) for w in DIMINUTIVOS):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#AUMENTATIVOS

#Contador de aumentativos
def contAumentativ(stringToCheck):
    sum = 0
    doc = nlp(stringToCheck)
    for token in doc:
        if 'ADJ' == token.pos_ or 'NOUN' == token.pos_:
            if any (str(token).endswith(w) for w in AUGMENTATIVOS):
                sum += 1
    return sum

#Contador unico de aumentativos
def contUnicAumentativ(stringtoCheck):
    list_sign = dict([])
    doc = nlp(stringtoCheck)
    for token in doc:
        if 'ADJ' == token.pos_ or 'NOUN' == token.pos_:
            if any (str(token).endswith(w) for w in AUGMENTATIVOS):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#PEYORATIVOS

#Contador de peyorativos
def contPeroyativ(stringToCheck):
    sum = 0
    doc = nlp(stringToCheck)
    for token in doc:
        if 'ADJ' == token.pos_ or 'NOUN' == token.pos_:
            if any (str(token).endswith(w) for w in PEYORATIVOS):
                sum += 1
    return sum

#SUPERLATIVOS

#Contador de superlativos
def contSuperlativ(stringToCheck):
    sum = 0
    doc = nlp(stringToCheck)
    for token in doc:
        if token.pos_ =='ADJ' or token.pos_ == 'NOUN':
            if any (str(token).endswith(w) for w in SUPERLATIVOS):
                sum += 1
    return sum

#Contador unico de superlativos
def contUnicSuperlativ(stringtoCheck):
    list_sign = dict([])
    doc = nlp(stringtoCheck)
    for token in doc:
        if token.pos_ =='ADJ' or token.pos_ == 'NOUN':
            if any (str(token).endswith(w) for w in SUPERLATIVOS):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

## LEXICOS

#ARTICULOS

#Contador de determinantes
def contDeterminantes(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if i == "el" or i == "la" or i == "los" or i == "las":
            sum += 1
    return sum

#Contador unico de determinantes
def contUnicDeterminantes(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if i == "el" or i == "la" or i == "los" or i == "las":
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#Contador de indeterminados
def contIndeterminados(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if i == "un" or i == "una" or i == "unos" or i == "unas":
            sum += 1
    return sum

#Contador unico de indeterminantes
def contUnicIndeterminantes(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if i == "un" or i == "una" or i == "unos" or i == "unas":
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#Contador de demostrativos
def contDemostrativos(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if i == "este" or i == "esta" or i == "aquel" or i == "aquella":
            sum += 1
    return sum

#Contador unico de demostrativos
def contUnicDemostrativos(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if i == "este" or i == "esta" or i == "aquel" or i == "aquella":
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#PRONOMBRES

#Contador de pronombres de 1era persona
def contPronombres1era(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if i == "yo" or i == "nosotros" or i == "nosotras" :
            sum += 1
    return sum

#Contador unico de pronombres en 1era persona
def contUnicPronombres1era(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if i == "yo" or i == "nosotros" or i == "nosotras" :
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#Contador de pronombres de 2nda persona
def contPronombres2ona(stringToCheck):
    sum = 0
    string_to_analize = word_tokenize(stringToCheck)
    for i in string_to_analize:
        if i == "tu" or i == "vosotros" or i == "vosotras" :
            sum += 1
    return sum

#Contador unico de pronombres en 2ona persona
def contUnicPronombres2ona(stringtoCheck):
    list_sign = dict([])
    string_to_analize = word_tokenize(stringtoCheck)
    for i in string_to_analize:
        if i == "tu" or i == "vosotros" or i == "vosotras" :
            if ( list_sign.get(i) ==  None ):
                list_sign[i] = 1
            else:
                list_sign[i] = int(list_sign[i]) + 1
    return list_sign

#VERBOS

#Contador de verbos Ser Estar Parecer
def contVerbosSerEstarParecer(stringToCheck):
    sum = 0
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.lemma_) == 'ser' or str(token.lemma_) == 'estar' or str(token.lemma_) == 'parecer':
            sum = sum + 1
    return sum

#Contador unico de verbos Ser Estar Parecer
def contUnicVerbosSerEstarParecer(stringtoCheck):
    list_sign = dict([])
    doc = nlp(stringtoCheck)
    for token in doc:
        if str(token.lemma_) == 'ser' or str(token.lemma_) == 'estar' or str(token.lemma_) == 'parecer':
            if ( list_sign.get(str(token)) ==  None ):
                list_sign[str(token)] = 1
            else:
                list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en 1era persona
def contVerbosEnPrimeraPersona(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_first_person):
                sum = sum + 1
    return sum

#Contador unico de verbos en 1era persona
def contUnicVerbosEnPrimeraPersona(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_first_person):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en 2nda persona
def contVerbosEnSegundaPersona(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_second_person):
                sum = sum + 1
    return sum

#Contador unico de verbos en 2nda persona
def contUnicVerbosEnSegundaPersona(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_second_person):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos subjuntivos
def contVerbosSubjuntivos(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_subj):
                sum = sum + 1
    return sum

#Contador unico de verbos subjuntivos
def contUnicVerbosEnSegundaPersona(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_subj):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos indicativos
def contVerbosIndicativos(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_indi):
                sum = sum + 1
    return sum

#Contador unico de verbos indicativos
def contUnicVerbosIndicativos(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_indi):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en preterito
def contVerbosPreterito(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_pret):
                sum = sum + 1
    return sum

#Contador unico de verbos indicativos
def contUnicVerbosPreterito(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_pret):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en futuro
def contVerbosFuturo(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_futu):
                sum = sum + 1
    return sum

#Contador unico de verbos futuros
def contUnicVerbosFuturo(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_futu):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en presente
def contVerbosPresente(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_pres):
                sum = sum + 1
    return sum

#Contador unico de verbos futuros
def contUnicVerbosPresente(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_pres):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en imperativo
def contVerbosImperativo(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_impe):
                sum = sum + 1
    return sum

#Contador unico de verbos imperativos
def contUnicVerbosImperativos(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_impe):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en participio
def contVerbosParticipio(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if str(token.morph.get('VerbForm')) == '[\'Part\']':
                sum = sum + 1
    return sum

#Contador unico de verbos en participio
def contUnicVerbosParticipio(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if str(token.morph.get('VerbForm')) == '[\'Part\']':
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en gerundio
def contVerbosGerundio(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if str(token.morph.get('VerbForm')) == '[\'Ger\']':
                sum = sum + 1
    return sum

#Contador unico de verbos en gerundio
def contUnicVerbosGerundio(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if str(token.morph.get('VerbForm')) == '[\'Ger\']':
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de verbos en condicional
def contVerbosCondicional(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_cond):
                sum = sum + 1
    return sum

#Contador unico de verbos condicional
def contUnicVerbosCondicional(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'VERB' or str(token.pos_) == 'AUX':
            if any(str(token).endswith(s) for s in ending_in_cond):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

# ADVERBIOS

#Contador de adverbios de cantidad
def contAdverbiosCant(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_CANT):
                sum = sum + 1
    return sum

#Contador unico de adverbios de cantidad
def contUnicAdverbiosCant(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_CANT):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de adverbios de negacion
def contAdverbiosNeg(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_NEG):
                sum = sum + 1
    return sum

#Contador unico de adverbios de negacion
def contUnicAdverbiosNeg(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_NEG):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#Contador de adverbios de duda
def contAdverbiosDud(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_DUD):
                sum = sum + 1
    return sum

#Contador unico de adverbios de duda
def contUnicAdverbiosDud(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADV':
            if any(str(token).endswith(s) for s in ADVERBIOS_DUD):
                if ( list_sign.get(str(token)) ==  None ):
                    list_sign[str(token)] = 1
                else:
                    list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

# ADJETIVOS

#Contador de adjetivos de cantidad
def contAdjetivosCant(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if str(token.pos_) == 'ADJ':
            if any(str(token).endswith(s) for s in ADVERBIOS_CANT):
                sum = sum + 1
    return sum

# INSULTOS

#Contador de insultos
def contInsultos(stringToCheck):
    sum = 0
    stringToCheck = unicodedata.normalize("NFKD", stringToCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if any(str(token).endswith(s) for s in insultos):
            sum = sum + 1
    return sum

#Contador unico de insultos
def contUnicInsultos(stringtoCheck):
    list_sign = dict([])
    stringToCheck = unicodedata.normalize("NFKD", stringtoCheck).encode("ascii","ignore").decode("ascii")
    doc = nlp(stringToCheck)
    for token in doc:
        if any(str(token).endswith(s) for s in insultos):
            if ( list_sign.get(str(token)) ==  None ):
                list_sign[str(token)] = 1
            else:
                list_sign[str(token)] = int(list_sign[str(token)]) + 1
    return list_sign

#TRACTAMENT TWEET
def tractarTweet(tweetAAnalitzar):

    tweetAAnalitzarMinuscula = ''.join([letter.lower() for letter in tweetAAnalitzar])

    list_atrib = []
    list_atrib.append(contMencion(tweetAAnalitzar))
    list_atrib.append(contPalabrasConArrDentro(tweetAAnalitzar))
    list_atrib.append(contCaracspecial(tweetAAnalitzar))
    list_atrib.append(contSignosPunt(tweetAAnalitzar))
    list_atrib.append(contCaracMayusculas(tweetAAnalitzar))
    list_atrib.append(contLetrRepetidas(tweetAAnalitzar))
    list_atrib.append(contParentesis(tweetAAnalitzar))
    list_atrib.append(contEmojis(tweetAAnalitzar))
    list_atrib.append(contOnomato(tweetAAnalitzarMinuscula))
    list_atrib.append(contInterj(tweetAAnalitzarMinuscula))
    list_atrib.append(contInterpelac(tweetAAnalitzarMinuscula))
    list_atrib.append(contDiminutiv(tweetAAnalitzarMinuscula))
    list_atrib.append(contAumentativ(tweetAAnalitzarMinuscula))
    list_atrib.append(contPeroyativ(tweetAAnalitzarMinuscula))
    list_atrib.append(contSuperlativ(tweetAAnalitzarMinuscula))
    list_atrib.append(contDeterminantes(tweetAAnalitzarMinuscula))
    list_atrib.append(contIndeterminados(tweetAAnalitzarMinuscula))
    list_atrib.append(contDemostrativos(tweetAAnalitzarMinuscula))
    list_atrib.append(contPronombres1era(tweetAAnalitzarMinuscula))
    list_atrib.append(contPronombres2ona(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosSerEstarParecer(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosEnPrimeraPersona(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosEnSegundaPersona(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosIndicativos(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosSubjuntivos(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosPresente(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosImperativo(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosPreterito(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosFuturo(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosCondicional(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosParticipio(tweetAAnalitzarMinuscula))
    list_atrib.append(contVerbosGerundio(tweetAAnalitzarMinuscula))
    list_atrib.append(contAdverbiosCant(tweetAAnalitzarMinuscula))
    list_atrib.append(contAdverbiosNeg(tweetAAnalitzarMinuscula))
    list_atrib.append(contAdverbiosDud(tweetAAnalitzarMinuscula))
    list_atrib.append(contAdjetivosCant(tweetAAnalitzarMinuscula))
    list_atrib.append(contInsultos(tweetAAnalitzarMinuscula))

    return list_atrib
 