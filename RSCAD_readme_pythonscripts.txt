Steps for running Pthon-RSCAD auto initialization

1. ('H6E_AutoInitialization_Routine.py') - The main script which imports data from all three other scripts. This prompts the user to locate the directory where the initial RSCAD file is present for the purpose of modyfying and initializing the model into a new name. The main steps are detailed as
	-) The user provides initial RSCAD .dft file
	-) The code executes asking the user with the needed data
	-) User supplies data
	-) User defines a directory and name for final modified .dft file
	-) Final file is output with a .csv log file for identifying the parameters that have 	   been modified

2. ('H6E_init.py') - Is the initialization code for the H6E model. It will produce a final output of the states in the variable 's' which is later imported to all the other scripts. This script needs all contents from 'H6E_LoadData.py' imported into it to access all other data and run properly.

3. ('H6E_LoadData.py') - Is the load data file with the specifications mentioned for the various parameters including the load data, gen data, PID data. This executes a prompt to the user for input and then stores them in the assigned variables in the script. 

4. ('interpolation.py') - Is the interpolation funtion used in the CAM curves for the gate vs head and the power vs flow curves used in H6E model. This needs to be imported into 'H6E_LoadData.py' in order to interpolate when called in there.
