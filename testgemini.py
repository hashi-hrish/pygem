import google.generativeai as genai

#Configure the API key
api_key = "AIzaSyCyI5ou--3vOwURusDQNSKrL3B9ADRFQO0"
genai.configure(api_key=api_key)

#Load the Gemini Pro model
model = genai.GenerativeModel('gemini-2.0-flash')

def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text

def generate_follow_up_question(response):
    follow_up_prompt = response + "\n create a follow up question on this"
    follow_up_response = model.generate_content(follow_up_prompt)
    return follow_up_response.text

def main():
    initial_prompt = input("Enter your initial question: ")
    current_prompt = initial_prompt

    while True:
        response = get_response(current_prompt)
        print("Response:", response)

        follow_up_question = generate_follow_up_question(response)
        print("Follow-up Question:", follow_up_question)

        cont = input("Press Enter to continue or type 'exit' to stop: ")
        if cont.lower() == 'exit':
            break


        current_prompt = follow_up_question

if __name__ == "__main__":
    main()
