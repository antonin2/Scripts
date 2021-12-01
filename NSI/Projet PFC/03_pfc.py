 
import turtle, random, time

# variables globales
# sc désigne la fenêtre
sc = turtle.Screen()
# tr désigne la tortue
tr = turtle.Turtle()
score = 0

# constantes
# coordonnées du centre des imagettes
# pierre
XP = -150
YP = 100
# feuille
XF = XP
YF = 0
# ciseaux
XC = XP
YC = -100
# joueur
XJ = -50
YJ = 0
# ordi
XO = 100 
YO = YJ
# longueur en pixels du coté imagettes
C = 65


def placement(image, x, y):
    """
    placement(image: str, x: float, y: float) -> None
    place l'image (gif) aux coordonnées (x, y)
    """
    global sc, tr
    # si l'image n'est pas déjà "enregistrée"
    if not(image in sc._shapes):
        sc.register_shape(image)
    tr.shape(image)
    tr.setposition((x, y))
    tr.stamp()


def initialisation():
    """
    initilisation() -> None
    paramètre turtle et positionne les éléments dans l'interface
    """
    global sc, tr
    sc.setup(450, 350)
    sc.bgcolor('blue')
    # la plus rapide
    tr.speed("fastest")
    tr.up()
    tr.color("white")
    # positionnement de la tortue
    tr.setposition((XJ, YJ + C//2))
    # écriture
    tr.write("Joueur", align = "center", font = ("Arial", 15, "normal"))
    tr.setposition((XO, YO + C//2))
    tr.write("Ordi", align = "center", font = ("Arial", 15, "normal"))
    placement("pierre_gris.gif", XP, YP)
    placement("feuille_gris.gif", XF, YF)
    placement("ciseaux_gris.gif", XC, YC)
    placement("blanc.gif", XJ, YJ )
    placement("blanc.gif", XO, YO )
    print(f"Score : {score}")
    print("Faîtes votre choix svp...\n")


def affiche(x, y):
    """
    affiche(x : float, y: float) -> None
    affiche l'imagette du choix du joueur aux coordonnées (x, y)
    """
    ecart = C//2
    choix = ""
    if (XP - ecart <= x <= XP + ecart):
        if (YP - ecart <= y <= YP + ecart):
            image = "pierre.gif"
            choix = "pierre"
        elif (YF - ecart <= y <= YF + ecart):
            image = "feuille.gif"
            choix = "feuille"
        elif (YC - ecart <= y <= YC + ecart):
            image = "ciseaux.gif"
            choix = "ciseaux"
    if choix != "": # dans ce cas, une des imagettes a été cliquée
            print(f"Vous : {choix}")
            placement(image, XJ, YJ)
            # pour vérification du bon fonctionnement de la fonction tirage 
            tirage()


def tirage():
    """
    tirage() -> str
    renvoie aléatoirement 'pierre', 'feuille' ou 'ciseaux'
    """
    alea = "pierre"
    nb = random.randint(1, 3)
    if nb == 1:
        alea = "feuille"
    elif nb == 2:
        alea = "ciseaux"
    image = alea + ".gif"
    print(f"Ordi : {alea}")
    placement(image, XO, YJ)
    return alea


def gain(choix_joueur1, choix_joueur2):
    """
    gain(choix_joueur1: str, choix_joueur2: str) -> int
    renvoie :
    * 1 si choix_joueur1 gagne devant choix_joueur2
    * -1 si choix_joueur1 perd devant choix_joueur2
    * 0 en cas d'égalité
    Exemples :
    gain('feuille', 'pierre') -> 1
    gain('ciseaux', 'pierre') -> -1
    gain('pierre', 'pierre') -> 0
    """
    pass


def jouer(choix):
    """
    jouer(choix: str) -> None
    """
    pass


# fonction principale
def main():
    global sc
    initialisation()
    # chaque clic sur la fenêtre appelle la fonction affiche
    sc.onclick(affiche)
    turtle.mainloop()

    
#appel de la fonction principale (à recopier tel quel dans tout programme Python)
if __name__ == '__main__' :
    main()
