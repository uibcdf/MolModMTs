from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest

@digest(form='molsysmt.StructuresNEW', to_form='molsysmt.StructuresNEW')
def add(to_item, item, atom_indices='all', structure_indices='all'):

    to_item.append_structures(id = item.id,
                              time = item.time,
                              coordinates = item.coordinates,
                              velocities = item.velocities,
                              box = box,
                              temperature = temperature,
                              potential_energy = potential_energy,
                              kinetic_energy = kinetic_energy)

    pass

