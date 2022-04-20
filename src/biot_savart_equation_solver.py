import numpy as np
import math
from scipy.constants import mu_0, pi

from src.fields import VectorField


from scipy.integrate import quad
import sympy as smp
from sympy.vector import cross



class BiotSavartEquationSolver:
    """
    A Biot–Savart law solver used to compute the resultant magnetic field B in 2D-space generated by a constant current
    field I (for example due to wires).
    """

    def solve(self, electric_current: VectorField) -> VectorField:
        """
        Solve the Biot–Savart equation to compute the magnetic field given an electric current field.

        Parameters
        ----------
        electric_current : VectorField
            A vector field I : ℝ² → ℝ³ ; (x, y) → (I_x(x, y), I_y(x, y), I_z(x, y)), where I_x(x, y), I_y(x, y) and
            I_z(x, y) are the 3 components of the electric current vector at a given point (x, y) in space. Note that
            I_z = 0 is always True in our 2D world.

        Returns
        -------
        magnetic_field : VectorField
            A vector field B : ℝ² → ℝ³ ; (x, y) → (B_x(x, y), B_y(x, y), B_z(x, y)), where B_x(x, y), B_y(x, y) and
            B_z(x, y) are the 3 components of the magnetic vector at a given point (x, y) in space. Note that
            B_x = B_y = 0 is always True in our 2D world.
        """
        x, y, z = electric_current.shape

        x, y, z = int(x), int(y), int(z)

        constante = mu_0/(4*pi)

        magnetic_field = np.zeros(electric_current.shape)
        mat_interim = electric_current.copy()


        for col in range(x):
            for ran in range(y):

                if (electric_current[col, ran] == np.array([0,0,0])).all() :
                    continue

                else:

                    for co in range(x):
                        for ra in range(y):

                            if (electric_current[co, ra] == np.array([0,0,0])).all() :

                                r_cursif = [col-co, ran-ra, 0]
                                norme_r_cursif = np.sqrt(np.sum(np.square(r_cursif)))
                                r_unitaire = r_cursif/norme_r_cursif
                                mat_interim[co, ra] = (mu_0* (np.cross(r_unitaire, electric_current[col, ran])/(norme_r_cursif**2)))/(4*pi)
                            else:
                                continue

                    magnetic_field = np.add(mat_interim, magnetic_field)

        return VectorField(magnetic_field)

