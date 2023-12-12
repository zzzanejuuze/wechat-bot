import openai 
import requests 
import constants

from PIL import Image 
from io import BytesIO

#os.environ["OPENAI_API_KEY"] = constants.APIKEY
openai.api_key = constants.APIKEY

# Text generation
def gpt(PROMPT, max_tokens=500, outputs=1):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=PROMPT,
        max_tokens=max_tokens,
        # number of outputs generated in one call
        n=outputs          
    )
    res = response['choices'][0]['text'].strip()
    return res


# Chat
def chat(message, maxtokens=50, outputs=1):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        max_tokens=maxtokens,
        n=outputs
    )
    res = response.choices[0].message.content
    return res


# Generate image
def generate_img(text):
    res = openai.Image.create(
        prompt=text,
        n=1,
        size="256x256"
    )
    url = res["data"][0]["url"]
    response = requests.get(url, stream=True)
    with open("bot_draw_img.jpg", "wb") as f:
        f.write(response.content)

    #return url

#text = "draw batman in red and blue color"
#generate_img(text)

#PROMPT = '帮我写一段简单的离职申请邮件，离职原因是家里有点事需要处理，离职日期是1月2号'
#res = gpt(PROMPT, max_tokens=2000)
#print(res)



