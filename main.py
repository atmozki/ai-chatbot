import openai # pip install openai
import gradio as gr  # pip install gradio

openai.api_key = "openai.api_key" # Replace with your API key (example: sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx)

messages = [
{"role": "system", "content": "You are an AI chatbot. You can talk to humans about anything."}, # Change the content to get more specific responses from the AI
]

def chatbot(input): 
    if input:
        messages.append({"role": "user", "content": input}) 
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages  # Uses the new GPT-3.5 model (chatgpt-3.5-turbo).
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply}) 
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Chat with AI") # Create textboxs 
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything Me want",
             theme="default").launch(share=True)  # Creates a shareable link.