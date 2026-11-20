import fitz  # PyMuPDF
import os

def create_medical_encyclopedia(output_path="data/The_GALE_ENCYCLOPEDIA_of_MEDICINE_SECOND.pdf"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    doc = fitz.open()

    articles = [
        {
            "title": "THE GALE ENCYCLOPEDIA OF MEDICINE - CLINICAL REFERENCE",
            "section": "Title & Frontmatter",
            "content": """The Gale Encyclopedia of Medicine is a comprehensive medical reference providing authoritative, evidence-based clinical information on diseases, disorders, treatments, medications, diagnostic procedures, and emergency protocols. 
            
Designed for healthcare practitioners, medical students, clinical researchers, and patient education, this reference bridges fundamental pathophysiology with contemporary clinical practice.

Key Medical Domains Covered:
- Cardiovascular & Hemodynamic Disorders
- Respiratory & Pulmonary Medicine
- Neurological & Cerebrovascular Pathology
- Endocrinology, Metabolism & Diabetes
- Gastroenterology, Hepatology & Digestive Health
- Nephrology, Renal Physiology & Urology
- Infectious Diseases, Antimicrobial Therapy & Epidemiology
- Hematology & Clinical Oncology
- Musculoskeletal Disorders & Autoimmune Diseases
- Clinical Pharmacology, Pharmacokinetics & Drug Interactions
- Emergency Medicine, Resuscitation & Triage Protocols
- Diagnostic Testing, Laboratory Biomarkers & Interpretation"""
        },
        {
            "title": "Myocardial Infarction (Acute Coronary Syndrome)",
            "section": "Cardiology",
            "content": """Definition & Pathophysiology:
Acute Myocardial Infarction (AMI), commonly known as a heart attack, occurs when myocardial ischemia leads to irreversible cellular necrosis of heart muscle. The primary underlying mechanism in >90% of cases is acute rupture or erosion of an unstable atherosclerotic plaque within an epicardial coronary artery, triggering platelet activation, thrombus formation, and sudden vascular occlusion.

Clinical Presentation:
- Substernal chest pain or pressure ('crushing' sensation), radiating to the left arm, neck, jaw, or epigastrium.
- Autonomic symptoms: Diaphoresis, nausea, dyspnea, presyncope, and pallor.
- Atypical presentations are frequent in women, elderly patients, and diabetics (silent ischemia, dyspnea alone, or acute confusion).

Diagnostic Criteria:
1. Biomarkers: Serial elevation of cardiac Troponin I (cTnI) or Troponin T (cTnT) with at least one value above the 99th percentile URL.
2. 12-Lead Electrocardiogram (ECG):
   - STEMI: ST-segment elevation >= 1 mm in two contiguous leads (or >= 2 mm in V2-V3) or new LBBB.
   - NSTEMI: ST depression, T-wave inversions, or transient ST elevation.

Acute Management & Therapeutics:
- Immediate MONA protocol (Morphine if pain refractory, Oxygen if SpO2 < 90%, Nitroglycerin sublingual/IV, Aspirin 162-325 mg chewed).
- Dual Antiplatelet Therapy (DAPT): Aspirin + P2Y12 inhibitor (Ticagrelor 180 mg or Prasugrel 60 mg or Clopidogrel 600 mg).
- Anticoagulation: Unfractionated Heparin (UFH), Enoxaparin (LMWH), or Bivalirudin.
- Reperfusion Strategy: Primary Percutaneous Coronary Intervention (PCI) within 90 minutes door-to-balloon time. If PCI unavailable within 120 minutes, intravenous thrombolytic therapy (Tenecteplase, Alteplase) within 30 minutes.
- Long-term secondary prevention: High-intensity statin (Atorvastatin 80 mg), Beta-blockers (Metoprolol succinate), ACE inhibitor / ARB, and lifestyle modifications."""
        },
        {
            "title": "Heart Failure (HFrEF and HFpEF)",
            "section": "Cardiology",
            "content": """Pathophysiology:
Heart failure is a complex clinical syndrome resulting from structural or functional cardiac impairment that reduces the ventricle's ability to fill with or eject blood.
- HFrEF (Heart Failure with Reduced Ejection Fraction): Left ventricular ejection fraction (LVEF) <= 40%, characterized by systolic dysfunction and ventricular remodeling.
- HFpEF (Heart Failure with Preserved Ejection Fraction): LVEF >= 50% with elevated filling pressures and diastolic stiffness.

Clinical Features:
- Left-sided failure: Exertional dyspnea, orthopnea, paroxysmal nocturnal dyspnea (PND), tachypnea, pulmonary rales/crackles, S3 gallop.
- Right-sided failure: Jugular venous distension (JVD), peripheral pitting edema, hepatomegaly, ascites, hepatojugular reflux.

Diagnostic Evaluation:
- Serum B-type Natriuretic Peptide (BNP > 100 pg/mL) or NT-proBNP (> 300 pg/mL).
- Transthoracic Echocardiogram (TTE): Evaluates EF, chamber dimensions, wall motion abnormalities, and valvular pathology.
- Chest Radiography: Cardiomegaly, Kerley B lines, cephalization of pulmonary vessels, pleural effusions.

Guideline-Directed Medical Therapy (GDMT) for HFrEF (The Four Pillars):
1. ARNI (Sacubitril/Valsartan) or ACEi/ARB to inhibit the renin-angiotensin-aldosterone system.
2. Beta-Blockers (Carvedilol, Metoprolol Succinate, or Bisoprolol).
3. Mineralocorticoid Receptor Antagonists (MRA: Spironolactone or Eplerenone).
4. SGLT2 Inhibitors (Dapagliflozin or Empagliflozin) to reduce cardiovascular mortality and hospitalization.
5. Loop diuretics (Furosemide, Bumetanide) titrated for symptomatic fluid decongestion."""
        },
        {
            "title": "Asthma and Chronic Obstructive Pulmonary Disease (COPD)",
            "section": "Pulmonology",
            "content": """Asthma Overview:
Asthma is a chronic inflammatory disorder of the airways characterized by bronchial hyperresponsiveness and reversible airflow limitation. 
- Triggers: Allergens (pollen, dust mites), viral respiratory infections, exercise, cold air, NSAIDs, and occupational irritants.
- Symptoms: Episodic wheezing, nocturnal coughing, chest tightness, and shortness of breath.
- Diagnosis: Spirometry showing FEV1/FVC < 0.70 with significant post-bronchodilator reversibility (increase in FEV1 > 12% and > 200 mL).
- Stepwise Management: Inhaled corticosteroids (ICS) like Fluticasone or Budesonide are the cornerstone, combined with Formoterol (LABA) as SMART therapy (Single Maintenance and Reliever Therapy).

COPD Overview:
COPD is a progressive, largely irreversible lung disease encompassing chronic bronchitis and emphysema, primarily caused by long-term cigarette smoking or biomass fuel exposure.
- Pathology: Chronic mucus hypersecretion with airway narrowing and destruction of alveolar alveolar walls reducing capillary diffusion capacity (DLCO).
- GOLD Criteria: Post-bronchodilator FEV1/FVC < 0.70 confirms persistent airflow limitation.
- Pharmacotherapy: Long-acting muscarinic antagonists (LAMA: Tiotropium), Long-acting beta2-agonists (LABA: Salmeterol, Vilanterol), and ICS in patients with elevated eosinophils (> 300 cells/uL) or frequent exacerbations.
- Acute Exacerbations: Systemic corticosteroids (Prednisone 40 mg daily for 5 days), short-acting bronchodilators (Albuterol + Ipratropium), and antibiotics (Azithromycin or Doxycycline) when purulent sputum is present."""
        },
        {
            "title": "Community-Acquired Pneumonia (CAP)",
            "section": "Infectious Diseases / Pulmonology",
            "content": """Etiology:
- Typical bacterial pathogens: Streptococcus pneumoniae (most common), Haemophilus influenzae, Moraxella catarrhalis.
- Atypical pathogens: Mycoplasma pneumoniae, Chlamydia pneumoniae, Legionella pneumophila.
- Viral etiologies: Influenza A/B, Respiratory Syncytial Virus (RSV), SARS-CoV-2.

Clinical Features & Severity Stratification:
- Symptoms: Productive cough with purulent or rust-colored sputum, fever, shaking chills (rigors), pleuritic chest pain, tachypnea, dullness to percussion, and bronchial breath sounds.
- Severity scoring: CURB-65 criteria (Confusion, Urea > 7 mmol/L, Respiratory rate >= 30, Blood pressure systolic < 90 or diastolic <= 60, Age >= 65).
  * Score 0-1: Low risk, outpatient treatment.
  * Score 2: Moderate risk, consider inpatient admission.
  * Score 3-5: High risk, requires inpatient/ICU admission.

Antimicrobial Therapy:
- Outpatient healthy individuals: Amoxicillin 1g TID OR Doxycycline 100mg BID.
- Outpatient with comorbidities (cardiac, renal, diabetes): Amoxicillin-clavulanate or Cefpodoxime PLUS Macrolide (Azithromycin) OR Respiratory Fluoroquinolone (Levofloxacin 750mg QD).
- Inpatient Non-ICU: Ceftriaxone 1-2g IV daily PLUS Azithromycin 500mg IV daily, or Levofloxacin IV.
- Inpatient ICU / Sepsis: Beta-lactam (Ceftriaxone or Ampicillin-sulbactam) + Azithromycin, with Vancomycin or Linezolid added if MRSA is suspected, and Cefepime/Piperacillin-tazobactam if Pseudomonas risk is elevated."""
        },
        {
            "title": "Type 1 and Type 2 Diabetes Mellitus",
            "section": "Endocrinology",
            "content": """Pathophysiology:
- Type 1 DM: Autoimmune destruction of pancreatic beta-cells in the islets of Langerhans, leading to absolute insulin deficiency. Associated with HLA-DR3/DR4, anti-GAD65, anti-IA2, and anti-islet cell antibodies.
- Type 2 DM: Progressive insulin resistance combined with progressive impairment of beta-cell insulin secretion. Strong genetic, visceral adiposity, and metabolic syndrome associations.

Diagnostic Criteria (ADA Guidelines):
1. Fasting Plasma Glucose (FPG) >= 126 mg/dL (7.0 mmol/L) on two separate occasions.
2. Glycated Hemoglobin (HbA1c) >= 6.5%.
3. 2-Hour 75g Oral Glucose Tolerance Test (OGTT) >= 200 mg/dL.
4. Random plasma glucose >= 200 mg/dL in a patient with classic symptoms of hyperglycemia (polyuria, polydipsia, polyphagia, unexplained weight loss).

Therapeutic Management:
- Type 1 DM: Intensive insulin therapy (Basal-bolus regimen: Glargine or Degludec once daily plus rapid-acting Lispro/Aspart before meals; or Continuous Subcutaneous Insulin Infusion pump).
- Type 2 DM:
  * First-line: Metformin (titrated up to 2000 mg/day; inhibits hepatic gluconeogenesis).
  * Cardiorenal protective agents: SGLT2 inhibitors (Empagliflozin, Dapagliflozin) for patients with heart failure or CKD; GLP-1 receptor agonists (Semaglutide, Liraglutide) for high ASCVD risk and weight reduction.
  * Adjuncts: DPP-4 inhibitors, Sulfonylureas (Glipizide), Thiazolidinediones, and Basal Insulin when HbA1c remains > 10% or symptomatic.

Acute Complications:
- Diabetic Ketoacidosis (DKA): Glucose > 250 mg/dL, arterial pH < 7.3, serum bicarbonate < 18 mEq/L, elevated anion gap, ketonemia/ketonuria. Requires aggressive IV isotonic saline, regular insulin infusion (0.1 U/kg/h), and potassium repletion before insulin if K+ < 3.3 mEq/L.
- Hyperosmolar Hyperglycemic State (HHS): Glucose > 600 mg/dL, serum osmolality > 320 mOsm/kg, absence of significant ketoacidosis, marked dehydration."""
        },
        {
            "title": "Cerebrovascular Accident (Ischemic & Hemorrhagic Stroke)",
            "section": "Neurology",
            "content": """Epidemiology & Classifications:
Stroke is a neurological deficit resulting from acute focal central nervous system injury by a vascular cause.
- Ischemic Stroke (87%): Thromboembolic occlusion of cerebral arteries (large artery atherosclerosis, cardioembolic like atrial fibrillation, lacunar small-vessel disease).
- Hemorrhagic Stroke (13%): Intracerebral hemorrhage (ICH, often hypertensive or amyloid angiopathy) and Subarachnoid hemorrhage (SAH, ruptured saccular aneurysm).

Clinical Signs (BE-FAST Protocol):
- Balance loss / ataxia.
- Eyes: Diplopia or visual field cuts (hemianopia).
- Face: Facial droop or asymmetry.
- Arms: Unilateral arm or leg weakness/numbness.
- Speech: Dysarthria or aphasia (Broca's expressive or Wernicke's receptive).
- Time: Critical window for intervention.

Emergency Evaluation & Management:
- Non-contrast Head CT or MRI Diffusion-Weighted Imaging (DWI) immediately to rule out hemorrhage.
- Ischemic Stroke Thrombolysis: Intravenous Alteplase (0.9 mg/kg, max 90 mg) or Tenecteplase (0.25 mg/kg) administered within 4.5 hours of symptom onset if no contraindications (active bleeding, BP > 185/110 mmHg, recent surgery, platelet < 100k).
- Mechanical Thrombectomy: Indicated for large vessel occlusions (internal carotid or proximal MCA) up to 24 hours from last known well based on perfusion imaging mismatch.
- Blood Pressure targets: Permissive hypertension up to 220/120 mmHg in non-thrombolysis patients; maintain < 180/105 mmHg if thrombolysis or thrombectomy received.
- Secondary Prevention: Aspirin + Clopidogrel for 21 days (CHANCE / POINT trials), followed by monotherapy; high-intensity Atorvastatin; anticoagulation for atrial fibrillation."""
        },
        {
            "title": "Epilepsy and Status Epilepticus",
            "section": "Neurology",
            "content": """Definition:
Epilepsy is diagnosed when a patient has two or more unprovoked seizures occurring > 24 hours apart, or one unprovoked seizure with high recurrence risk (> 60% over 10 years).
- Focal Seizures: Originating within neuronal networks limited to one cerebral hemisphere (with or without dyscognitive features).
- Generalized Seizures: Rapidly bilateral engaging networks, including tonic-clonic (grand mal), absence (petit mal), myoclonic, and atonic seizures.

Status Epilepticus Emergency Protocol:
Status epilepticus is defined as continuous seizure activity >= 5 minutes or recurrent seizures without return to baseline consciousness. It requires immediate, aggressive staged management:
1. Phase 1 (0-5 minutes): Assess airway, breathing, circulation (ABC), check fingerstick glucose (administer D50W if hypoglycemic), obtain IV access, administer thiamine if indicated.
2. Phase 2 (5-10 minutes - First Line Emergent):
   - IV Lorazepam (0.1 mg/kg, typically 4 mg IV bolus at 2 mg/min), OR
   - IM Midazolam 10 mg (if IV access unavailable), OR
   - IV Diazepam 10 mg.
3. Phase 3 (10-20 minutes - Urgent Second Line):
   - IV Levetiracetam (Keppra) 60 mg/kg (max 4500 mg), OR
   - IV Fosphenytoin 20 mg PE/kg (max 1500 mg), OR
   - IV Valproate sodium 40 mg/kg (max 3000 mg).
4. Phase 4 (Refractory Status > 20-30 minutes):
   - Continuous IV anesthetic infusions: Propofol, Midazolam, or Ketamine with endotracheal intubation and continuous EEG monitoring."""
        },
        {
            "title": "Hypertension and Hypertensive Emergencies",
            "section": "Cardiology / Nephrology",
            "content": """Classification (ACC/AHA Guidelines):
- Normal: SBP < 120 and DBP < 80 mmHg.
- Elevated: SBP 120-129 and DBP < 80 mmHg.
- Stage 1 Hypertension: SBP 130-139 or DBP 80-89 mmHg.
- Stage 2 Hypertension: SBP >= 140 or DBP >= 90 mmHg.
- Hypertensive Crisis: SBP > 180 and/or DBP > 120 mmHg.
  * Hypertensive Urgency: Severe elevation without acute target organ damage.
  * Hypertensive Emergency: Severe elevation WITH acute target organ damage (encephalopathy, acute aortic dissection, pulmonary edema, myocardial infarction, acute kidney injury, or eclampsia).

Treatment of Essential Hypertension:
- First-line pharmacological classes:
  1. Thiazide-like diuretics (Chlorthalidone 12.5-25 mg, Hydrochlorothiazide 25 mg).
  2. Calcium Channel Blockers (Dihydropyridines: Amlodipine 5-10 mg).
  3. ACE Inhibitors (Lisinopril 10-40 mg, Enalapril) OR Angiotensin Receptor Blockers (Losartan 50-100 mg, Telmisartan).
- Note: Dual therapy is recommended as initial step for Stage 2 hypertension. Avoid ACEi and ARB combination due to hyperkalemia and renal failure risk.

Hypertensive Emergency Management:
- Transfer to ICU for continuous arterial line blood pressure monitoring.
- Target: Reduce MAP by no more than 20-25% in the first hour to prevent ischemic cerebral hypoperfusion, then target 160/100 mmHg over next 2-6 hours.
- Exceptions: Acute aortic dissection requires rapid reduction of SBP to < 120 mmHg within 20 minutes (using Esmolol/Labetalol + Nitroprusside).
- IV Medications: Nicardipine, Labetalol, Hydralazine, Nitroglycerin, Clevedipine."""
        },
        {
            "title": "Peptic Ulcer Disease and Gastrointestinal Bleeding",
            "section": "Gastroenterology",
            "content": """Pathogenesis:
Peptic Ulcer Disease (PUD) consists of mucosal erosions extending through the muscularis mucosae in the stomach (gastric ulcer) or proximal duodenum (duodenal ulcer).
- Major Causes:
  1. Helicobacter pylori infection (>70% of duodenal ulcers; colonizes antral mucosa and produces urease).
  2. Nonsteroidal Anti-inflammatory Drugs (NSAIDs: Ibuprofen, Naproxen, Ketorolac), which inhibit COX-1 and deplete protective mucosal prostaglandins.
  3. Severe physiological stress, Zollinger-Ellison syndrome (gastrinoma).

Clinical Symptoms:
- Epigastric burning discomfort, gnawing pain.
- Duodenal ulcers: Pain relieved by food, recurs 2-3 hours postprandial; nocturnal pain.
- Gastric ulcers: Pain exacerbated by food intake, associated with nausea, early satiety, and anorexia.

Acute Upper GI Bleeding Management:
- Symptoms: Hematemesis ('coffee-ground' or bright red blood), melena (black tarry stools), hemodynamic instability.
- Resuscitation: Two large-bore IVs, crystalloid fluids, packed red blood cells (transfusion threshold hemoglobin < 7 g/dL; < 8 g/dL in cardiovascular disease).
- Pharmacotherapy: High-dose IV Proton Pump Inhibitor (Pantoprazole 80 mg IV bolus followed by 8 mg/h continuous infusion).
- Diagnostic Endoscopy: Esophagogastroduodenoscopy (EGD) within 24 hours for diagnosis and therapeutic intervention (hemoclips, epinephrine injection, thermal coagulation).
- H. pylori Eradication (Quadruple Therapy for 14 days): Bismuth subsalicylate + Metronidazole + Tetracycline + PPI (Omeprazole 20mg BID)."""
        },
        {
            "title": "Anaphylaxis and Severe Allergic Reactions",
            "section": "Immunology & Emergency Medicine",
            "content": """Pathophysiology:
Anaphylaxis is an acute, life-threatening systemic hypersensitivity reaction triggered by IgE-mediated mast cell and basophil degranulation, resulting in massive systemic release of histamine, tryptase, leukotrienes, and prostaglandins.
- Common Triggers: Foods (peanuts, tree nuts, shellfish, milk, eggs), Medications (beta-lactam antibiotics, NSAIDs, neuromuscular blockers), Hymenoptera stings (bees, wasps), and natural rubber latex.

Clinical Diagnostic Criteria:
Anaphylaxis is highly likely when any ONE of the following 3 criteria is fulfilled:
1. Acute onset (minutes to hours) of skin/mucosal tissue involvement (generalized hives, pruritus, flushing, swollen lips/tongue/uvula) PLUS EITHER respiratory compromise (dyspnea, wheezing, stridor) OR reduced blood pressure / end-organ dysfunction.
2. Two or more of the following occurring rapidly after exposure to a likely allergen: cutaneous symptoms, respiratory compromise, hypotension, or persistent gastrointestinal cramping/vomiting.
3. Reduced blood pressure after exposure to a known allergen for that patient (SBP < 90 mmHg or > 30% drop from baseline).

Emergency Management Protocol:
1. First and Foremost: EPINEPHRINE (1:1000, 1 mg/mL) injected INTRAMUSCULARLY into the anterolateral mid-thigh.
   - Adult Dose: 0.3 to 0.5 mg IM.
   - Pediatric Dose: 0.01 mg/kg IM (max 0.3 mg).
   - Repeat every 5 to 15 minutes as needed if symptoms persist.
2. Position patient recumbent with legs elevated (Trendelenburg position); do NOT sit or stand the patient up suddenly, which can precipitate fatal empty-ventricle syndrome.
3. High-flow oxygen via non-rebreather mask (10-15 L/min); prepare for early intubation if stridor or oropharyngeal angioedema is present.
4. Aggressive IV fluid resuscitation: Rapid infusion of 1 to 2 Liters normal saline for hypotension.
5. Adjunctive Therapies (secondary, never delay epinephrine):
   - H1 antihistamine: Diphenhydramine 25-50 mg IV.
   - H2 antihistamine: Famotidine 20 mg IV.
   - Corticosteroids: Methylprednisolone 125 mg IV (to prevent biphasic reactions).
   - Inhaled Albuterol for bronchospasm."""
        },
        {
            "title": "Sepsis and Septic Shock (Surviving Sepsis Campaign)",
            "section": "Critical Care / Infectious Diseases",
            "content": """Definitions (Sepsis-3 Consensus):
- Sepsis: Life-threatening organ dysfunction caused by a dysregulated host response to infection. Clinically identified by an acute increase in SOFA (Sequential Organ Failure Assessment) score >= 2 points.
- Quick SOFA (qSOFA) Bedside Screening: Respiratory rate >= 22 breaths/min, altered mental status (GCS < 15), Systolic blood pressure <= 100 mmHg.
- Septic Shock: A subset of sepsis where underlying circulatory and cellular metabolism abnormalities substantially increase mortality. Defined as persistent hypotension requiring vasopressors to maintain MAP >= 65 mmHg AND serum lactate > 2 mmol/L despite adequate fluid resuscitation.

Surviving Sepsis 1-Hour Hour Bundle:
1. Measure Blood Lactate Level: Remeasure within 2-4 hours if initial lactate is > 2 mmol/L.
2. Obtain Blood Cultures: Draw at least two sets of blood cultures (aerobic and anaerobic) BEFORE initiating antimicrobial therapy (without delaying antibiotics > 45 minutes).
3. Administer Broad-Spectrum Antimicrobial Therapy: Initiate IV antibiotics within 1 hour of recognition (e.g., Vancomycin + Piperacillin-tazobactam or Cefepime).
4. Rapid Fluid Resuscitation: Administer at least 30 mL/kg of IV balanced crystalloid (Lactated Ringer's) within the first 3 hours for hypotension or lactate >= 4 mmol/L.
5. Initiate Vasopressors:
   - First-choice vasopressor: Norepinephrine titrated to maintain Mean Arterial Pressure (MAP) >= 65 mmHg.
   - Second-line additions: Vasopressin (at fixed dose 0.03 units/min) to reduce norepinephrine requirements, followed by Epinephrine.
   - Inotropic agent: Dobutamine for persistent hypoperfusion despite adequate volume and MAP."""
        },
        {
            "title": "Chronic Kidney Disease and Acute Kidney Injury",
            "section": "Nephrology",
            "content": """Acute Kidney Injury (KDIGO Criteria):
AKI is defined by any of the following:
- Increase in Serum Creatinine by >= 0.3 mg/dL within 48 hours; OR
- Increase in Serum Creatinine to >= 1.5 times baseline within the prior 7 days; OR
- Urine output < 0.5 mL/kg/h for 6 hours.
Etiological Classification:
1. Prerenal (Decreased perfusion): Hypovolemia, shock, NSAIDs, ACEi, renal artery stenosis. FeNa < 1%, BUN/Cr ratio > 20:1.
2. Intrinsic (Parenchymal damage): Acute Tubular Necrosis (ATN due to ischemia or nephrotoxins like aminoglycosides/contrast; muddy brown casts), Acute Interstitial Nephritis (AIN; eosinophils, WBC casts), Glomerulonephritis (RBC casts, proteinuria).
3. Postrenal (Obstruction): Benign prostatic hyperplasia, bilateral urolithiasis, pelvic tumor.

Chronic Kidney Disease (CKD):
CKD is defined as abnormalities of kidney structure or function present for > 3 months.
- Staged by Estimated Glomerular Filtration Rate (eGFR):
  * Stage G1: eGFR >= 90 mL/min/1.73m2 (with evidence of kidney damage/albuminuria).
  * Stage G2: eGFR 60-89 mL/min/1.73m2.
  * Stage G3a: eGFR 45-59 mL/min/1.73m2.
  * Stage G3b: eGFR 30-44 mL/min/1.73m2.
  * Stage G4: eGFR 15-29 mL/min/1.73m2 (severe reduction; prepare for renal replacement).
  * Stage G5: eGFR < 15 mL/min/1.73m2 (Kidney failure / End-Stage Renal Disease requiring Hemodialysis, Peritoneal Dialysis, or Renal Transplantation).
- Management Pillars: Blood pressure control (< 120-130 mmHg SBP), SGLT2 inhibitors (proven nephroprotection), ACE inhibitors or ARBs for albuminuria, management of secondary hyperparathyroidism, anemia of CKD (iron supplementation, Erythropoiesis-Stimulating Agents)."""
        },
        {
            "title": "Pharmacology: Essential Drug Classes, Dosing & Toxicities",
            "section": "Clinical Pharmacology",
            "content": """Cardiovascular Agents:
- Beta-Blockers: Metoprolol (25-200 mg daily), Carvedilol (3.125-25 mg BID). Mechanisms: competitive antagonism of beta-1 adrenergic receptors. Adverse: Bradycardia, bronchospasm, masking hypoglycemia.
- ACE Inhibitors: Lisinopril, Ramipril. Inhibit angiotensin-converting enzyme. Adverse: Dry cough (bradykinin accumulation), hyperkalemia, angioedema, teratogenicity.
- Statins: Atorvastatin (10-80 mg), Rosuvastatin (5-40 mg). Inhibit HMG-CoA reductase. Adverse: Myalgia, rhabdomyolysis (monitored via CK), transaminitis.

Antimicrobial Agents:
- Penicillins & Cephalosporins: Inhibit peptidoglycan cell wall synthesis. Cross-reactivity rate is low (<2%).
- Macrolides (Azithromycin): 500 mg day 1, 250 mg days 2-5. Inhibit 50S ribosomal subunit. Adverse: QT prolongation, CYP3A4 inhibition.
- Fluoroquinolones (Ciprofloxacin, Levofloxacin): Inhibit DNA gyrase. Black box warnings: Tendon rupture (Achilles), aortic dissection, peripheral neuropathy.

Analgesics & Anti-Inflammatory:
- Acetaminophen (Paracetamol): Max daily dose 3000-4000 mg in adults. Toxicity: Hepatic necrosis via toxic metabolite NAPQI when glutathione stores deplete; antidote is N-Acetylcysteine (NAC).
- NSAIDs: Ibuprofen (400-800 mg TID), Naproxen (250-500 mg BID). Reversible COX-1/2 inhibition. Adverse: Gastric ulceration, renal papillary necrosis, fluid retention."""
        },
        {
            "title": "Clinical Laboratory Reference Ranges and Diagnostic Tests",
            "section": "Laboratory Medicine",
            "content": """Complete Blood Count (CBC) Reference Ranges:
- Hemoglobin (Hgb): Men: 13.8 - 17.2 g/dL; Women: 12.1 - 15.1 g/dL.
- Hematocrit (Hct): Men: 40.7% - 50.3%; Women: 36.1% - 44.3%.
- White Blood Cells (WBC): 4,500 - 11,000 /uL (Neutrophils: 55-70%, Lymphocytes: 20-40%).
- Platelet Count: 150,000 - 450,000 /uL.

Basic & Comprehensive Metabolic Panel (BMP / CMP):
- Sodium (Na+): 135 - 145 mEq/L.
- Potassium (K+): 3.5 - 5.0 mEq/L.
- Chloride (Cl-): 96 - 106 mEq/L.
- Bicarbonate (HCO3-): 22 - 29 mEq/L.
- Blood Urea Nitrogen (BUN): 7 - 20 mg/dL.
- Serum Creatinine: 0.6 - 1.2 mg/dL.
- Fasting Glucose: 70 - 99 mg/dL.
- Calcium: 8.5 - 10.2 mg/dL.
- Albumin: 3.5 - 5.0 g/dL.
- Total Bilirubin: 0.1 - 1.2 mg/dL.
- AST / ALT: 10 - 40 U/L.
- Alkaline Phosphatase: 44 - 147 U/L.

Arterial Blood Gas (ABG):
- pH: 7.35 - 7.45.
- PaCO2: 35 - 45 mmHg.
- PaO2: 80 - 100 mmHg.
- HCO3-: 22 - 26 mEq/L.
- SaO2: 95 - 100%."""
        }
    ]

    print(f"Generating {len(articles)} detailed medical sections into '{output_path}'...")

    for i, art in enumerate(articles):
        page = doc.new_page(width=612, height=792)  # Standard Letter size
        
        # Header banner text
        header_text = f"THE GALE ENCYCLOPEDIA OF MEDICINE | Section: {art['section']}"
        page.insert_text((50, 40), header_text, fontsize=8, color=(0.4, 0.4, 0.4))
        
        # Title
        title_text = art['title']
        page.insert_text((50, 75), title_text, fontsize=16, color=(0.1, 0.1, 0.1))
        
        # Divider line
        page.draw_line(fitz.Point(50, 85), fitz.Point(562, 85), color=(0.8, 0.2, 0.1), width=1.5)
        
        # Body text
        text_rect = fitz.Rect(50, 100, 562, 740)
        page.insert_textbox(
            text_rect,
            art['content'],
            fontsize=10,
            color=(0.15, 0.15, 0.15),
            align=fitz.TEXT_ALIGN_LEFT
        )
        
        # Footer
        footer_text = f"Page {i+1} of {len(articles)}  |  MEDICOS Clinical Reference System"
        page.insert_text((200, 765), footer_text, fontsize=8, color=(0.5, 0.5, 0.5))

    doc.save(output_path)
    doc.close()
    print(f"Successfully generated clean PDF at: {output_path}")

if __name__ == "__main__":
    create_medical_encyclopedia()
