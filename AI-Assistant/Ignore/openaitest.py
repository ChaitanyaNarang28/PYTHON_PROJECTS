# # # from openai import OpenAI
# # # import os
# # # client = OpenAI()

# # # response = client.chat.completions.create(
# # #   model="gpt-3.5-turbo",
# # #   messages=[
# # #     {
# # #       "role": "system", 
# # #       "content": [
# # #         {
# # #           "type": "text",
# # #           "text": "write an email to boss  for resignation"
# # #         }
# # #       ]
# # #     }
# # #   ],
# # #   temperature=1,
# # #   max_tokens=256,
# # #   top_p=1,
# # #   frequency_penalty=0,
# # #   presence_penalty=0
# # # )

# # import openai

# # openai.api_key = "sk-proj-0LR1E9IHs35Ne12NTnsET3BlbkFJKlhu893xEO8Tlkac9Mx2"

# # response = openai.ChatCompletion.create(
# #   model="gpt-3.5-turbo",
# #   messages=[
# #     {
# #       "role": "system", 
# #       "content": "write an email to boss for resignation"
# #     }
# #   ],
# #   temperature=1,
# #   max_tokens=256,
# #   top_p=1,
# #   frequency_penalty=0,
# #   presence_penalty=0
# # )

# # # print(response.choices[0].message['content'])


# # print(response)

# import openai
# import os

# # Set your API key
# openai.api_key = os.getenv("sk-proj-0LR1E9IHs35Ne12NTnsET3BlbkFJKlhu893xEO8Tlkac9Mx2")

# # Making a request with reduced max_tokens
# response = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "write an email to boss for resignation"}
#   ],
#   temperature=0.7,  # Lowering temperature might slightly reduce token usage
#   max_tokens=100,   # Reducing the max tokens to consume fewer resources
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# )

# print(response.choices[0].message['content'])


import openai
import os

# Directly setting the API key
openai.api_key = "sk-proj-L3tZ8RelViNXRepy54waT3BlbkFJOLLT84pcsRRS4Pz2kGTU"

# Making a request to the API
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "write an email to boss for resignation"}
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response.choices[0].message['content'])



