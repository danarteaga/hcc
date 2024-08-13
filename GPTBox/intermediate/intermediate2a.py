DATA = """
### UNIVERSAL RULES ### 

User is a clinical expert who wants you to process clinical (i.e. patient) information (which is found in ‘### DATA TO CONSUME ###’ section) in order to construct practical and actionable recommendations for the user (a clinician). To complete this task, use the task definition and rules, found in the ‘### TASK DEFINITION AND RULES ###’ section. Check the ‘### FORMAT ###’ section for output formatting (e.g., text with bullet points, table format).

#########
 
 ### TASK DEFINITION AND RULES ###
Your task is to read the patient record and first determine if one or more of the medical conditions exist as listed under ‘### MEDICAL CONDITIONS ###’. Only perform this task for the pateint's medical conditions and NOT family medical conditions (e.g. if mother has cancer, do not include this in the output). If one or more of these medical conditions exist, review the tables listing ICD codes and description for the relevant medical condition under ‘### DISEASE STATE DEFINITION ###’ and select the pertinent item. Codes with higher weights should be favored. If there are no relevant items, then do not output anything. If the patient does not have at least one of the medical conditions listed under ‘### MEDICAL CONDITIONS ###’ ‘### DISEASE STATE DEFINITION ###’, then do not output anything. You will be penalized for outputting a code for a condition that the patient does not have. Only list a code if there is a problem that specifically and definitely matches to it; do not guess or confabulate. Only code can be listed per disease.

Again, only perform this task for the patient's personal medical conditions and NOT family medical conditions (e.g. if mother or father are mentioned next to a condition, do NOT include this). 

#########

### MEDICAL CONDITIONS ###
- Gastrointestinal Disorders
- Leukemia
- Lymphoma
#########
 
### DATA TO CONSUME ### -- Optional (most likely patient information)
‘’’
Records-Notes 
‘’’

### DISEASE STATE DEFINITION ###
Gastrointestinal Disorders:
Gastrointestinal Disorders HCC 

Leukemia:
Leukemia HCC 

Lymphoma:
Lymphoma HCC 
########
 
 ### FORMAT ###
- Combine all of the output into a single 3-column table format (in markdown). The final output should be a table with 3 columns. The first column should be titled "Code description". The second column should be titled "ICD-10 Code". The third column should be titled "HCC Code". 
- Only a single table is allowed in the output. No more text or other tables are allowed beyond this single table. Do not include phrases such as "no relevant staging data available for..".
"""