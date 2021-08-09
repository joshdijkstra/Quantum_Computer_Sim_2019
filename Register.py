"""
This file contains the Register class which holds the qubit data
"""
import numpy as np
import Qbit
import Gates
import Grover

class Register():
    def __init__(self,numQbits):
        """Creates a register taking in the number of qubits inside

        Keyword argument:
        numQbits -- The number of qbits held within the register
        (All  qbits set to default |0> state)
        """
        self.numQbits = numQbits
        qbts = []
        qbtsStates =[]
        # Creates n qbits all in the |0> state
        for x in range(numQbits):
            qbts.append(Qbit.Qbit())
            qbtsStates.append(qbts[x].state)
        tnsr = Qbit.OperatorTensor(qbtsStates)
        self.state = []
        for x in range(len(tnsr)):
            self.state.append(tnsr[x][0])
        self.statedim = 2**self.numQbits
        self.listStates = [self.state]
        # array that each element contains a tensored gate row (matrix)
        self.operations = []

    def performMeasurement(self):
        """
        Function that collapses the system into a state in the computational basis
        Returns the state its collapsed into
        """
        rn = np.random.rand()
        threshold = 0
        for k in range(self.statedim):
            prob = np.abs(self.state[k])**2 # prob of being observed in |k>
            threshold += prob
            if rn<threshold:
                collapsed_state = np.zeros(self.statedim)
                collapsed_state[k] = 1
                self.state = collapsed_state
                print('system observed in state |'+str(k)+'>')
                return k

    def updateState(self,newState):
        """Function that updates the current tensored state to a newState"""
        # updates the tensored state of qbits
        self.listStates.append(newState)
        self.state = newState

    def addGates(self, list_of_gates):
        """
        Function that takes in an array of gates e.g [Gates.Hadamard(),Gates.Hadamard(),Gates.Hadamard() ]
        Adds the set of gates onto the operations stack before computation
        """
        # Adds a row of gates to the list of operations
        gates = []
        for x in range(len(list_of_gates)):
            print(list_of_gates[x].name)
            gates.append(list_of_gates[x].gate)
        operator = Qbit.OperatorTensor(gates)
        assert np.shape(operator)==(self.statedim, self.statedim), "operator is wrong dimension"
        self.operations.append(operator)

    def applyGates(self):
        """Function that performs all the calculations from the operations stack"""
        # multiplies all tensored gates in self.operations and updates state
        for x in range(len(self.operations)):
            newState = np.matmul(self.operations[x],self.state)
            self.updateState(newState)
        #print(self.state)

    def setInitial(self,qbits):
        """Function that takes in a list of edited qbits that arent necessarily in the default |0> state"""
        assert len(qbits) == self.numQbits, "Wrong Qbit size for register"
        qbtsStates = []
        for x in range(self.numQbits):
            qbtsStates.append(qbits[x].state)
        tnsr = Qbit.OperatorTensor(qbtsStates)
        self.state = []
        for x in range(len(tnsr)):
            self.state.append(tnsr[x][0])
        self.listStates = [self.state]


def allHadamard(numQbits):
    """Function that creates a array of gates that are all hadamards"""
    # Creates a row of all hadamard gates to act on all qbits
    hdmd = Gates.Hadamard()
    row = []
    for x in range(numQbits):
        row.append(hdmd)
    return row
