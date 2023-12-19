import gradio as gr
from ia import get_response

PITCH = "Hello, i'm a chatbot."  # TODO: Default message of the chatbot

with gr.Blocks(css="index.css", title="IA Chatbot", theme="monochrome") as interface:  # TODO: Change the website title

    gr.Markdown(value="Chatbot", elem_classes="chatbot_header")  # TODO: You can change the title of the chatbot

    with gr.Group():
        chatbot = gr.Chatbot(value=[[None, PITCH]], show_share_button=True, show_copy_button=True,
                             avatar_images=("icons/human.png", "icons/robot.png"))

        with gr.Row():
            msg = gr.Textbox(show_label=False, placeholder="Type a message...", autofocus=True,
                             scale=7)
            submit_btn = gr.Button(value="Submit", scale=1)  # TODO: You can change the text of the button

    with gr.Row():
        retry_btn = gr.Button(value="Retry")  # TODO: You can change the text of the button
        undo_btn = gr.Button(value="Undo")  # TODO: You can change the text of the button
        clear_btn = gr.Button(value="Clear")  # TODO: You can change the text of the button


        def respond(message, chat_history):
            if message == "":
                return "", chat_history

            chat_history.append((message, get_response(message)))
            return "", chat_history

        def retry(chat_history):
            if len(chat_history) == 1:
                return [[None, PITCH]]

            message = chat_history[-1][0]
            chat_history.pop()

            chat_history.append((message, get_response(message)))
            return chat_history

        def undo(chat_history):
            if len(chat_history) == 1:
                return "", chat_history

            return chat_history[-1][0], chat_history[:-1]

        def clear():
            return [[None, PITCH]]


        msg.submit(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot], show_progress="minimal")
        submit_btn.click(fn=respond, inputs=[msg, chatbot], outputs=[msg, chatbot], show_progress="minimal")

        retry_btn.click(fn=retry, inputs=chatbot, outputs=chatbot, show_progress="minimal")
        undo_btn.click(fn=undo, inputs=chatbot, outputs=[msg, chatbot], show_progress="minimal")
        clear_btn.click(fn=clear, outputs=chatbot, show_progress="minimal")

if __name__ == "__main__":
    interface.launch()
