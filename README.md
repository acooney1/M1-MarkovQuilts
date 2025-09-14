# M1-MarkovQuilts

1. MarkovQuilts
This computational system is titled MarkovQuilts, and offers users a baseline system for digital quilt-making! Markov chains are the engine behind this system, as patch designs can be uploaded to the repository and then be assigned specific transition proabilities.
The transition matrix in this system acts as a "design dial," allowing each user to tailor their quilt generation to their personal preferences. Changing the transition probabilities of a given matrix has immediate and visual design impacts. For example, increasing the probability of a given patch following itself will increase clustering and changing the starting patch will inherently alter the quilting process. Furthermore, different patch images can be uploaded to the assets folder, which changes the building blocks of the quilting system and can have significant impact on contrast and visual aesthetic. Three template matrices have been created to offer a starting point for multiple strategies of quilting. 

The randomized transition matrix offers an approach that will lend itself to "improv" quilting, where design decisions are made spontaneously and without extensive planning. Examples of such randomized, improvised output can be observed in the *examples* folder (files generated_quilt(1).png, generated_quilt(2).png, and generated_quilt(3).png). 

The other matrices reflect a more rules-based design structure, as the matrices are constructed to create quilts with uniformly toned patches. A sample matrix is provided for both warm- and cool-toned quilts. The respective outputs can be observed in the *examples* folder (generated_quilt(4).png and generated_quilt(5).png).

The possibilities for expansion of this system are numerous, as additional matrices could be designed to specifically investigate symmetry, unity, and shapes.

2. Set-up + Running Code

This public repository can be utilized to generate digital patchwork quilts, using Python scripts and libraries. Necessary libraries/imports include pillow, random, and matplotlib. If pillow is not yet installed on a machine, open a terminal window and run the following command: python3 -m pip install Pillow

Other imports include matplotlib, an open-source Python library helpful for static visualizations, and random, which provides 
functions to generate random numbers and utilize random operations. These imports are included in the markov_quilt.py script.

**markov_quilt.py**: the main Python script in this computationally creative system -- contains mutable transition matrix to be used as the design. Overall workflow runs as follows: starting patch is hard-coded by user, then next patches are generated according to transition matrix. Images are pulled from the *assets* folder to prepare for visual generation. An 8x6 subplot is generated using matplotlib to visually model the quilt. Dimensions can be altered by the user depending on desired quilt size. Index variable (idx) can be edited to reflect the specific quilt generated (number identity helps to keep each design unique and traceable). When the markov_quilt script is executed, the output is then saved with the unique number identifier to the *examples* folder.
**assets**: a folder housing the patch designs to be utilized
**examples**: storage folder for saved outputs -- example quilts generated using different transition matrices
