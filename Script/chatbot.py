import pathlib
import textwrap
import time


import google.generativeai as genai
import google.ai.generativelanguage as glm



genai.configure(api_key='AIzaSyAVAGaFOLUoOIjMUZcNf63DDR2zE2jOEwM')

title = ["The world is a book and those who do not travel read only one page",
         "The only way to do great work is to love what you do",
         "The only thing we have to fear is fear itself",
         "The only true wisdom is in knowing you know nothing",
         "The only thing necessary for the triumph of evil",
         "Death is not the greatest loss in life. The greatest loss is what dies inside us while we live",
         "The only thing we have to fear is fear itself",
         "The only true wisdom is in knowing you know nothing",
         ]


def SearchByTitle(titles: str):
      for i in range(len(title)):
         if titles == title[i]:
               return i
      return "Not Found"
    
model = genai.GenerativeModel(model_name= "gemini-pro" , tools = [SearchByTitle])
chat = model.start_chat(enable_automatic_function_calling=True)


while(True):
   x = input("Ask me anything (Type 'exit' to Exit Program and 'history' to show history) : ")

   if(x == "exit"):
      break
   if(x == "history"):
      for content in chat.history:
         part = content.parts[0]
         print(content.role, "->", type(part).to_dict(part))
         print('-'*80)
      continue
   response = chat.send_message(x)

   print(response.text)
