# PHYS281_Simulation-Project
## Introduction
My name is Deneth Weerasinghe and I'm a second year Physics, Astrophysics and Cosmology student at Lancaster University.

This project is my gravity simulator written in Python, made as a solution to the Week 6-10 project of the PHYS281 module: Scientific Programming and Modelling Project. 

## Directory structure
### base_classes
This holds all the classes used for the project, placed under a different subdirectory to make importing these classes easier.
###### EphemeridesObjects.py
Class for pulling initial conditions from the JPL Ephemeris using the `astropy` module.  
Each instance is supplied a list of string labels and planet masses from which to form a list of Particle objects i.e. a solar system.  
This is fully dynamic: you can make a solar system containing any combination of solar objects, as long as data exists for that object in the JPL ephemeris.
###### *~~GraphPlotting.py~~ [depreciated]*  
Class used to generate position plots for each planet, depreciated because it could not scale well with large systems of multiple bodies.  
Kept for legacy reasons (mainly for tests of two body systems).
###### NBodyGraphPlotting.py
Class used to generate every plot for each complete system dataset, rather than for individual solar objects like with `GraphPlotting.py`.  
###### Particle.py
The main class in the simulation. This class models particles that undergo gravitation by supplying the constructor with initial conditions.  
It contains methods that update position, velocity and acceleration.
### data_files
Subdirectory for storing all data files containing generated data from various simulations.
### out
Output subdirectory for LaTex and BibTex.
### plots
Storage location for image files of every plot generated.
### simulations
Simulation files that generate data and then save them as binary numpy files for later use.
###### compare_methods.py
Simulates the differences between each of the updating methods: Euler, Euler-Cromer, Euler-Richardson and Verlet by modelling the same object 4 times.
###### solar_sim_1.py
The main simulation for the report, consisting of simulating the solar system, consisting of the Sun, the planets and Pluto.
###### five_bodies_sim.py
A simple simulation for testing out a three body system.
###### two_bodies_sim.py
A simple simulation for testing out a two body system, used for the Moodle exercises.
### tests
Subdirectory holding all test files i.e. files that output data in the terminal or output plots.  
The data has been saved by the simulation files so all the test files extract already generated data.
#### exercise
Subdirectory that holds all tests relating to the exercises for the project set in the Moodle page.
###### exercise_1_2.py
Test file for generating the projectile motion plot to be used in the report.
#### indev
"In development"; holds all the remaining tests, including some unit tests as well as the final tests.
###### compare_methods_test.py
Plots 4 identical satellites orbiting Earth with the same initial conditions, only differing in the numerical method used.
###### different_methods_test.py
Only plots 2 satellites, one using Euler and the other using Euler-Cromer.
###### ephemerides_test.py
Testing to get used to retrieving data from JPL.
###### indev_tests.py
Miscellaneous testing.
###### solar_sim_tests.py
The main testing file used to generate all solar system plots, in both 3D and 2D as well as energy and momentum plots.
###### five_body_test.py
A simple 3 body test consisting of the Earth and 2 satellites.
###### two_body_test.py
A simple 2 body test consisting of the Earth and a single satellite.