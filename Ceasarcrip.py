def caesarCipher(s, k):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lista = list(alphabet)
    listb = list(alphabet)
    for j in range(k):
        oldx = lista[0]
        lista.remove(oldx)
        lista.append(oldx)
    news = ""
    for i in range(n):
        if s[i].isalpha():
            if s[i].isupper():
                x = s[i].lower()
                news = news + (lista[listb.index(x)]).upper()
            else:
                news = news + (lista[listb.index(s[i])])
        else:
            news = news + s[i]
    return news


s = input()
n = len(s)
k = 3
result = caesarCipher(s, k)
print(result)