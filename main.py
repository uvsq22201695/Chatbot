import gradio as gr
from ia import get_response

PITCH = "Hello, i'm a chatbot."  # TODO: Default message of the chatbot

with gr.Blocks(css="index.css", title="IA Chatbot", theme="soft") as interface:  # TODO: Change the website title

    gr.Markdown(value="Chatbot", elem_classes="chatbot_header")  # TODO: You can change the title of the chatbot

    chatbot = gr.Chatbot(value=[[None, PITCH]], show_share_button=True, show_copy_button=True,
                         avatar_images=("icons/human.png", "icons/robot.png"))
    msg = gr.Textbox(label="Prompt", autofocus=True, show_copy_button=True)
    clear = gr.Button(value="Clear chat history")  # TODO: You can change the text of the button


    def respond(message, chat_history):
        chat_history.append((message, get_response(message.lower())))
        return "", chat_history


    def clear_chat():
        return [[None, PITCH]]


    msg.submit(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot], show_progress="minimal")
    clear.click(fn=clear_chat, outputs=chatbot, show_progress="minimal")


if __name__ == "__main__":
    interface.launch()
