DATA = """
Step 1. Determine the Type of Pulmonary Disease.

First, select one or more categories of pulmonary disease relevant to the patient. Of note, the patient could have more than one category of pulmonary disease. If one or more pulmonary disease categories are present, proceed to step 2. If no pulmonary disease categories are present, simply return an empty string ("") and proceed no further than step 1.

Respiratory Failure

Chronic Obstructive Pulmonary Disease (COPD)

Emphysema

Step 2. Follow the Instructions for Identifying ICD-10 Codes for All Relevant Heart Disease Types.

A. Respiratory Failure

Step A1. Determine the Respiratory Failure Chronicity

Below are 4 different types of heart failure based upon how long the patient has had symptoms. If this is unknown or unclear, then use "unspecified".

Acute respiratory failure [J96.0X]

Chronic respiratory failure [J96.1X]

Acute on respiratory respiratory failure [J96.2X]

Unspecified [J96.9X]

Acute respiratory failure develops suddenly and the symptoms are initially severe. Chronic respiratory failure usually develops slowly over time; those who have chronic respiratory failure usually have a previous history of heart respiratory and are usually already on home medications for this. Acute on chronic respiratory failure implies that a patient with chronic respiratory failure develops worsening acute respiratory failure symptoms (i.e. a respiratory failure exacerbation for a patient with known COPD).

For acute respiratory failure, the ICD-10 code should have a 0 as the first integer after the decimal (e.g. J96.0X). For chronic respiratory failure, the ICD-10 code should have a 1 as the first integer after the decimal (e.g. J96.1X). For acute on chronic respiratory failure, the ICD-10 code should have a 2 as the first integer after the decimal (e.g. J96.2X). For respiratory failure with an unspecified chronicity, the ICD-10 code should have a 9 as the first integer after the decimal (e.g. J96.9X).

Step A2. Determine if Hypoxia or Hypercapnia is Present

Below are 4 different types of heart failure, listed in the following format: heart failure type [ICD-10 code structure].

Only hypercanpia present [J96.X2]

Only hypoxia present [J96.X1]

Unspecified whether hypercanpia or hypoxia is present [J96.X0]

For respiratory failure with hypercapnia present, the ICD-10 code should have a 2 as the second integer after the decimal (e.g. J96.X2). For respiratory failure with hypoxia present, the ICD-10 code should have a 1 as the second integer after the decimal (e.g. J96.X1). For respiratory failure where it is not specified if hypercapnia or hypoxia is present, the ICD-10 code should have a 0 as the second integer after the decimal (e.g. J96.X0). If both hypercanpia and hypoxia are present, then default to only hypercapnia present [J96.X2].

For example:

Acute and chronic respiratory failure with hypercapnia [J96.22]

Acute respiratory failure with hypoxia [J96.01]

Chronic respiratory failure, unspecified whether with hypoxia or hypercapnia [J96.10]

Respiratory failure, unspecified, unspecified whether with hypoxia or hypercapnia [J96.90]

B. Chronic Obstructive Pulmonary Disease

Step B1. Determine if There an an Associated Exacerbation or Infection

Below are 3 different types of COPD codes based upon exacerbation or infection status. If there is no associated condition, then just use unspecified.

Chronic obstructive pulmonary disease with (acute) exacerbation [J44.1]

Chronic obstructive pulmonary disease with acute lower respiratory infection [J44.0]

Chronic obstructive pulmonary disease, unspecified [J44.9]

C. Emphysema

Step C1. Determine the Specific Type of Emphysema

Below are 4 different types of emphysema codes based where in the lungs the emphysema affects (panlobular, centrilobular, or interstitial). If there is no associated subtype, then just use unspecified.

Interstitial emphysema [J98.2]

Centrilobular emphysema [J43.2]

Panlobular emphysema [J43.1]

Emphysema, unspecified [J43.9]
"""