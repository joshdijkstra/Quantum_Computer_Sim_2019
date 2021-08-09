"""
This file includes a class for creating Qbits and several methods for tensor operations.
"""
import numpy as np
import random as rnd
import math
import Gates

class Qbit():
    """Form a Qbit with a defined state."""
    def __init__(self,setup=np.array([1,0]),type=None):
        """Create a Qbit and sets the initial state.

        Keyword arguments:
        setup -- the basic array to build the gate (default np.array([1,0]))
        type -- the type of gate desired (default None)
        """
        # e.g. Qbit.Qbit(type='One') will create a qbit in the |1> state
        self.state = setup
        if (type == "One"):
            self.state = np.array([0,1])

    def set(self,input):
        """Set the state of a given Qbit."""
        self.state = input

def qbitTensorPrinter(tensor):
    """Print the probability of the qbits from its tensor."""
    # e.g 1|010> ....can be easily changed to |2>
    strng = ""
    base = math.log(len(tensor),2)
    #print(sum(tensor)**2)
    for x in range(len(tensor)):
        binval = bin(x)[2:].zfill(int(base))
        num = tensor[x]**2
        num = round(num,3)
        #if(num != 0):
            # To change to integer notation change binval to x
        strng += (str(num)+"|"+str(binval)+"> ")
    return strng

def SingleOperatorTensor(A, B):
    """Return the tensor product of two operators A and B in the computational basis."""
    A = np.array(A)
    B = np.array(B)
    if len(np.shape(B))==1:
        B = B.reshape(len(B),1)
    if len(np.shape(A))==1:
        A = A.reshape(len(A),1)
    B_tmp = np.tile(B, np.shape(A))
    A_tmp = A.repeat(np.shape(B)[0], axis=0).repeat(np.shape(B)[1], axis=1)
    return np.multiply(A_tmp, B_tmp)

def OperatorTensor(mylist):
    """Apply the tensor product of cubits from an input array of operation gates"""
    # (tensor product of qubits counting from left to right) """
    result = [1]
    for q in reversed(mylist):
        result = SingleOperatorTensor(q, result)
    return result
