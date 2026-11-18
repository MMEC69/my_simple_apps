# Considering facts
    # AI Score
    # Similarity Score
    # Content Marking
    # Citations are mentioned or not
    # Diagrams being utilized or not

# make sure to provide content marks out of 100
# Marks will be given out of hundred

def ai_score_processor(ai_score, ignored_ai_score_level, mark_reduction_ai_violation):
    score_multiplier = 1
    if 0 > ai_score or  ai_score > 100:
        raise ValueError("AI Score should be between 0 and 100")
    if ai_score <= ignored_ai_score_level:
        return score_multiplier
    else:
        score_multiplier = score_multiplier - (((ai_score - ignored_ai_score_level) / 60 * 0.5) + 0.5)
        return score_multiplier
    ## return 0

def similarity_score_processor(similarity_score, ignored_similarity_score_level):
    score_multiplier = 1
    if similarity_score < 0 or similarity_score > 100:
        raise ValueError("Content marks should be between 0 and 100")
    if similarity_score <= ignored_similarity_score_level:
        return score_multiplier
    else:
        score_multiplier = score_multiplier - (((similarity_score - ignored_similarity_score_level) / 60 * 0.5) + 0.5)
        # print(score_multiplier)
        return score_multiplier
    # return 0

def content_marks_processor(content_marks):
    if content_marks < 0 or content_marks > 100:
        raise ValueError("Content marks should be between 0 and 100")
    return content_marks

def citations_score_processor(is_cited):
    cite_score_multiplier = 0.3
    if is_cited == 0:
        cite_score_multiplier = 0
        return cite_score_multiplier
    else:
        return cite_score_multiplier
    # return 0

def diagrams_score_processor(are_diagrams_there):
    diagram_score_multiplier = 0.2
    if are_diagrams_there == 0:
        diagram_score_multiplier = 0
        return diagram_score_multiplier
    else:
        return diagram_score_multiplier
    # return 0

if __name__ == '__main__':
    ignored_ai_score_level = 40  # 40%
    ignored_similarity_score_level = 40  # 40%
    mark_reduction_ai_violation = 50  # 50%

    final_score = 0

    student_no = 1
    while (True):
        print(f"======Marking of Student No {student_no}======")
        content_marks = int(input("Content marks: "))
        content_marks = content_marks_processor(content_marks)

        ai_score = int(input("AI score: "))
        ai_reductor = ai_score_processor(ai_score, ignored_ai_score_level, mark_reduction_ai_violation)

        final_score += ai_reductor * content_marks * 0.35

        similarity_score = int(input("Similarity score: "))
        similarity_reductor = similarity_score_processor(similarity_score, ignored_similarity_score_level)

        final_score += similarity_reductor * content_marks * 0.15

        is_cited = int(input("Is cited? "))
        cite_reductor = citations_score_processor(is_cited)

        final_score += cite_reductor * content_marks


        are_diagrams_there = input("Are the diagrams there? ")
        diagrams_reductor = diagrams_score_processor( are_diagrams_there)

        final_score += diagrams_reductor * content_marks

        print(f"======Final Score====== \n {final_score}\n=======================")

        student_no += 1
