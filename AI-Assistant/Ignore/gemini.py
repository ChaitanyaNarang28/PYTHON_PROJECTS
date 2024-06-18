"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyB8zuQL1oUKyhTMiY7cKzlMYWG446-mkcw")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  safety_settings=safety_settings,
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "wite an essay on ai\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "## The Rise of the Machines: Exploring the Power and Potential of Artificial Intelligence\n\nArtificial Intelligence (AI) is no longer a futuristic fantasy relegated to science fiction. It has permeated our lives, from the personalized recommendations on our social media feeds to the self-driving cars slowly taking to our roads. This essay will explore the fascinating world of AI, examining its current capabilities, its potential for advancement, and the ethical considerations that accompany its rapid growth.\n\nAt its core, AI encompasses the creation of machines that can perform tasks typically requiring human intelligence, such as learning, problem-solving, and decision-making. This is achieved through algorithms and data sets that train AI systems to recognize patterns, make predictions, and adapt to new information. The field can be broadly categorized into two main types: Narrow AI, designed for specific tasks like playing chess or translating languages, and General AI, which",
      ],
    },
  ]
)

response = chat_session.send_message("essay on ai")

print(response)
# print(response.text)
# # print(chat_session.history)



'''
response:
GenerateContentResponse(
    done=True,
    iterator=None,
    result=glm.GenerateContentResponse({
      "candidates": [
        {
          "content": {
            "parts": [
              {
                "text": "## The Rise of the Machines: Exploring the Power and Potential of Artificial Intelligence\n\nArtificial Intelligence (AI) is no longer a futuristic fantasy relegated to science fiction. It has permeated our lives, from the personalized recommendations on our social media feeds to the self-driving cars slowly taking to our roads. This essay will explore the fascinating world of AI, examining its current capabilities, its potential for advancement, and the ethical considerations that accompany its rapid growth.\n\nAt its core, AI encompasses the creation of machines that can perform tasks typically requiring human intelligence, such as learning, problem-solving, and decision-making. This is achieved through algorithms and data sets that train AI systems to recognize patterns, make predictions, and adapt to new information. The field can be broadly categorized into two main types: Narrow AI, designed for specific tasks like playing chess or translating languages, and General AI, which aims to create systems with human-level intelligence capable of performing any intellectual task.\n\nThe rise of AI is largely attributed to advancements in computing power, the availability of vast amounts of data, and breakthroughs in machine learning algorithms. This combination has enabled AI to achieve remarkable feats in various domains. In healthcare, AI-powered systems can analyze medical images for early disease detection, personalize treatment plans, and accelerate drug discovery. In finance, AI algorithms are used for fraud detection, risk assessment, and automated trading. In manufacturing, AI systems optimize production processes, improve quality control, and predict equipment failures.\n\nHowever, the rapid advancement of AI also raises critical ethical concerns. The potential for bias in AI algorithms, based on the data they are trained on, raises questions about fairness and equity. The automation of jobs, particularly those requiring repetitive tasks, presents challenges for the future of work and societal well-being. Furthermore, the development of increasingly sophisticated AI systems raises concerns about the potential for misuse, including the development of autonomous weapons systems and the manipulation of information.\n\nDespite these challenges, AI holds immense promise for improving our lives in numerous ways. It has the potential to revolutionize industries, address complex global problems like climate change, and even enhance our understanding of the universe. The key to realizing this potential lies in responsible development and ethical deployment of AI. This requires collaboration between scientists, policymakers, and the public to ensure that AI benefits all of humanity.\n\nIn conclusion, AI is a transformative technology with profound implications for our future. Understanding its capabilities, potential, and ethical challenges is crucial for navigating its rapid development and ensuring its responsible use. By embracing the opportunities while mitigating the risks, we can harness the power of AI to create a better world for all. \n"
              }
            ],
            "role": "model"
          },
          "finish_reason": 1,
          "index": 0,
          "safety_ratings": [
            {
              "category": 9,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 8,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 7,
              "probability": 1,
              "blocked": false
            },
            {
              "category": 10,
              "probability": 1,
              "blocked": false
            }
          ],
          "citation_metadata": {
            "citation_sources": [
              {
                "start_index": 558,
                "end_index": 681,
                "uri": "https://www.leewayhertz.com/ai-use-cases-in-education/",
                "license_": ""
              },
              {
                "start_index": 1132,
                "end_index": 1254,
                "uri": "https://www.pyromedia.co.za/tag/visual-effects/",    
                "license_": ""
              }
            ]
          },
          "token_count": 0,
          "grounding_attributions": []
        }
      ]
    }),
)
'''