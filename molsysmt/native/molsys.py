class MolSys():

    def __init__(self):

        from .topology import Topology
        from .structures_collection import StructuresCollection

        self.topology = Topology()
        self.structures = StructuresCollection()

    def extract(self, atom_indices='all', structure_indices='all'):

        if (atom_indices is 'all') and (structure_indices is 'all'):

            return self.copy()

        else:

            tmp_item = MolSys()
            tmp_item.topology = self.topology.extract(atom_indices=atom_indices, structure_indices=structure_indices)
            tmp_item.structures = self.structures.extract(atom_indices=atom_indices, structure_indices=structure_indices)

            return tmp_item

    def add(self, item, selection='all', structure_indices='all', syntaxis='MolSysMT'):

        from molsysmt import convert, get_form, select

        if get_form(item)!='molsysmt.MolSys':
            tmp_item = convert(item, selection=selection, structure_indices=structure_indices,
                               to_form='molsysmt.MolSys', syntaxis=syntaxis)
            self.topology.add(tmp_item.topology)
            self.structures.add(tmp_item.trajectory)
        else:
            atom_indices=select(item, selection=selection, syntaxis=syntaxis)
            self.topology.add(item.topology, selection=atom_indices)
            self.structures.add(item.trajectory, selection=atom_indices, structure_indices=structure_indices)

    def load_frames(self, selection='all', structure_indices='all', syntaxis='MoolSysMT'):

        atom_indices = self.select(selection=selection, syntaxis=syntaxis)
        return self.structures.load_frames(atom_indices=atom_indices, structure_indices=structure_indices)

    def copy(self):

        tmp_item = MolSys()
        tmp_item.topology = self.topology.copy()
        tmp_item.structures = self.structures.copy()
        return tmp_item

