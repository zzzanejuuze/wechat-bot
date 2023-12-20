from lib import itchat
from lib.itchat.content import TEXT
from gpt import gpt, chat, generate_img


@itchat.msg_register(TEXT)
def print_content(msg):
    print(msg['Text'])


@itchat.msg_register(TEXT)
def reply_msg(msg):
    if msg['Text'] == 'hi':
        itchat.send_msg(msg='hi', toUserName=msg['FromUserName'])


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']: 
    if msg['isAt']:
        nickname = 'AI'
        message = msg['Text']
        message = message.split(nickname)[1].strip()

        msg_prefix = message[0]
        if msg_prefix in ['画']:
            generate_img(message)
            itchat.send_image(fileDir="bot_draw_img.jpg", toUserName=msg['FromUserName'])
        else:
            bot_res = chat(message, maxtokens=4000)
            print(message)
            print(bot_res)
            itchat.send_msg(msg=bot_res, toUserName=msg['FromUserName'])


# 启动微信机器人
itchat.auto_login(enableCmdQR=2,hotReload=True)
itchat.run()
