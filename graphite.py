from ase.lattice.hexagonal import *
import ase.io as io
from ase import Atoms, Atom

index1=20
index2=18
mya = 2.46
myc = 6.70 

stacks = 1 

gra = Graphite(symbol = 'C',latticeconstant={'a':mya,'c':myc},
               size=(index1,index2,stacks))
io.write('test.xyz', gra, format='xyz')

print "The lattice vector is {", index1*mya, 1.42*index2/2 + 2.84*index2/2 , stacks*6.70, "}"
