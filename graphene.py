from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom

index1=6
index2=7
mya = 2.45
myc = 20.0

gra = Graphene(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,1))
io.write('test.xyz', gra, format='xyz')
