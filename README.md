In recent years, there has been a growing trend toward reducing the dimensions of MOSFETs, driven largely by the need for higher performance and efficiency in electronic devices. This reduction has created the need for accurate models that can replicate the behaviour of MOSFETs in different scenarios. This project focuses on the study of N-channel MOSFETs (NMOS) in two different technologies: 45nm and 130nm.

Project Requirements:

To run this project, you will need to follow these steps:

1. Obtain the Technology Files:
    - The technology files for both the 45nm and 130nm NMOS models are required to perform simulations.
    - These files contain essential information about the properties of the transistors for each technology and are necessary for accurate simulations.
    - You can download the technology files from the nanoHUB platform: https://nanohub.org/resources.
2. Set up the LTspice Simulations:
    - You will need to use the LTspice simulator to perform DC simulations for both 45nm and 130nm NMOS. The setup for this experience is illustrated in the figure below:
       
      ![Webp net-resizeimage-2](https://github.com/user-attachments/assets/ad433eb9-05aa-441e-ac94-43233b9daea0)

    - This simulation will yield the transfer characteristics for each technology.
3. Export the Results:
    - After running the simulations in LTspice, export the transfer characteristic data to a `.txt` file.
    - This file will be used as input for the Python code to further analyze the data and determine the Shockley model parameters.
4. Python Code:
    - The Python code provided in this project is designed to process the exported transfer characteristic data and analyze the accuracy of the Shockley model.
    - The goal is to evaluate the error associated with using the Shockley model and determine if the technology size (45nm vs 130nm) has an impact on the accuracy.
