# late submmition to qhack, but fun experience
Team Name:
POIG

Project Description:   
goal:   
predict the ground state energies of molecules using Coulomb matrices as input using quantum-classical Neural Networks. I hope to combine advanced feed forward neural network(FFNN) and quantum neural network(QNN) to achieve higher learning rate, this could also lead to futher project like predict atomization energies, prioritize geometry searches, and interpret rotational spectra with columb matrices using quantum computation power.   
   
To conclude this project main purpose is using the ability to predict electronic properties without performing new simulations for each molecule/material, machine learning techniques open up exciting pathways for rational design of new compounds. Combined with numerous efforts to catalog and standardize datasets (such as Materials Project and Aflow), these methods will be invaluable for many scientific and technological applications.  
   
in this project I found hard to use qiskit pytorch with some serious bug, so I spend sometime working with the qiskit-machine-learning module.But instead, using pennylane is faster.

It will train over 16,242 Molecules ground state with FNN&QNN. training databset from kaggle

1.1.2 reference (those I think is important)-  
[1] Predicting excited states from ground state wavefunction by supervised quantum machine learning Hiroki Kawai, Yuya O. Nakagawa (where my idea come from)  
[2] Tree based machine learning framework for predicting ground state energies of molecules (where the data set from, can download from kaggle)  
[3] qiskit- hybrid neural network (where I get idea how to do it)  
[4] pennylane- recurrent neural network lstm (where I get idea of####)  
[5] github- AdvancedNNfromScratch (where I understand step need for this project)  
[6] Can One Hear the Shape of a Molecule (from its Coulomb Matrix Eigenvalues)? Joshua Schrier Journal of Chemical Information and Modeling 2020 60 (8), 3804-3811 DOI: 10.1021/acs.jcim.0c00631 (where I understand little about coulomb matrix, how much thing can do with it)  

Presentation:
https://github.com/poig/QHack/blob/main/qhack2022/latest-using%20pennylane.ipynb

Source code:
https://github.com/poig/qhack

Which challenges/prizes would you like to submit your project for?  
Young Scientist Challenge
