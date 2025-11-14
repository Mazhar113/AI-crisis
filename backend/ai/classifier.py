import spacy

nlp = spacy.blank("en")
CATEGORIES = ["Flood","Fire","Earthquake","Medical Emergency","Food/Water Shortage","Power Outage","Road Block","Building Collapse","Security/Violence","Other"]

def classify_report(description):
    desc = description.lower()
    if "flood" in desc or "water" in desc: return "Flood",0.85
    elif "fire" in desc or "burn" in desc: return "Fire",0.85
    elif "earthquake" in desc or "quake" in desc: return "Earthquake",0.9
    elif "medical" in desc or "injury" in desc: return "Medical Emergency",0.88
    elif "food" in desc or "water shortage" in desc: return "Food/Water Shortage",0.8
    elif "power" in desc or "electricity" in desc: return "Power Outage",0.82
    elif "road" in desc or "traffic" in desc or "block" in desc: return "Road Block",0.8
    elif "collapse" in desc or "building" in desc: return "Building Collapse",0.85
    elif "attack" in desc or "violence" in desc or "security" in desc: return "Security/Violence",0.88
    else: return "Other",0.7
