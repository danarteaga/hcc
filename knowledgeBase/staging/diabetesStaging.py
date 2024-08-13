DATA = """
Step 1. Determine the Type of Diabetes

Below are 5 different types of diabetes, listed in the following format: diabetes type (ICD-10 code structure).

Type 1 diabetes mellitus  (E10.XXXX)

Type 2 diabetes mellitus (E11.XXXX)

Diabetes mellitus due to underlying condition (E08.XXX)

Drug or chemical-induced diabetes mellitus (E09.XXXX)

Other specified diabetes mellitus (E13.XXXX)

Select the most relevant diabetes type + (ICD-10 code structure) for the patient. Of note, use this category when the diabetes is documented as diabetes type 1.5; synonymous terms used in the documentation may also include combined diabetes type 1 and type 2, latent autoimmune diabetes of adults (LADA), slow-progressing type 1 diabetes, or double diabetes.  If the type of diabetes is unclear, Type 2 diabetes mellitus (E11.XXX) should be used (do NOT use other specified diabetes if the types of diabetes is unclear).

Step 2. Determine if the Patient’s Diabetes Is Currently Well Controlled

Associated diabetes complications such as hyperglycemia, hypoglycemia, ulcers, retinopathy, nephropathy, or neuropathy all suggest poorly controlled diabetes. It is important to remember that poorly controlled diabetes is the most common. Many patients with diabetes have hyperglycemia, which is considered a complication.

That said, if a person’s diabetes is well controlled, the first digit after the decimal point is 9 (i.e., EXX.9). For example, a person with type 2 diabetes that is well controlled who has no complications would be indicated by the code E11.9. Likewise, a person with type 1 diabetes that is well controlled who has no complications would be indicated by the code E10.9.

Step 3. For Diabetes That Is Not Well Controlled, Identify Any Complications

The first digit after the decimal point describes both the level of metabolic control and the presence of complications. Further digits subcategorize the complications. As mentioned above, the number 9 after the decimal point (i.e., E10.9 or E11.9) both defines the diabetes as controlled (i.e., without hyperglycemia or hypoglycemia) and documents the absence of complications. Thus, using a 9 after the decimal point should be the exception rather than the rule, given that most people with diabetes have either suboptimal control, complications, or both. The following codes pertain to complications of type 2 diabetes:

Severe hyperosmolarity: E11.0X

Kidney complications: E11.2X

Eye complications: E11.3X

Nerve complications: E11.4X

Peripheral vascular disease: E11.5X

Other specified complications, including musculoskeletal, oral, and skin complications; hypoglycemia; and hyperglycemia: E11.6X

Other unspecified complications: E11.8X

Well-controlled type 2 diabetes without hyperglycemia, hypoglycemia, or complications: E11.9X

More detailed codes further subcategorize complications. Table 2 provides ICD-10 codes for complications associated with type 1 diabetes; Table 3 lists codes for complications associated with type 2 diabetes.

TABLE 2:

Code

Used to report type 1 diabetes:

E10.1X

With the presence of diabetic ketoacidosis

 E10.10

With diabetic ketoacidosis without coma

 E10.11

With diabetic ketoacidosis with coma

E10.2X

With renal disease

 E10.21

With diabetic nephropathy

 E10.22

With diabetic chronic kidney disease

 E10.29

With other diabetic kidney

E10.3X

With eye disease

 E10.311

With ophthalmic complications without macular edema

 E10.319

With ophthalmic complications with macular edema

 E10.321

With mild nonproliferative diabetic retinopathy with macular edema

 E10.329

With mild nonproliferative diabetic retinopathy without macular edema

 E10.331

With macular edema

 E10.339

Without macular edema

 E10.341

With severe nonproliferative diabetic retinopathy with macular edema

 E10.349

With severe nonproliferative diabetic retinopathy without macular edema

 E10.351

With proliferative diabetic retinopathy with macular edema

 E10.359

With proliferative diabetic retinopathy without macular edema

 E10.36

With diabetic cataract

 E10.39

With other diabetic ophthalmic complication

E10.4X

With nerve disease

 E10.40

With diabetic neuropathy, unspecified

 E10.41

With diabetic mononeuropathy

 E10.42

With diabetic polyneuropathy

 E10.43

With diabetic autonomic (poly)neuropathy

 E10.44

With diabetic amyotrophy

 E10.49

With other diabetic neurological complication

E10.5X

With peripheral vascular disease

 E10.51

With diabetic peripheral angiopathy without gangrene

 E10.52

With diabetic peripheral angiopathy with gangrene

 E10.59

With other circulatory complications

E10.6X

With diabetes-related musculoskeletal, oral, or skin complications; hypoglycemia; or hyperglycemia

 E10.61

With diabetic arthropathy

 E10.610

With diabetic neuropathic arthropathy

 E10.618

With other diabetic arthropathy

 E10.620

With diabetic dermatitis

 E10.621

With foot ulcer

 E10.622

With other skin ulcer

 E10.628

With other skin complications

 E10.630

With periodontal disease

 E10.638

With other oral complications

 E10.641

With hypoglycemia with coma

 E10.649

With hypoglycemia without coma or with hypoglycemia unawareness

 E10.65

With hyperglycemia

 E10.69

With other specified complication

E10.8

With complications, unspecified

E10.9

Without complications

TABLE 3:

Code

Used to report type 2 diabetes with:

E11.0X

With hyperosmolarity

 E11.00

Without nonketotic hyperglycemic hyperosmolar coma

 E11.01

With nonketotic hyperglycemic hyperosmolar coma

E11.2X

With kidney complications

 E11.21

With diabetic nephropathy

 E11.22

With diabetic chronic kidney disease

 E11.29

With other diabetic kidney complications

E11.3X

With eye complications

 E11.31

With diabetic retinopathy, unspecified

 E11.311

With diabetic retinopathy with macular edema

 E11.319

With diabetic retinopathy without macular edema

 E11.32

With mild nonproliferative diabetic retinopathy`

 E11.321

With mild nonproliferative diabetic retinopathy with macular edema

 E11.329

With mild nonproliferative diabetic retinopathy without macular edema

 E11.33

With moderate nonproliferative diabetic retinopathy

 E11.331

With moderate nonproliferative diabetic retinopathy with macular edema

 E11.339

With moderate nonproliferative diabetic retinopathy without macular edema

 E11.34

With severe nonproliferative diabetic retinopathy

 E11.341

With severe nonproliferative diabetic retinopathy with macular edema

 E11.349

With severe nonproliferative diabetic retinopathy without macular edema

 E11.36

With diabetic cataract

 E11.39

With other diabetic ophthalmic complication

E11.4X

With nerve complications

 E11.40

With diabetic neuropathy, unspecified

 E11.41

With mononeuropathy

 E11.42

With diabetic polyneuropathy

 E11.45

With autonomic neuropathy (e.g., gastroparesis)

 E11.49

With other diabetic neurological complications

E11.5X

With peripheral vascular disease

 E11.51

With diabetic peripheral angiopathy without gangrene

 E11.52

With diabetic peripheral angiopathy with gangrene

 E11.59

With other circulatory complications

 E11.6X

With diabetes-related musculoskeletal, oral, or skin complications; hypoglycemia; or hyperglycemia

 E11.61

With diabetic arthropathy

 E11.610

With diabetic neuropathic arthropathy

 E11.618

With other diabetic arthropathy

 E11.62

With skin complications

 E11.620

With diabetic dermatitis

 E11.621

With foot ulcer

 E11.622

With other skin ulcer

 E11.628

With other skin complications

 E11.63

With oral complications

 E11.630

With periodontal disease

 E11.638

With other oral complications

 E11.64

With hypoglycemia

 E11.641

With hypoglycemia with coma

 Ell.649

Without hypoglycemia without coma

 E11.65

With hyperglycemia

 E11.69

With other complications

E11.8X

With other unspecified complication

E11.9X

Well controlled without hyperglycemia, hypoglycemia, or complications

Step 4. Create a Second Code to Describe Any Identified Complication

This means you will use a primary diabetes code that describes the type of diabetes, then specify whether it is controlled and whether there is a complication, and then add a second code specific to that complication. Sample codes for complications of diabetes are shown in Table 4; codes for common comorbidities are shown in Table 5.

TABLE 4:

ICD10 CODE

NAME

S81.801

Open wound, unspecified, right lower leg

L97.X–L98.X

Site of ulceration

L97.411

Non-pressure chronic ulcer of right heel and mid-foot limited to breakdown of skin

L97.5

Non-pressure chronic ulcer of other part of the foot

L97.533

Non-pressure chronic ulcer of other part of left foot with necrosis of muscle

N18.1

Chronic kidney disease (CKD) stage I

N18.2

CKD stage II

N18.3

CKD stage III

N18.4

CKD stage IV

N18.5

CKD stage V

N18.6

End-stage renal disease

R80.9

Microalbuminuria

Z99.2

Dependence on renal dialysis

E10.42

Presence of arteriovenous shunt for dialysis

E10.649

Type 1 diabetes with hypoglycemia without coma

E11.649

Type 2 diabetes with hypoglycemia without coma

E08.64

Diabetes due to underlying condition with hypoglycemia

E09.64

Drug- or chemical-induced diabetes with hypoglycemia

E16.0

Drug-induced hypoglycemia without coma

E16.1

Other hypoglycemia

E16.2

Hypoglycemia, unspecified

EXX.641

Fill in with code for type of diabetes with hypoglycemia and coma

TABLE 5:

ICD10 CODE

NAME

F17.210

Nicotine dependence, cigarettes, uncomplicated

K31.84

Gastroparesis

I10

Essential hypertension

E78.0

Pure hypercholesterolemia

E78.1

Pure hypertriglyceridemia

E78.2

Mixed hyperlipidemia

E78.5

Hyperlipidemia, unspecified

E06.3

Due to Hashimoto’s disease

E89.0

Postoperative or postablative

E03.9

Acquired Hashimoto’s disease

Z13.29

Thyroid disorder screen

R94.6

Abnormal thyroid blood test or screen

E66.0

Obesity due to excess calories

E66.01

Morbid severe obesity due to excess calories

E66.9

Obesity, unspecified

Z68.30

BMI 30.0–30.9 kg/m2

Z68.31

BMI 31.0–31.9 kg/m2

Z68.32

BMI 32.0–32.9 kg/m2

Example 1

A patient has type 2 diabetes with polyneuropathy, hypertension with albuminuria, and dyslipidemia. The coding to document this patient should be E11.65 (type 2 diabetes with hyperglycemia), E11.42 (type 2 diabetes with polyneuropathy), I10 (hypertension), R80.9 (microalbuminuria), and E78.2 (mixed hyperlipidemia).

Example 2

A patient with type 1 diabetes has an active foot ulcer on the bottom of his right foot. The coding to document this patient should be E10.621 (type 1 diabetes with foot ulcer) and L97.411 (non-pressure chronic ulcer of right heel and mid-foot limited to breakdown of skin).

Codes to Document Complexity of Care Provided

Finally, there are codes that demonstrate the additional work you do or the additional complexity of the care you are providing. These codes help to justify this higher level of care.

Did you provide dietary or exercise counseling? These are noted with an additional Z code:

Dietary counseling and surveillance: Z71.3

Exercise counseling: Z71.89

Is the patient using insulin? Note that the “long-term use” code Z79.4 can be used once the drug has been initiated for any person who is taking insulin chronically.

Is the patient on an insulin pump? Codes related to pump use include:

Insulin pump: Z96.41

Counseling, titration, removal, training, or fitting/adjustment of insulin pump: Z46.81

Insulin pump complications: T85.694

Has the patient underdosed or overdosed insulin? Codes related to these situations include:

Underdosing of insulin: T38.3X6

Unintentional overdosing of insulin: T38.3X1

Suspected self-harm by overdosing insulin: T38.3X2X

After these T codes, there should be a modifier at the end to denote initial encounter (A), subsequent encounter (D), or sequalae (S). For example, an initial encounter for intentional self-harm by overdosing insulin should be “T38.3X2A.”
"""