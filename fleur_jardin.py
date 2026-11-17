import turtle

# Configuration de la fenêtre
ecran = turtle.Screen()
ecran.title("Fleur dans un jardin vert")
ecran.setup(width=800, height=600)
ecran.bgcolor("#87CEEB")  # Ciel bleu clair

t = turtle.Turtle()
t.speed(8)
t.hideturtle()

def dessiner_rectangle(couleur, x, y, largeur, hauteur):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(couleur)
    t.begin_fill()
    for _ in range(2):
        t.forward(largeur)
        t.left(90)
        t.forward(hauteur)
        t.left(90)
    t.end_fill()

# 1. Dessiner le jardin vert (herbe)
dessiner_rectangle("#228B22", -400, -300, 800, 220)

# 2. Dessiner la tige de la fleur
dessiner_rectangle("#006400", -6, -150, 12, 200)

# 3. Dessiner les feuilles sur la tige
def dessiner_feuille(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.setheading(angle)
    t.pendown()
    t.color("#32CD32")
    t.begin_fill()
    t.circle(45, 90)
    t.left(90)
    t.circle(45, 90)
    t.end_fill()

dessiner_feuille(6, -60, 0)     # Feuille droite
dessiner_feuille(-6, -40, 90)   # Feuille gauche

# 4. Dessiner les pétales de la fleur
t.penup()
t.goto(0, 60)
t.pendown()

nombre_petales = 12
for _ in range(nombre_petales):
    t.color("#FF1493")  # Rose vif
    t.begin_fill()
    t.circle(60, 60)
    t.left(120)
    t.circle(60, 60)
    t.left(120)
    t.end_fill()
    t.left(360 / nombre_petales)

# 5. Dessiner le cœur jaune de la fleur
t.penup()
t.goto(0, 35)
t.setheading(0)
t.pendown()
t.color("#FFD700")  # Jaune or
t.begin_fill()
t.circle(25)
t.end_fill()

# Maintenir la fenêtre ouverte
turtle.done()