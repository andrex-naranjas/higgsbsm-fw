
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import math
import pythia8

pythia_qq2zg = pythia8.Pythia()
pythia_qq2zg.readString("WeakBosonAndParton:qqbar2gmZg = on")
#pythia_qq2zg.readString("StringFlav:probQQtoQ = 0.0")    # Evita producción de quarks ligeros
#pythia_qq2zg.readString("StringFlav:probSQtoQQ = 0.0")  # dejar en 0
#pythia_qq2zg.readString("StringFlav:probQQ1toQQ0 = 0.0") 
#pythia_qq2zg.readString("TimeShower:weightGluonToQuark = 6") 
#pythia_qq2zg.readString("TimeShower:scaleGluonToQuark = 2")
#pythia_qq2zg.readString("HadronLevel:all = off")
#pythia_qq2zg.readString("PhaseSpace:pTHatMin = 27")
pythia_qq2zg.readString("23:onMode = off")
pythia_qq2zg.readString("23:onIfMatch = 11 -11") #electron
pythia_qq2zg.readString("23:onIfMatch = 13 -13") #muon
#pythia_qq2zg.readString("Beams:eCM = 14000")

pythia_qq2zg.init()


#**************LISTAS PARA BACKGROUND****************
electron_px_bg_s = []
electron_py_bg_s = []
electron_pz_bg_s = [] 
electron_e_bg_s = []
positron_px_bg_s  = []
positron_py_bg_s = []
positron_pz_bg_s = []
positron_e_bg_s = []
muon_px_bg_s = []
muon_py_bg_s = []
muon_pz_bg_s = []
muon_e_bg_s = []
antimuon_px_bg_s = []
antimuon_py_bg_s = []
antimuon_pz_bg_s = []
antimuon_e_bg_s = []


electron_px_bg_c = []
electron_py_bg_c = []
electron_pz_bg_c = [] 
electron_e_bg_c = []
positron_px_bg_c  = []
positron_py_bg_c = []
positron_pz_bg_c = []
positron_e_bg_c = []
muon_px_bg_c = []
muon_py_bg_c = []
muon_pz_bg_c = []
muon_e_bg_c = []
antimuon_px_bg_c = []
antimuon_py_bg_c = []
antimuon_pz_bg_c = []
antimuon_e_bg_c = []


electron_px_bg_b = []
electron_py_bg_b = []
electron_pz_bg_b = [] 
electron_e_bg_b = []
positron_px_bg_b  = []
positron_py_bg_b = []
positron_pz_bg_b = []
positron_e_bg_b = []
muon_px_bg_b = []
muon_py_bg_b = []
muon_pz_bg_b = []
muon_e_bg_b = []
antimuon_px_bg_b = []
antimuon_py_bg_b = []
antimuon_pz_bg_b = []
antimuon_e_bg_b = []

#listas para b quarks asociados a electrones
bquark_px_e_bg = []
bquark_py_e_bg = []
bquark_pz_e_bg = []
bquark_e_e_bg = []
anti_bquark_px_e_bg = []
anti_bquark_py_e_bg = []
anti_bquark_pz_e_bg = []
anti_bquark_e_e_bg = []

#listas para b quarks asociados a muones
bquark_px_m_bg = []
bquark_py_m_bg = []
bquark_pz_m_bg = []
bquark_e_m_bg = []
anti_bquark_px_m_bg = []
anti_bquark_py_m_bg = []
anti_bquark_pz_m_bg = []
anti_bquark_e_m_bg = []

#listas para c quarks asociados a electrones
cquark_px_e_bg = []
cquark_py_e_bg = []
cquark_pz_e_bg = []
cquark_e_e_bg = []
anti_cquark_px_e_bg = []
anti_cquark_py_e_bg = []
anti_cquark_pz_e_bg = []
anti_cquark_e_e_bg = []

#listas para c quarks asociados a muones
cquark_px_m_bg = []
cquark_py_m_bg = []
cquark_pz_m_bg = []
cquark_e_m_bg = []
anti_cquark_px_m_bg = []
anti_cquark_py_m_bg = []
anti_cquark_pz_m_bg = []
anti_cquark_e_m_bg = []

#listas para s quarks asociados a electrones
squark_px_e_bg = []
squark_py_e_bg = []
squark_pz_e_bg = []
squark_e_e_bg = []
anti_squark_px_e_bg = []
anti_squark_py_e_bg = []
anti_squark_pz_e_bg = []
anti_squark_e_e_bg = []

#listas para s quarks asociados a muones
squark_px_m_bg = []
squark_py_m_bg = []
squark_pz_m_bg = []
squark_e_m_bg = []
anti_squark_px_m_bg = []
anti_squark_py_m_bg = []
anti_squark_pz_m_bg = []
anti_squark_e_m_bg = []

#Listas para histogramas
masasZ_background_hist = []
masasH_background_hist = []
masasA0_background_hist = []
z_real = []
z_recons = []

contador_s = 0
contador_c = 0
contador_b = 0
contador_gluones = 0
contadorZ=0
contador_electrones=0
contador_positrones=0
num_events=10000

                   
def find_daughter(event, particle_idx, particle_id):
    current_idx = particle_idx
    while True:  # Continúa retrocediendo mientras haya hijas
        daughter1 = event[current_idx].daughter1()  # posicion de la madre principal
        daughter_particle = event[daughter1]
        
        if daughter_particle.id() != particle_id:
            #print(event[mother1].id()).
            return daughter1, evento[daughter1].mother1() #regresa a la hija del gluon y al gluon efectivo
        
        # Seguimos retrocediendo en la madre
        current_idx = daughter1

for k in range(num_events):
    #print('Evento: ', k)
    if not pythia_qq2zg.next():
        continue
    
    evento = pythia_qq2zg.event
    

    for i, particle in enumerate(evento):
        
        '''
        if particle.id() == 21:
            hija1 = evento[particle.daughter1()]
            hija2 = evento[particle.daughter2()]
            
            if abs(hija1.id()) == 3 and abs(hija2.id()) == 3 and hija2.id() == - hija1.id():
                masasH_background_hist.append((hija1.p() + hija2.p()).mCalc())
                        
            if abs(hija1.id()) == 4 and abs(hija2.id()) == 4 and hija2.id() == - hija1.id():
                masasH_background_hist.append((hija1.p() + hija2.p()).mCalc())
            
            if abs(hija1.id()) == 5 and abs(hija2.id()) == 5 and hija2.id() == - hija1.id():
        
                masasH_background_hist.append((hija1.p() + hija2.p()).mCalc())
        '''
        
            #Se eligen los Z 'iniciales' para que sea fácil identificar los gluones hermanos.
        if particle.id()==23 and evento[particle.mother1()].id() != 23:
            contadorZ+=1
            z_real.append(particle.m())
            madre1 = evento[particle.mother1()] #particula
            madre2 = evento[particle.mother2()] #particula
            
            hermana1_1 = madre1.daughter1() #posicion
            hermana2_1 = madre1.daughter2() #GLUOOOOOON - posicion
            hermana1_2 = madre2.daughter1() #posicion
            hermana2_2 = madre2.daughter2() #posicion
            
            hermana = evento[hermana2_1] #partícula. GLUONES HERMANOS DE Z's. Ningún gluon está en otras hijas.
            #print(evento[hermana1_1].id(), evento[hermana2_1].id(), evento[hermana2_2].id(), evento[hermana2_2].id(), hermana1_1, hermana2_1, hermana1_2, hermana2_2 )
                        
            #se recupera el Z efectivo (se quitan los virtuales)
            hija1_Z, Z_efectivo = find_daughter(evento, i,23)
            
            hijaZ_1 = evento[Z_efectivo].daughter1() #posición
            hijaZ_2 = evento[Z_efectivo].daughter2() #posición
            
            if evento[hijaZ_1].pT() > 27 and evento[hijaZ_2].pT() > 27:
                z_recons.append(evento[Z_efectivo].m())
            
            g_ssbar = False
            g_ccbar = False
            g_bbbar = False
                            
            #print(evento[evento[Z_efectivo].daughter1()].id(), evento[evento[Z_efectivo].daughter2()].id(), evento[Z_efectivo].daughter1(), evento[Z_efectivo].daughter2(), k)
                 
            if hermana.id() == 21: #cambiar nombre a algo como "hermanaZ"
                contador_gluones += 1 
                hija1_gluon = hermana.daughter1() #posicion
                hija2_gluon = hermana.daughter2() #posicion
                
                #print(evento[hija1_gluon].id(), evento[hija2_gluon].id(), len(hermana.daughterList()), hija1_gluon,hija2_gluon,  '-----------')
                
                if abs(evento[hija1_gluon].id()) == 3 and abs(evento[hija2_gluon].id()) == 3 and evento[hija2_gluon].id() == -evento[hija1_gluon].id(): #poner !=
                    contador_s += 1
                    g_ssbar = True
                    if evento[hija1_gluon].id() == 3:
                        quark_s = evento[hija1_gluon]
                        antiquark_s = evento[hija2_gluon]
                    else:
                        quark_s = evento[hija2_gluon]
                        antiquark_s = evento[hija1_gluon]
                                                
                if abs(evento[hija1_gluon].id()) == 4 and abs(evento[hija2_gluon].id()) == 4 and evento[hija2_gluon].id() == -evento[hija1_gluon].id():
                    contador_c += 1
                    g_ccbar = True
                    if evento[hija1_gluon].id() == 4:
                        quark_c = evento[hija1_gluon]
                        antiquark_c = evento[hija2_gluon]
                    else:
                        quark_c = evento[hija2_gluon]
                        antiquark_c = evento[hija1_gluon]
                
                if abs(evento[hija1_gluon].id()) == 5 and abs(evento[hija2_gluon].id()) == 5 and evento[hija2_gluon].id() == -evento[hija1_gluon].id():
                    contador_b += 1
                    g_bbbar = True
                    if evento[hija1_gluon].id() == 5:
                        quark_b = evento[hija1_gluon]
                        antiquark_b = evento[hija2_gluon]
                    else:
                        quark_b = evento[hija2_gluon]
                        antiquark_b = evento[hija1_gluon]
                
                if len(hermana.daughterList()) == 1 and evento[hija1_gluon].id() == 21: 
                    hija_gluon1, gluon_efectivo1 = find_daughter(evento, hija1_gluon,21)
                    hija_gluon2 = evento[gluon_efectivo1].daughter2() #posicion
                    
                    
                    if evento[hija_gluon1].id() == 3 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == -3:
                        contador_s += 1
                        quark_s = evento[hija_gluon1]
                        antiquark_s = evento[hija_gluon2]
                        g_ssbar = True
                        
                    elif evento[hija_gluon1].id() == -3 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == 3:
                        contador_s += 1 
                        quark_s = evento[hija_gluon2]
                        antiquark_s = evento[hija_gluon1]
                        g_ssbar = True
                    
                    elif evento[hija_gluon1].id() == 4 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == -4:
                        contador_c += 1
                        quark_c = evento[hija_gluon1]
                        antiquark_c = evento[hija_gluon2]
                        g_ccbar = True
                        
                    elif evento[hija_gluon1].id() == -4 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == 4:
                        contador_c += 1 
                        quark_c = evento[hija_gluon2]
                        antiquark_c = evento[hija_gluon1]
                        g_ccbar = True
                        
                    elif evento[hija_gluon1].id() == 5 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == -5:
                        contador_b += 1
                        quark_b = evento[hija_gluon1]
                        antiquark_b = evento[hija_gluon2]
                        g_bbbar = True
                        
                    elif evento[hija_gluon1].id() == -5 and len(evento[gluon_efectivo1].daughterList()) == 2 and evento[hija_gluon2].id() == 5:
                        contador_b += 1 
                        quark_b = evento[hija_gluon2]
                        antiquark_b = evento[hija_gluon1]
                        g_bbbar = True
                        
            if g_bbbar and evento[hijaZ_1].id() == 11 and evento[hijaZ_2].id() == -11: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas electrón
                electron_px_bg_b.append(lepton_minus.px())
                electron_py_bg_b.append(lepton_minus.py())
                electron_pz_bg_b.append(lepton_minus.pz())
                electron_e_bg_b.append(lepton_minus.e())
                
                #variables cinemáticas positrón   
                positron_px_bg_b.append(lepton_plus.px())
                positron_py_bg_b.append(lepton_plus.py())
                positron_pz_bg_b.append(lepton_plus.pz())
                positron_e_bg_b.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a electrones
                bquark_px_e_bg.append(quark_b.px())
                bquark_py_e_bg.append(quark_b.py()) 
                bquark_pz_e_bg.append(quark_b.pz()) 
                bquark_e_e_bg.append(quark_b.e())
                
                    #variables cinemáticas de los anti b quarks asociados a electrones
                anti_bquark_px_e_bg.append(antiquark_b.px()) 
                anti_bquark_py_e_bg.append(antiquark_b.py()) 
                anti_bquark_pz_e_bg.append(antiquark_b.pz())
                anti_bquark_e_e_bg.append(antiquark_b.e())  
                
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('********',lepton_minus.id(), lepton_plus.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_b.p() + antiquark_b.p() + lepton_plus.p() + lepton_minus.p()).mCalc())
        
            
            if g_bbbar and evento[hijaZ_1].id() == 13 and evento[hijaZ_2].id() == -13: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas electrónç
                muon_px_bg_b.append(lepton_minus.px())
                muon_py_bg_b.append(lepton_minus.py())
                muon_pz_bg_b.append(lepton_minus.pz())
                muon_e_bg_b.append(lepton_minus.e())
                
                #variables cinemáticas positrón   
                antimuon_px_bg_b.append(lepton_plus.px())
                antimuon_py_bg_b.append(lepton_plus.py())
                antimuon_pz_bg_b.append(lepton_plus.pz())
                antimuon_e_bg_b.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a muones
                bquark_px_m_bg.append(quark_b.px())
                bquark_py_m_bg.append(quark_b.py()) 
                bquark_pz_m_bg.append(quark_b.pz()) 
                bquark_e_m_bg.append(quark_b.e())
                
                    #variables cinemáticas de los anti b quarks asociados a muones
                anti_bquark_px_m_bg.append(antiquark_b.px()) 
                anti_bquark_py_m_bg.append(antiquark_b.py()) 
                anti_bquark_pz_m_bg.append(antiquark_b.pz())
                anti_bquark_e_m_bg.append(antiquark_b.e())         
                
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('-----------',quark_b.id(), antiquark_b.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_b.p() + antiquark_b.p() + lepton_plus.p() + lepton_minus.p()).mCalc())                    
            

            if g_ccbar and evento[hijaZ_1].id() == 11 and evento[hijaZ_2].id() == -11: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas electrónç
                electron_px_bg_c.append(lepton_minus.px())
                electron_py_bg_c.append(lepton_minus.py())
                electron_pz_bg_c.append(lepton_minus.pz())
                electron_e_bg_c.append(lepton_minus.e())
                
                #variables cinemáticas positrón   
                positron_px_bg_c.append(lepton_plus.px())
                positron_py_bg_c.append(lepton_plus.py())
                positron_pz_bg_c.append(lepton_plus.pz())
                positron_e_bg_c.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a electrones
                cquark_px_e_bg.append(quark_c.px())
                cquark_py_e_bg.append(quark_c.py()) 
                cquark_pz_e_bg.append(quark_c.pz()) 
                cquark_e_e_bg.append(quark_c.e())
                
                    #variables cinemáticas de los anti b quarks asociados a electrones
                anti_cquark_px_e_bg.append(antiquark_c.px()) 
                anti_cquark_py_e_bg.append(antiquark_c.py()) 
                anti_cquark_pz_e_bg.append(antiquark_c.pz())
                anti_cquark_e_e_bg.append(antiquark_c.e())  
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('-----------',quark_c.id(), antiquark_c.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_c.p() + antiquark_c.p() + lepton_plus.p() + lepton_minus.p()).mCalc())
            
            if g_ccbar and evento[hijaZ_1].id() == 13 and evento[hijaZ_2].id() == -13: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas muon
                muon_px_bg_c.append(lepton_minus.px())
                muon_py_bg_c.append(lepton_minus.py())
                muon_pz_bg_c.append(lepton_minus.pz())
                muon_e_bg_c.append(lepton_minus.e())
                
                #variables cinemáticas amntimuon
                antimuon_px_bg_c.append(lepton_plus.px())
                antimuon_py_bg_c.append(lepton_plus.py())
                antimuon_pz_bg_c.append(lepton_plus.pz())
                antimuon_e_bg_c.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a muones
                cquark_px_m_bg.append(quark_c.px())
                cquark_py_m_bg.append(quark_c.py()) 
                cquark_pz_m_bg.append(quark_c.pz()) 
                cquark_e_m_bg.append(quark_c.e())
                
                    #variables cinemáticas de los anti b quarks asociados a muones
                anti_cquark_px_m_bg.append(antiquark_c.px()) 
                anti_cquark_py_m_bg.append(antiquark_c.py()) 
                anti_cquark_pz_m_bg.append(antiquark_c.pz())
                anti_cquark_e_m_bg.append(antiquark_c.e())   
                
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('-----------',quark_c.id(), antiquark_c.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_c.p() + antiquark_c.p() + lepton_plus.p() + lepton_minus.p()).mCalc())

            if g_ssbar and evento[hijaZ_1].id() == 11 and evento[hijaZ_2].id() == -11: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas electrónç
                electron_px_bg_s.append(lepton_minus.px())
                electron_py_bg_s.append(lepton_minus.py())
                electron_pz_bg_s.append(lepton_minus.pz())
                electron_e_bg_s.append(lepton_minus.e())
                
                #variables cinemáticas positrón   
                positron_px_bg_s.append(lepton_plus.px())
                positron_py_bg_s.append(lepton_plus.py())
                positron_pz_bg_s.append(lepton_plus.pz())
                positron_e_bg_s.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a electrones
                squark_px_e_bg.append(quark_s.px())
                squark_py_e_bg.append(quark_s.py()) 
                squark_pz_e_bg.append(quark_s.pz()) 
                squark_e_e_bg.append(quark_s.e())
                
                    #variables cinemáticas de los anti b quarks asociados a electrones
                anti_squark_px_e_bg.append(antiquark_s.px()) 
                anti_squark_py_e_bg.append(antiquark_s.py()) 
                anti_squark_pz_e_bg.append(antiquark_s.pz())
                anti_squark_e_e_bg.append(antiquark_s.e())  
                
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('-----------',quark_s.id(), antiquark_s.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_s.p() + antiquark_s.p() + lepton_plus.p() + lepton_minus.p()).mCalc())
            
            if g_ssbar and evento[hijaZ_1].id() == 13 and evento[hijaZ_2].id() == -13: #no pasa que el índice de la hija 1 sea negativo
                lepton_minus = evento[hijaZ_1] #Electrón
                lepton_plus= evento[hijaZ_2] #Positrón
                
            # variables cinemáticas electrónç
                muon_px_bg_s.append(lepton_minus.px())
                muon_py_bg_s.append(lepton_minus.py())
                muon_pz_bg_s.append(lepton_minus.pz())
                muon_e_bg_s.append(lepton_minus.e())
                
                #variables cinemáticas positrón   
                antimuon_px_bg_s.append(lepton_plus.px())
                antimuon_py_bg_s.append(lepton_plus.py())
                antimuon_pz_bg_s.append(lepton_plus.pz())
                antimuon_e_bg_s.append(lepton_plus.e())
                
                #variables cinemáticas de los b quarks asociados a muones
                squark_px_m_bg.append(quark_s.px())
                squark_py_m_bg.append(quark_s.py()) 
                squark_pz_m_bg.append(quark_s.pz()) 
                squark_e_m_bg.append(quark_s.e())
                
                    #variables cinemáticas de los anti b quarks asociados a muones
                anti_squark_px_m_bg.append(antiquark_s.px()) 
                anti_squark_py_m_bg.append(antiquark_s.py()) 
                anti_squark_pz_m_bg.append(antiquark_s.pz())
                anti_squark_e_m_bg.append(antiquark_s.e())   
                if lepton_minus.pT()>27 and lepton_plus.pT()>27:
                    masasH_background_hist.append((particle.p() + hermana.p()).mCalc())
                    masasZ_background_hist.append((lepton_plus.p() + lepton_minus.p()).mCalc())
                    #print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), evento[Z_efectivo].m(), evento[Z_efectivo].id())
                    #print('-----------',quark_s.id(), antiquark_s.id())
                    print('*******', (lepton_plus.p() + lepton_minus.p()).mCalc(), particle.m(), particle.id())
                    masasA0_background_hist.append((quark_s.p() + antiquark_s.p() + lepton_plus.p() + lepton_minus.p()).mCalc())


# Crear DataFrame para electrones
df_electrones_s = pd.DataFrame({
    'electron_px_s': electron_px_bg_s,
    'electron_py_s': electron_py_bg_s,
    'electron_pz_s': electron_pz_bg_s,
    'electron_e_s': electron_e_bg_s,
    'positron_px_s': positron_px_bg_s,
    'positron_py_s': positron_py_bg_s,
    'positron_pz_s': positron_pz_bg_s,
    'positron_e_s': positron_e_bg_s,
    'squark_px_e': squark_px_e_bg,
    'squark_py_e': squark_py_e_bg,
    'squark_pz_e': squark_pz_e_bg,
    'squark_e_e': squark_e_e_bg,
    'anti_squark_px_e': anti_squark_px_e_bg,
    'anti_squark_py_e': anti_squark_py_e_bg,
    'anti_squark_pz_e': anti_squark_pz_e_bg,
    'anti_squark_e_e': anti_squark_e_e_bg,
    
})
# Guardar como CSV
df_electrones_s.to_csv('data_electrons_s_gg2zg.csv', index=False) 


df_muones_s = pd.DataFrame({
    'muon_px_s': muon_px_bg_s,
    'muon_py_s': muon_py_bg_s,
    'muon_pz_s': muon_pz_bg_s,
    'muon_e_s': muon_e_bg_s,
    'antimuon_px_s': antimuon_px_bg_s,
    'antimuon_py_s': antimuon_py_bg_s,
    'antimuon_pz_s': antimuon_pz_bg_s,
    'antimuon_e_s': antimuon_e_bg_s,
    'squark_px_m': squark_px_m_bg,
    'squark_py_m': squark_py_m_bg,
    'squark_pz_m': squark_pz_m_bg,
    'squark_e_m': squark_e_m_bg,
    'anti_squark_px_m': anti_squark_px_m_bg,
    'anti_squark_py_m': anti_squark_py_m_bg,
    'anti_squark_pz_m': anti_squark_pz_m_bg,
    'anti_squark_e_m': anti_squark_e_m_bg,
    
})
# Guardar como CSV
df_muones_s.to_csv('data_muons_s_gg2zg.csv', index=False) 


# Crear DataFrame para electrones
df_electrones_c = pd.DataFrame({
    'electron_px_c': electron_px_bg_c,
    'electron_py_c': electron_py_bg_c,
    'electron_pz_c': electron_pz_bg_c,
    'electron_e_c': electron_e_bg_c,
    'positron_px_c': positron_px_bg_c,
    'positron_py_c': positron_py_bg_c,
    'positron_pz_c': positron_pz_bg_c,
    'positron_e_c': positron_e_bg_c,
    'cquark_px_e': cquark_px_e_bg,
    'cquark_py_e': cquark_py_e_bg,
    'cquark_pz_e': cquark_pz_e_bg,
    'cquark_e_e': cquark_e_e_bg,
    'anti_cquark_px_e': anti_cquark_px_e_bg,
    'anti_cquark_py_e': anti_cquark_py_e_bg,
    'anti_cquark_pz_e': anti_cquark_pz_e_bg,
    'anti_cquark_e_e': anti_cquark_e_e_bg,
    
})
# Guardar como CSV
df_electrones_c.to_csv('data_electrons_c_gg2zg.csv', index=False) 


df_muones_c = pd.DataFrame({
    'muon_px_c': muon_px_bg_c,
    'muon_py_c': muon_py_bg_c,
    'muon_pz_c': muon_pz_bg_c,
    'muon_e_c': muon_e_bg_c,
    'antimuon_px_c': antimuon_px_bg_c,
    'antimuon_py_c': antimuon_py_bg_c,
    'antimuon_pz_c': antimuon_pz_bg_c,
    'antimuon_e_c': antimuon_e_bg_c,
    'cquark_px_m': cquark_px_m_bg,
    'cquark_py_m': cquark_py_m_bg,
    'cquark_pz_m': cquark_pz_m_bg,
    'cquark_e_m': cquark_e_m_bg,
    'anti_cquark_px_m': anti_cquark_px_m_bg,
    'anti_cquark_py_m': anti_cquark_py_m_bg,
    'anti_cquark_pz_m': anti_cquark_pz_m_bg,
    'anti_cquark_e_m': anti_cquark_e_m_bg,
    
})
# Guardar como CSV
df_muones_c.to_csv('data_muons_c_gg2zg.csv', index=False) 


# Crear DataFrame para electrones
df_electrones_b = pd.DataFrame({
    'electron_px_b': electron_px_bg_b,
    'electron_py_b': electron_py_bg_b,
    'electron_pz_b': electron_pz_bg_b,
    'electron_e_b': electron_e_bg_b,
    'positron_px_b': positron_px_bg_b,
    'positron_py_b': positron_py_bg_b,
    'positron_pz_b': positron_pz_bg_b,
    'positron_e_b': positron_e_bg_b,
    'bquark_px_e': bquark_px_e_bg,
    'bquark_py_e': bquark_py_e_bg,
    'bquark_pz_e': bquark_pz_e_bg,
    'bquark_e_e': bquark_e_e_bg,
    'anti_bquark_px_e': anti_bquark_px_e_bg,
    'anti_bquark_py_e': anti_bquark_py_e_bg,
    'anti_bquark_pz_e': anti_bquark_pz_e_bg,
    'anti_bquark_e_e': anti_bquark_e_e_bg,
    
})
# Guardar como CSV
df_electrones_b.to_csv('data_electrons_b_gg2zg.csv', index=False) 


df_muones_b = pd.DataFrame({
    'muon_px_b': muon_px_bg_b,
    'muon_py_b': muon_py_bg_b,
    'muon_pz_b': muon_pz_bg_b,
    'muon_e_b': muon_e_bg_b,
    'antimuon_px_b': antimuon_px_bg_b,
    'antimuon_py_b': antimuon_py_bg_b,
    'antimuon_pz_b': antimuon_pz_bg_b,
    'antimuon_e_b': antimuon_e_bg_b,
    'bquark_px_m': bquark_px_m_bg,
    'bquark_py_m': bquark_py_m_bg,
    'bquark_pz_m': bquark_pz_m_bg,
    'bquark_e_m': bquark_e_m_bg,
    'anti_bquark_px_m': anti_bquark_px_m_bg,
    'anti_bquark_py_m': anti_bquark_py_m_bg,
    'anti_bquark_pz_m': anti_bquark_pz_m_bg,
    'anti_bquark_e_m': anti_bquark_e_m_bg,
    
})
# Guardar como CSV
df_muones_b.to_csv('data_muons_b_gg2zg.csv', index=False) 
