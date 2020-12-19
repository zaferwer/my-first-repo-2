from fractions import Fraction as frac

###############################################################
# Programinizi yazmaya bu yorumun altindan baslayiniz.        #
# Fonksiyon isimlerini ve parametre sayisini degistirmeyiniz. #
# Ust satiri kesinlikle silmeyiniz                            #
###############################################################


############# kullaniciFonksiyonlari #########################

liste = [1.1, 13.86, 25.346, 17.1, 2.2]


############# ontanimli Fonksiyonlar #########################


def kesirKarsilastirma(kesir1, kesir2):
    """
    kesir1 ve kesir2, [pay, payda] seklinde tutulan iki elemanli listelerdir.
    Buyukten kucuge, ya da kucukten buyuge siralama yaparken iki kesrin karsilastirilmasini bu fonksiyon blogunda tanimlayiniz:

    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """


def kucuktenbuyuge(liste):
    """
    liste kucukten buyuge sirali olacagi icin
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz
    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    for i in range(len(liste)):
        if liste[i][0] / liste[i][1] < liste[0][0] / liste[0][1]:
            liste.remove(liste[i])
            liste.insert(liste[0])
        else:
            pass
        return liste


def buyuktenkucuge(liste):
    """
    liste buyukten kucuge sirali olacagi icin
    eklenecek 'eleman'in yerini tespit edip, uygun yere ekleyeceksiniz
    Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """
    for i in range(len(liste)):
        if liste[i][0] / liste[i][1] > liste[-1][0] / liste[-1][1]:
            liste.append(liste[i])
            liste.remove(liste[i])
        else:
            pass
    return liste


def soru1(liste):
    """
    1. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz:
    liste1 icerisinde kucukten buyuge olan elemanlari, liste2 icerisinde de buyukten kucuge olan elemanlari tutacaksiniz
    """
    liste1 = []
    liste2 = []
    for i in liste:
        pay = frac(str(i)).numerator
        payda = frac(str(i)).denominator
        paypayda = []
        paypayda.append(pay)
        paypayda.append(payda)
        if pay + payda <= 50:
            liste1.append(paypayda)
        else:
            liste2.append(paypayda)
    print(kucuktenbuyuge(liste1), buyuktenkucuge(liste2))


soru1(liste)


# Kodunuzu bu satirdan itibaren yaziniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:


def soru2(liste):
    """
    soru2 icerisinde istenilen sozlugu olusturduktan sonra, size verdigimiz ornekteki stile bagli kalarak sonucu ekrana yazdiriniz,
    lutfen gorsellik katacagini dusunerek ekrana ekstra ifadeler bastirmayiniz.
    2. soru icin gerekenleri bu fonksiyonun altinda yapacaksiniz, verilen satirlari silmeden istediginiz kadar satir kullanabilirsiniz:
    """


############ test ##############################################
""" 
Fonksiyon cagirma icin bir ornek, bu kismi kodunuzu test etmek icin yorumdan cikararak calistirabilir ve degisiklikler yapabilirsiniz:
Testleri tamamladiktan sonra, gondermeden once test kismini tamamen silebilir, ya da yoruma alabilirsiniz
"""
# liste = [1.1, 13.86, 25.346, 17.1, 2.2]
# liste1, liste2 = soru1(liste)

# soru2(liste)
