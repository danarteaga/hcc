DATA = """
Your job is to generate documentation in the form of MEAT criteria for documenting the necessity of services provided in the healthcare setting.

The services can be found in the section below called Codes, demarcated by <<>>. Some of the information already available for this documentation may be found in the section called "Already Known" demarcated by ```.

Meat stands for:

    Monitoring: Observing and checking the progress of a condition over time.
    Evaluating: Making judgments about the patient's condition, including how it's responding to treatment.
    Assessing/Addressing: Testing or attempting to improve a condition, or directly addressing it in some manner.
    Treating: Providing management and care for a condition with the aim of combating it.


Apply the MEAT criteria to each of these codes <<ICD10-List/output>>

'''Already known:
Records-Notes
'''

Use the following format for each ICD-10 code provided.
1. ICD-10 code and Problem
2. 

    Monitoring: Including any lab trends if known.
    Evaluating: Evaluating effectiveness of responsiveness to treatment. 
    Assessing/Addressing: Assessing the need for changes in his medication dosages or the addition of new medications, diet, exercise, etc.
    Treating: The management and care plan for this issue
"""