import pickle
import re

pipeline_path = r'D:\Dev\DevPfa\Model\my_pipeline.pkl'
with open(pipeline_path, 'rb') as f:
    pipe = pickle.load(f)

keywords = ['price', 'category', 'subcategory','subcategories','product','products']

def normalize_question(question):
        question = question.upper()
        for keyword in keywords:
            question = re.sub(fr'\b{keyword}\b', f'{keyword}', question, flags=re.IGNORECASE)
            question = re.sub(r'\bhow much\b', 'the price of', question, flags=re.IGNORECASE)
            return question

def generate_questions(original_question):
        if re.search(r'price', original_question, re.IGNORECASE) and not re.search(r'member|regular', original_question, re.IGNORECASE):
            # Generate two questions
            question_member = re.sub(r'price', 'member price', original_question, flags=re.IGNORECASE)
            question_regular = re.sub(r'price', 'regular price', original_question, flags=re.IGNORECASE)
            return [question_member, question_regular]
        else:
            return [original_question]
        
# Define a function to ask questions using the loaded pipeline and show only the first answer
def ask_question(question):
    normalized_question = normalize_question(question)

    generated_questions = generate_questions(normalized_question)

    L = []
    for q in generated_questions:
            prediction = pipe.run(
                query=q, params={"Retriever": {"top_k": 10}, "Reader": {"top_k": 5}}
            )

            best_answer = prediction['answers'][0]  # Get the best answer
            if re.search(r'price', q, re.IGNORECASE) and re.search(r'member', q, re.IGNORECASE):
                L.append(f"\nthe member price is: {best_answer.answer}")
            elif re.search(r'price', q, re.IGNORECASE) and re.search(r'regular', q, re.IGNORECASE):
                L.append(f"\nthe regular price is: {best_answer.answer}")
            else:
                L.append(f'{best_answer.answer}')
    return ", ".join(L)
