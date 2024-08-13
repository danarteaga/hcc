DATA = """
Step 1. Determine the Type of Liver Disease.

First, select one or more categories of liver disease relevant to the patient. Of note, the patient could have more than one category of liver disease. If one or more liver disease categories are present, proceed to step 2. If no liver disease categories are present, simply return an empty string ("") and proceed no further than step 1.

Hepatic Failure

Cirrhosis

Hepatitis

Hepatic failure implies complete dysfunction of the liver, can be either acute or chronic, and is often associated with coma. Cirrhosis suggests chronic liver damage although the liver still is functioning. Hepatitis refers to inflammation of the liver and may be acute or chronic. Signs and symptoms of cirrhosis include: portal hypertension, ascites, hepatorenal syndrome, hepatopulmonary syndrome, and esophageal varices.

Step 2. Follow the Instructions for Identifying ICD-10 Codes for All Relevant Liver Disease Types.

A. Hepatic Failure

Step A1. Determine the Hepatic Failure Type

Below are 5 different types of hepatic failure based upon whether it was caused by alcohol or simply how long the patient has had symptoms, listed in the following format: hepatic failure type [ICD-10 code structure]:

Acute and subacute hepatic failure [K72.0X]

Chronic hepatic failure [K72.1X]

Alcoholic hepatic failure [K70.4X]

Hepatic failure, unspecified [K72.9]

If the type of hepatic failure is not known, then "Hepatic disease, unspecified" should be used. Of note, Step A2 is not relevant for "Hepatic disease, unspecified", as K72.9 is the final ICD-10 code for "Hepatic disease, unspecified"; therefore, do not proceed to Step A2 if the type of heart failure is "Hepatic disease, unspecified" .

Step A2. Determine if Coma is Present with Hepatic Failure

For hepatic failure without coma, the ICD-10 code should have a 0 as the second integer after the decimal (e.g. K72.X0). For hepatic failure with coma, the ICD-10 code should have a 1 as the second integer after the decimal (e.g. K72.X1).

For example:

Acute and subacute hepatic failure with coma [K72.01]

Chronic hepatic failure without coma [K72.10]

Alcoholic hepatic failure with coma [K70.41]

B. Cirrhosis

Step B1. Determine the Cirrhosis Type

Below are 3 different types of cirrhosis, listed in the following format: hepatic failure type [ICD-10 code structure]:

Alcoholic cirrhosis of liver [K70.3X]

Biliary cirrhosis [K74.X]

Unspecified cirrhosis of liver [K74.60]

Biliary cirrhosis is a form of liver cirrhosis caused by disease or defects of the bile ducts; symptoms usually include cholestasis (accumulation of bile in the liver). Alcoholic cirrhosis is liver cirrhosis caused by alcohol. If the type of cirrhosis is not known, then "Unspecified cirrhosis of liver" should be used. Of note, Step B2 is not relevant for "Unspecified cirrhosis of liver", as K74.60 is the final ICD-10 code for "Unspecified cirrhosis of liver"; therefore, do not proceed to Step B2 if the type of heart failure is "Unspecified cirrhosis of liver" .

Step B2. Determine if Ascites is Present with Alcoholic Cirrhosis

Alcoholic cirrhosis of liver with ascites [K70.31]

Alcoholic cirrhosis of liver without ascites [K70.30]

Step B3. Determine the Type of Biliary Cirrhosis

Primary biliary cirrhosis [K74.3]

Secondary biliary cirrhosis [K74.4]

Biliary cirrhosis, unspecified [K74.5]

Primary biliary cirrhosis involves inflammation and destruction of bile ducts in the liver, usually due to an autoimmune disease in which the body's immune system mistakenly attacks healthy tissues. Secondary biliary cirrhosis results from prolonged bile duct obstruction or narrowing or closure of the bile duct for other reasons, such as a tumor.

Step B4. Determine if Additional Symptoms of Cirrhosis are Present

If portal hypertension, ascites, hepatorenal syndrome, hepatopulmonary syndrome, and/or esophageal varices are listed as symptoms for the patient, additional includes these diagnoses (can be more than 1).

Esophageal varices with bleeding [I85.01]

Esophageal varices without bleeding [I85.00]

Hepatopulmonary syndrome [K76.81]

Hepatorenal syndrome [K76.7]

Portal hypertension [K76.6]

C. Hepatitis

Step C1. Determine the Etiology of the Hepatitis

Select the most specific hepatitis [ICD-10 code structure]:

Cytomegaloviral hepatitis [B25.1]

Autoimmune hepatitis [K75.4]

Chronic viral hepatitis B with delta-agent [B18.0]

Chronic viral hepatitis B without delta-agent [B18.1]

Chronic viral hepatitis C [B18.2]

Other chronic viral hepatitis [B18.8]
"""