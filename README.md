# CS540-Assignment-4
Page Replacement Algorithms

Introduction
This project provides a Python implementation of three classic page replacement algorithms used in operating systems for memory management. Understanding these algorithms is crucial for grasping how modern computers efficiently handle memory access and paging. The algorithms simulated here include:

- First In First Out (FIFO)
- Least Recently Used (LRU)
- Optimal
The simulation demonstrates how each algorithm processes a predefined sequence of page requests and manages a limited number of memory frames.

Prerequisites
The code is written in Python and requires Python 3.6 or later. You can download Python from python.org and install it on your machine if it's not already installed.

Installation
This program does not require any external libraries and only uses Python's standard libraries. To get started, clone this repository to your local machine:

git clone https://github.com/vylvo/CS540-Assignment-4.git
cd CS540-Assignment-4

Running the Simulation
To run the simulation, navigate to the project directory in your terminal and execute the following command:

python Page_Replacement_Algorithms.py
This will run the script and display the results for each page replacement algorithm based on the predefined page sequence and frame size.

Program Structure
Page_Replacement_Algorithms.py: This script contains the implementations of the FIFO, LRU, and Optimal algorithms. It also includes a set of predefined page references and frame counts, which are used to simulate the page replacement process.

Page Replacement Algorithms
FIFO: This algorithm manages memory frames based on a first-in, first-out logic. It evicts the oldest page when a new page needs to be loaded, and no free frames are available.
LRU: LRU prioritizes keeping the most recently used pages. It evicts the page that has been used least recently when a new page needs to be loaded into a full memory frame.
Optimal: This theoretical algorithm predicts future requests to determine which page to evict, aiming to minimize the total number of page faults by keeping pages that will be needed again soonest.