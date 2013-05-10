from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom

index1=6
index2=7
mya = 2.46
myc = 6.70 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,4))
io.write('graphite_8_layers.xyz', gra, format='xyz')
