from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister

qr = QuantumRegister(1, name="quantum")
cr = ClassicalRegister(1, name="classical")
qc = QuantumCircuit(qr, cr)

qc.h(0)
qc.measure(0, 0)

qc.draw("mpl", filename="quantum_circuit.png")
