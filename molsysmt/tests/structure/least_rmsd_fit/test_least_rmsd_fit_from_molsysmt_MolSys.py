"""
Unit and regression test for the least_rmsd_fit module of the molsysmt package on molsysmt MolSys molecular
systems.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
import numpy as np

# Distance between atoms in space and time

def test_least_rmsd_fit_molsysmt_MolSys_1():

    molsys = msm.demo.classes.pentalanine_traj(to_form='molsysmt.MolSys')
    fitted_molsys = msm.structure.least_rmsd_fit(molsys, selection='backbone', frame_indices='all',
                                             reference_frame_index=0, to_form='molsysmt.MolSys')
    fitted_rmsd = msm.structure.get_rmsd(fitted_molsys, selection='backbone', frame_indices='all', reference_frame_index=0)
    lrmsd = msm.structure.get_least_rmsd(molsys, selection='backbone', frame_indices='all', reference_frame_index=0)
    check_value_1 = np.allclose(msm.puw.get_value(fitted_rmsd, to_unit='nm'), msm.puw.get_value(lrmsd, to_unit='nm'))
    true_value_2 = np.array([[ 0.73690029,  0.38164221,  0.05291509],
       [ 0.74055027,  0.27346991,  0.04001069],
       [ 0.67508401,  0.41352975, -0.03100723]])
    check_value_2 = np.allclose(true_value_2, msm.puw.get_value(fitted_molsys.trajectory.coordinates[1000,10:13,:], to_unit='nm'))
    assert check_value_1 and check_value_2

