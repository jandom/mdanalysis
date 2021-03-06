import MDAnalysis as mda
import numpy as np
from six.moves import range


def create_test_trj(uni, fname):
    n_atoms = uni.atoms.n_atoms
    pos = np.arange(3 * n_atoms).reshape(n_atoms, 3)
    uni.trajectory.ts.dt = 1
    print(uni.trajectory)
    print(uni.trajectory.ts.__class__)
    with mda.Writer(fname, n_atoms) as w:
        for i in range(5):
            # print(uni.atoms.dimensions)
            print(uni.trajectory.ts.dimensions)
            uni.atoms.positions = 2 ** i * pos
            uni.trajectory.ts.time = i
            uni.trajectory.ts.velocities = uni.atoms.positions / 10
            uni.trajectory.ts.forces = uni.atoms.positions / 100
            uni.trajectory.ts.frame = i
            w.write(uni)


def main():
    pdb = 'test_topology.pdb'
    u = mda.Universe(pdb)

    create_test_trj(u, 'test.xyz')
    create_test_trj(u, 'test.xtc')
    create_test_trj(u, 'test.trr')

if __name__ == '__main__':
    main()
