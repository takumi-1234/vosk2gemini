import google.generativeai as genai
import os
import sys

args = sys.argv

os.environ["API_KEY"] = 'AIzaSyA-U5pwi5Zu9p4qyk6hwBI3mzYsIA9WzIw'
genai.configure(api_key=os.environ["API_KEY"])

gemini_pro = genai.GenerativeModel("gemini-pro")

def chat():
    prompt = input("send me a prompt : ") 
    while(prompt != "stop"):
        response = gemini_pro.generate_content(prompt)
        print(response.text)  
        prompt = input("send me a prompt : ")     

chat()