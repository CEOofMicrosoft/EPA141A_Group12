# Introduction
This assignment was done for the course EPA141A, Model-based Decision Making. In this respository, all the files necessary to run the analyses are included, as well as the documents that make up the assignment: the report and the political reflection. Below, an overview is given of the files of interest. 

|Group Number |12|
|---|---|
|Tarik Bousair| 5331900 |
|Juliëtte van Alst| 5402409|
|Merijn Beemster|5380421 |
|Lale Günhan | 4858441 |

# Files of Interest
## Reports
(Report EPA141A Group 12.pdf)[https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Reports/Report%20EPA141A%20Group%2012.pdf]
## Model
The model is included in the folder and is mostly unchanged, except for the following files:
- problem_formulation.py: our custom problem formulation is included in problem_formulation
- funs_generate_network.py: a typo has been fixed preventing it to run on DelftBlue
## Analysis
- Sensitivy Analaysis: Jupyter Notebook file containing the senstivity analysis
- PRIM: Jupyter Notebook file containing the scenario discovery 
- MORDM: Jupyter Notebook file containing the mulit-scenario MORDM
- Robustness: Jupyter Notebook file containing the robustness analysis
- run_MORDM_script.py: Python script for running the optimization and saving the results to an external file 
- slurm_script?
## EMA Workbench Moderation
- optimization_fixed.py: this file should replace optimization.py in EMA Workbench for our code to run well, as it includes changes to how archives are read and processed. With the original version, the archives wouldn't be read in the right way.

# Dependencies
The analysis mostly relies on the EMA Workbench framework. That framework, and the other Python dependencies are included in the requirements.txt file.
