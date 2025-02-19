# Finite Element Method (FEM) for Electromagnetic Potential

This repository contains a Python implementation of the Finite Element Method (FEM) for solving electromagnetic potential problem. The project was developed as part of the Differential Equations course at AGH University of Cracow.

![obraz](https://github.com/user-attachments/assets/ed45b92c-41a2-403c-98f0-dccdc8eb8247)

![obraz](https://github.com/user-attachments/assets/72d2d6a9-a2b6-470c-a43e-7122a7f8295a)

## Overview

The repository includes the following key components:

- **main.py**: Sets up a graphical user interface using Matplotlib and Seaborn for visualizing the FEM solution. It provides interactive elements such as a text box for inputting the number of points and a button to trigger the drawing of the solution plot.
- **solver.py**: Contains the core functions for calculating the FEM solution. It defines various helper functions for basis functions, their derivatives, and the assembly of matrices required for solving the FEM equation. The `solve` function computes the solution for a specified number of points.

## Getting Started

### Prerequisites

Make sure you have the required Python libraries installed. You can install them using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Running the Project

**Clone the repository:**

```bash
git clone https://github.com/OlaszPL/Finite_element_method.git
cd Finite_element_method
```

**Run the main script:**

```bash
python main.py
```

Enter the desired number of points in the text box and click the **"Draw"** button to visualize the FEM solution.

## Files

* **main.py**: Sets up the GUI and handles user interactions.
* **solver.py**: Contains the implementation of the FEM solver.
* *wyliczenia sformułowania wariacyjnego.pdf*: Documentation of the variational formulation calculations (in Polish).

## License

This project is licensed under the MIT License.
