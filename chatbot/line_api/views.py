from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

from utils import message_creater
from talk import chat
from line_api.line_message import LineMessage
from .models import Message

@csrf_exempt
def index(request):
    if request.method == 'POST':
        request = json.loads(request.body.decode('utf-8'))
        data = request['events'][0]
        message = data['message']
        reply_token = data['replyToken']
        Message(content = message['text']).save()
        # line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        # line_message = LineMessage(chat.generate_text(message['text']))
        line_message = LineMessage(message_creater.create_single_text_message(message['text']))
        line_message.reply(reply_token)
        return HttpResponse("ok")

