# MatGL Interatomic Potential Tutorial

This project contains a Jupyter notebook tutorial for exploring MatGL, a Python framework for machine learning interatomic potentials.

## Project Overview

**MatGL** provides fast, DFT-accurate interatomic potentials using graph neural networks. The tutorial demonstrates structure relaxation using the M3GNet universal potential trained on Materials Project data.

## Project Structure

- `explore_matgl.ipynb` - Main tutorial notebook (10-minute overview)
- `explore_matgl.py` - Original Python script (kept for reference)
- `.venv/` - Python virtual environment managed by uv
- GitHub repo: https://github.com/rpmuller/explore_matgl

## Technical Details

- **Environment**: Uses `uv` for Python package management
- **Backend**: Configured for PyTorch Geometric (PYG) instead of DGL (better for macOS)
- **Visualization**: Uses 3Dmol.js for interactive 3D structure viewing
- **Key Libraries**: matgl, pymatgen, ase, py3Dmol

## Tutorial Contents

The notebook covers:
1. Creating crystal structures (BCC Molybdenum example)
2. Loading pre-trained M3GNet models
3. Structure relaxation (geometry optimization)
4. Interactive 3D visualization
5. Next steps and extensions

## Future Work / Extension Ideas

- Add examples with different crystal systems (FCC, HCP)
- Include trajectory analysis and energy plots
- Add property prediction examples (bulk modulus, formation energy)
- Explore molecular systems (not just crystals)
- Add Materials Project API integration examples
