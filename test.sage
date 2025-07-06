M = matroids.Uniform(5, 7)
L1 = M.lattice_of_flats()
print(Matroid(L1).equals(M))