import eel
import desktop
import gtranslate

app_name="html"
end_point="index.html"
size=(800,500)


# 言語選択用のドロップダウンリストの
# optionタグを返す
@eel.expose
def make_lang_option():
    tags = gtranslate.make_lang_option()
    return tags

# 翻訳して返す
@eel.expose
def do_translate(lang_src, lang_dest, before_text):
    translated = gtranslate.do_translate(lang_src, lang_dest, before_text)
    return translated

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)