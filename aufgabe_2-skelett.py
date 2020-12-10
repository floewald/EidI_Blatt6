import random
import timeit

def sum_possible_aux(l, i, s):
    return None


def sum_possible(l, s):
    return None


def sum_possible_memo_aux(l, i, s, m):
    return None


def sum_possible_memo(l, s):
    return None


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
