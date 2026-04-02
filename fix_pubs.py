import re
from pathlib import Path

# Need to manually map the files we have to the actual titles since parsing the latex was slightly off
# The numbering matches the original list provided to the user. Let's look up the titles again.

mapping = {
    "11 - SICLC.png": "Socioeconomic Impacts of COVID-19 in Low-Income Countries",
    "12 - CFRTE.png": "Contract Farming and Rural Transformation",
    "13 - SFEED.png": "One Size Fits All? Experimental Evidence on the Digital Delivery of Personalized Extension Advice in Nigeria",
    "14 - REBSB.png": "Research Ethics Beyond the IRB",
    "15 - UPURU.jpg": "Ulysses' Pact or Ulysses' Raft",
    "17 - AGRIC.png": "Agriculture in the Process of Development",
    "19 - MMRYP.png": "Money Matters: The Role of Yields and Profits in Agricultural Technology Adoption",
    "20 - CONSE.png": "Conservation Agriculture and Climate Resilience",
    "22 - BFEAA.png": "Beasts of the Field? Ethics in Agricultural and Applied Economics",
    "24 - SDADP.png": "To Specialize or Diversify: Agricultural Diversity and Poverty Dynamics in Ethiopia",
    "28 - RDIPA.png": "Risk, Crop Yields, and Weather Index Insurance in Village India",
    "3 - IEDEC.jpg": "Impact Evaluations in Data-Scarce Environments",
    "33 - VSSAR.png": "VSSAR", # Don't know this one yet
    "34 - LCMEF.png": "LCMEF",
    "4 - MWUEO.png": "The Mismeasure of Weather",
    "5 - FWFNE.png": "Food Without Fire",
    "6 - CHLDF.png": "Coping or Hoping",
    "7 - EUREO.png": "Expanding Undergraduate Research",
    "8 - PPMEI.png": "Privacy Protection",
    "9 - FIDFY.png": "Food Insecurity During the First Year",
}

def get_image_for_pub(title):
    # fuzzy match
    import difflib

    images_dir = Path("/app/assets/images/publications")
    if not images_dir.exists():
        return ""

    for img_file in images_dir.iterdir():
        file_key = img_file.name
        if file_key in mapping:
            # check if title contains the mapping or vice-versa
            clean_title = title.lower()
            clean_map = mapping[file_key].lower()
            if clean_map in clean_title or clean_title in clean_map:
                return f"assets/images/publications/{img_file.name}"
            # Some mapping are short, let's just check the first 20 chars
            if clean_title.startswith(clean_map[:20]) or clean_map.startswith(clean_title[:20]):
                return f"assets/images/publications/{img_file.name}"

    # fallback to code match
    words = [w.capitalize() for w in re.findall(r'[a-zA-Z]+', title) if len(w) > 2]
    code = "".join(w[0] for w in words[:5]).upper()
    if len(code) < 5:
        code += "X" * (5 - len(code))

    for img in images_dir.iterdir():
        if code in img.name:
            return f"assets/images/publications/{img.name}"

    return ""

def test():
    titles = [
        "Impact Evaluations in Data-Scarce Environments: The Case of Stress-Tolerant Rice Varieties in Bangladesh.",
        "The Mismeasure of Weather: Using Earth Observation Data for Estimation of Socioeconomic Outcomes.",
        "Food Without Fire: Nutritional and Environmental Impacts from a Solar Stove Field Experiment.",
        "Coping or Hoping? Livelihood Diversification and Food Insecurity in the COVID-19 Pandemic.",
        "Expanding Undergraduate Research Experience: Opportunities, Challenges, and Lessons for the Future.",
        "Privacy Protection, Measurement Error, and the Integration of Remote Sensing and Socioeconomic Survey Data.",
        "Food Insecurity During the First Year of the COVID-19 Pandemic in Four African Countries.",
        "Risk, Crop Yields, and Weather Index Insurance in Village India."
    ]
    for t in titles:
        print(f"{t[:20]}... -> {get_image_for_pub(t)}")

test()
