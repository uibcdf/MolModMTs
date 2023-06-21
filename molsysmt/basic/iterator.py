from molsysmt._private.digestion import digest
from molsysmt._private.exceptions import NotImplementedIteratorError
#from molsysmt._private.exceptions import IteratorError

class Iterator():
    """
    Iterator over attributes of a molecular system.

    This class is an iterator over specific topological or structural
    attributes of a molecular system. New objects can be instanstated
    specifying the set of attributes to be iterated, the selection of elements
    to get those attributes, and some input parameters to
    control the iterations.

    Parameters
    ----------

    molecular_system : molecular system
        The molecular system in any of :ref:`the supported forms
        <Introduction_Forms>` to be analysed by the function.

    selection : tuple, list, numpy.ndarray or str, default 'all'
        Selection of elements of the molecular system to be checked by the function. The selection can be
        given by a list, tuple or numpy array of atom indices (0-based
        integers); or by means of a string following any of :ref:`the selection
        syntaxes parsable by MolSysMT <Introduction_Selection>`.

    syntax : str, default 'MolSysMT'
        :ref:`Supported syntax <Introduction_Selection>` used in the `selection` argument (in case
        it is a string).

    **kwargs : {{keyword : str,  value : (bool, int)}, default None}
        The elements to be checked in the molecular system are introduced as
        additional keywords with value either 'True', 'False', or by means of an integer to
        indicate to amount of specific elements the system is composed of.


    """


    @digest()
    def __init__(self,
                 molecular_system,
                 element = 'atom',
                 selection = 'all',
                 start = 0,
                 stop = None,
                 step = 1,
                 chunk = 1,
                 structure_indices = None,
                 syntax = 'MolSysMT',
                 output_type = 'values',
                 output_form = 'molsysmt.MolSys',
                 **kwargs,
                 ):
        """
        Iterator over attributes of a molecular system.

        This class is an iterator over specific topological or structural
        attributes of a molecular system. New objects can be instanstated
        specifying the set of attributes to be iterated, the selection of elements
        to get those attributes, and some input parameters to
        control the iterations.
        """



        from . import select, get_form, where_is_attribute, convert
        from molsysmt.attribute import is_structural_attribute
        from molsysmt.form import _dict_modules

        self.molecular_system = molecular_system
        self.element = element
        self.indices = select(molecular_system, element=element, selection=selection, syntax=syntax)
        self.structure_indices = structure_indices
        self.start = start
        self.stop = stop
        self.step = step
        self.chunk = chunk
        self.iterator_index = 0

        self.arguments = []

        self._iterators = []
        self._output_dictionary = {}
        self._output_type = output_type
        self._output_form= output_form
        self._output_molecular_system = None

        for ii, key in enumerate(kwargs.keys()):
            if kwargs[key]:
                self.arguments.append(key)

        if len(self.arguments)==0:
            self.arguments = ['structure_id', 'time', 'coordinates', 'box']
            self._output_molecular_system = convert(self.molecular_system, selection=selection,
                    structure_indices=None, to_form=self._output_form)

        self._output_dictionary = {ii:None for ii in self.arguments}

        aux_items_forms = {}
        aux_items_arguments = {}

        for argument in self.arguments:
            item, form = where_is_attribute(self.molecular_system, argument)
            if item in aux_items_forms:
                aux_items_arguments[item].append(argument)
            else:
                aux_items_forms[item]=form
                aux_items_arguments[item]=[argument]

        runs_in_structures = False
        if all([is_structural_attribute(ii) for ii in self.arguments]):
            runs_in_structures = True

        for item in aux_items_forms:

            tmp_arguments = {ii:True for ii in aux_items_arguments[item]}

            if runs_in_structures:
                if item is not None:
                    tmp_iterator = _dict_modules[aux_items_forms[item]].StructuresIterator(item, atom_indices=self.indices, start=self.start,
                       stop=self.stop, step=self.step, chunk=self.chunk, structure_indices=self.structure_indices, output_type='dictionary',
                       **tmp_arguments)
            else:
                tmp_iterator = _dict_modules[aux_items_forms[item]].TopologyIterator(item, element=self.element, indices=self.indices, start=self.start,
                       stop=self.stop, step=self.step, chunk=self.chunk, output_type='dictionary',
                       **tmp_arguments)

            self._iterators.append(tmp_iterator)

        del(aux_items_forms, aux_items_arguments)

    def __iter__(self):
        """
        Iterator over attributes of a molecular system.

        This class is an iterator over specific topological or structural
        attributes of a molecular system. New objects can be instanstated
        specifying the set of attributes to be iterated, the selection of elements
        to get those attributes, and some input parameters to
        control the iterations.
        """


        return self

    def __next__(self):
        """
        Iterator over attributes of a molecular system.

        This class is an iterator over specific topological or structural
        attributes of a molecular system. New objects can be instanstated
        specifying the set of attributes to be iterated, the selection of elements
        to get those attributes, and some input parameters to
        control the iterations.
        """


        try:

            for iterator in self._iterators:

                self._output_dictionary.update(iterator.__next__())

        except:

            raise StopIteration

        if self._output_molecular_system is None:
            if self._output_type=='values':
                output = list(self._output_dictionary.values())
                if len(output) == 1:
                    output = output[0]
            elif self._output_type=='dictionary':
                output = self._output_dictionary
            return  output
        else:
            from . import set
            set(self._output_molecular_system, element='atom', coordinates=self._output_dictionary['coordinates'])
            set(self._output_molecular_system, element='system', box=self._output_dictionary['box'],
                    structure_id=self._output_dictionary['structure_id'], time=self._output_dictionary['time'])
            return self._output_molecular_system

