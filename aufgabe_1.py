import time


emptytree=()

def init2():
    words = ["a","an","and", "by", "effects", "for", "from", "high", "in", "of", "on", "the", "to", "with"]
    frequency = [32,7,69,13,6,15,10,8,64,142,22,79,18,9]
    return (len(words),words,frequency)

def output(tree):
    if tree!=emptytree:
        x = "("
        if tree[0] != emptytree:
            x += output(tree[0])
        x +=  words[tree[1]]
        if tree[2] != emptytree:
            x += output(tree[2])
        return x+")"

def gg(tree):
    def weighted(tree,factor):
        if tree==emptytree:
            return 0
        else:
            return factor*frequency[tree[1]] +\
                    weighted(tree[0],factor+1) +\
                    weighted(tree[2],factor+1)
    return weighted(tree,1)


def solveRecursive(i,j):
    if i==j:
        return emptytree
    if j==i+1:
        return (emptytree,i,emptytree)
    else:
        tree = (emptytree,i,solveRecursive(i+1,j))
        for k in range(i+1,j):
            left = solveRecursive(i,k)
            right = solveRecursive(k+1,j)
            if gg((left,k,right)) < gg(tree):
                tree = (left,k,right)
        return tree

def solveDP():
    result = {}
    for g in range(0,n+1):
        for i in range(n+1):
            j=i+g
            if j in range(n+1):
                if i == j: 
                    result[(i,j)]=emptytree
                elif j==i+1:
                    result[(i,j)]=(emptytree,i,emptytree)
                else:
                    tree = (emptytree,i,result[(i+1,j)])
                    for k in range(i+1,j):
                        left = result[(i,k)]
                        right = result[(k+1,j)]
                        if gg((left,k,right)) < gg(tree):
                            tree = (left,k,right)
                    result[(i,j)]=tree
    return result[(0,n)]              

# Please complete the function above
# Bitte füllen Sie die obige Funktion aus
def extended_solveRecursive(i,j,dictionary):
    """
    Achtung folgender Code ist von mir, Florian Ewald (333 068 94, 08.1995) erstellt worden.
    Beginn der Bearbeitung der Aufgabe 1:
    17.12.2020
    11:16 Uhr

    Ende der Bearbeitung:
    17.12.2020
    
    Florian Ewald
    """
    if (i, j) in dictionary.keys():
        return dictionary[(i,j)]
    if i==j:
        # dictionary[(i,j)] = emptytree
        return emptytree
    if j==i+1:
        # dictionary[(i,j)] = (emptytree,i,emptytree)
        return (emptytree,i,emptytree)
    else:
        tree = (emptytree,i,solveRecursive(i+1,j))
        for k in range(i+1,j):
            left = solveRecursive(i,k)
            right = solveRecursive(k+1,j)
            if gg((left,k,right)) < gg(tree):
                tree = (left,k,right)
        dictionary[(i,j)] = tree
        return tree



(n,words,frequency)=init2()
print(len(words))
print(words)

print("\n\n")
print("We have the following terms:")
print(words)

print("\n with the following frequency:")
print(frequency)
print("\n")

t0 = time.process_time()
x=solveDP()
t1 = time.process_time() - t0
print("Time needed with DP",t1,"seconds.")

print("\n")
u0 = time.process_time()
y=solveRecursive(0,n)
u1 = time.process_time() - u0
print("Time needed with Recursion: "+str(u1)+ " seconds." )

print("\n")
print("The three calculated search trees the same? " + ("yes " if x==y else "no :(")) 

dictionary={}
print("\n")
z0 = time.process_time()
z=extended_solveRecursive(0,n,dictionary)
z1 = time.process_time() - z0
print("Time needed with extended Recursion: "+str(z1)+ " seconds." )




print("Calculated search tree using recursion")
print(y)
print(output(y))
print("Total weight of this tree:"+str(gg(y)))

print("\n")
print("Calculated search tree using extended recursion")
print(z)
print(output(z))
print("Total weight of this tree:"+str(gg(z)))

print("\n")
print("The three calculated search trees the same? " + ("yes " if x==y==z else "no :(")) 