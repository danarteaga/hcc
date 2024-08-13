DATA = """
Step 1. Determine the Stage of Kidney Disease

Below are 6 different stages of chronic kidney disease (CKD) with the last stage being end stage renal disease (ESRD), listed in the following format: kidney disease type (ICD-10 code structure).

Chronic kidney disease stage 1 (N18.1)

Chronic kidney disease stage 2 (N18.2)

Chronic kidney disease stage 3 (N18.3)

Chronic kidney disease stage 4 (N18.4)

Chronic kidney disease stage 5 (N18.5)

End stage renal disease (N18.6)

Of note, ESRD is the same as CKD stage 5 but with additional requirement for dialysis, where patients with CKD stage 5 do not require dialysis. If dialysis is not mentioned, then the patient does not have ESRD.

Select the most relevant kidney disease disease type + (ICD-10 code structure) for the patient. Of note, the stage should be determine by the GFR lab if it specified, and this should overrule what is stated in the note. For example, if the note states CKD stage 3 but the GFR is listed as 26, then the patient actually has CKD stage 4 as their GFR is between 15-29. See below for kidney disease staging based upon GFR values.

Kidney Disease Stage

GFR range (units: mL/min/1.73 m^2)

CKD Stage 1

60-89

CKD Stage 2

45-59

CKD Stage 3

30-44

CKD Stage 4

15-29

CKD Stage 5 (ESRD)

<15

Step 2. Determine if there is an additional common Comorbidity

Associated kidney disease comorbidities include hypertension and heart failure. Follow the steps 2a-2c below to determine the best code, if relevant.

Step 2a. If the patient has CKD stage 1-4, and both hypertension and heart failure, then the following description + code should be used instead of the N18.X code:

Hypertensive heart and chronic kidney disease with heart failure and stage 1 through stage 4 chronic kidney disease, or unspecified chronic kidney disease [I13.0]

Step 2b. If the patient has CKD stage 5 (including ESRD), and both hypertension and heart failure, then the following description + code should be used instead of the N18.X code:

Hypertensive heart and chronic kidney disease with heart failure and with stage 5 chronic kidney disease, or end stage renal disease [I13.2]

Step 2c. If the patient has CKD stage 5 (including ESRD), and hypertension but not heart failure, then the following description + code should be used instead of the N18.X code:

Hypertensive heart and chronic kidney disease without heart failure, with stage 5 chronic kidney disease, or end stage renal disease [I13.11]

Step 3. For Patient requiring a Dialysis or Nephrostomy Catheter, Determine if any Complications are Present

A nephrostomy catheter is a tube that lets urine drain from the kidney through an opening in the skin on the back and is used due to severe kidney infection, kidney stones, trauma or other issues preventing normal urination. Dialysis catheters can either be vascular (inserted into the arteries) or peritoneal (inserted along the lining of the abdomen). If the type of dialysis catheter is not specified, assume it is a vascular dialysis catheter. Codes are also separated by whether or not this is the first encounter with the patient (initial encounter) or a follow-up encounter (subsequent encounter). If the encounter status is not known, use "sequala" instead.

Of note, if no complications are present but the patient is on dialysis, additional include the following description + code:

Dependent on renal dialysis [Z99.2]

For vascular dialysis catheter complications, refer to the table below.

ICD Code

Description

T82.41XA

Breakdown (mechanical) of vascular dialysis catheter, initial encounter

T82.41XS

Breakdown (mechanical) of vascular dialysis catheter, sequela

T82.41XD

Breakdown (mechanical) of vascular dialysis catheter, subsequent encounter

T82.42XA

Displacement of vascular dialysis catheter, initial encounter

T82.42XS

Displacement of vascular dialysis catheter, sequela

T82.42XD

Displacement of vascular dialysis catheter, subsequent encounter

T82.43XA

Leakage of vascular dialysis catheter, initial encounter

T82.43XS

Leakage of vascular dialysis catheter, sequela

T82.43XD

Leakage of vascular dialysis catheter, subsequent encounter

T82.49XA

Other complication of vascular dialysis catheter, initial encounter

T82.49XS

Other complication of vascular dialysis catheter, sequela

T82.49XD

Other complication of vascular dialysis catheter, subsequent encounter

For peritoneal dialysis catheter complications, refer to the table below.

ICD Code

Description

T85.611A

Breakdown (mechanical) of intraperitoneal dialysis catheter, initial encounter

T85.611S

Breakdown (mechanical) of intraperitoneal dialysis catheter, sequela

T85.611D

Breakdown (mechanical) of intraperitoneal dialysis catheter, subsequent encounter

T85.621A

Displacement of intraperitoneal dialysis catheter, initial encounter

T85.621S

Displacement of intraperitoneal dialysis catheter, sequela

T85.621D

Displacement of intraperitoneal dialysis catheter, subsequent encounter

Z49.32

Encounter for adequacy testing for peritoneal dialysis

Z49.01

Encounter for fitting and adjustment of extracorporeal dialysis catheter

Z49.02

Encounter for fitting and adjustment of peritoneal dialysis catheter

Y62.2

Failure of sterile precautions during kidney dialysis and other perfusion

T85.71XA

Infection and inflammatory reaction due to peritoneal dialysis catheter, initial encounter

T85.71XS

Infection and inflammatory reaction due to peritoneal dialysis catheter, sequela

T85.71XD

Infection and inflammatory reaction due to peritoneal dialysis catheter, subsequent encounter

T85.631A

Leakage of intraperitoneal dialysis catheter, initial encounter

T85.631S

Leakage of intraperitoneal dialysis catheter, sequela

T85.631D

Leakage of intraperitoneal dialysis catheter, subsequent encounter

T85.691A

Other mechanical complication of intraperitoneal dialysis catheter, initial encounter

T85.691S

Other mechanical complication of intraperitoneal dialysis catheter, sequela

T85.691D

Other mechanical complication of intraperitoneal dialysis catheter, subsequent encounter

For dialysis complications agnostic to type (either vascular or peritoneal), refer to the table below.

ICD Code

Description

T81.512A

Adhesions due to foreign body accidentally left in body following kidney dialysis, initial encounter

T81.512S

Adhesions due to foreign body accidentally left in body following kidney dialysis, sequela

T81.512D

Adhesions due to foreign body accidentally left in body following kidney dialysis, subsequent encounter

Y62.2

Failure of sterile precautions during kidney dialysis and other perfusion

T81.522A

Obstruction due to foreign body accidentally left in body following kidney dialysis, initial encounter

T81.522S

Obstruction due to foreign body accidentally left in body following kidney dialysis, sequela

T81.522D

Obstruction due to foreign body accidentally left in body following kidney dialysis, subsequent encounter

T81.592A

Other complications of foreign body accidentally left in body following kidney dialysis, initial encounter

T81.592S

Other complications of foreign body accidentally left in body following kidney dialysis, sequela

T81.592D

Other complications of foreign body accidentally left in body following kidney dialysis, subsequent encounter

T81.532A

Perforation due to foreign body accidentally left in body following kidney dialysis, initial encounter

T81.532S

Perforation due to foreign body accidentally left in body following kidney dialysis, sequela

T81.532D

Perforation due to foreign body accidentally left in body following kidney dialysis, subsequent encounter

T81.502A

Unspecified complication of foreign body accidentally left in body following kidney dialysis, initial encounter

T81.502S

Unspecified complication of foreign body accidentally left in body following kidney dialysis, sequela

T81.502D

Unspecified complication of foreign body accidentally left in body following kidney dialysis, subsequent encounter

For nephrostomy catheter complications, refer to the table below.

ICD Code

Description

T83.012A

Breakdown (mechanical) of nephrostomy catheter, initial encounter

T83.022A

Displacement of nephrostomy catheter, initial encounter

T83.512A

Infection and inflammatory reaction due to nephrostomy catheter, initial encounter

T83.032A

Leakage of nephrostomy catheter, initial encounter

T83.092A

Other mechanical complication of nephrostomy catheter, initial encounter
"""