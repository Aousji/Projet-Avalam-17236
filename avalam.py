import cherrypy
import sys


class Server:

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        body = cherrypy.request.json
        print(body["game"])
        #déterminer avec quel pions je vais jouer 
        if body["players"][0] == body["you"]:
            mon_pion = 0
        else:
            mon_pion = 1
        print("mon pion est :",mon_pion)
        print("Player name :",body["you"])

        mes_pions_niv1=[]
        mes_pions_niv2=[]
        mes_pions_niv3=[]
        mes_pions_niv4=[]

        pions_adversaire_niv1=[]
        pions_adversaire_niv2=[]
        pions_adversaire_niv3=[]
        pions_adversaire_niv4=[]
        
        van=[]
        naar=[]
        #Remplissage des listes avec les positions des pions 
                
        for ligne in range(len(body["game"])):
            for colonne in range(len(body["game"][ligne])):
                for i in body["game"][ligne][colonne]:
                    if (i == mon_pion and len(body["game"][ligne][colonne]) == 1):
                        mes_pions_niv1.append([ligne,colonne])
                    elif (i != mon_pion and len(body["game"][ligne][colonne]) == 1):
                        pions_adversaire_niv1.append([ligne,colonne])

        for ligne in range(len(body["game"])):
            for colonne in range(len(body["game"][ligne])):
                for i in body["game"][ligne][colonne]:
                    if (mon_pion == body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 2):
                        if [ligne,colonne] not in mes_pions_niv2:
                            mes_pions_niv2.append([ligne,colonne])
                    elif (mon_pion != body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 2):
                        if  [ligne,colonne] not in pions_adversaire_niv2:
                            pions_adversaire_niv2.append([ligne,colonne])

        for ligne in range(len(body["game"])):
            for colonne in range(len(body["game"][ligne])):
                for i in body["game"][ligne][colonne]:
                    if (mon_pion == body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 3):
                        if [ligne,colonne] not in mes_pions_niv3:
                            mes_pions_niv3.append([ligne,colonne])
                    elif (mon_pion != body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 3):
                        if  [ligne,colonne] not in pions_adversaire_niv3:
                            pions_adversaire_niv3.append([ligne,colonne])
                        
        for ligne in range(len(body["game"])):
            for colonne in range(len(body["game"][ligne])):
                for i in body["game"][ligne][colonne]:
                    if (mon_pion == body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 4):
                        if [ligne,colonne] not in mes_pions_niv4:
                            mes_pions_niv4.append([ligne,colonne])
                    elif (mon_pion != body["game"][ligne][colonne][-1] and len(body["game"][ligne][colonne]) == 4):
                        if  [ligne,colonne] not in pions_adversaire_niv4:
                            pions_adversaire_niv4.append([ligne,colonne])
        #mouvements 
        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv4:
                for j in mes_pions_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv4:
                for j in pions_adversaire_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv4:
                for j in mes_pions_niv1:
                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    
                            
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv3:
                for j in mes_pions_niv2:
                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    
                            
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv3:
                for j in pions_adversaire_niv2:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv3:
                for j in mes_pions_niv2:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv1:
                for j in mes_pions_niv2:
                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)    
                            
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        van.append(j)
                        if i not in naar:
                            naar.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv2:
                for j in pions_adversaire_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv1:
                for j in pions_adversaire_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
                            
        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv1:
                for j in pions_adversaire_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                                
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv1:
                for j in mes_pions_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                                
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv2:
                for j in pions_adversaire_niv2:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                                
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv2:
                for j in pions_adversaire_niv2:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv3:
                for j in pions_adversaire_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv2:
                for j in mes_pions_niv2:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        if (len(van)==0 and len(naar)==0):                   
            for i in mes_pions_niv3:
                for j in mes_pions_niv1:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        #négative
        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv2:
                for j in pions_adversaire_niv3:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)
        
        # Négative
        if (len(van)==0 and len(naar)==0):                   
            for i in pions_adversaire_niv1:
                for j in pions_adversaire_niv4:

                    if ((i[0]-1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0]+1 == j[0]) and  (i[1] == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    

                    elif ((i[0] == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can : ", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)    
                        
                    elif ((i[0] == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]-1 == j[0]) and  (i[1]+1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

                    elif ((i[0]+1 == j[0]) and  (i[1]-1 == j[1])):
                        print("Yes we can :", j)
                        naar.append(j)
                        if i not in van:
                            van.append(i)

        print("from :", van[0],"to:",naar[0])      

        # print("les places vides sont :",place_vide)
        # print("mes pions level 1 :",mes_pions_niv1)
        print("mes pions level 2 :",mes_pions_niv2) 
        print("mes pions level 3 :",mes_pions_niv3)  
        # print("mes pions level 4 :",mes_pions_niv4)
        print("les pions de l'adversaire level 1 :",pions_adversaire_niv1)
        print("les pions de l'adversaire level 2 :",pions_adversaire_niv2)
        print("les pions de l'adversaire level 3 :",pions_adversaire_niv3)
        # print("les pions de l'adversaire level 4 :",pions_adversaire_niv4)                            

        return {"move": {"from":van[0] ,"to":naar[0] },"message": ""}

        
    @cherrypy.expose
    def ping(self):
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8081

    cherrypy.config.update({'server.socket_host': '127.0.0.1', 'server.socket_port': port})
    cherrypy.quickstart(Server())