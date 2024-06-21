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
The documents for this project are included in the Reports folder.
- [Report EPA141A Group 12.pdf](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Reports/Report%20EPA141A%20Group%2012.pdf): The complete report for this project which describes the process, analysis and recommendations.
- [Political Reflection EPA141A Group 12.pdf](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Reports/Political%20Reflection%20EPA141A%20Group%2012.pdf): The political reflection describing the political aspects of the process and how we experienced them.
## Dependencies
The analysis mostly relies on the EMA Workbench framework. That framework, and the other Python dependencies are included in the [requirements.txt](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/requirements.txt) file.
## Model
The model is included in the folder and is mostly unchanged, except for the following files:
- [problem_formulation.py](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/problem_formulation.py): our custom problem formulation is included in problem_formulation, it is problem formulation 6, with seperated outcomes, focusing on dike A2, while also having split the investment costs, damages and the Room for River costs per location
- [funs_generate_network.py](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/funs_generate_network.py): a typo has been fixed preventing it to run on DelftBlue
- [dike_model_function.py](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/dike_model_function.py): we have seperated the reported RfR outcomes, so we can examine the outcomes seperately for each location
## Analysis
- [Analysis_Step1_Sensitivity_Analysis.ipynb](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Analysis_Step1_Sensitivity_Analysis.ipynb): Jupyter Notebook file containing the senstivity analysis
- [Analysis_Step2_Scenario_Discovery.ipynb](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Analysis_Step2_Scenario_Discovery.ipynb): Jupyter Notebook file containing the scenario discovery 
- [Analysis_Step3_MORDM.ipynb](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Analysis_Step3_MORDM.ipynb): Jupyter Notebook file containing the mulit-scenario MORDM
- [Analysis_Step4_Robustness.ipynb](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/Analysis_Step4_Robustness.ipynb): Jupyter Notebook file containing the robustness analysis
- [run_MORDM_script.py](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/run_MORDM_script.py): Python script for running the optimization and saving the results to an external file 
## EMA Workbench Modification
One file of the EMA Workbench Python package had to be modified for the analysis to work.
- [optimization_fixed.py](https://github.com/CEOofMicrosoft/EPA141A_Group12/blob/main/optimization_fixed.py): this file should replace optimization.py in EMA Workbench for our code to run well, as it includes changes to how archives are read and processed. With the original version, the archives wouldn't be read in the right way
