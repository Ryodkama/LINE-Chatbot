import torch
from transformers import T5Tokenizer, AutoModelForCausalLM

text='こんにちは、今日はいい天気ですねー!最近どうですか'

# tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt-1b")
# model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt-1b")

# if torch.cuda.is_available():
#     model = model.to("cuda")

def generate_text(text):
    tokenizer = T5Tokenizer.from_pretrained("rinna/japanese-gpt2-medium")
    model = AutoModelForCausalLM.from_pretrained("rinna/japanese-gpt2-medium")

    if torch.cuda.is_available():
        model = model.to("cuda")
    token_ids = tokenizer.encode(text[-100:], add_special_tokens=False, return_tensors="pt")
    
    max_length=20
    min_length=20
#     print(len(text))
    if max_length < len(text):
        max_length = len(text)*2
        min_length = len(text)*2
    
    with torch.no_grad():
        output_ids = model.generate(
            token_ids.to(model.device),
            max_length=max_length,
            min_length=10,
            do_sample=True,
            top_k=500,
            top_p=0.95,
            pad_token_id=tokenizer.pad_token_id,
            bos_token_id=tokenizer.bos_token_id,
            eos_token_id=tokenizer.eos_token_id,
            # bad_word_ids=[[tokenizer.unk_token_id]]
        )

    output = tokenizer.decode(output_ids.tolist()[0])
    return output.replace(text[-100:],'').replace('</s>','')


text_list_A=[text]
text_list_B=[]

# count=0
# while count < 5:
#     if count == 0:
# #         text_list_A.append(generate_text(text))
#         print('Aさん: ' + text_list_A[0])
        
#         print('あなた: ', end="")
#         text_list_B.append(input("入力: "))
#     else:
#         text_list_A.append(generate_text(text_list_B[count-1]))
#         print('Aさん: ' + text_list_A[count])
#         print('あなた: ', end="")
#         text_list_B.append(input())
        
#     count=count+1