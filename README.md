# Virtual Screening-Analysis

## Python Script for Virtual Screening Results Analysis

### Introduction

This script provides top poses amongst the screened compounds with the lowest binding affinity.
It parses all log files present in a directory and then fetches the desired (user input) number of compounds with the binding affinity of the top pose given in the log file.
The results are provided in an output file along with filename and binding affinity sorted in ascending order.
You can run it on Linux as well as on Windows using the command given below. Don't forget to provide the full path to this file, if it is saved in another directory.

### Usage:

To use this script, run the following command:

```$ python vs_analysis.py```

While executing, it will ask the user to enter a valid number of compounds/top poses to fetch the low binding affinities.

***For example,***
You have 50 log files in your directory and you want to fetch the top 20 results/poses sorted with the lowest binding affinities.
Then run the above command and while prompted enter 20. It will provide the top 20 results in the 'output.txt' file.
Remember to enter a valid number, i.e., the number you enter must be less than or equal to the number of files present in the directory.

***NOTE:
This script screens for the log files containing the word 'log' in their filenames.
It is recommended to name your log files along with the name of a compound. That would make the results more presentable and easy to understand.***

For more information on this script, please visit the following link:
https://bioinformaticsreview.com/20210509/vs-analysis-a-python-script-to-analyze-virtual-screening-results-of-autodock-vina/
