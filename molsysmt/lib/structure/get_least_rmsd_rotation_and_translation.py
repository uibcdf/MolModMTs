import numpy as np
import numba as nb
from ..math import dot_product, quaternion_to_rotation_matrix
from .rotate_and_translate import rotate_and_translate_single_structure
import math
from ..make_numba_signature import make_numba_signature


arguments=[
    nb.float64[:,:], # coordinates: [n_atoms, 3]
    nb.float64[:,:], # reference_coordinates: [n_atoms, 3]
]
output=[nb.float64[:], nb.float64[:,:], nb.float64[:]]
@nb.njit(make_numba_signature(arguments,output), cache=True)
def get_least_rmsd_rotation_and_translation_single_structure(coordinates, reference_coordinates):

    n_atoms = coordinates.shape[0]

    center_ref=np.empty((3), dtype=nb.float64)
    center=np.empty((3), dtype=nb.float64)

    x=np.zeros((n_atoms,3), dtype=nb.float64)
    y=np.zeros((n_atoms,3), dtype=nb.float64)

    R=np.zeros((3,3), dtype=nb.float64)
    F=np.zeros((4,4), dtype=nb.float64)

    w=np.ones((n_atoms), dtype=nb.float64) # without weights

    # reference coordinates

    for ii in range(n_atoms):
        x[ii,:]=w[ii]*reference_coordinates[ii,:]

    x_norm=0.0
    for ii in range(3):
        center_ref[ii]=np.sum(x[:,ii])/n_atoms
        x[:,ii]=x[:,ii]-center_ref[ii]
        x_norm=x_norm+dot_product(x[:,ii],x[:,ii])

    # coordinates

    for ii in range(n_atoms):
        y[ii,:]=w[ii]*coordinates[ii,:]

    y_norm=0.0
    for ii in range(3):
        center[ii]=np.sum(y[:,ii])/n_atoms
        y[:,ii]=y[:,ii]-center[ii]
        y_norm=y_norm+dot_product(y[:,ii], y[:,ii])

    # R matrix
    for ii in range(3):
        for jj in range(3):
            R[ii,jj]=dot_product(x[:,ii], y[:,jj])

    # F matrix
    F[0,0]=R[0,0]+R[1,1]+R[2,2]
    F[1,0]=R[1,2]-R[2,1]
    F[2,0]=R[2,0]-R[0,2]
    F[3,0]=R[0,1]-R[1,0]
    F[0,1]=F[1,0]
    F[1,1]=R[0,0]-R[1,1]-R[2,2]
    F[2,1]=R[0,1]+R[1,0]
    F[3,1]=R[0,2]+R[2,0]
    F[0,2]=F[2,0]
    F[1,2]=F[2,1]
    F[2,2]=-R[0,0]+R[1,1]-R[2,2]
    F[3,2]=R[1,2]+R[2,1]
    F[0,3]=F[3,0]
    F[1,3]=F[3,1]
    F[2,3]=F[3,2]
    F[3,3]=-R[0,0]-R[1,1]+R[2,2]

    # Diagonalization with dsyevx (Lapack)
    eigvalues, eigvectors = np.linalg.eigh(F)

    # Rotation matrix
    rotation=quaternion_to_rotation_matrix(eigvectors[:,3])
    center_rotation = center

    # New positions with translation and rotation
    translation = center_ref

    return center_rotation, rotation, translation
    #rotate_and_translate_single_structure(coordinates, center, U, center_ref, atom_indices_to_move)


arguments=[
    nb.float64[:,:,:], # coordinates: [n_structures, n_atoms, 3]
    nb.float64[:,:,:], # reference_coordinates: [n_ref_structures, n_ref_atoms, 3]
]
output=[nb.float64[:,:,:], nb.float64[:,:], nb.float64[:,:,:]]
@nb.njit(make_numba_signature(arguments,output), cache=True)
def get_least_rmsd_rotation_and_translation(coordinates, reference_coordinates):

    n_structures, n_atoms = coordinates.shape[0:2]

    center_rotation = np.empty([n_structures,0,3], dtype=np.float64)
    rotation = np.empty([n_structures,3,3], dtype=np.float64)
    translation = np.empty([n_structures,0,3], dtype=np.float64)

    w=np.ones((n_atoms), dtype=nb.float64)

    center_ref=np.empty((3), dtype=nb.float64)
    center=np.empty((3), dtype=nb.float64)

    x=np.zeros((n_atoms,3), dtype=nb.float64)
    y=np.zeros((n_atoms,3), dtype=nb.float64)

    R=np.zeros((3,3), dtype=nb.float64)
    F=np.zeros((4,4), dtype=nb.float64)

    for ii in range(n_structures):

        # reference coordinates

        x_norm=0.0
        x[:,:]=0.0

        for jj in range(n_atoms):
            x[jj,:]=w[jj]*reference_coordinates[ii,jj,:]

        for jj in range(3):
            center_ref[jj]=np.sum(x[:,jj])/n_atoms
            x[:,jj]=x[:,jj]-center_ref[jj]
            x_norm=x_norm+dot_product(x[:,jj],x[:,jj])

        # coordinates

        y_norm=0.0
        y[:,:]=0.0

        for jj in range(n_atoms):
            y[jj,:]=w[jj]*coordinates[ii,jj,:]

        for jj in range(3):
            center[jj]=np.sum(y[:,jj])/n_atoms
            y[:,jj]=y[:,jj]-center[jj]
            y_norm=y_norm+dot_product(y[:,jj],y[:,jj])

        R[:,:]=0.0
        F[:,:]=0.0

        # R matrix
        for ll in range(3):
            for mm in range(3):
                R[ll,mm]=dot_product(x[:,ll], y[:,mm])

        # F matrix
        F[0,0]=R[0,0]+R[1,1]+R[2,2]
        F[1,0]=R[1,2]-R[2,1]
        F[2,0]=R[2,0]-R[0,2]
        F[3,0]=R[0,1]-R[1,0]
        F[0,1]=F[1,0]
        F[1,1]=R[0,0]-R[1,1]-R[2,2]
        F[2,1]=R[0,1]+R[1,0]
        F[3,1]=R[0,2]+R[2,0]
        F[0,2]=F[2,0]
        F[1,2]=F[2,1]
        F[2,2]=-R[0,0]+R[1,1]-R[2,2]
        F[3,2]=R[1,2]+R[2,1]
        F[0,3]=F[3,0]
        F[1,3]=F[3,1]
        F[2,3]=F[3,2]
        F[3,3]=-R[0,0]-R[1,1]+R[2,2]

        # Diagonalization with dsyevx (Lapack)
        eigvalues, eigvectors = np.linalg.eigh(F)

        # Rotation matrix
        rotation[ii,:,:]=quaternion_to_rotation_matrix(eigvectors[:,3])
        center_rotation[ii,0,:]=center

        # Translation
        translation[ii,0,:]=center_ref

        # New positions with translation and rotation
        #rotate_and_translate_single_structure(coordinates[ii,:,:],
        #                                      np.expand_dims(center,0),
        #                                      np.expand_dims(U,0),
        #                                      np.expand_dims(center_ref,0),
        #                                      atom_indices_to_move)


    return center_rotation, rotation, translation


arguments=[
    nb.float64[:,:,:], # coordinates: [n_structures, n_atoms, 3]
    nb.float64[:,:], # reference_coordinates: [n_ref_atoms, 3]
]
output=[nb.float64[:,:,:], nb.float64[:,:], nb.float64[:,:,:]]
@nb.njit(make_numba_signature(arguments,output), cache=True)
def get_least_rmsd_rotation_and_translation_with_single_reference_structure(coordinates, reference_coordinates):

    n_structures, n_atoms = coordinates.shape[0:2]

    center_rotation = np.empty([n_structures,0,3], dtype=np.float64)
    rotation = np.empty([n_structures,3,3], dtype=np.float64)
    translation = np.empty([n_structures,0,3], dtype=np.float64)

    w=np.ones((n_atoms), dtype=nb.float64)

    center_ref=np.empty((3), dtype=nb.float64)
    center=np.empty((3), dtype=nb.float64)

    x=np.zeros((n_atoms,3), dtype=nb.float64)
    y=np.zeros((n_atoms,3), dtype=nb.float64)

    R=np.zeros((3,3), dtype=nb.float64)
    F=np.zeros((4,4), dtype=nb.float64)

    # reference coordinates

    x_norm=0.0
    x[:,:]=0.0

    for jj in range(n_atoms):
        x[jj,:]=w[jj]*reference_coordinates[jj,:]

    for jj in range(3):
        center_ref[jj]=np.sum(x[:,jj])/n_atoms
        x[:,jj]=x[:,jj]-center_ref[jj]
        x_norm=x_norm+dot_product(x[:,jj],x[:,jj])

    for ii in range(n_structures):

        # coordinates

        y_norm=0.0
        y[:,:]=0.0

        for jj in range(n_atoms):
            y[jj,:]=w[jj]*coordinates[ii,jj,:]

        for jj in range(3):
            center[jj]=np.sum(y[:,jj])/n_atoms
            y[:,jj]=y[:,jj]-center[jj]
            y_norm=y_norm+dot_product(y[:,jj],y[:,jj])

        R[:,:]=0.0
        F[:,:]=0.0

        # R matrix
        for ll in range(3):
            for mm in range(3):
                R[ll,mm]=dot_product(x[:,ll], y[:,mm])

        # F matrix
        F[0,0]=R[0,0]+R[1,1]+R[2,2]
        F[1,0]=R[1,2]-R[2,1]
        F[2,0]=R[2,0]-R[0,2]
        F[3,0]=R[0,1]-R[1,0]
        F[0,1]=F[1,0]
        F[1,1]=R[0,0]-R[1,1]-R[2,2]
        F[2,1]=R[0,1]+R[1,0]
        F[3,1]=R[0,2]+R[2,0]
        F[0,2]=F[2,0]
        F[1,2]=F[2,1]
        F[2,2]=-R[0,0]+R[1,1]-R[2,2]
        F[3,2]=R[1,2]+R[2,1]
        F[0,3]=F[3,0]
        F[1,3]=F[3,1]
        F[2,3]=F[3,2]
        F[3,3]=-R[0,0]-R[1,1]+R[2,2]

        # Diagonalization with dsyevx (Lapack)
        eigvalues, eigvectors = np.linalg.eigh(F)

        # Rotation matrix
        rotation[ii,:,:]=quaternion_to_rotation_matrix(eigvectors[:,3])
        center_rotation[ii,0,:]=center

        # Translation
        translation[ii,0,:]=center_ref

        # New positions with translation and rotation
        #rotate_and_translate_single_structure(coordinates[ii,:,:],
        #                                      np.expand_dims(center,0),
        #                                      np.expand_dims(U,0),
        #                                      np.expand_dims(center_ref,0),
        #                                      atom_indices_to_move)


    return center_rotation, rotation, translation

