# fonction afficher (collection)
# .......listes des pizzas (4)....
# afficher les pizzas 1 pizza par ligne

def tri_personnalise(e):
    return len(e)

def afficher(collection, n_premiers_elements=-1):
    c = collection
    c.sort(reverse=True, key=tri_personnalise)
    if not n_premiers_elements == -1:
        c= collection[:n_premiers_elements]
    nb_pizzas = len(c)
    if nb_pizzas == 0 :
        print("AUCUN PIZZZA...")
        return
 
    print(f"-------LISTE DES PIZZAS ({nb_pizzas})")

    for i in c:
        print(i)
    print()
    print("Première Pizza est ",c[0])
    print("La dernière pizza est :"+ c[-1])
    

# ajouter d pizza
def ajouter_pizza_utilisateurs(c):
    p = input("Pizza à ajouter : ")
    if p.lower() in c:
    # if pizza_existe(p, collection):
        print("ERREUR : Cette pizza existe déja ")
    else:
        c.append(p)

# def pizza_existe(e, collection):
#     for i in collection:
#         if i == e:
#             return True
#     return False

pizzas = ["4 fromages", "vegetarienne", "hawai", "calzone" ]

ajouter_pizza_utilisateurs(pizzas)
afficher(pizzas)



