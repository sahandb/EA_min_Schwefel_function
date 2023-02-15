# EA_min_Schwefel_function
Implementing an Evolutionary Algorithm (EA) with adaptive mutation

The goal of this project is for you to become familiarized with
I. Implementing an Evolutionary Algorithm (EA) with adaptive mutation step control to solve a classic multi-dimensional function optimization problem
II. Conducting scientific experiments involving EAs
III. Statistically analyzing experimental results from stochastic algorithms
IV. Writing proper technical reports

# Problem
The generalized Schwefel function is defined as follows:
![image](https://user-images.githubusercontent.com/24508376/219115651-0e59bbc8-6e88-4f9e-840b-c4e54dda9572.png)
𝑥𝑖 ∈ [−500,500],𝑖=1,…,𝑛 and 𝛼=418.9829
The Schwefel function is complex, with many local minima. Its dimensionality is controlled by the parameter 𝑛.
The global minimum: 𝑓(𝑥∗)=0,𝑎𝑡 𝑥∗=(420.9687,…,420.9687)
The following plot illustrates the generalized Schwefel function for 𝑛 = 2 :
![image](https://user-images.githubusercontent.com/24508376/219115937-2394a36a-cf3a-4426-ad99-44bab8193076.png)
The problem you are attempting to solve is using an EA with adaptive mutation step control for each dimension to find the global minimum of the Schwefel objective function.

# Implementation


Implement an EA solution for the generalized Schwefel function employing a real-valued representation with adaptive mutation step control for each dimension and appropriate reproduction operators. The adaptive mutation step control must be implemented as 𝑑 real values corresponding to the mutation rates of the 𝑛 elements in 𝑥.

Instead of hard coding all the EA parameters you are to employ a separate configuration file. The EA strategy parameters in your configuration file include, but are not limited to, parameters for initialization, parent selection, reproduction, competition and termination. It must be possible to enable or disable the adaptive mutation step control in your configuration file. Furthermore, your configuration file should also include experiment parameters including, but not limited to, number of runs, dimensionality of generalized Schwefel function (𝑛) and logging parameters.
