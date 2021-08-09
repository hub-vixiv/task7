from googletrans import Translator

# 言語選択用のドロップダウンリストの
# optionタグを返す
def make_lang_option():
    tag_option=""
    with open("langlist.csv", 'r', encoding='utf-8') as f :
        for line in f:
            code_lang = line.strip().split(',')
            tag_option += f'<option value="{code_lang[0]}">{code_lang[1]}</option>'
    return tag_option

def do_translate(lang_src,lang_dest,before_text):
    translator = Translator()
    translated = translator.translate(before_text, src=lang_src , dest=lang_dest)
    return translated.text
