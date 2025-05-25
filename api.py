import requests

def diagnose(existing_conditions: str, symptoms: str) -> str:
    existing = [e.strip().lower() for e in existing_conditions.split(',') if e.strip()]
    symptoms_list = [s.strip().lower() for s in symptoms.split(',') if s.strip()]
    if not symptoms_list:
        return "Please enter at least one symptom."

    # Call the API
    response = requests.get(
        "https://clinicaltables.nlm.nih.gov/api/conditions/v3/search",
        params={"terms": ", ".join(symptoms_list), "maxList": 10, "df": "consumer_name"}
    )
    if response.status_code != 200:
        return "API error."

    data = response.json()
    names = [item[0] for item in data[3]] if len(data) > 3 else []
    if not names:
        return "No matching conditions found."

    # Score and rank
    scores = []
    for i, name in enumerate(names):
        base_score = len(names) - i
        boost = 2 if name.lower() in existing else 1
        scores.append(base_score * boost)

    best_index = scores.index(max(scores))
    best_condition = names[best_index]

    # Output all candidates briefly
    print("\nTop possible conditions:")
    for name, score in zip(names, scores):
        note = " (pre-existing)" if name.lower() in existing else ""
        print(f"- {name}{note}")

    return f"\nMost likely condition: {best_condition}"

if __name__ == "__main__":
    print("Enter existing conditions (comma-separated), or press Enter to skip:")
    existing_input = input("Existing: ")
    print("\nEnter symptoms (comma-separated):")
    symptoms_input = input("Symptoms: ")

    result = diagnose(existing_input, symptoms_input)
    print(result)
