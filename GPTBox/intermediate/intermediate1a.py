DATA = """

### UNIVERSAL RULES ### 

User is a clinical expert who wants you to process clinical (i.e. patient) information (which is found in ‘### DATA TO CONSUME ###’ section) in order to construct practical and actionable recommendations for the user (a clinician). To complete this task, use the task definition and rules, found in the ‘### TASK DEFINITION AND RULES ###’ section. Check the ‘### FORMAT ###’ section for output formatting (e.g., text with bullet points, table format).

#########
 
 ### TASK DEFINITION AND RULES ###

Your task is to read the patient record and first determine if one or more of the medical conditions exist as listed under ‘### MEDICAL CONDITIONS ###’. If one or more of these medical conditions exist, follow the instructions for each of the medical conditions as defined under ‘### DISEASE STATE DEFINITION ###’ to generate relevant ICD-10 codes and descriptions that are as specific as possible. Follow the rules below to achieve this task. If the patient does not have at least one of the medical conditions listed under ‘### MEDICAL CONDITIONS ###’, or if there is no relevant ICD-10 data under ‘### DISEASE STATE DEFINITION ###’, then do not output anything.

Importantly, the output should not include the original description of the problem from ### DATA TO CONSUME ###. Instead, the output should conform to the code descriptions listed under ### DISEASE STATE DEFINITION ###. For example, if the patient is listed as having "Coronary atherosclerosis of unspecified type of vessel, native or graft", the final output for the code description should instead be "Atherosclerotic heart disease of native coronary artery with unspecified angina pectoris" as per the information provided under ### DISEASE STATE DEFINITION ###.

#########

### MEDICAL CONDITIONS ###

- Diabetes
- Kidney disease
- Pulmonary disease
- Heart disease
- Liver disease
- Morbid obesity
- Stroke

#########
 
### DATA TO CONSUME ###
‘’’
Records-Notes 
‘’’

### DISEASE STATE DEFINITION ###
Diabetes Staging:
Diabetes Staging

Kidney Staging:
Kidney Staging 

Pulmonary Disease Staging:
Pulmonary Staging 

Heart Disease Staging:
Heart Disease Staging

Liver Disease Staging:
Liver Disease Staging

Obesity Staging:
Obesity Staging

Stroke Staging:
Stroke Staging 
########
 
 ### FORMAT ###
- Combine all of the output into a single 2-column table format (in markdown). The first column should contain descriptions ideally matching the exact description of the actual ICD-10 code (e.g. type 2 diabetes with hyperglycemia, microalbuminuria, dietary counseling and surveillance) under the column title "Description". The second column should display the actual ICD-10 code (e.g. E11.65, R80.9, Z71.3) under the column title "ICD-10 Code."
- Only a single table is allowed in the output. No more text or other tables are allowed beyond this single table. Do not include phrases such as "no relevant staging data available for..".
"""