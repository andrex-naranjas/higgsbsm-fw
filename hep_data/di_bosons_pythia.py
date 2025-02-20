import pandas as pd
import pythia8

pythia=pythia8.Pythia()
pythia.readString("WeakDoubleBoson:ffbar2gmZgmZ = on")  # diboson ffbar -> ZZ

# Z decays
pythia.readString("23:onMode = off")
pythia.readString("23:onIfMatch = 11 -11") # electron
pythia.readString("23:onIfMatch = 13 -13") # muon
pythia.readString("23:onIfMatch = 5 -5") # quark b
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

# electrones bquarks
bquark_px_e = []
bquark_py_e = []
bquark_pz_e = []
bquark_e_e = []
anti_bquark_px_e = []
anti_bquark_py_e = []
anti_bquark_pz_e = []
anti_bquark_e_e = []

# muons bquarks
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

def find_ancestor(event, particle):
    particle_id = particle.id()
    current_idx = particle.mother1()
    while True:
        mother1_idx = event[current_idx].mother1()
        mother1 = event[mother1_idx]
        mother1_id = mother1.id()
        if mother1_id != particle_id and abs(mother1_id) in [1,2,3,4,5,6]:
            return (mother1_id, mother1_idx) # returns tuple
        current_idx = mother1_idx
    

num_events=10000
for j in range(num_events):
    
    if not pythia.next():
        continue
    
    event = pythia.event
    Zboson_lepton = None
    Zboson_quark = None

    for particle in event:
        if particle.id() == 23: # Z boson
            Z_boson = particle
            daughter1_Z = event[Z_boson.daughter1()]
            daughter2_Z = event[Z_boson.daughter2()]

            if abs(daughter1_Z.id()) == 11 and abs(daughter2_Z.id()) == 11:   
                mother_lepton_Z = find_ancestor(event, Z_boson)
                Zboson_lepton = Z_boson
                
            if abs(daughter1_Z.id()) == 13 and abs(daughter2_Z.id()) == 13:   
                mother_lepton_Z = find_ancestor(event, Z_boson)
                Zboson_lepton = Z_boson

            if abs(daughter1_Z.id()) == 5 and abs(daughter2_Z.id()) == 5:
                mother_quark_Z = find_ancestor(event, Z_boson)
                Zboson_quark = Z_boson

    if Zboson_lepton != None and Zboson_quark != None: # entering a valid event
        Zboson_daughter1 = event[Zboson_lepton.daughter1()]
        Zboson_daughter2 = event[Zboson_lepton.daughter2()]
    
        if mother_lepton_Z == mother_quark_Z and mother_lepton_Z != None and abs(Zboson_daughter1.id()) == 11 and abs(Zboson_daughter2.id()) == 11: # check that Z and Z come from same mother

            if Zboson_daughter1.id()==11:
                electron = Zboson_daughter1
            elif Zboson_daughter2.id()==11:
                electron = Zboson_daughter2

            if Zboson_daughter1.id()==-11:
                positron = Zboson_daughter1
            elif Zboson_daughter2.id()==-11:
                positron = Zboson_daughter2

            Zqqboson_daughter1 = event[Zboson_quark.daughter1()]
            Zqqboson_daughter2 = event[Zboson_quark.daughter2()]

            # electron bottoms
            if Zqqboson_daughter1.id()==5:
                quark_b = Zqqboson_daughter1
            elif Zqqboson_daughter2.id()==5:
                quark_b = Zqqboson_daughter2
                    
            if Zqqboson_daughter1.id()==-5:
                antiquark_b = Zqqboson_daughter1
            elif Zqqboson_daughter2.id()==-5:
                antiquark_b = Zqqboson_daughter2
    
            # electron kinematics
            electron_px.append(electron.px())
            electron_py.append(electron.py())
            electron_pz.append(electron.pz())
            electron_e.append(electron.e())
                    
            # positron kinematics 
            positron_px.append(positron.px())
            positron_py.append(positron.py())
            positron_pz.append(positron.pz())
            positron_e.append(positron.e())
                    
            # bquark - electron kinematics
            bquark_px_e.append(quark_b.px())
            bquark_py_e.append(quark_b.py()) 
            bquark_pz_e.append(quark_b.pz()) 
            bquark_e_e.append(quark_b.e())
                    
            # antibquark - electron kinematics
            anti_bquark_px_e.append(antiquark_b.px()) 
            anti_bquark_py_e.append(antiquark_b.py()) 
            anti_bquark_pz_e.append(antiquark_b.pz())
            anti_bquark_e_e.append(antiquark_b.e())
         
        if mother_lepton_Z == mother_quark_Z and mother_lepton_Z != None and abs(Zboson_daughter1.id()) == 13 and abs(Zboson_daughter2.id()) == 13: # check that Z and Z come from same mother

            if Zboson_daughter1.id()==13:
                muon = Zboson_daughter1
            elif Zboson_daughter2.id()==13:
                muon = Zboson_daughter2

            if Zboson_daughter1.id()==-13:
                antimuon = Zboson_daughter1
            elif Zboson_daughter2.id()==-13:
                antimuon = Zboson_daughter2
        
            Zqqboson_daughter1 = event[Zboson_quark.daughter1()]
            Zqqboson_daughter2 = event[Zboson_quark.daughter2()]

            # electron bottoms
            if Zqqboson_daughter1.id()==5:
                quark_b = Zqqboson_daughter1
            elif Zqqboson_daughter2.id()==5:
                quark_b= Zqqboson_daughter2
                    
            if Zqqboson_daughter1.id()==-5:
                antiquark_b = Zqqboson_daughter1
            elif Zqqboson_daughter2.id()==-5:
                antiquark_b = Zqqboson_daughter2
    
            # electron kinematics
            muon_px.append(muon.px())
            muon_py.append(muon.py())
            muon_pz.append(muon.pz())
            muon_e.append(muon.e())
                    
            # positron kinematics 
            antimuon_px.append(antimuon.px())
            antimuon_py.append(antimuon.py())
            antimuon_pz.append(antimuon.pz())
            antimuon_e.append(antimuon.e())
                    
            # bquark - electron kinematics
            bquark_px_m.append(quark_b.px())
            bquark_py_m.append(quark_b.py()) 
            bquark_pz_m.append(quark_b.pz()) 
            bquark_e_m.append(quark_b.e())
                    
            # antibquark - electron kinematics
            anti_bquark_px_m.append(antiquark_b.px()) 
            anti_bquark_py_m.append(antiquark_b.py()) 
            anti_bquark_pz_m.append(antiquark_b.pz())
            anti_bquark_e_m.append(antiquark_b.e()) 
        
# end event generation
pythia.stat()
# electron data frame
df_electrones = pd.DataFrame({
    'electron_px': electron_px,
    'electron_py': electron_py,
    'electron_pz': electron_pz,
    'electron_e': electron_e,
    'positron_px': positron_px,
    'positron_py': positron_py,
    'positron_pz': positron_pz,
    'positron_e': positron_e,
    'quark_px': bquark_px_e,
    'quark_py': bquark_py_e,
    'quark_pz': bquark_pz_e,
    'quark_e': bquark_e_e,
    'anti_quark_px': anti_bquark_px_e,
    'anti_quark_py': anti_bquark_py_e,
    'anti_quark_pz': anti_bquark_pz_e,
    'anti_quark_e': anti_bquark_e_e,
})

# save as csv
df_electrones.to_csv('mc_zzllbb_electrons.csv', index=False) 

df_muones = pd.DataFrame({
    'muon_px': muon_px,
    'muon_py': muon_py,
    'muon_pz': muon_pz,
    'muon_e': muon_e,
    'antimuon_px': antimuon_px,
    'antimuon_py': antimuon_py,
    'antimuon_pz': antimuon_pz,
    'antimuon_e': antimuon_e,
    'quark_px': bquark_px_m,
    'quark_py': bquark_py_m,
    'quark_pz': bquark_pz_m,
    'quark_e': bquark_e_m,
    'anti_quark_px': anti_bquark_px_m,
    'anti_quark_py': anti_bquark_py_m,
    'anti_quark_pz': anti_bquark_pz_m,
    'anti_quark_e': anti_bquark_e_m,
})

# save as csv
df_muones.to_csv('mc_zzllbb_muons.csv', index=False)