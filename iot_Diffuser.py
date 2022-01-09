from flask import Flask, request, abort, render_template
from time import sleep
from linebot.models import * 
import pumps,automization,dht22
import os


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)
        
line_bot_api = LineBotApi('29soPW0XVBPhxCoF9WU1Z2w7AxETAqmFrTWrK6KGV8W4O5tqi3bGiCZmuBGzJHL4hkpN+ATZhnDUZC4siaOpD42VXdd92XDsB03k78jcs5OvIKW+gmCW+c84iSYrYArHBb1GjWYntpyA8DZenJI6eAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('30f30854f53f6715311d1eb57389be72')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    # 
    
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if event.message.text == '薰衣草':  #可能可刪
        text = "欲滴入幾滴呢？"
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
   
    #CarouselTemplate內最多只能有3個ButtonTemplate
    elif event.message.text == "精油選單":
        Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://i.epochtimes.com/assets/uploads/2020/03/lavender-essential-oil_1152083036.jpg',
                title='薰衣草',
                text='讓你安穩睡掉早九',
                actions=[
                    PostbackTemplateAction(
                        type="postback",
                        label='1滴',
                        text='1滴薰衣草精油 plz!',
                        data='type=oil_1&ratio=1'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='2滴',
                        text='2滴薰衣草精油 plz!',
                        data='type=oil_1&ratio=2'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='3滴',
                        text='3滴薰衣草精油 plz!',
                        data='type=oil_1&ratio=3'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2020/03/shutterstock_586681421-e1585042555703.jpg',
                title='玫瑰',
                text='漂亮女生one pick!',
                actions=[
                    PostbackTemplateAction(
                        type="postback",
                        label='1滴',
                        text='1滴玫瑰精油 plz!',
                        data='type=oil_2&ratio=1'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='2滴',
                        text='2滴玫瑰精油 plz!',
                        data='type=oil_2&ratio=2'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='3滴',
                        text='3滴玫瑰精油 plz!',
                        data='type=oil_2&ratio=3'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://www.gomaji.com/blog/wp-content/uploads/2020/03/shutterstock_658290292-e1584438902963.jpg',
                title='茶樹',
                text='aka精油界酒精',
                actions=[
                    PostbackTemplateAction(
                        type="postback",
                        label='1滴',
                        text='1滴茶樹精油 plz!',
                        data='type=oil_3&ratio=1'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='2滴',
                        text='2滴茶樹精油 plz!',
                        data='type=oil_3&ratio=2'
                    ),
                    PostbackTemplateAction(
                        type="postback",
                        label='3滴',
                        text='3滴茶樹精油 plz!',
                        data='type=oil_3&ratio=3'
                    )
                ]
            )            
        ]
    )
)
        line_bot_api.reply_message(event.reply_token,Carousel_template)    

    

    elif event.message.text == '目前溫溼度':
        humi = 30
        text = "目前溫度為：20.1度\n濕度為：73.0%"
      
        if(humi<40):
            text += "\n建議開啟擴香機唷～"
 
        elif(humi>70):
            text +="\n建議關閉擴香機囉～"
            
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text))
        

    elif event.message.text == "電源開關":
        Confirm_template = TemplateSendMessage(
        alt_text='Confrim template',
        template=ConfirmTemplate(
            title='請選擇要開啟或關閉',
            text='還沒寫防呆...請謹慎選擇...',
            actions=[                              
                MessageTemplateAction(
                    label='開啟',
                    text='已開始運作',
                ),
                MessageTemplateAction(
                    label='關閉',
                    text='已停止運作'
                )
            ]
        )
    )
        line_bot_api.reply_message(event.reply_token,Confirm_template)

    elif event.message.text == '已開始運作':
        automization.automization_open()
        
    
    elif event.message.text == '已停止運作':
        automization.automization_close()


#處理PostbackTemplateAction的data(回傳回server的值)
@handler.add(PostbackEvent)
def handle_postback(event):
    ts = event.postback.data
    #print(ts)
    #line_bot_api.reply_message(event.reply_token, TextSendMessage(text=ts))    
    
    type = ts[5:10]
    ratio = ts[-1]
    pumps.dripProcess(type,ratio)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text="精油已添加完畢！"))


if __name__ == "__main__":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 5000)))







