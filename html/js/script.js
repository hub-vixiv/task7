// ウィンドウ表示時に言語のoption記述
window.onload = get_lang_option();

// pyからoptionを文字列で受け取る
function get_lang_option(){
  async function run(){
      var option_tags = await eel.make_lang_option()();
      select_lang_src.innerHTML = option_tags;
      select_lang_src.options[0].selected = true;
      select_lang_dest.innerHTML = option_tags;
      select_lang_dest.options[1].selected = true;

  }
  run();
}

// function lang_change(){
//   if (select_lang_src.value == "ja"){
//     select_lang_dest.value = "en";
//   }

// }

function btn_translate_click(){
  // 翻訳元言語と翻訳先言語と翻訳する文をhtmlから取得
  var lang_src = select_lang_src.value;
  var lang_dest = select_lang_dest.value;
  var before_text = before_textarea.value;
  // after_textarea.value = '';
  console.log(lang_src,lang_dest,before_text)
  // 上記をpyに渡して、翻訳
  async function run(){
    var translated = await eel.do_translate(lang_src,lang_dest,before_text)();
    after_textarea.value = translated;
  }
  run();
}