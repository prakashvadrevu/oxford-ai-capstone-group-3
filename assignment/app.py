
from custom_qa_chain import CustomQAChain

def answer_question(query, history=None):
    custom_qa_chain = CustomQAChain()
    return custom_qa_chain.run(query, history)

if __name__ == "__main__":
    question = "Your test question"
    print(answer_question(question))
