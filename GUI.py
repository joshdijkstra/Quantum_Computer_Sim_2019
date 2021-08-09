import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure



import tkinter as tk
from tkinter import ttk
import os
import subprocess
import math

from Register import Register
import Gates
import Grover
import Qbit


LARGE_FONT= ("Verdana", 12)


class QuantumComputingGUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "QCGP")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Home Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.configure(background='#cdcdcd') # colour of the background




        button = ttk.Button(self, text="Custom Circuit",
                            command=lambda: controller.show_frame(PageTwo))
        button.pack(fill="both")

        button3 = ttk.Button(self, text="Grovers",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack(fill="both")

        button4 = ttk.Button(self, text="Open Read Me",
                            command=self.openReadme)
        button4.pack(fill="both")

    def openReadme(self):
        file = "README.md"
        cwd = os.getcwd()
        subprocess.call(file,shell=True)



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Custom Circuit", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()



        self.Tbox = tk.Text(self, height=20, width=40)
        self.Tbox.pack(fill="both",expand=True)



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        self.numQbits = 3
        self.Gates = []
        self.pointer = 0
        self.phase = 0
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Custom Circuit", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        self.gatesDict ={
                    "Identity":Gates.Id(),
                    "Hadamard":Gates.Hadamard(),
                    "X":Gates.X(),
                    "Y":Gates.Y(),
                    "Z":Gates.Z(),
                    "T":Gates.T(),
                    "THerm":Gates.THerm(),
                    "S":Gates.S(),
                    "SHerm":Gates.SHerm(),
                    "CNOT":Gates.CNOT(),
                    "CV":Gates.CV(),
                    "Toffoli":Gates.Toffoli(),
                    "Phase":Gates.PhaseShift(self.phase)
                    }

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="top")

        #button2 = ttk.Button(self, text="Restart Animation",
    #                        command=self.restart)
    #    button2.pack(side="top")
        button7 = ttk.Button(self, text="Select Number of Qbits",
                            command=self.changeQbits)
        button7.pack(side="top",fill="x")

        maxQbits = 6
        optionList = list(range(1,maxQbits))
        self.v = tk.StringVar()
        self.v.set("Qbits")
        self.om1 = tk.OptionMenu(self, self.v, *optionList)
        self.om1.pack(fill="both")

        button3 = ttk.Button(self, text="Add Gates",
                            command=self.addGates)
        button3.pack(side="top",fill="x")

        button4 = ttk.Button(self, text="Remove last Gates",
                            command=self.removeGates)
        button4.pack(side="top",fill="x")

        button5 = ttk.Button(self, text="Clear All Gates",
                            command=self.clearGates)
        button5.pack(side="top",fill="x")

        button6 = ttk.Button(self, text="Run Gates",
                            command=self.applyGates)
        button6.pack(side="top",fill="x")

        button7 = ttk.Button(self, text="Enter Phase",
                            command=self.enterPhase)
        button7.pack(side="bottom",fill="x")

        self.entr1 = ttk.Entry(self,text="Phase Gate Angle")
        self.entr1.pack(side="bottom",fill="x")





        self.Tbox = tk.Text(self, height=60, width=50,wrap="word")
        self.Tbox.pack(side="left")
        self.Tbox.insert("end","Welcome to the custom circuit creator, to get started select a number of qubits\n")

        self.ddms = []
        self.ddmv = []


    def enterPhase(self):
        ph = self.entr1.get()
        try:
            self.phase = float(ph)
        except:
            self.Tbox.insert("end","Phase is not a float\n")

    def addQbits(self):
        self.ddmv=[]
        self.ddms = []
        gateOptionList = []
        for gates in self.gatesDict:
            gateOptionList.append(gates)
        for x in range(self.numQbits):
            self.ddmv.append(tk.StringVar())
            self.ddmv[x].set("Identity")
            self.ddms.append(tk.OptionMenu(self, self.ddmv[x], *gateOptionList))
            self.ddms[x].pack(side="left",fill="x")

    def destroyMenus(self):
        for x in range(len(self.ddms)):
            self.ddms[x].pack_forget()

    def changeQbits(self):
        if(self.v.get()=="Qbits"):
            self.Tbox.insert("end","Please Select a number of Qbits to Change to\n")
        else:
            self.numQbits = int(self.v.get())
            self.destroyMenus()
            self.Gates = []
            self.Tbox.delete(1.0,"end")
            self.addQbits()
            tk.update()


    def addGates(self):
        boxData = []
        gates = []
        applied_gates = []

        for x in range(len(self.ddmv)):
            boxData.append(self.ddmv[x].get())
            gates.append(self.gatesDict[boxData[x]])


        for x in range(len(gates)):
            if(gates[x] != 0):
                qs = gates[x].numQbits
                print(gates[x].name + str(qs))
                if(qs > 1):
                    if(x + qs > len(gates)):
                        self.Tbox.insert("end","Multiqubit gate out of range\n")
                        return
                    for j in range(1,qs):
                        gates[x+j] = 0
                        print(gates)

        for x in range(len(gates)):
            if(gates[x] != 0):
                applied_gates.append(gates[x])

        for x in range(len(applied_gates)):
            self.Tbox.insert("end",applied_gates[x].name+" ")

        for x in range(len(applied_gates)):
            if(applied_gates[x].name == "PhaseShift"):
                print("Changing Phase Gate, Phase: "+str(self.phase))
                applied_gates[x] = Gates.PhaseShift(self.phase)
                self.Tbox.insert("end","Phase:"+ str(self.phase)+"\n")



        self.Tbox.insert("end","\n")
        self.Gates.append(applied_gates)
        print(self.Gates)

    def removeGates(self):
        if (len(self.Gates) > 0):
            self.Gates.pop()
        self.Tbox.insert("end","Removing last Gate added\n")
        print(self.Gates)

    def clearGates(self):
        self.Gates = []
        self.Tbox.delete(1.0,"end")
        self.Tbox.insert("end","Gates Cleared\n")

    def applyGates(self):
        self.Tbox.insert("end","Simulating Gates\n")
        self.reg = Register(self.numQbits)
        for x in range(len(self.Gates)):
            self.reg.addGates(self.Gates[x])
        self.reg.applyGates()
        string1 = str(Qbit.qbitTensorPrinter(self.reg.state))
        self.Tbox.insert("end",string1+"\n")
        self.ys = self.reg.listStates




class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        self.pointer = 0
        tk.Frame.__init__(self, parent)
        maxQbits = 10
        maxIterations = 15


        label = tk.Label(self, text="Visualisation Of Grovers algorithm in practice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack(side="top", fill = "x")

        button2 = ttk.Button(self, text="Restart Animation", command=self.restart)
        button2.pack(side="top",fill = "x")

        button3 = ttk.Button(self, text="Run Grovers", command=self.Grovers)
        button3.pack(side="top",fill="x")


        # Qbits
        optionList = list(range(2,maxQbits))
        self.v = tk.StringVar()
        self.v.set("Select Number of Qbits")
        self.om1 = tk.OptionMenu(self, self.v, *optionList)
        self.om1.pack(side="top",fill="x")

        # Iterations
        optionList = list(range(1,maxIterations))
        self.vi = tk.StringVar()
        self.vi.set("Select Number of Iterations")
        self.om2 = tk.OptionMenu(self, self.vi, *optionList)
        self.om2.pack(side="top",fill="x")

        # Location
        optionList = list(range(0,2**(maxQbits)))
        self.vk = tk.StringVar()
        self.vk.set("Target Location")
        self.om3 = tk.OptionMenu(self, self.vk, *optionList)
        self.om3.pack(side="top",fill="x")


        # Text Boxs
        self.Tbox = tk.Text(self, height=20, width=40,wrap="word")
        self.Tbox.pack(side="left",fill="both",expand=True)


        self.xs = 0
        self.ys = [0]

        self.fig = plt.figure()
        self.win = self.fig.canvas.manager.window
        self.win.after(100, self.animated_barplot)
        ax1 = self.fig.add_subplot(111)


        plt.ylabel('Amplitude')
        plt.title('Grovers')
        plt.xlabel("State")
        plt.ylim(-1.1,1.1)

        plt.axhline(y=0, xmin=0, xmax=1)

        canvas = FigureCanvasTkAgg(self.fig, self)
        #canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def animated_barplot(self):
        x = self.ys[self.pointer]
        rects = plt.bar(self.xs, x,  align = 'center')
        for i in range(1,len(self.ys)):
            x = self.ys[i]
            for rect, h in zip(rects, x):
                rect.set_height(h)
            self.fig.canvas.draw()
            plt.pause(1.2)

    def restart(self):
        self.pointer = 0
        plt.clf()
        plt.ylabel('Amplitude')
        plt.title('Grovers')
        plt.xlabel("State")
        #self.win = self.fig.canvas.manager.window
        plt.ylim(-1.1,1.1)
        #self.win.after(100, self.animated_barplot)
        plt.axhline(y=0, xmin=0, xmax=1)
        self.win.after(100, self.animated_barplot)

    def Grovers(self):
        qbits = int(self.v.get())
        iterations = int(self.vi.get())
        location = int(self.vk.get())
        if(location < 2**qbits):
            strn = ("New run with " + str(qbits) + " qbits, " + str(iterations) + " iterations, target state: " + str(location)+"\n")
            self.Tbox.insert("end",strn)
            self.Tbox.insert("end","Gates:\n")
        else:
            self.Tbox.insert("end","Target location not within allowed range\n")
        reg = Register(qbits)

        grov = Grover.Grovers(qbits,iterations,location)
        grov.run(reg)
        grov.getOpNames()
        for x in range(len(grov.listofnames)):
            self.Tbox.insert("end",str(grov.listofnames[x])+"\n")

        self.xs = list(range(0,2**qbits))
        self.ys = reg.listStates
        self.qbits = qbits
        self.restart()

app = QuantumComputingGUI()
app.mainloop()
