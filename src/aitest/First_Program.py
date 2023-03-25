import os
import openai



openai.api_key = os.getenv("OPENAI_API_KEY")
x="meat beater"
y = "smash"
#x= input("please enter a subject which you would like to have a tagline written on:")

prompt = f"""You are a tagline writer for a media company. 
You're give the following subject:{x}. Write four taglines about this subject, formatted as a JSON list object."""

print(prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt,
  temperature=.7,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)

# print the first completion from the API
r_text = response["choices"][0]["text"]

import json
a = json.loads(r_text)

lstr = ", ".join(f"'{e}'" for e in a)
prompt2= f"""You are a tagline writer for a media company. 
You're given the following taglines: {lstr}. Which of these is most similar to the subject '{x}'?"""
print(prompt2)

response1 = openai.Completion.create(
  model="text-davinci-003",
  prompt= prompt2,
  temperature=.7,
  max_tokens=300,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.0,
)
print(":", response1["choices"][0]["text"])