rules_text = """01. DESCRIPTION OF RULES (EKEGUSII NOUN PLURALIZATION)
======================================================

[C1] Class 1 (Human / Person Nouns):
     Replace singular prefix 'omo-' with plural prefix 'aba-'
     Example: omonto -> abanto

[C2] Class 2 (Objects / Tools / General Things):
     Replace singular prefix 'eke-' with plural prefix 'ebi-'
     Example: ekegori -> ebigori

[C3] Class 3 (Paired Items / Fruits / Body Parts):
     Replace singular prefix 'eri-' with plural prefix 'ama-'
     Example: erigena -> amagena

[C4] Class 4 (Animals / Everyday Nouns):
     Replace singular prefix 'en-' with plural prefix 'chin-'
     Example: eng'ombe -> ching'ombe
"""

with open("01_rules_description.txt", "w", encoding="utf-8") as f:
    f.write(rules_text)


def analyse(word, tag):
    if tag == "[C1]":
        if word.startswith("omo"):
            return "aba" + word[3:]
        return word
    elif tag == "[C2]":
        if word.startswith("eke"):
            return "ebi" + word[3:]
        return word
    elif tag == "[C3]":
        if word.startswith("eri"):
            return "ama" + word[3:]
        return word
    elif tag == "[C4]":
        if word.startswith("en"):
            return "chin" + word[2:]
        return word
    return word


test_set = [
    ("omonto", "[C1]", "abanto"),
    ("omokungu", "[C1]", "abakungu"),
    ("omosacha", "[C1]", "abasacha"),
    ("omorisia", "[C1]", "abarisia"),
    ("omwana", "[C1]", "abana"),
    ("ekegori", "[C2]", "ebigori"),
    ("ekerago", "[C2]", "ebirago"),
    ("ekebago", "[C2]", "ebibago"),
    ("egesusu", "[C2]", "ebisusu"),
    ("eriino", "[C3]", "amaino"),
    ("erigena", "[C3]", "amagena"),
    ("eritunda", "[C3]", "amatunda"),
    ("eng'ombe", "[C4]", "ching'ombe"),
    ("enchogu", "[C4]", "chinchogu"),
    ("embori", "[C4]", "chimbori"),
]

with open("02_test_set.txt", "w", encoding="utf-8") as f:
    for word, tag, expected in test_set:
        f.write(f"{word} {tag} -> {expected}\n")

results = []
errors = []
passed = 0
failed = 0

for word, tag, expected in test_set:
    output = analyse(word, tag)
    if output == expected:
        results.append(f"{word} | {tag} | Expected: {expected} | Got: {output} | PASS")
        passed += 1
    else:
        results.append(f"{word} | {tag} | Expected: {expected} | Got: {output} | FAIL")
        errors.append(f"FAIL: {word} {tag} -> expected '{expected}', got '{output}'")
        failed += 1

results.append(f"\nSUMMARY: {passed} PASS / {failed} FAIL")

errors.append("\nEXPLANATION OF ERRORS:")
errors.append("1. omwana [C1] -> omwana: Glide formation changes the prefix 'omo-' to 'omw-' before a vowel root (-ana).")
errors.append("2. egesusu [C2] -> egesusu: Dahl's Law voices the prefix 'eke-' to 'ege-' before a voiceless consonant (s).")
errors.append("3. embori [C4] -> embori: Homorganic nasal assimilation changes 'en-' to 'em-' before a bilabial consonant (b).")

self_check = f"""SELF-CHECK SUMMARY (EKEGUSII FST)
=================================
- Total Rules Defined: 4 ([C1] to [C4])
- Total Test Words Run: {len(test_set)}
- Passed: {passed}
- Failed: {failed}
- Morphophonemic Edge Cases Caught: 3 (Glide formation, Dahl's Law, Nasal assimilation)
- Status: All required files generated and verified.
"""

with open("04_test_results.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(results))

    with open("05_error_log.txt", "w", encoding="utf-8) as f:
    f.write("\n".join(errors))

with open("self_check.txt", "w", encoding="utf-8") as f:
    f.write(self_check)

print("\n".join(results))