import sys
#from this import d
import pennylane as qml
from pennylane import numpy as np


def second_renyi_entropy(rho):
    """Computes the second Renyi entropy of a given density matrix."""
    # DO NOT MODIFY anything in this code block
    rho_diag_2 = np.diagonal(rho) ** 2.0
    return -np.real(np.log(np.sum(rho_diag_2)))


def compute_entanglement(theta):
    """Computes the second Renyi entropy of circuits with and without a tardigrade present.

    Args:
        - theta (float): the angle that defines the state psi_ABT

    Returns:
        - (float): The entanglement entropy of qubit B with no tardigrade
        initially present
        - (float): The entanglement entropy of qubit B where the tardigrade
        was initially present
    """
    

   

    dev = qml.device("default.qubit", wires=3)

    # QHACK #
    @qml.qnode(dev)
    def circuit():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0,1])
        qml.PauliX(wires=0)
        qml.CRY(theta,wires=[1,2])
        qml.PauliX(wires=1)
        return qml.density_matrix(wires=1)
    
    @qml.qnode(dev)
    def circuit_1():
        qml.Hadamard(wires=0)
        qml.CNOT(wires=[0,1])
        qml.PauliX(wires=1)
        qml.CRY(theta,wires=[1,2])
        qml.CNOT(wires=[2,1])
        return qml.density_matrix(wires=1)

    probs = circuit()
    probs_1= circuit_1()
    

    DMatrix = second_renyi_entropy(probs)
    DMatrix_1 = second_renyi_entropy(probs_1)
    
    return DMatrix,DMatrix_1


    # QHACK #


if __name__ == "__main__":
    # DO NOT MODIFY anything in this code block
    theta = np.array(sys.stdin.read(), dtype=float)

    S2_without_tardigrade, S2_with_tardigrade = compute_entanglement(theta)
    #answ = compute_entanglement(theta)
    print(*[S2_without_tardigrade, S2_with_tardigrade], sep=",")
    #print(answ)
