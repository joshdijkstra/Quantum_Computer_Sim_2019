# Quantum Computing Group Project

This project is a simulator for a circuit-model quantum computer, together with an implementation of Grover's Algorithm that uses it.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them
To run this you require the following:

*  [Python version 3](https://www.python.org/downloads/) //download the version compatible with your system

Python packages you'll require are:
*  [Matplotlib](https://matplotlib.org/)
*  [Numpy](https://www.numpy.org/)
*  [tkinter](https://wiki.python.org/moin/TkInter)
*  [abc](https://docs.python.org/3/library/abc.html) or [abcplus]

NB: In order to run the GUI, a PC environment or similar C++ Visual Redistributable package may be requried.  


### Installing

A step by step series of examples that tell you how to get a development env running
To download these packages, you can use pip installation for python associated packages with the following code:
```
pip install <package>
```
Download and unzip the zip file of this [quantumcomputing directory](https://gitlab.com/LDobson/quantumcomputing)


A simple way to run the system which should work on any system is using the Command Line UI

## Running the tests

Explain how to run the automated tests for this system


## Deployment
This application is accessed from the command line.
There are 2 ways to run the system: GUI and Command Line. The GUI is the primary way as it includes the visualisation system.

### Running the GUI

The GUI can be temperamental on mac with pop in issues, for the best experience use windows or linux.

To run the GUI use the following command from within the quantum computing directory:
```
python GUI.py
```
If you have a version error you may need to use the following command instead to make sure python 3.x runs:
```
python3 GUI.py
```

The GUI will pop up with buttons for Grover's Method, Custom Path, and the README.


#### Custom Path
Pressing the Custom Cicuit Button will take you to the circuit building screen, Immediately the user will be required to select a number of qubits to run the register on, this can be done by pressing the qbits button and selecting a number from the drop down menu
Once a number has been selected the user must then press the 'Select number of Qbits' Button to lock in their choice.


This will reveal a new set of drop down with gate choices. Set the drop down menus to create a assortment of gates and add them to the stack by pressing the 'Add Gates' Button.
(Note: Adding multiqbit Gates will ignore the next selections depending on their qbit input)

To remove all gates press the 'Clear All Gates' or to remove the last stack press 'Remove last Gates'.

To Compile press the 'Run Gates' button, this will simulate the gates and relay the state probabilities in the dialog box, the user can continue to add gates on top of the current arrangement.

#### Grover's Method
Pressing the Grovers Button will take you to a new screen with a selection of inputs.
Before the simulation can run the user must input three values:

* Number of Qubits: This selects the number of Quantum Bits held within the register
* Number of Iterations: This determines how many times the Grover sequence is repeated, the ideal number of iterations is  $\sqrt{k}$ $$\sqrt{k}$$ where $N$ is the number of Qubits 
* Target Location: This defines the target state the Oracle is searching for (Note: The Target location $T$ must be within the range $0 <= T < 2^(N)$)

Once the three inputs have been selected, Grovers can be run by pressing the 'Run Grovers' Button, this will cause the dialog box to show the inputs selected and other various important information


Running the simulation will also trigger an animated visualisation, this can be restarted by pressing the 'Restart Animation' Button.

If you wish to return to the home page of the application simply press the 'Back to Home' Button.

----------------------------------------------------------------------------------------------------------------------------------------------
### Running the Command Line UI

To run the Command Line UI use the following command:
```
python cmd_runner.py
```

A message will appear welcoming you to the system followed by a prompt to decide whether you'd like to make a custom path or use grovers.

Input `1` for Grovers or `2` for Custom Path

#### GROVERS

Once you select Grovers you will receive separate prompts for each of the following:
* Number of qbits in the register
* Number of iterations grover should perform
* Target location for the algorithm

> All of the above require integers as their inputs

The system should then output a representation of the final state of the register after the application of the algorithm with your specifications.

#### Custom Path

Once you've selected the custom path you will be prompted with the following:
* Number of qbits in the register
* Number of gate sets in the path

> Both of the above prompts require integers as their inputs

Having taken in your specifications the system will now prompt you to input your choices for the distinct gate slots in each of the active gates sets.
> Note that some gates occupy multiple slots in a set

Finally, when you have added all of the gates the system will run and output the final state of the register.




## Authors

* **Max Barnett** - *UI, Documentation, Test Code*
* **Lizzie Dobson** - *Shor's, Tensor Product*
* **Josh Dykstra** - *Gates, Grovers, GUI, Visualisation, Qbit*
* **Nicoline Hemme** - *Gates, Test Code, Error Correction*
* **Asuka Nakamaru-Pinder** - *Code*
* **Lewis Trainer** - *Gates, Grovers*"# Quantum_Computer_Sim" 
"# Quantum_Computer_Sim" 
