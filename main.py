import os
import asyncio
from openai import AsyncOpenAI

API_KEY = os.environ['API_KEY']

patient_case = 2
run_meat = True


from inputData.case1 import DATA as patientCase1
from inputData.case2 import DATA as patientCase2
from inputData.case3 import DATA as patientCase3
from inputData.case4 import DATA as patientCase4
from inputData.case5 import DATA as patientCase5

from GPTBox.intermediate.intermediate1a import DATA as intermediate_step1a
from GPTBox.intermediate.intermediate1b import DATA as intermediate_step1b
from GPTBox.intermediate.intermediate2a import DATA as intermediate_step2a
from GPTBox.intermediate.intermediate2b import DATA as intermediate_step2b
from GPTBox.intermediate.intermediate2c import DATA as intermediate_step2c
from GPTBox.intermediate.intermediate2d import DATA as intermediate_step2d

from knowledgeBase.hcc.amputation import DATA as amputation
from knowledgeBase.hcc.arrythmia import DATA as arrythmia
from knowledgeBase.hcc.cancer import DATA as cancer
from knowledgeBase.hcc.diabetes import DATA as diabetes
from knowledgeBase.hcc.gastrointestinal import DATA as gastrointestinal
from knowledgeBase.hcc.heartDisease import DATA as heartDisease
from knowledgeBase.hcc.infection import DATA as infection
from knowledgeBase.hcc.kidney import DATA as kidney
from knowledgeBase.hcc.leukemia import DATA as leukemia
from knowledgeBase.hcc.liver import DATA as liver
from knowledgeBase.hcc.lymphoma import DATA as lymphoma
from knowledgeBase.hcc.obesity import DATA as obesity
from knowledgeBase.hcc.PAD import DATA as PAD
from knowledgeBase.hcc.psychiatry import DATA as psychiatry
from knowledgeBase.hcc.pulmonary import DATA as pulmonary
from knowledgeBase.hcc.rheumatology import DATA as rheumatology
from knowledgeBase.hcc.seizure import DATA as seizure
from knowledgeBase.hcc.spinalCord import DATA as spinalCord
from knowledgeBase.hcc.stroke import DATA as stroke
from knowledgeBase.hcc.thyroid import DATA as thyroid
from knowledgeBase.hcc.transplant import DATA as transplant

from knowledgeBase.staging.diabetesStaging import DATA as diabetesStaging
from knowledgeBase.staging.heartDiseaseStaging import DATA as heartDiseaseStaging
from knowledgeBase.staging.kidneyStaging import DATA as kidneyStaging
from knowledgeBase.staging.liverStaging import DATA as liverStaging
from knowledgeBase.staging.obesityStaging import DATA as obesityStaging
from knowledgeBase.staging.pulmonaryStaging import DATA as pulmonaryStaging
from knowledgeBase.staging.strokeStaging import DATA as strokeStaging

from GPTBox.proposals import DATA as proposals
from GPTBox.meat import DATA as meat 


patientCase = ['', patientCase1, patientCase2, patientCase3, patientCase4, patientCase5][patient_case]
intermediate_step1a.replace('Record-Notes', patientCase) \
        .replace('Diabetes Staging ', diabetesStaging) \
        .replace('Kidney Staging ', kidneyStaging) \
        .replace('Heart Disease Staging ', heartDiseaseStaging) \
        .replace('Liver Disease Staging ', liverStaging) \
        .replace('Obesity Staging ', obesityStaging) \
        .replace('Stroke Staging ', strokeStaging)
intermediate_step1b.replace('Diabetes HCC', diabetes) \
        .replace('Kidney HCC', kidney) \
        .replace('Pulmonary HCC', pulmonary) \
        .replace('Heart Disease HCC', heartDisease) \
        .replace('Liver Disease HCC', liver) \
        .replace('Obesity HCC', obesity) \
        .replace('Stroke HCC', stroke)
intermediate_step2a.replace('Gastrointestinal Disorders HCC', gastrointestinal) \
        .replace('Leukemia HCC', leukemia) \
        .replace('lymphoma HCC', lymphoma) \
        .replace('Record-Notes', patientCase) 
intermediate_step2b.replace('Amputations HCC', amputation) \
        .replace('Transplant HCC', transplant) \
        .replace('Thyroid HCC', thyroid) \
        .replace('Record-Notes', patientCase) 
intermediate_step2c.replace('Peripheral Artery Disease HCC', amputation) \
        .replace('Seizure HCC', transplant) \
        .replace('Rheutomologic Disease HCC', rheumatology) \
        .replace('Record-Notes', patientCase) 
intermediate_step2d.replace('Cardiac Arrythmia HCC', amputation) \
        .replace('Psychiatric Disorders HCC', transplant) \
        .replace('Record-Notes', patientCase)
proposals.replace('Record-Notes', patientCase) 
meat.replace('Record-Notes', patientCase) 


client = AsyncOpenAI(
    api_key=os.environ.get("API_KEY"),
)

async def main() -> None:

    step1a = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step1a,
            }
        ],
        model="gpt-4o",
    )

    step1b = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step1b.replace('intermediate-step-1a/output', step1a.choices[0].message.content),
            }
        ],
        model="gpt-4o",
    )

    step2a = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step2a,
            }
        ],
        model="gpt-4o",
    )

    step2b = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step2b,
            }
        ],
        model="gpt-4o",
    )

    step2c = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step2c,
            }
        ],
        model="gpt-4o",
    )

    step2d = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": intermediate_step2d,
            }
        ],
        model="gpt-4o",
    )

    proposalStep = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": proposals.replace('intermediate-step-1b/output', step1b.choices[0].message.content) \
                        .replace('intermediate-step-2a/output', step2a.choices[0].message.content) \
                        .replace('intermediate-step-2b/output', step2b.choices[0].message.content) \
                        .replace('intermediate-step-2c/output', step2c.choices[0].message.content) \
                        .replace('intermediate-step-2d/output', step2d.choices[0].message.content)
            }
        ],
        model="gpt-4o",
    )

    if run_meat:
        meatStep = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": meat.replace('ICD10-List/output', proposalStep.choices[0].message.content),
                }
            ],
            model="gpt-4o",
        )
    else:
        meatStep = ''

    outputs = [proposalStep, meatStep]
    print(outputs)


asyncio.run(main())