from talk import chat
from emotion import emotion_2

def create_single_text_message(message):
    if message == '今日はどうでしたか':
        message = emotion_2.emotionAnalyzer()
        test_message = [
                {
                    'type': 'text',
                    'text': message
                }
            ]

    else :
        test_message = [
                    {
                        'type': 'text',
                        'text': chat.generate_text(message)
                    }
                ]
    return test_message