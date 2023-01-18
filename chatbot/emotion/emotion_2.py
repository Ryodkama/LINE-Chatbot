from mlask import MLAsk
emotion_analyzer = MLAsk()
# print(emotion_analyzer.analyze('こんな朝にはただただ世界が好きでたまらないという気がしない？')["orientation"])
# print(emotion_analyzer.analyze('こんな朝にはただただ世界が好きでたまらないという気がしない？')["intension"])
print(emotion_analyzer.analyze('彼のことは嫌いではない！(;´Д`)'))

def emotionAnalyzer(text):
    emotion= emotion_analyzer.analyze(text)

    if  "orientation" not in emotion or "intension" not in  emotion:
        return 'POSITIVE', 0
    else :
        return emotion["orientation"], emotion["intension"]

print(emotionAnalyzer("しんどいな今日は嫌な日だ"))