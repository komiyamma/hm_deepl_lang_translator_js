// HmDeepLLangTranslator_nodejs.js v1.3.0.1

const deepl = require('deepl-node');

// コマンドライン引数からパラメータを取得。存在しない場合はデフォルト値を設定
const authKey = process.argv[2] || ''; // 認証キー
const sourceLang = process.argv[3] || ''; // 翻訳元の言語
const targetLang = process.argv[4] || ''; // 翻訳先の言語

process.stdin.setEncoding('utf8');
process.stderr.setEncoding('utf8');

if (!authKey) {
    process.stderr.write('エラー: 認証キーが指定されていません。');
    process.exit(1); // エラー終了
}
if (!sourceLang) {
    process.stderr.write('エラー: 翻訳元の言語が指定されていません。');
    process.exit(1); // エラー終了
}
if (!targetLang) {
    process.stderr.write('エラー: 翻訳先の言語が指定されていません。');
    process.exit(1); // エラー終了
}

let inputText = '';

process.stdin.on('data', (chunk) => {
    inputText += chunk; // データを受け取るたびに蓄積
});

process.stdin.on('end', () => {
    translate(inputText);
});

process.stdin.on('error', (err) => {
    process.stderr.write('入力データのエラー:', err);
});

async function translate(text) {
    const translator = new deepl.Translator(authKey);
    try {
        const result = await translator.translateText(text, sourceLang, targetLang);
        process.stdout.write(result.text);
    } catch (error) {
        process.stderr.write('翻訳中にエラーが発生しました:' + error);
    }
}