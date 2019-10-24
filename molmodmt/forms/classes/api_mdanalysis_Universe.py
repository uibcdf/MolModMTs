from os.path import basename as _basename
from os import remove as _remove
from MDAnalysis import Universe as _mdanalysis_Universe

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _mdanalysis_Universe : form_name,
    'mdanalysis.Universe' : form_name
}

def to_nglview(item, atom_indices=None, frame_indices=None):

    from nglview import show_mdtraj as _nglview_show_mdanalysis

    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)

    return _nglview_show_mdanalysis(tmp_item)

def to_pdb(item, output_file_path=None, atom_indices=None, frame_indices=None, multiframe=False):

    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)

    return tmp_item.atoms.write(output_file_path, multiframe=multiframe)

def to_MDTraj(item, atom_indices=None, frame_indices=None, multiframe=False):

    from molmodmt.utils.pdb import tmp_pdb_filename
    from molmodmt.forms.files.api_pdb import to_mdtraj as _pdb_to_mdtraj

    tmp_item = extract_subsystem(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_file = tmp_pdb_filename()
    to_pdb(tmp_item=item, output_file_path=tmp_file, multiframe)
    tmp_item=_pdb_to_mdtraj(tmp_file)
    _remove(tmp_file)

    return tmp_item

def select_with_MDTraj(item, selection):

    tmp_form=to_mdtraj(item,multiframe=True)

    return tmp_form.topology.select(selection)

def select_with_MDAnalysis(item, selection):

    tmp_atomgroup=item.select_atoms(selection)
    tmp_sel = tmp_atomgroup.atoms.ids
    del(tmp_atomgroup)

    return tmp_sel

def extract_subsystem(item, atom_indices=None, frame_indices=None):

    if (atom_indices is None) and (frame_indices is None):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError

###### Get

## system

def get_form_from_system(item, indices=None, frame_indices=None):

    from molmodmt import get_form
    return get_form(item)

