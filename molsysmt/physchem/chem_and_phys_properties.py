from molsysmt._private.exceptions import NotImplementedMethodError
from molsysmt._private.digestion import digest
from ._private.forcefields import digest_forcefields
from ._private.engines import digest_engine
from openmm import unit as _unit

@digest()
def get_mass(item, atom_indices, forcefield=['AMBER99SB-ILDN','TIP3P']):

    from molsysmt import get_form

    form_in = get_form(item)
    mass=[]

    if form_in in ["openmm.Modeller", "openmm.System", "pdbfixer.PDBFixer"]:

        if form_in in ["openmm.Modeller", "pdbfixer.PDBFixer"]:
            from openmm.app import ForceField
            forcefield_openmm = _digest_forcefields(forcefield)
            system = ForceField(*forcefield_openmm).createSystem(item.topology)

        elif form_in == "openmm.System":
            system = item

        atom_indices = set(atom_indices)
        for particle_index in range(system.getNumParticles()):
            if particle_index in atom_indices:
                mass.append(system.getParticleMass(particle_index))
        return mass

    else:
        raise NotImplementedError

@digest()
def get_net_mass(item, atom_indices, forcefield=['AMBER99SB-ILDN','TIP3P']):

    from molsysmt import get_form

    form_in = get_form(item)

    if form_in in ["openmm.Modeller", "openmm.System", "pdbfixer.PDBFixer"]:

        if form_in in ["openmm.Modeller", "pdbfixer.PDBFixer"]:
            from openmm.app import ForceField
            forcefield_openmm = _digest_forcefields(forcefield)
            system = ForceField(*forcefield_openmm).createSystem(item.topology)

        elif form_in == "openmm.System":
            system = item

        atom_indices = set(atom_indices)
        net_mass = 0.0 * _unit.amu
        for particle_index in range(system.getNumParticles()):
            if particle_index in atom_indices:
                net_mass += system.getParticleMass(particle_index)
        return net_mass.in_units_of(_unit.gram/_unit.mole)/_unit.AVOGADRO_CONSTANT_NA

    else:
        raise NotImplementedError

@digest()
def get_degrees_of_freedom(item, forcefield=['AMBER99SB-ILDN','TIP3P']):

    from molsysmt import get_form

    form_in = get_form(item)

    if form_in in ["openmm.Modeller", "openmm.System", "pdbfixer.PDBFixer"]:

        if form_in in ["openmm.Modeller", "pdbfixer.PDBFixer"]:
            from openmm.app import ForceField
            forcefield_openmm = _digest_forcefields(forcefield)
            system = ForceField(*forcefield_openmm).createSystem(item.topology)

        elif form_in == "openmm.System":
            system = item

        return 3*system.getNumParticles() - system.getNumConstraints()

    else:
        raise NotImplementedError


