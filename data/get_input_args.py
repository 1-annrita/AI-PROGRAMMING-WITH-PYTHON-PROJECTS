#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: ANNRITA MUKAMI GITONGA
# DATE CREATED: 01/08/2024                                  
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
#####argparse module is imported to use the ArgumentParser class, which handles command line argument parsing
# Imports python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
#####the get_input_args() function - create & retrieve the command line arguments
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArguementParser method
    # Path to a folder that contains the pet images
    parser.add_argument('--dir', type = str, default = 'pet_images/',
                        help='Path to the folder of pet images')
    # The CNN model architecture to use. resnet, alexnet, or vgg (pick one as the default). You will find them in classifier.py.
    parser.add_argument('--arch', type = str, default = 'vgg',
                        help='CNN model architecture to use')
    # The file that contains the list of valid dognames
    parser.add_argument('--dogfile', type = str, default = 'dognames.txt',
                        help='Text file with dog names')

    
    # # Parse arguments
    # in_args = parser.parse_args()

    # # Print parsed arguments for testing/debugging
    # print("Image Folder:", in_args.dir)
    # print("CNN Model Architecture:", in_args.arch)
    # print("Dog Names File:", in_args.dogfile)


    
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # you created with this function 
    # return None
    return parser.parse_args()
    # return in_args

