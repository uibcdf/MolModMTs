from molsysmt._private.variables import is_all
from molsysmt.basic import select
import numpy as np

class MSMH5Reporter(object):

    def __init__(self, file, reportInterval, steps, selection='all',
            topology=True, time=True, box=True, coordinates=True, velocities=False,
            potentialEnergy=False, kineticEnergy=False, temperature=False,
            includeInitialContext=True, constantReportInterval=True,
            constantStepSize=True, constantBox=True,
            compression='gzip', compression_opts=4,
            int_precision='single', float_precision='single',
            syntax='MolSysMT'):

        self._initialized = False

        self._needsPositions = coordinates
        self._needsVelocities = velocities
        self._needsForces = False
        self._needEnergy = (potentialEnergy or kineticEnergy or totalEnergy or temperature)

        self._time = time
        self._box = box
        self._coordinates = coordinates
        self._velocities = velocities
        self._potentialEnergy = potentialEnergy
        self._kineticEnergy = kineticEnergy
        self._temperature = temperature

        self._reportInterval = reportInterval
        self._stepSize = stepSize
        self._steps = steps

        self._atom_indices = selection

        if not is_all(self._atom_indices):
            if topology is None:
                raise ValueError('A topology object is needed.')
            self._atom_indices = select(topology, selection=selection, syntax=syntax)

        self._file_handler = MSMH5FileHandler(file, io_mode='w', creator='OpenMM',
                compression=compression, compression_opts=compression_opts,
                int_precision=int_precision, float_precision=float_precision,
                length_unit='nm', time_unit='ps', energy_unit='kJ/mol',
                temperature_unit='kelvin', charge_unit='e', mass_unit='dalton')

        if topology is not None:
            self._file_handler.write_topology(topology, selection=self._atom_indices)


    def _initialize(self, simulation):

        import openmm as mm
        system = simulation.system
        frclist = system.getForces()
        if self._temperature:
            dof = 0
            for i in range(system.getNumParticles()):
                if system.getParticleMass(i) > 0*unit.dalton:
                    dof += 3
            dof -= system.getNumConstraints()
            if any(isinstance(frc, mm.CMMotionRemover) for frc in frclist):
                dof -= 3
            self._dof = dof

        # Tengo que detectar si hay barostato

        self._initialized = True

    def describeNextReport(self, simulation):

        steps_left = simulation.currentStep % self._reportInterval
        steps = self._reportInterval - steps_left
        return (steps, self._needsPositions, self._needsVelocities, self._needsForces, self._needEnergy)

    def report(self, simulation, state):

        if not self._initialized:
            self._initialize(simulation)

    def close(self):

        return self._file_handler.close()

