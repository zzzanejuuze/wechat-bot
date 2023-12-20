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


# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
#def group_id(name):
#    df = itchat.search_chatrooms(name=name)
#    return df[0]['UserName']


@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']: 
    if msg['isAt']:
        nickname = 'AI'
        message = msg['Text']
        message = message.split(nickname)[1].strip()

        #if ['画', 'draw'] in message:
            # generate image from text
            #generate_img(message)
            #itchat.send_image(fileDir="bot_draw_img.jpg", toUserName=msg['FromUserName'])
         
        bot_res = chat(message, maxtokens=4000)
        print(message)
        print(bot_res)
        itchat.send_msg(msg=bot_res, toUserName=msg['FromUserName'])



# 启动微信机器人
itchat.auto_login(enableCmdQR=2,hotReload=True)
#member_lst = itchat.get_friends()
#itchat.send_msg(msg='hi', toUserName='@b12b03e2ad3dbf97d6ad3af4deefc94d7adc3f1b82423a8dd835f47208b44763')

itchat.run()
