"""
This program runs the system entirely from the command line.
"""
from Register import Register
import Gates
import Grover
import Qbit

def user_setup():
    """Fill in the variables for the main by asking for user input."""
    not_an_integer = "\nPlease input an integer"
    #General variables for any run method
    indicator = False
    while (indicator == False):
        run_method = int(input("\nWould you like to run 1) Grover's Algorithm or 2) a custom gate path? -- Please enter 1 or 2\n\n"))
        if (run_method == 1):
            indicator = True
        elif (run_method ==2):
            indicator = True
        else:
            print("Sorry, that input is not valid, please choose 1 or 2 \n\n")
    indicator = False
    while (indicator == False):
        try:
            num_qbits = int(input("\nHow many qbits do you want in the register? (Please choose an integer between 1 and 12, other numbers may exceed computer memory).\n\n"))
        except ValueError:
            print(not_an_integer)
        if (num_qbits >= 1) and (num_qbits <= 12):
            indicator = True
        else:
            print("Sorry, that input is not valid, please choose an integer between 1 and 12\n\n")
    indicator = False
    #Generate the register now that you have the number of qbits required
    reg = Register(num_qbits)
    return run_method, reg, num_qbits

def run_method_grover(reg, num_qbits):
    """Run Grover's method with extra variable input.


        Keyword arguments:
        reg -- the generated register for the system
        num_qbits -- the specified number of qbits for the system
    """
    not_an_integer = "\nPlease input an integer"
    indicator = False
    iterations = 0
    target_location = 0
    while (indicator == False):
        try:
            iterations = int(input("\nHow many iterations of Grover should run? -- please give an integer\n\n"))
        except ValueError:
            print(not_an_integer)
        else:
            indicator = True
    indicator = False
    while (indicator == False):
        try:
            target_location = int(input("\nWhat is the target location? -- please give an integer\n\n"))
        except ValueError:
            print(not_an_integer)
        else:
            indicator = True
    #instantiate premade path of grovers
    grov = Grover.Grovers(num_qbits, iterations, target_location)
    #run grovers using the register
    grov.run(reg)
    print("\n" + Qbit.qbitTensorPrinter(reg.state))

def run_method_custom(reg, num_qbits):
    """Generate a custom path of gates based on user inputs.

        Keyword arguments:
        reg -- the generated register for the system
        num_qbits -- the specified number of qbits for the system
    """
    not_an_integer = "\nPlease input an integer"
    indicator = False
    while (indicator == False):
        try:
            num_gate_sets = int(input("\nHow many gate sets should the path have?\n\n"))
        except ValueError:
            print(not_an_integer)
        else:
            indicator = True
    for x in range(num_gate_sets):
        print("\nEnter a number associated with each gate\n\n")
        print("id:      1       hd:         2\n")
        print("X:       3       Y:          4\n")
        print("Z:       5       T:          6\n")
        print("THerm:   7       S:          8\n")
        print("SHerm:   9       PhaseShift: 10\n")
        print("CNOT:    11      CV:         12\n")
        print("Toffoli: 13\n")
        active_gates = [None] * num_qbits
        i = 0
        while (i < num_qbits):
            indicator = False
            while(indicator == False):
                try:
                    gate_choice = int(input("\nPlease enter the gate you would like to use for the " + str(i) + " port on the " + str(x) + " set\n\n"))
                    if (gate_choice <= 13 and gate_choice >= 1):
                        print("\n You have chosen " + str(gate_choice) + "\n")
                    else:
                        raise ValueError("That is not a valid gate choice.")
                except ValueError:
                        print(not_an_integer)
                else:
                    #CNOT, CV, Toffoli are multibit
                    #PhaseShift requires an angle
                    if (gate_choice == 1):
                        active_gates[i] = (Gates.Id())
                        print("ID gate added\n")
                    elif (gate_choice == 2):
                        active_gates[i] = (Gates.Hadamard())
                        print("Hadamard gate added\n")
                    elif (gate_choice == 3):
                        active_gates[i] = (Gates.X())
                        print("X gate added\n")
                    elif (gate_choice == 4):
                        active_gates[i] = (Gates.Y())
                        print("Y gate added\n")
                    elif (gate_choice == 5):
                        active_gates[i] = (Gates.Z())
                        print("Z gate added\n")
                    elif (gate_choice == 6):
                        active_gates[i] = (Gates.T())
                        print("T gate added\n")
                    elif (gate_choice == 7):
                        active_gates[i] = (Gates.THerm())
                        print("THerm gate added\n")
                    elif (gate_choice == 8):
                        active_gates[i] = (Gates.S())
                        print("S gate added\n")
                    elif (gate_choice == 9):
                        active_gates[i] = (Gates.SHerm())
                        print("SHerm gate added\n")
                    elif (gate_choice == 10):
                        try:
                            shift_angle = float(input("\nInput an angle for the PhaseShift gate\n\n"))
                        except ValueError:
                            print("Sorry please put in a float between 0 and 2pi")
                        else:
                            active_gates[i] = (Gates.PhaseShift(shift_angle))
                            print("PhaseShift gate added with angle " + str(shift_angle) + "\n")
                    elif (gate_choice == 11):
                        if (i == num_qbits - 1):
                            active_gates[i] = None
                            print("\nSorry, that gate requires more qbits than available. Please put another choice.\n")
                        else:
                            active_gates[i] = (Gates.CNOT())
                            i+=1
                            print("CNOT gate added (NB: CNOT GATES TAKE 2 QBITS)\n")
                    elif (gate_choice == 12):
                        if (i == num_qbits - 1):
                            active_gates[i] = None
                            print("\nSorry, that gate requires more qbits than available. Please put another choice.\n")
                        else:
                            active_gates[i] = (Gates.CV())
                            i+=1
                            print("CV gate added (NB: CV GATES TAKE 2 QBITS\n")
                    else:
                        if (i == num_qbits - 2):
                            active_gates[i] = None
                            print("\nSorry, that gate requires more qbits than available. Please put another choice.\n")
                        else:
                            active_gates[i] = (Gates.Toffoli())
                            i+=2
                            print("Toffoli gate added (NB: Toffoli GATES TAKE 3 QBITS)\n")
                    indicator = True
                    i+=1
        hold_gates = []
        for j in range(len(active_gates) ):
            if (active_gates[j] != None):
                hold_gates.append(active_gates[j])
        print(hold_gates)
        reg.addGates(hold_gates)
        active_gates = [None] * num_qbits
        hold_gates = []
    #Run the register with the custom path
    reg.applyGates()
    print("\n" + Qbit.qbitTensorPrinter(reg.state))



def main():
    """Run the user setup method then the appropriate run method"""
    print("\n***Welcome to the command line UI for the QCGP***\n\n")
    run_method, reg, num_qbits = user_setup()
    if (run_method == 1):
        run_method_grover(reg, num_qbits)
    else:
        run_method_custom(reg, num_qbits)

main()
