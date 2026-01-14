import matgl
from matgl.ext.ase import Relaxer
from pymatgen.core import Structure, Lattice

# 1. Create a "distorted" Molybdenum structure 
# (The true DFT lattice constant is ~3.16 Å; we'll start at 3.3 Å)
coords = [[0, 0, 0], [0.5, 0.5, 0.5]]
lattice = Lattice.cubic(3.3) 
mo_structure = Structure(lattice, ["Mo", "Mo"], coords)

# 2. Load the M3GNet Universal Potential
# This model was trained on the Materials Project (MP) database
model = matgl.load_model("M3GNet-MP-2021.2.8-PES")

# 3. Initialize the Relaxer
# This handles the optimization of both atom positions and lattice shape
relaxer = Relaxer(potential=model)

# 4. Perform the relaxation
print("Starting M3GNet relaxation...")
results = relaxer.relax(mo_structure)

# 5. Extract results
final_structure = results["final_structure"]
final_energy = results["trajectory"].energies[-1]

print(f"\nResults:")
print(f"Initial Lattice: 3.300 Å")
print(f"Relaxed Lattice: {final_structure.lattice.a:.3f} Å (M3GNet)")
print(f"Final Energy:   {final_energy:.4f} eV/atom")