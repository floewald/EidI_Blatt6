# Carina Moitov
# Arthur Flaum
# Florian Ewald, 333 068 94
import random
import timeit

"""
Achtung folgender Code ist aus MEINER Aufgabe 1 Blatt 5
Dies ist trotz des Vorwurfs als Plagiat selbst erstellt worden.
Aufgabe 1 von Blatt 5 ist KEIN Plagiat.
Beginn der Bearbeitung der Aufgabe 2:
17.12.2020
10:22 Uhr

Ende der Bearbeitung:
17.12.2020
11:08
edited 11:27 (Kommentare)
Florian Ewald
"""
def terminate(err):
    print("Script terminates due to ", err, "!")

def inputTest_aux(l, i, s):
    if l == []:
        raise ValueError("No empty list allowed!")
        terminate("ValueError")
    if s < 0:
        raise ValueError("No negative integer values for s!")
        terminate("ValueError")
    if (type(i) != int) :
        raise ValueError("i is not an integer!")
        terminate("ValueError")
    elif i < 0 :
        raise ValueError("i is not a positive integer!")
        terminate("ValueError")


def sum_possible_aux(l, i, s):
    """
    Quit ugly code....
    What could be improved and how?s
    """
    inputTest_aux(l, i, s)
    if ( s == 0 ) or ( i == 0 ):
        return []
    elif sum(l[:i+1]) == s:
        return l[:]
    elif sum(l[:i+1]) < s:
        return None
    elif sum(l[:i+1]) > s:
        for m in l[:i+1]:
            if m == s:
                return [m]
        
        lcopy = l[:i+1]
        for m in range(len(l[:i+1])):
            lnew = lcopy[:m]+lcopy[m+1:]
            if len(lnew) >= 1:
                res = sum_possible_aux(lnew, len(lnew), s)
                if (type(res) == list) and (len(res) > 0):
                    return res 

        return None

def sum_possible(l, s):
    return sum_possible_aux(l, len(l)-1, s)


def sum_possible_memo_aux(l, i, s, m):
    inputTest_aux(l, i, s)
    if (i, s) in m.keys():
        return m[(i,s)]
    elif ( s == 0 ) or ( i == 0 ):
        return []
    elif sum(l[:i+1]) == s:
        return l[:]
    elif sum(l[:i+1]) < s:
        return None
    elif sum(l[:i+1]) > s:
        for o in l[:i+1]:
            m[(i,o)] = [o]
            if o == s:
                # auch möglich, dauert aber besimmt etwas länger
                """
                return m[(i,s)]
                """
                # Beschleunigung der Berechnung wenn [o] zurückgegeben wird anstatt auf das dictionary zuzugreifen. Zugriff benötigt Zeit.
                # Bei Zugriff auf innere Listen / Tupel habe ich bereits bei der Analyse von Abaqus .odb Files Erfahrungen gemacht. 
                # Das Auslesen geht deutlich schneller, wenn ncht ständig auf innere Listen zugegriffen werden muss sondern die innere Liste in einer Variablen gespeicher wird.
                # Ähnlich ist es hier
                return [o]
        
        lcopy = l[:i+1]
        for o in range(len(l[:i+1])):
            lnew = lcopy[:o]+lcopy[o+1:]
            if len(lnew) >= 1:
                res = sum_possible_memo_aux(lnew, len(lnew), s, m)
                if res != None:
                    len_res = len(res)
                    m[(len(res)+1, sum(res))] = res[:]
                    if (type(res) == list):
                        # return m[(len_res+1, s)]
                        return res[:]
                        # Warum res zurückgegeben wird ist von Zeile 83 bis 90 erklärt. Vermutlich Beschleunigung der Berechnung

        return None

def sum_possible_memo(l, s):
    """
    Bei bestimmten Eingaben ist die Funktion mit Memosiation lngsamer:
    Bspw. Länge 1000, Höchstwert 46, s=841
    Geben Sie die Länge der Liste ein: 1000

    Output der Funktion:
    Geben Sie eine Höchstzahl ein: 46
    [19, 25, 41, 40, 31, 27, 44, 42, 7, 32, 28, 9, 9, 46, 23, 34, 42, 33, 4, 3, 32, 43, 1, 19, 22, 35, 11, 30, 43, 16, 2, 16, 1, 10, 23, 14, 14, 37, 15, 29, 34, 3, 7, 36, 26, 16, 40, 41, 28, 19, 33, 30, 10, 24, 2, 30, 42, 6, 41, 37, 41, 41, 32, 8, 11, 39, 27, 12, 40, 21, 7, 39, 31, 7, 9, 24, 16, 17, 23, 45, 45, 46, 44, 33, 14, 22, 1, 17, 8, 19, 32, 9, 37, 22, 40, 27, 41, 5, 14, 24, 10, 31, 6, 24, 4, 12, 31, 3, 17, 15, 39, 16, 31, 25, 35, 35, 15, 8, 46, 28, 10, 33, 1, 16, 40, 42, 5, 18, 33, 24, 32, 45, 10, 22, 19, 13, 4, 16, 42, 45, 46, 9, 18, 10, 25, 40, 25, 38, 16, 25, 16, 30, 45, 12, 7, 41, 1, 34, 30, 7, 36, 29, 7, 35, 44, 36, 9, 14, 39, 7, 19, 41, 34, 32, 26, 21, 35, 40, 9, 44, 1, 37, 
    44, 8, 24, 11, 14, 45, 5, 11, 14, 44, 45, 44, 36, 3, 41, 35, 30, 7, 16, 28, 20, 34, 26, 44, 27, 32, 13, 10, 27, 17, 37, 28, 9, 43, 21, 5, 32, 46, 44, 41, 14, 19, 26, 42, 5, 39, 1, 3, 30, 8, 27, 25, 21, 43, 23, 45, 37, 20, 43, 1, 24, 15, 18, 27, 34, 42, 22, 37, 39, 4, 1, 21, 46, 40, 10, 43, 31, 41, 22, 37, 20, 36, 2, 26, 21, 9, 46, 9, 46, 33, 38, 35, 8, 46, 23, 24, 16, 5, 44, 39, 8, 18, 14, 40, 25, 25, 43, 39, 4, 36, 33, 21, 31, 27, 20, 45, 2, 5, 46, 25, 16, 
    17, 11, 42, 41, 7, 46, 2, 40, 7, 24, 39, 38, 33, 11, 45, 19, 6, 33, 40, 24, 1, 22, 2, 21, 37, 31, 32, 12, 15, 37, 45, 11, 8, 39, 20, 15, 38, 20, 45, 42, 24, 43, 11, 1, 40, 36, 28, 19, 30, 44, 28, 13, 11, 20, 6, 25, 9, 45, 27, 25, 45, 22, 43, 31, 29, 45, 19, 40, 15, 1, 36, 38, 9, 13, 12, 37, 17, 25, 25, 31, 20, 46, 19, 7, 1, 26, 1, 1, 38, 3, 46, 3, 7, 12, 35, 14, 5, 14, 14, 39, 27, 27, 31, 39, 32, 8, 17, 2, 41, 22, 14, 37, 20, 42, 24, 29, 21, 42, 22, 32, 1, 15, 45, 22, 12, 23, 8, 1, 39, 3, 39, 44, 31, 43, 8, 8, 10, 40, 36, 37, 25, 21, 9, 33, 28, 16, 6, 19, 18, 15, 41, 9, 18, 33, 39, 19, 42, 8, 46, 15, 26, 21, 17, 17, 17, 9, 17, 14, 3, 36, 29, 7, 7, 32, 33, 29, 12, 20, 4, 24, 20, 17, 10, 23, 18, 9, 1, 43, 23, 11, 1, 30, 26, 4, 3, 40, 26, 38, 1, 42, 43, 24, 13, 8, 13, 14, 4, 28, 3, 39, 28, 9, 43, 24, 3, 24, 1, 23, 13, 9, 40, 42, 28, 3, 44, 45, 34, 2, 2, 19, 46, 20, 23, 18, 12, 15, 13, 35, 40, 4, 29, 33, 6, 40, 23, 43, 33, 16, 32, 4, 9, 1, 10, 7, 37, 34, 1, 8, 2, 21, 46, 44, 26, 46, 30, 42, 20, 14, 17, 11, 10, 28, 12, 46, 8, 18, 26, 43, 12, 39, 20, 4, 23, 7, 25, 20, 2, 30, 10, 4, 8, 41, 28, 43, 22, 11, 13, 18, 32, 39, 44, 23, 28, 43, 10, 4, 
    4, 8, 7, 6, 4, 45, 43, 41, 17, 15, 34, 34, 14, 26, 12, 15, 14, 7, 29, 27, 14, 28, 35, 22, 10, 4, 19, 28, 14, 22, 40, 23, 29, 27, 35, 18, 42, 27, 45, 40, 13, 39, 20, 36, 37, 17, 41, 4, 5, 1, 38, 28, 45, 2, 11, 17, 4, 30, 4, 19, 16, 
    42, 17, 18, 39, 28, 33, 38, 37, 32, 34, 3, 2, 31, 3, 42, 11, 16, 22, 16, 6, 1, 44, 13, 4, 20, 42, 2, 43, 44, 27, 4, 12, 18, 17, 44, 46, 8, 10, 14, 13, 3, 6, 8, 44, 32, 11, 43, 43, 30, 11, 6, 34, 1, 15, 17, 41, 9, 13, 28, 9, 20, 45, 40, 42, 37, 39, 19, 22, 38, 2, 1, 27, 31, 15, 45, 37, 18, 26, 13, 30, 3, 6, 39, 42, 3, 38, 10, 17, 19, 2, 32, 9, 22, 1, 7, 9, 43, 29, 4, 29, 5, 3, 35, 18, 19, 4, 5, 16, 20, 9, 44, 40, 42, 6, 18, 21, 26, 8, 38, 35, 9, 39, 34, 11, 22, 12, 25, 6, 29, 41, 35, 23, 26, 28, 27, 43, 44, 28, 5, 35, 4, 38, 46, 8, 32, 23, 26, 29, 32, 45, 31, 27, 40, 35, 15, 17, 38, 39, 45, 41, 3, 20, 24, 21, 4, 7, 44, 39, 2, 38, 41, 25, 21, 32, 28, 26, 39, 41, 14, 14, 43, 35, 9, 35, 18, 10, 7, 13, 23, 31, 32, 37, 37, 3, 35, 43, 20, 22, 31, 25, 46, 19, 43, 1, 28, 38, 33, 37, 1, 45, 8, 46, 17, 3, 10, 8, 38, 19, 22, 27, 9, 2, 29, 42, 6, 33, 15, 39, 24, 25, 45, 41, 34, 18, 33, 11, 5, 19, 45, 24, 3, 7, 13, 34, 12, 21, 32, 17, 37, 46, 6, 46, 17, 22, 36, 18, 20, 36, 5, 41, 37, 8, 12, 31, 30, 46, 44, 40, 18, 8, 40, 43, 18, 15, 29, 30, 20, 30, 13, 21, 39, 30, 44, 9, 4, 16, 31, 39, 39, 41, 45, 3, 33, 17, 3, 23, 30, 1, 29, 3, 30, 39, 14, 41, 15, 37, 15, 18, 31, 15, 31, 27, 45, 44, 14, 2, 34, 34, 11, 13, 19, 39, 2, 38, 34, 16, 3, 15, 11, 17]

    Geben Sie eine Zahl ein: 841
    *** Mit sum_possible ***
    Ergebnis: [33, 17, 3, 23, 30, 1, 29, 3, 30, 39, 14, 41, 15, 37, 15, 18, 31, 15, 31, 27, 45, 44, 14, 34, 34, 11, 13, 19, 39, 2, 38, 34, 16, 3, 15, 11, 17]
    Zeit: 0.1247448999999996 s
    *** Mit sum_possible_memo ***
    Ergebnis: [33, 17, 3, 23, 30, 1, 29, 3, 30, 39, 14, 41, 15, 37, 15, 18, 31, 15, 31, 27, 45, 44, 14, 34, 34, 11, 13, 19, 39, 2, 38, 34, 16, 3, 15, 11, 17]
    Zeit: 0.3047164000000002 s
    
    Woran liegt das?
    An dem Dictionary, das ist klar. 
    Daran, dass ich überall die Länge der Liste, dessen Summe als Werte paar (j, k) und anschließend die Liste Speichere?
    Ist dadurch bei größeren Zahlen das Dictionary größer, es müssen mehr Listen, viele kleinere Listen mit kleinen s Werten gespeichert werden.
    Stimmt das?
    """
    laenge_l = len(l)
    i = laenge_l -1
    m = {(laenge_l, s): l[:]}
    return sum_possible_memo_aux(l=l, i=i, s=s, m=m)



# l = [10, 45, 2, 63, 7, 2, 4]
# i = len(l)-1
# s = 62
# summe = sum(l)
# m = {(i+1, summe): summe}
# print(sum_possible_aux(l, i, s))
# print(sum_possible_memo_aux(l, i, s, m))


def main():
    n = int(input("Geben Sie die Länge der Liste ein: "))
    k = int(input("Geben Sie eine Höchstzahl ein: "))
    l = []
    for i in range(n):
        l.append(random.randint(1, k))
    print(l)

    print()
    s = int(input("Geben Sie eine Zahl ein: "))
    g = globals()
    g["l"] = l
    g["s"] = s
    print("*** Mit sum_possible ***")
    t = timeit.timeit('print("Ergebnis: " + str(sum_possible(l, s)))', number = 1, globals = g)
    print("Zeit: " + str(t) + " s")
    print("*** Mit sum_possible_memo ***")
    t = timeit.timeit('print("Ergebnis: " + str(sum_possible_memo(l, s)))', number = 1, globals = g)
    print("Zeit: " + str(t) + " s")


main()