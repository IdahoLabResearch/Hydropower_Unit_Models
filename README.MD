# CODENAME Hydro_Unit_Models
CODENAME Hydro Unit Models

CODE INTRO
Description: This software package includes hydrogovernor and turbine models developed in Simulink (The Mathworks, Inc.) and RSCAD (RTDS Technologies Inc.) 
for low-head bulb-style Kaplan turbine hydropower plants. The model developed in Simulink has been designed and tuned to match the governor-turbine 
response for a real-world run-of-river (ROR) hydropower unit owned by Idaho Falls Power (IFP). The Simulink and RSCAD models enable real-time testing in a hardware-in-the-loop
(HIL) implementation using OPAL-RT and RTDS digital real-time simulators, respectively. An automatic initialization for dynamic simulation has also been 
integrated to each model in both Simulink and RSCAD. The RSCAD initialization involves a novel python based interfacing for automatic modification of 
the initial conditions in the model. The parameters of these models can be tuned to match other hydropower plants in this class.


MODEL BENEFITS
This high-fidelity model will enable capturing dynamic behavior of a low-head bulb-style Kaplan turbine – specially in an islanded mode of operation. 
This is critical to assess the associated electromechanical instability (sustained or ceasing)  properly so that an effective and efficient mitigation 
(such as sizing an energy storage to be integrated) scheme can be analyzed off-line, validated and de-risked through digital real-time simulation, and
 deployed with the particular hydropower unit.    


SOFTWARE REQUIREMENTS
Matlab 
Simulink 
RTDS/RSCAD
Python 3.7

HOW TO CITE
Abhishek Banerjee, S M Shafiul Alam, Thomas M. Mosier, and John Undrill, "Modeling a Bulb-Style Kaplan Unit Hydrogovernor and Turbine in Mathworks-Simulink and RTDS-RSCAD", in proceedings of 2022 IEEE PES T&D Conference and Exposition, April 25-28, 2022, New Orleans, LA, USA.

 
### Other Software
Idaho National Laboratory is a cutting edge research facility which is a constantly producing high quality research and software. Feel free to take a look at our other software and scientific offerings at:

[Primary Technology Offerings Page](https://www.inl.gov/inl-initiatives/technology-deployment)

[Supported Open Source Software](https://github.com/idaholab)

[Raw Experiment Open Source Software](https://github.com/IdahoLabResearch)

[Unsupported Open Source Software](https://github.com/IdahoLabCuttingBoard)

### License

Copyright 2021 Battelle Energy Alliance, LLC

Licensed under the LICENSE TYPE (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

	https://opensource.org/licenses/GPL-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



Licensing
-----
This software is licensed under the terms you may find in the file named "LICENSE" in this directory.


Developers
-----
By contributing to this software project, you are agreeing to the following terms and conditions for your contributions:

You agree your contributions are submitted under the LICENSE TYPE license. You represent you are authorized to make the contributions and grant the license. If your employer has rights to intellectual property that includes your contributions, you represent that you have received permission to make contributions and grant the required license on behalf of that employer.
