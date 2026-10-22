
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types 

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
client =genai.Client(api_key=GEMINI_API_KEY)



question_types = {
    "MCQs": "Generate multiple-choice questions with four options and the correct answer.",
    "Short Answer": "Generate short-answer questions based on the given content.",
    "Interview": "Generate interview-style questions based on the given content."
}

def question_generator(question, persona):
    system_prompt = question_types[persona],
    response = client.model.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4     ),
        contents=question,
    )
    return response.text


demo = gr.Interface(
    fn=question_generator,
    inputs=[
        gr.Textbox(lines=4, placeholder="Ask a question...", label="Question"),
        gr.Radio(choices=list(question_types.keys()), value="MCQs", label="Personality")
    ],
    outputs=gr.Textbox(lines=10, label="Response"),
    title="Interview Question Generator",
    description="Ask the AI to create questions for your interview.You can choose which type of questions you want."
)

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))

