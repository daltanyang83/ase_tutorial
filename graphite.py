from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom

index1=6
index2=7
mya = 1.42
myc = 3.35

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,2))
io.write('graphite.xyz', gra, format='xyz')
