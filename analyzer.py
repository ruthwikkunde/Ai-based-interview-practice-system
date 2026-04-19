import random

def analyze_answer(answer, question):

    answer_lower = answer.lower()
    score = 0
    tips = []

    keyword_map = {
        "polymorphism":["oop","method","overriding","overloading"],
        "list and tuple":["list","tuple","mutable","immutable"],
        "database":["database","table","data"],
        "api":["request","response","communication"],
        "multithreading":["thread","process","parallel"],
        "strength":["skill","improve"],
        "yourself":["student","skills","career"]
    }

    for key in keyword_map:
        if key in question.lower():
            for word in keyword_map[key]:
                if word in answer_lower:
                    score += 1

    corrected = answer

    if corrected:
        corrected = corrected[0].upper() + corrected[1:]

    if corrected and corrected[-1] not in ".!?":
        corrected += "."

    if len(answer.split()) < 5:
        tips.append("Explain in more detail")

    fillers = ["um","uh","like"]
    for f in fillers:
        if f in answer_lower:
            tips.append("Avoid filler words")
            break

    score = min(10, score + random.randint(4,6))

    if score >= 8:
        feedback = "Good answer"
    elif score >= 6:
        feedback = "Average answer"
    else:
        feedback = "Weak answer"

    feedback += " | Corrected: " + corrected

    if tips:
        feedback += " | Tips: " + ", ".join(tips)

    return {
        "score":score,
        "feedback":feedback
    }