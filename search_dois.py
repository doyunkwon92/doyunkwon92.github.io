import urllib.request
import urllib.parse
import json
import sys

titles = [
    "Optimising the Therapeutic Window: A Systematic Review and Network Meta-Analysis of Pregabalin Dosing Strategies for Painful Diabetic Neuropathy",
    "Comparing the effectiveness of pregabalin and gabapentin in patients with lumbar radiculopathy: A systematic review and meta-analysis",
    "Acute piriformis syndrome in a military pilot with chronic lumbar radiculopathy: A case report",
    "Quantitative evaluation of upper extremity strength recovery after cervical epidural block: a retrospective study",
    "Evaluation of Upper Extremity Muscle Strength Improvement in Patients with Cervical Disc Herniation through Cervical Epidural Block: A Pilot Study",
    "Clinical impairments and rotator Cuff Tendon pathology in primary and intrinsic secondary adhesive capsulitis",
    "Comparing the therapeutic effects of pregabalin and gabapentin after transforaminal epidural nerve block in lumbar radiculopathy",
    "Combination Therapy of Polydeoxyribonucleotide and Microcurrent in Muscle Regeneration on Cast-Induced Muscle Atrophy in Rabbit",
    "Airway invasion in non-neurologically ill patients with dysphagia: Contributing factors and associated problems during swallowing process. A retrospective observational study"
]

for title in titles:
    query = urllib.parse.quote(title)
    url = f"https://api.crossref.org/works?query.title={query}&select=DOI,title&rows=1"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'mailto:test@example.com'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            items = data.get('message', {}).get('items', [])
            if items:
                print(f"{title} -> https://doi.org/{items[0].get('DOI')}")
            else:
                print(f"{title} -> NOT FOUND")
    except Exception as e:
        print(f"{title} -> ERROR {e}")
