import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pythia8
import math


pythia=pythia8.Pythia()
pythia.readString("HiggsSM:ffbar2HZ = on")  #  ZH production via qqbar -> ZH
pythia.readString("36:onIfMatch = 25 23")
# pythia.readString("Beams:eCM = 100000")

# Z decays
pythia.readString("23:onMode = off")
pythia.readString("23:onIfMatch = 11 -11") # electron
pythia.readString("23:onIfMatch = 13 -13") # muon

# Higgs decays
pythia.readString("25:onMode = off")
pythia.readString("25:onIfMatch= 5 -5") # quark b

pythia.init()

# list to save data
electron_px = []
electron_py = []
electron_pz = [] 
electron_e = []
positron_px  = []
positron_py = []
positron_pz = []
positron_e = []
muon_px = []
muon_py = []
muon_pz = []
muon_e = []
antimuon_px = []
antimuon_py = []
antimuon_pz = []
antimuon_e = []

# listas para b quarks asociados a electrones
bquark_px_e = []
bquark_py_e = []
bquark_pz_e = []
bquark_e_e = []
anti_bquark_px_e = []
anti_bquark_py_e = []
anti_bquark_pz_e = []
anti_bquark_e_e = []

#listas para b quarks asociados a muones
bquark_px_m = []
bquark_py_m = []
bquark_pz_m = []
bquark_e_m = []
anti_bquark_px_m = []
anti_bquark_py_m = []
anti_bquark_pz_m = []
anti_bquark_e_m = []

Z_px = []
Z_px_m = []
cos_theta_hist =[]
eta=[]
contador=0



def find_ancestor(event, particle):
    particle_id = particle.id()
    current_idx = particle.mother1()
    while True:
        mother1_idx = event[current_idx].mother1()
        mother1 = event[mother1_idx]
        mother1_id = mother1.id()

        if mother1_id != particle_id and abs(mother1_id) in [1,2,3,4,5,6]:
            # print(mother1_id, mother1_idx, particle_id)
            return mother1_id, mother1_idx

        current_idx = mother1_idx
    

num_events=500
for j in range(num_events):
    
    if not pythia.next():
        continue
    
    evento = pythia.event

    print("********************************************************")
    mother_fermion_Z = None
    mother_fermion_Z = None

    for particle in evento:
            
        if particle.id() == 23: # Z boson
            Z_boson = particle
            daughter1_Z = evento[Z_boson.daughter1()]
            daughter2_Z = evento[Z_boson.daughter2()]

            if abs(daughter1_Z.id()) == 11 and abs(daughter2_Z.id()) == 11:
                mother_fermion_Z = find_ancestor(evento, Z_boson)
                Zboson_final = Z_boson

        if particle.id() == 25: # Z boson
            H_boson = particle
            daughter1_H = evento[H_boson.daughter1()]
            daughter2_H = evento[H_boson.daughter2()]

            if abs(daughter1_H.id()) == 5 and abs(daughter2_H.id()) == 5:
                mother_fermion_H = find_ancestor(evento, H_boson)
                Hboson_final = H_boson

    if mother_fermion_Z == mother_fermion_H and mother_fermion_Z != None:
        print(evento[Zboson_final.daughter1()].id(), evento[Zboson_final.daughter2()].id(), "ZBoson")
        print(evento[Hboson_final.daughter1()].id(), evento[Hboson_final.daughter2()].id(), "HBoson")   
            
        '''
        if particle.id() == 25 or False: # Z boson mother

            
            ancestor_index_H = find_ancestor(evento, mother_pos)
            #print(ancestor_index_H)



     
        if particle.id() == 23 or particle.id() == 25 and False: # Z boson mother
            print(particle.id(), particle.daughter1(), evento[particle.daughter1()].id(), evento[particle.mother1()].id(), j)


           
            daughter1_Z = evento[particle.daughter1()]
            daughter2_Z = evento[particle.daughter2()]
            
            if (abs(daughter1_Z.id()) == 23 or abs(daughter1_Z.id()) == 25) and (abs(daughter2_Z.id()) == 23 or abs(daughter2_Z.id()) == 25) :
                
                if abs(daughter1_Z.id())==23:
                    Zboson_Z = daughter1_Z
                elif abs(daughter2_Z.id())==23:
                    Zboson_Z = daughter2_Z
                    
                if abs(daughter1_Z.id())==25:
                    Hboson_Z = daughter1_Z
                elif abs(daughter2_Z.id())==25:
                    Hboson_Z = daughter2_Z
                
                # Higgs daughters
                daughter1_H = evento[Hboson_Z.daughter1()]
                daughter2_H = evento[Hboson_Z.daughter2()]
                Hdecay_ok = False
                if abs(daughter1_H.id()) == 5 and abs(daughter2_H.id()) == 5:
                    Hdecay_ok = True
                # Z daughters
                daughter1_Z = evento[Zboson_Z.daughter1()]
                daughter2_Z = evento[Zboson_Z.daughter2()]
                
                if abs(daughter1_Z.id()) == 11 and abs(daughter2_Z.id()) == 11 and Hdecay_ok:
                   #acomodar electrones
                    if daughter1_Z.id()==11:
                        electron = daughter1_Z
                    elif daughter2_Z.id()==11:
                        electron = daughter2_Z
                    
                    if daughter1_Z.id()==-11:
                        positron = daughter1_Z
                    elif daughter2_Z.id()==-11:
                        positron = daughter2_Z
                    
                    #bottoms para electrones
                    if daughter1_H.id()==5:
                        quark_b = daughter1_H
                    elif daughter2_H.id()==5:
                        quark_b= daughter2_H
                    
                    if daughter1_H.id()==-5:
                        antiquark_b = daughter1_H
                    elif daughter2_H.id()==-5:
                        antiquark_b = daughter2_H
                    
                if abs(daughter1_Z.id()) == 13 and abs(daughter2_Z.id()) == 13 and Hdecay_ok:
                   #acomodar muones
                    if daughter1_Z.id()==13:
                        muon = daughter1_Z
                    elif daughter2_Z.id()==13:
                        muon= daughter2_Z
                    
                    if daughter1_Z.id()==-13:
                        antimuon = daughter1_Z
                    elif daughter2_Z.id()==-13:
                        antimuon = daughter2_Z
                    
                    #bottoms para muones
                    if daughter1_H.id()==5:
                        quark_b = daughter1_H
                    elif daughter2_H.id()==5:
                        quark_b= daughter2_H
                    
                    if daughter1_H.id()==-5:
                        antiquark_b = daughter1_H
                    elif daughter2_H.id()==-5:
                        antiquark_b = daughter2_H
                        '''
                    