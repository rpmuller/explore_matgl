# MatGL Interatomic Potential Tutorial

This project contains a Jupyter notebook tutorial for exploring MatGL, a Python framework for machine learning interatomic potentials.

## Project Overview

**MatGL** provides fast, DFT-accurate interatomic potentials using graph neural networks. The tutorial demonstrates structure relaxation using the TensorNet universal potential trained on MatPES data with PBE-level accuracy.

## Project Structure

- `explore_matgl.ipynb` - Main tutorial notebook (10-minute overview)
- `explore_matgl.py` - Original Python script (kept for reference)
- `.venv/` - Python virtual environment managed by uv
- GitHub repo: https://github.com/rpmuller/explore_matgl

## Technical Details

- **Environment**: Uses `uv` for Python package management
- **Backend**: Configured for PyTorch Geometric (PYG) - required for TensorNet models
- **Model**: TensorNet-MatPES-PBE-v2025.1-PES (PYG-compatible)
- **Visualization**: Uses 3Dmol.js with CIF format for interactive 3D viewing with unit cells
- **Key Libraries**: matgl, pymatgen, ase, py3Dmol

### Important Notes

- **Model Compatibility**: M3GNet and CHGNet models require DGL backend, while TensorNet models work with PYG
- **macOS Setup**: PYG backend is preferred on macOS (DGL installation can be problematic)
- **CIF vs XYZ**: The viewer uses CIF format (not XYZ) to properly display unit cell boundaries

## Tutorial Contents

The notebook covers:
1. Creating crystal structures (BCC Molybdenum example)
2. Loading pre-trained TensorNet models
3. Structure relaxation (geometry optimization)
4. Interactive 3D visualization with unit cell display
5. Next steps and extensions

## Future Work / Extension Ideas

- Add examples with different crystal systems (FCC, HCP)
- Include trajectory analysis and energy plots
- Add property prediction examples (bulk modulus, formation energy)
- Explore molecular systems (not just crystals)
- Add Materials Project API integration examples
