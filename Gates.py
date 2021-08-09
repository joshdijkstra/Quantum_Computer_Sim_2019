"""
This file contains the abstract gate class as well as each of the individual gate classes.
"""
import numpy as np
import math
import cmath
import Qbit
from abc import ABC, abstractmethod

class Gate(ABC):
    """Abstract gate class for inheritance."""
    def __init__(self,name,qbts=None):
        self.name = name
        self.numQbits = qbts

class Id(Gate):
    """Identity gate object"""
    def __init__(self):
        """Generate an Identity gate object."""
        Gate.__init__(self,"Identity",1)
        self.gate = np.array([[1,0],[0,1]])

class Hadamard(Gate):
    """Hadamard gate object."""
    def __init__(self):
        """Generate a Hadamard gate object"""
        Gate.__init__(self,'Hadamard',1)
        self.gate = 1/math.sqrt(2) * np.array([[1,1],[1,-1]])

class X(Gate):
    """X gate object."""
    def __init__(self):
        """Generate an X gate object."""
        Gate.__init__(self,'X',1)
        self.gate = np.array([[0,1],[1,0]])

class Y(Gate):
    """Y gate object."""
    def __init__(self):
        """Generate a Y gate object."""
        Gate.__init__(self,'Y',1)
        self.gate = np.array([[0,-1*cmath.sqrt(-1)],[1*cmath.sqrt(-1),0]])

class Z(Gate):
    """Z gate object."""
    def __init__(self):
        """Generate a Z gate object."""
        Gate.__init__(self,'Z',1)
        self.gate = np.array([[1,0],[0,-1]])

class cZ(Gate):
    """cZ gate object."""
    def __init__(self,size,location):
        """Generate a cZ gate object taking size and location arguments."""
        Gate.__init__(self,'Oracle',size)
        mat = np.identity(2**(size))
        mat[location][location] *= -1
        self.gate = mat

class GrovDiffusion(Gate):
    """GrovDiffusion gate object."""
    def __init__(self,size,N):
        """Generate a GrovDiffusion gate with size and N arguments."""
        Gate.__init__(self,"Grovers Diffusion Gate",size)
        id = np.identity(2**size)
        mat = np.full((2**size,2**size),2/N)
        mat -= id
        self.gate = mat

class T(Gate):
    """T gate object."""
    def __init__(self):
        """Generate a T gate object."""
        Gate.__init__(self,"T",1)
        self.gate = np.array([[1,0],[0,(1+1*cmath.sqrt(-1))/math.sqrt(2)]])

class THerm(Gate):
    """THerm gate object."""
    def __init__(self):
        """Generate a THerm gate object."""
        Gate.__init__(self,"T-Hermitian",1)
        self.gate = np.array([[1,0],[0,(1-1*cmath.sqrt(-1))/math.sqrt(2)]])

class S(Gate):
    """S gate object."""
    def __init__(self):
        """Generate an S gate object."""
        Gate.__init__(self,"S Phase",1)
        self.gate = np.array([[1,0],[0,(1*cmath.sqrt(-1))]])

class SHerm(Gate):
    """SHerm gate object."""
    def __init__(self):
        """Generate a SHerm gate object."""
        Gate.__init__(self,"S Phase Hermitian",1)
        self.gate = np.array([[1,0],[0,(-1*cmath.sqrt(-1))]])


class PhaseShift(Gate):
    """ Phase Shift Gate Object. """
    def __init__(self,phase):
        """Generate a Phase Shift with input of the phase"""
        Gate.__init__(self,'PhaseShift',1)
        a =  cmath.e**(cmath.sqrt(-1)*phase)
        self.gate = np.array([[1,0],[0,a]])

class CNOT(Gate):
    """CNOT gate object."""
    def __init__(self):
        """Generate a CNOT gate object."""
        Gate.__init__(self,'CNOT',2)
        self.gate  = np.array([[1,0,0,0],
                            [0,1,0,0],
                            [0,0,0,1],
                            [0,0,1,0]])

class CV(Gate):
    """CV gate object."""
    def __init__(self):
        """Generate a CV gate object."""
        Gate.__init__(self,'CV-Gate',2)
        self.gate = np.array([[1,0,0,0],
                                [0,1,0,0],
                                [0,0,1,0],
                                [0,0,0,cmath.sqrt(-1)]])

class Toffoli(Gate):
    """Toffoli gate object."""
    def __init__(self):
        """Generate a Toffoli gate object."""
        Gate.__init__(self,'Toffoli',3)
        self.gate = np.array([[1,0,0,0,0,0,0,0],
                            [0,1,0,0,0,0,0,0],
                            [0,0,1,0,0,0,0,0],
                            [0,0,0,1,0,0,0,0],
                            [0,0,0,0,1,0,0,0],
                            [0,0,0,0,0,1,0,0],
                            [0,0,0,0,0,0,0,1],
                            [0,0,0,0,0,0,1,0]])

class Fourier(Gate):
    """ Discrete fourier transform matrix object. """
    def __init__(self, nqbits):
        """ Generate a fourier transformation taking in an argument for the
            number of qubits to act on."""
        Gate.__init__(self, 'Fourier-Gate', nqbits)
        size = 2**nqbits
        w = np.exp(2j*np.pi/size) # phase shift
        f = lambda k, x: w**(k*x)
        unnormalised_matrix= np.fromfunction(np.vectorize(f), (size, size))
        self.gate = unnormalised_matrix/np.sqrt(size)
