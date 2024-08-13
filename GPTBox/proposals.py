DATA = """
### TASK DEFINITION AND RULES ###
Your task is to combine data from 5 different sources, as listed under ###Data to Consume###, to create a single table with 3 columns (in markdown). The first column should be titled "Code description". The second column should be titled "ICD-10 Code". The third column should be titled "HCC Code". Only perform this task when an ICD-10 code and corresponding HCC code is identified. If an HCC is not present for the ICD-10 code, do not include the code at all (including the corresponding ICD-10 code that is missing the HCC code). You must include data from all 5 data sources in the final output. 

Remove exact duplicate ICD-10 code entries, such that only one unique ICD-10 code exists in the table. 

If more than 1 of the following 6 ICD-10 codes are present for chronic kidney disease (N18.1, N18.2, N18.3, N18.4, N18.5, N18.6), then next look at the most recent GFR (eGFR) value in the ###OTHER DATA### section. If GFR is available, follow the the <<GFR Task>> below. If the GFR value is not available, only include the single highest ICD-10 code in the following list and remove all other codes: N18.1, N18.2, N18.3, N18.4, N18.5, N18.6. For example, if N18.4 and N18.5 are both present, only include the entry for N18.5. You will be penalized if you include more than one ICD-10 code from this list of 6 ICD-10 codes: N18.1, N18.2, N18.3, N18.4, N18.5, N18.6

<<GFR Task>>:
If the GFR value is available for the patient, then determine the most correct CKD stage based upon the following data:
CKD Stage 1 (N18.,1) = GFR between 60-89
CKD Stage 2 (N18.2) = GFR between 45-59
CKD Stage 3 (N18.3) = GFR between 30-44
CKD Stage 4 (N18.4) = GFR between 15-29
CKD Stage 5 (ESRD) (N18.5) = GFR <15
As an example, if both CKD stage 3 (N18.3) and CKD stage 4 (N18.4) are listed in ###Data to Consume###, but the current GFR is 40, which is between 30-44, then only list CKD stage 3 [N18.4] and remove the entry for CKD stage 4 [N18.5].

Again, NEVER include more than 1 code from the following list: N18.1, N18.2, N18.3, N18.4, N18.5, N18.6
#################

###Data to Consume###
Data Source 1:
intermediate-step-1b/output 

Data Source 2:
intermediary-step-2a/output 

Data Source 3:
intermediate-step-2b/output 

Data Source 4:
intermediate-step-2c/output 

Data Source 5:
intermediate-step-2d/output 
#################


### OTHER DATA ###
‘’’
Records-Notes 
‘’’
"""