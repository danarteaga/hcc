DATA = """
Step 1. Determine the Type of Heart Disease.

First, select one or more categories of heart disease relevant to the patient. Of note, the patient could have more than one category of heart disease. If one or more heart disease categories are present, proceed to step 2. If no heart disease categories are present, simply return an empty string ("") and proceed no further than step 1.

Congestive Heart Failure

Ischemic / Atherosclerotic Heart Disease

Cardiomyopathy

Step 2. Follow the Instructions for Identifying ICD-10 Codes for All Relevant Heart Disease Types.

A. Congestive Heart Failure

Step A1. Determine the Type of Heart Failure

Below are 4 different types of heart failure, listed in the following format: heart failure type [ICD-10 code structure].

Systolic (congestive) heart failure [I50.2X]

Diastolic (congestive) heart failure [I50.3X]

Combined systolic (congestive) and diastolic (congestive) heart failure [I50.4X]

Heart disease, unspecified [I50.9]

Systolic heart failure is also known as heart failure with reduced ejection fraction (HFrEF). Diastolic heart failure is also known as heart failure with preserved ejection fraction (HFpEF). If the type of heart failure is not known, then "Heart disease, unspecified" should be used. If the provider does not specify "failure" and instead uses terminology such as "ventricular dysfunction", then "Heart disease, unspecified" should be used. Of note, Step A2 is not relevant for "Heart disease, unspecified", as I50.9 is the final ICD-10 code for "Heart disease, unspecified"; therefore, do not proceed to Step A2 if the type of heart failure is "Heart disease, unspecified" .

Step A2. Determine the Heart Failure Chronicity

Below are 3 different types of heart failure based upon how long the patient has had symptoms:

Acute heart failure

Chronic heart failure

Acute on chronic heart failure

Acute heart failure develops suddenly and the symptoms are initially severe. Chronic heart failure usually develops slowly over time; those who have chronic heart failure usually have a previous history of heart failure and are usually already on home medications for this. Acute on chronic heart failure implies that a patient with chronic heart failure develops worsening acute heart failure symptoms (i.e. a heart failure exacerbation for a patient with known congestive heart failure).

For acute heart failure, the ICD-10 code should have a 1 as the second integer after the decimal (e.g. IXX.X1). For chronic heart failure, the ICD-10 code should have a 2 as the second integer after the decimal (e.g. IXX.X2). If the heart failure chronicity is unknown, then the ICD-10 code should have a 0 as the second integer after the decimal (e.g. IXX.X0).

For example:

Unspecified systolic (congestive) heart failure [I50.20]

Acute diastolic (congestive) heart failure [I50.31]

Chronic combined systolic (congestive) and diastolic (congestive) heart failure [I50.42]

Acute on chronic diastolic (congestive) heart failure [I50.33]

B. Ischemic / Atherosclerotic Heart Disease

Patients experiencing a myocardial infarction are experiencing acute onset heart disease, whereas patents with chronic/stable heart disease will have atherosclerotic heart disease (with or without angina). Acute myocardial infarctions can be characterized as either Non-ST elevation myocardial infarction (NSTEMI) or ST-elevation myocardial infarction (STEMI). If the type of myocardial infarction (i.e. STEMI vs. NSTEMI) is unknown, you can just use "Acute myocardial infarction, unspecified".

Step B1. Below are 8 common ICD-10 codes for heart disease, listed in the following format: heart disease description [ICD-10 code]. Select the most relevant heart disease description + ICD-10 code for the patient.

Non-ST elevation (NSTEMI) myocardial infarction [I21.4]

Acute myocardial infarction, unspecified [I21.9]

ST elevation (STEMI) myocardial infarction of unspecified site [I21.3]

ST elevation (STEMI) myocardial infarction involving other coronary artery of inferior wall [I21.19]

ST elevation (STEMI) myocardial infarction involving other coronary artery of anterior wall [I21.09]

ST elevation (STEMI) myocardial infarction involving left anterior descending coronary artery [I21.02]

Atherosclerotic heart disease of native coronary artery with other forms of angina pectoris [I25.119]

Atherosclerotic heart disease of native coronary artery with unspecified angina pectoris [I25.119]

C. Cardiomyopathy

A cardiomyopathy is a disease that affects your myocardium (heart muscle), which can be genetic (congential cardiomyopathy) or acquired (e..g from alcohol).

Step C1. Below are 10 common ICD-10 codes for cardiomyopathies, listed in the following format: cardiomyopathy description [ICD-10 code]. Select the most relevant cardiomyopathy description + ICD-10 code for the patient. If the cardiomyopathy type is unclear, just use "Unspecified cardiomyopathy [I42.9]".

Dilated cardiomyopathy [I42.0], includes congestive cardiomyopathy

Obstructive hypertrophic cardiomyopathy [I42.1], includes idiopathic hypertrophic subaortic stenosis

Other hypertrophic cardiomyopathy [I42.2], includes nonobstructive hypertrophic cardiomyopathy

Endomyocardial (eosinophilic) disease [I42.3], includes endomyocardial (tropical) fibrosis and Loffler’s endocarditis

Endocardial fibroelastosis [I42.4], includes congenital cardiomyopathy and elastomyofibrosis

Other restrictive cardiomyopathy [I42.5], includes constrictive cardiomyopathy not otherwise specified

Alcoholic cardiomyopathy due to alcohol consumption [I42.6]

Cardiomyopathy due to drug and external agent: code first the poisoning due to drug or toxin [I42.7]

Other cardiomyopathies [I42.8]

Unspecified cardiomyopathy [I42.9]

Step 3. Determine if a Special Device or Status is Present

There are several additional codes to indicate that the patient has a health status related to the heart. If one or more of these codes listed below are present, please also include them separately.

Heart transplant status [Z94.1]

Presence of cardiac pacemaker [Z95.0]

Presence of aortocoronary bypass graft [Z95.1]

Presence of automatic (implantable) cardiac defibrillator [Z95.810]

Presence of heart assist device [Z95.811]

Presence of other vascular implants and grafts [Z95.828]
"""