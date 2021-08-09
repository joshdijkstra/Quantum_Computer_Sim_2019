"""
This File contains the grover class, an object used to implement Grover's Algorithm
"""
import Qbit
import Gates
import Register
import numpy as np


class Grovers():
    """ """
    def __init__(self, numQbits, iterations, location):
        """Creates a grover circuit specific to the register its going to act on

        Keyword arguments:
        numQbits -- the number of Qbits within the register
        iterations -- how many repeats of the oracle and grovers diffusion applied
        location -- target state location
        """
        self.qbits = numQbits
        self.iterations = iterations
        assert(location >= 0), "qbit location not positive"
        assert(location < 2**numQbits), "qbit location not within range"
        self.n = location
        self.initialHad = Register.allHadamard(numQbits)
        self.oracle = self.createOracle()
        self.amplitude = self.createAmplitude()
        self.listofnames = []

    def run(self,Register):
        """Function that takes in the register its going to act on and updates its state"""
        # Runs the algorithm on input register
        assert (Register.numQbits == self.qbits), "Register wrong size to apply this Grovers function"
        ops1 = self.collectOperators()
        for x in range(len(ops1)):
            Register.addGates(ops1[x])
        Register.applyGates()

    def collectOperators(self):
        """
        Gathers all the sets of gates together and returns it as a 2d array ready to be added to the
        register's list of operations
        """
        # Function to return the gate orders depending on iterations
        final = [self.initialHad]
        for x in range(self.iterations):
            for y in range(len(self.oracle)):
                final.append(self.oracle[y])
            for j in range(len(self.amplitude)):
                final.append(self.amplitude[j])
        return final

    def createOracle(self):
        """Creates the oracle gates set"""
        # Creates the oracle's set of operators
        zG = Gates.cZ(self.qbits,self.n)
        orc = [[zG]]
        return orc

    def createAmplitude(self):
        """Creates the grover diffusion set of gates"""
        # Creates the amplitude section of grovers
        grovDif = Gates.GrovDiffusion(self.qbits,2**self.qbits)
        ampl = [[grovDif]]
        return ampl

    def getOpNames(self):
        """Returns a list of the names of the operations used"""
        # Creates a list of all the names of operators being used
        ops = self.collectOperators()
        for x in range(len(ops)):
            self.listofnames.append(ops[x][0].name)
