# Importing package to connecting ollama server.
import ollama

SYSTEM_PROMPT = """
You are a docker expert. You can explain things in 1-2 line max.
You don't overthink, hallucinate or keep reasoning in a loop.
You Reason and Act according to user prompt.

these are the thnings you do:
1/ You tell errors (What went wrong, etc)
2/ You tell about the root cause (What was the cause likely)
3/ You tell about fix or solution in short
"""

while True:
    user_input = input("Enter your message :\n")

    if user_input == "exit":
        break

    response = ollama.chat(
        model="gemma4",
        messages=[{'role' : 'system', 'content' : SYSTEM_PROMPT},{
        "role":"user", 
        "content":user_input
        }]
    )

    print(response['message']['content']) 



