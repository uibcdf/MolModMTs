from os.path import basename as _basename
import urllib as _urllib
import json as _json

form_name=_basename(__file__).split('.')[0][4:]+':id'

is_form = {
    'pdb:id': form_name,
    'PDB:id': form_name
    }

info=["",""]
with_topology=True
with_trajectory=True

def to_pdb(item, output_filepath=None, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.miscellanea import download_pdb as download_pdb
    from molsysmt.forms.files.api_pdb import extract as extract_pdb
    from shutil import move
    tmp_item = item.split(':')[-1]
    download_pdb(tmp_item, output_filepath)
    tmp_item = extract_pdb(output_filepath, atom_indices=atom_indices, frame_indices=frame_indices)
    if tmp_item!=output_filepath:
        move(tmp_item, output_filepath)
    pass

def to_fasta(item, output_filepath=None, atom_indices='all', frame_indices='all'):

    from shutil import move
    from molsysmt.forms.files.api_fasta import extract as extract_fasta
    tmp_item = item.split(':')[-1]
    url = 'https://www.rcsb.org/pdb/download/downloadFastaFiles.do?structureIdList='+tmp_item+'&compressionType=uncompressed'
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    fasta_txt = response.read().decode('utf-8')
    with open(output_filepath,'w') as f:
        f.write(fasta_txt)
    f.close()
    tmp_item = extract_fasta(output_filepath, atom_indices=atom_indices,
            frame_indices=frame_indices)
    if tmp_item!=output_filepath:
        move(tmp_item, output_filepath)
    pass

def to_mmtf(item, output_filepath=None, atom_indices='all', frame_indices='all'):

    from .api_mmtf import to_mmtf as mmtf_to_mmtf_file
    tmp_item = 'mmtf:'+item.split(':')[-1]
    return mmtf_to_mmtf_file (tmp_item, output_filepath=output_filepath, atom_indices=atom_indices, frame_indices=frame_indices)


def to_mmtf_MMTFDecoder(item, atom_indices='all', frame_indices='all'):

    from .api_mmtf import to_mmtf_MMTFDecoder as mmtf_to_mmtf_MMTFDecoder
    tmp_item = 'mmtf:'+item.split(':')[-1]
    tmp_item = mmtf_to_mmtf_MMTFDecoder(tmp_item, atom_indices=atom_indices, frame_indices=frame_indices)
    return tmp_item

def to_molsysmt_MolSys(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.native.io.molsys.files import from_pdb as pdb_to_molsysmt
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_molsysmt(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_mdtraj_Trajectory(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_mdtraj_Trajectory as pdb_to_mdtraj_Trajectory
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_mdtraj_Trajectory(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_mdtraj_Topology(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_mdtraj_Topology as pdb_to_mdtraj_Topology
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_mdtraj_Topology(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_parmed_Structure(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_parmed_Structure as pdb_to_parmed_Structure
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_parmed_Structure(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_pdbfixer_PDBFixer(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_pdbfixer_PDBFixer as pdb_to_pdbfixer_PDBFixer
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_pdbfixer_PDBFixer(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_openmm_Modeller(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_openmm_Modeller as pdb_to_openmm_Modeller
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_openmm_Modeller(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_yank_Topography(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_yank_Topography as pdb_to_yank_Topography
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_yank_Topography(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item


def to_mdanalysis_Universe(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_mdanalysis_Universe as pdb_mdanalysis_Universe
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_mdanalysis_Universe(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_pytraj_Trajectory(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from molsysmt.forms.files.api_pdb import to_pytraj_Trajectory as pdb_pytraj_Trajectory
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file)
    tmp_item=pdb_to_pytraj_Trajectory(tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    remove(tmp_file)
    return tmp_item

def to_nglview(item, atom_indices='all', frame_indices='all'):

    from molsysmt.utils.pdb import tmp_pdb_filename
    from nglview import show_file as nglview_show_file
    from os import remove
    tmp_file = tmp_pdb_filename()
    to_pdb(item, output_filepath=tmp_file, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = nglview_show_file(tmp_file)
    remove(tmp_file)
    return tmp_item

def select_with_MDTraj(item, selection):
    tmp_form=to_mdtraj(item)
    tmp_sel=tmp_form.topology.select(selection)
    del(tmp_form)
    return tmp_sel

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

###### Get

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    tmp_item = to_mmtf_MMTFDecoder(item)
    return tmp_item.num_atoms

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    tmp_item = to_mmtf_MMTFDecoder(item)
    return tmp_item.num_models

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

