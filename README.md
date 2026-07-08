Airfoil Lift Polar Generator

A Python-based automation tool for generating and comparing lift polars of multiple NACA airfoils using XFOIL through the AeroPy interface.

This project was built as a step towards understanding computational aerodynamics and how programming can be used to automate aerodynamic analysis. Instead of manually running XFOIL for each airfoil and angle of attack, the program performs the entire workflow automatically and visualizes the results.

Features
Compare multiple NACA airfoils in a single run.
User-defined angle of attack range.
User-defined Reynolds number.
Automatic XFOIL execution for every angle of attack.
Generates lift coefficient ((C_L)) vs. angle of attack plots.
Clean comparison of lift polars for multiple airfoils.
How It Works
The user enters one or more NACA airfoil numbers.
The user specifies:
Minimum angle of attack
Maximum angle of attack
Reynolds number
The program creates a range of angles of attack.
For each airfoil and every angle, AeroPy calls XFOIL to compute the aerodynamic coefficients.
The lift coefficient ((C_L)) is extracted and stored.
Finally, all lift polars are plotted on a single graph for comparison.
Technologies Used
Python
AeroPy
XFOIL
NumPy
Matplotlib
Example Output

The program generates a comparison plot similar to the one below.

Add your generated plot here.

Why I Built This

I wanted to explore how programming could be applied to aerospace engineering beyond simple mathematical calculations.

While learning aerodynamics and computational methods, I realized that many engineering analyses involve repetitive workflows. This project was an opportunity to automate that process while gaining experience with:

Engineering software automation
Data collection and organization
Scientific plotting
Working with aerodynamic analysis tools

Although XFOIL performs the aerodynamic calculations, building the automation around it helped me better understand how computational tools are used in practical aerodynamic analysis.

Future Improvements
Add drag coefficient ((C_D)) plots.
Generate drag polars ((C_D) vs. (C_L)).
Calculate lift-to-drag ratio ((L/D)).
Export results to CSV.
Improve error handling for XFOIL convergence failures.
Add a graphical user interface (GUI).
Support additional airfoil formats beyond NACA series.
Motivation

This project is part of my journey into computational aerospace engineering.

My long-term goal is to build numerical solvers from first principles, beginning with solving Laplace's equation using the Finite Difference Method (FDM). Projects like this provide practical experience with engineering workflows while building the programming skills needed for more advanced computational methods.

License

This project is open-source under the MIT License.
