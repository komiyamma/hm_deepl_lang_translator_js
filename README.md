# HmDeepLLangTranslator

![release latest](https://img.shields.io/github/v/release/komiyamma/hm_deepl_lang_translator_js?label=HmDeepLLangTranslator&color=6479ff)
[![MIT](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)
![Hidemaru 9.35](https://img.shields.io/badge/Hidemaru-v9.35-6479ff.svg)

秀丸エディタ上で選択したテキスト（または非選択時は全テキスト）を、DeepL APIを利用して翻訳するマクロです。

## 概要

このマクロは、[DeepL APIのFreeプラン](https://www.deepl.com/ja/pro-api?cta=header-apis-free)（またはProプラン）を利用して、秀丸エディタから直接テキストの翻訳を実行します。

-   日本語から英語へ (`HmDeepLLangTranslator2En.mac`)
-   英語から日本語へ (`HmDeepLLangTranslator2Ja.mac`)

といったマクロを実行することで、指定された言語への翻訳が可能です。
翻訳処理は非同期で行われるため、翻訳中もエディタの操作を妨げません。

## 動作環境

-   秀丸エディタ v9.35 以降
-   秀丸エディタの `jsmode` のため、WebView2ランタイム
-   DeepL APIのアカウントと認証キー
-   以下のいずれかの実行環境
    -   **Python** と `deepl` ライブラリ
    -   **Node.js** と `deepl-node` ライブラリ

## インストール

1.  このリポジトリのファイル一式をダウンロードし、秀丸エディタのマクロ用フォルダなど、任意の場所に配置します。
2.  使用したい実行環境に応じて、以下のコマンドをターミナル（コマンドプロンプトなど）で実行し、必要なライブラリをインストールします。

    -   **Pythonの場合**
        ```cmd
        python -m pip install deepl
        ```

    -   **Node.jsの場合**
        `HmDeepLLangTranslator_nodejs.js` があるフォルダで、以下のコマンドを実行してください。
        ```cmd
        npm install deepl-node
        ```

## 設定

### 1. 実行エンジンの選択

まず、`HmDeepLLangTranslator.mac` ファイルをテキストエディタで開き、使用する実行エンジン（`node` または `python`）を選択します。

```javascript
// HmDeepLLangTranslator.mac の冒頭部分
js {

let command = "node"; // ← ここを "node" または "python" に書き換える

// ...
```

### 2. DeepL API 認証キーの設定

次に、DeepLの認証キーを設定します。設定方法は2通りあります。

#### 方法A: 環境変数の設定（推奨）

PCの環境変数として `DEEPL_SCRIPT_TRANSLATION` という名前の変数を追加し、その値としてご自身のDeepL認証キーを設定します。

この方法は、マクロファイル内に直接キーを書き込む必要がないため、安全です。

#### 方法B: マクロファイルへの直接書き込み

環境変数の設定が難しい場合、`HmDeepLLangTranslator.mac` を直接編集して認証キーを書き込むことも可能です。

```javascript
// HmDeepLLangTranslator.mac

// ご自身で環境変数「DEEPL_SCRIPT_TRANSLATION」にDeepLのAPIのAUTH_KEYを設定してください。
let auth_key = getenv("DEEPL_SCRIPT_TRANSLATION");

// 環境変数への登録が面倒、あるいは避けたいという場合は、下部へと直接認証キーの文字列を貼り付けること。
// ↓下の行のコメントを解除し、ご自身のキーに書き換えてください
// let auth_key = "********-****-****-****-************:**";
```

## 使い方

1.  秀丸エディタの `マクロ` > `マクロ登録` から、`HmDeepLLangTranslator2En.mac` や `HmDeepLLangTranslator2Ja.mac` などを登録します。
2.  お好みで、キーボードのショートカットキーに割り当てると便利です。
3.  秀丸エディタで翻訳したいテキストを選択し（または何も選択せず）、登録したマクロを実行します。
4.  翻訳されたテキストが、カーソル位置に挿入されます。

## 各ファイルの説明

-   `HmDeepLLangTranslator.mac`: 翻訳処理の本体となるマクロ。APIキーの設定や実行エンジンの選択はこのファイルで行います。
-   `HmDeepLLangTranslator2En.mac`: 日本語→英語の翻訳を実行するための呼び出しマクロ。
-   `HmDeepLLangTranslator2Ja.mac`: 英語→日本語の翻訳を実行するための呼び出しマクロ。
-   `HmDeepLLangTranslator_python.py`: Pythonで翻訳処理を行うスクリプト。
-   `HmDeepLLangTranslator_nodejs.js`: Node.jsで翻訳処理を行うスクリプト。
