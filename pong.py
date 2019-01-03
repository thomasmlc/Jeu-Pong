from tkinter import *
import math
import random
import time

largeur = 800
hauteur = 600
rayon_balle = 10
vitesse = 3
angle = 40
x = largeur/2
y = largeur/2
dx = vitesse*math.cos(angle)
dy = vitesse*math.sin(angle)

y1 = 225
dry1 = 15
y2 =225
dry2 = 15
#score
score1 = 0
score2 = 0


difficulté = 1
score_max = 5

def Pong ():
    global largeur, hauteur, rayon_balle, vitesse, angle, x, y, dx, dy, y1, dry1, y2, dry2, score1, score2, compte, difficulté, score_max
    def menu ():
        global largeur, hauteur, rayon_balle, vitesse, angle, x, y, dx, dy, y1, dry1, y2, dry2, score1, score2, compte, difficulté, score_max
        
        def jeu():
            global largeur, hauteur, rayon_balle, vitesse, angle, x, y, dx, dy, y1, dry1, y2, dry2, score1, score2, compte, difficulté, score_max
            largeur= 800
            hauteur = 600
            
            def mouvement():
                global largeur, hauteur, rayon_balle, vitesse, angle, x, y, dx, dy, y1, dry1, y2, dry2, score1, score2, compte, difficulté, score_max
 
                dry1 = 15
                dry2 = 15
                
                
                
                
                def raquette1_haut (event):
                    global dry1
                    if canevas.coords(rak1)[1]  > 0:
                        canevas.move(rak1, 0, -dry1)
                        fenetre.after(1, raquette1_haut)

                def raquette1_bas (event):
                    global dry1
                    if canevas.coords(rak1)[3] < 600:
                        canevas.move(rak1, 0, dry1)
                        fenetre.after(1, raquette1_bas)

                #deplacement joueur 2
                def raquette2_haut (event):
                    global dry2
                    if canevas.coords(rak2)[1] > 0:
                        canevas.move(rak2, 0, -dry2)
                        fenetre.after(1, raquette2_haut)       
                def raquette2_bas (event):
                    global dry2
                    if  canevas.coords(rak2)[3] < 600:
                        canevas.move(rak2, 0, dry2)
                        fenetre.after(1, raquette2_bas)  

                def joueur1 ():
                    fenetre.bind_all("<Up>", raquette2_haut) # haut
                    fenetre.bind_all("<Down>", raquette2_bas) # Bas 
		
                def joueur2():
                    fenetre.bind_all("<z>", raquette1_haut) # haut
                    fenetre.bind_all("<s>", raquette1_bas) # Bas 
                def actu_score():
                    canevas.itemconfigure(scoreg, text=score1)
                    canevas.itemconfigure(scored, text=score2)

                def mouvement_balle(): 
                    global largeur, hauteur, rayon_balle, vitesse, angle, x, y, dx, dy, y1, dry1, y2, dry2, score1, score2, compte, difficulté, score_max
                    
                    
                    
                    #rebond bas
                    if y+rayon_balle+dy > hauteur:
                        y = 2*(hauteur-rayon_balle)-y
                        dy = -dy
                    # rebond haut
                    if y-rayon_balle+dy < 0:
                        y = 2*rayon_balle-y
                        dy = -dy
                    #rebond raquette droit
                    if x+rayon_balle > canevas.coords(rak2)[0] and x+rayon_balle < canevas.coords(rak2)[2]  and y+rayon_balle+dy >= canevas.coords(rak2)[1] and y-rayon_balle+dy <= canevas.coords(rak2)[3] :   
                        vitesse += 0.5
                        dx = -dx
                        dx = vitesse*math.cos(angle)
                        if difficulté < 3: 
                            dy += difficulté
                        elif difficulté == 3:
                            dy += random.randint(1,3)
                        dry1 += 3
                        dry2 += 1.5
                        
                        
                        
				
                    #rebond rebond raquettgauche
                    if x - rayon_balle < canevas.coords(rak1)[2] and x-rayon_balle > canevas.coords(rak1)[0] and y+rayon_balle+dy >= canevas.coords(rak1)[1] and y - rayon_balle+dy <= canevas.coords(rak1)[3] :
                        vitesse += 0.5
                        dx = vitesse*math.cos(angle)
                        if difficulté < 3: 
                            dy += difficulté
                        elif difficulté == 3:
                            dy += random.randint(1,3)
                        dry1 += 1.5
                        dry2 += 3

                        dx = -dx
                        

                    
                    #score et relancement
                    if x - rayon_balle < 0:
                       
                        
                        score2 += 1
                        actu_score()
                        canevas.delete(balle)
                        x = largeur/2
                        y = largeur/2
                        vitesse = 3
                        dx = -vitesse*math.cos(angle)
                        dy = 3
                        return None
                        
                        

                        
                        
                        
                    if x + rayon_balle > largeur:
                        
                        score1 += 1
                        actu_score()
                        canevas.delete(balle)
                        x = largeur/2
                        y = largeur/2 
                        vitesse = 3
                        dx = vitesse*math.cos(angle)
                        dy = 3
                        return None
                        
                        
                        

                        
                       
                    
                    x = x+dx
                    y = y+dy
                    canevas.coords(balle, x-rayon_balle, y-rayon_balle, x+rayon_balle, y+rayon_balle)
                    if score_max == score1:
                        fenetre.destroy()
                        winner = Tk()
                        winner.title("VICTOIRE!!!")
                        win1 = Canvas(winner, width = 500, height = 500,bg = "black")
                        win1.pack()
                        victoire = win1.create_text(250, 250, fill="white", text="LE JOUEUR 1 A GAGNE")
                        victoire.pack()
                   
                    if score_max == score2:
                        fenetre.destroy()
                        winner = Tk()
                        winner.title("VICTOIRE!!!")
                        win1 = Canvas(winner, width = 500, height = 500,bg = "black")
                        win1.pack()
                        victoire = win1.create_text(250, 250, fill="white", text="LE JOUEUR 2 A GAGNE")
                        victoire.pack()
                        

                    fenetre.after(10, mouvement_balle)
                    

                          
                
                balle = canevas.create_oval(rayon_balle, rayon_balle, rayon_balle, rayon_balle, fill="white")
                mouvement_balle()
                joueur1()
                joueur2()
                menu.destroy()
                
                

            def lanceur (event): 
                
                mouvement()
                
                
                    
                
                

            fenetre=Tk()
            fenetre.title("PONG")
            canevas= Canvas(fenetre, width = largeur, height = hauteur, bg = 'black', )
            canevas.pack()
            bouton_quitter=Button(fenetre, text ='Quitter', command = fenetre.destroy)
            bouton_quitter.pack()
            scoreg = canevas.create_text(200, 50, fill="white", text="0")
            scored = canevas.create_text(600, 50, fill="white", text="0")
            menu.destroy()
            
           
            # Elements du jeu
            rak1 = canevas.create_rectangle(20, y1, 40, y1+150, fill="white")
            rak2 = canevas.create_rectangle(780, y2, 760, y2+150, fill="white")
            
            fenetre.bind_all("<r>", lanceur)
        
        def option():
            global difficulté, score_max
            menu.destroy()
            def score ():
                score_max = val.get()
                print(score_max)
            def option1():
                global difficulté
                difficulté = 1
                
            def option2():
                global difficulté
                difficulté = 2
            def option3():
                global difficulté
                difficulté = 3
            def back():
                opt.destroy()
                Pong()   

            opt = Tk()
            opt.title("Options")
            opti = Canvas(opt, width = 200, height = 20)
            opti.pack
            val = StringVar()
            val.set(5.0)
            sco = Spinbox(opt, text="score", from_=1, to=10,increment=1, textvariable=val, width= 15, command = score )
            sco.pack()
            bouton1 = Button(opt, text="Rebond normaux", width=15, height=10, command=option1 )
            bouton1.pack()
            bouton2 = Button(opt, text="Rebond anormaux", width=15, height=10, command=option2 ) 
            bouton2.pack()
            bouton3 = Button(opt, text="Rebond aleatoires", width=15, height=10, command=option3  )
            bouton3.pack()
            retour = Button(opt, text="Retour", width=15, height=10, command=back  )
            retour.pack()       
            

            
            

                       
                
            
                


        menu = Tk()
        menu.title("Menu Pong")
        men = Canvas(menu, width = 200,height = 20)
        men.pack()
        lancer = Button(menu, text="Lancer le jeu",width=15,height=10, command=jeu)
        lancer.pack()
        option = Button(menu, text="Options",width=15,height=10, command=option)
        option.pack()
        bouton_quitter=Button(menu, text ='Quitter',width=15,height=10, command = menu.destroy)
        bouton_quitter.pack()
        menu.mainloop()


    menu()
            

Pong()



'''
http://fsincere.free.fr/isn/python/cours_python_tkinter.php
'''