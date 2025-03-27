# HmDeepLLangTranslator_python.py v1.3.0.1

import sys
import io
import deepl

# 標準入出力のエンコーディングをUTF-8に設定
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# コマンドライン引数からパラメータを取得。存在しない場合はデフォルト値を設定
auth_key = sys.argv[1] if len(sys.argv) > 1 else ''  # 認証キー
source_lang = sys.argv[2] if len(sys.argv) > 2 else ''  # 翻訳元の言語
target_lang = sys.argv[3] if len(sys.argv) > 3 else ''  # 翻訳先の言語

if not auth_key:
    print('エラー: 認証キーが指定されていません。', file=sys.stderr, end="")
    sys.exit(1)  # エラー終了
if not source_lang:
    print('エラー: 翻訳元の言語が指定されていません。', file=sys.stderr, end="") 
    sys.exit(1)  # エラー終了
if not target_lang:
    print('エラー: 翻訳先の言語が指定されていません。', file=sys.stderr, end="")
    sys.exit(1)  # エラー終了

def translate(text):
    try:
        translator = deepl.Translator(auth_key)
        result = translator.translate_text(text, target_lang=target_lang, source_lang=source_lang)
        print(result.text, end="")
    except Exception as error:  # Include a general exception handler
        print(f'翻訳中にエラーが発生しました: {error}', file=sys.stderr, end="")

def main():
    text = sys.stdin.read()  # stdinからすべての入力を読み込む
    translate(text)

if __name__ == "__main__":
    main()
