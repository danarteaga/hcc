DATA = """
Your task is to match the ICD-10 codes from ###ICD-10 Data### to the same ICD-10 codes in ###HCC Data###. The final output should be a table (in markdown) with 3 columns. The first column should be titled "Code description". The second column should be titled "ICD-10 Code". The third column should be titled "HCC Code". Only perform this task for EXACT matches to the ICD-10 code. If an exact match does not exist, skip it. 

Only a single table is allowed in the output. No more text or other tables are allowed beyond this single table.

###ICD-10 Data###
intermediate-step-1a/output 


#######################

###HCC Data###
Diabetes HCC 
Kidney HCC 
Pulmonary HCC 
Heart Disease HCC 
Liver Disease HCC 
Obesity HCC 
Stroke HCC 
"""