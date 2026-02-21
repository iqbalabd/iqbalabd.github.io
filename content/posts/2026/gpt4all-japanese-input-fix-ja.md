Title: 日本語入力（Fcitx5/Mozc）の問題を解決する：GPT4AllをUbuntu 24.04で動作させる方法
Slug: fixing-japanese-input-fcitx-in-gpt4all-on-ubuntu
Lang: ja
Date: 2026-02-21 18:00
Modified: 2026-02-21 18:00
Tags: 日本語入力; ubuntu; ai; ツール;
Status: published
Authors: Iqbal Abdullah
Summary: Ubuntu 24.04 の GPT4All で日本語入力の問題。Qt 6.8 用 fcitx5 プラグインをビルドし配置すれば解決。

私は[Ollama](https://ollama.com)をローカルLLM（大規模言語モデル）に使用していましたが、[GPT4All](https://www.nomic.ai/gpt4all)について読んで試してみたくなりました。もしあなたが私のように日本語で書き込む場合、`fcitx5`とMozcをUbuntu上で利用し、Ctrl+Spaceで入力メソッドの切り替えができないという問題に遭遇するかもしれません。そこで調べてみた方法を以下に示します。

## 問題点

GPT4AllはQtベースのアプリケーションで、Qt 6.8ライブラリをバンドルしていますが、`fcitx5`入力メソッドプラグインが含まれていません。UbuntuのQt（Ubuntu 24.04では6.4）で構築されたシステムの`fcitx5`プラグインをコピーしようとしても、シンボル不一致が発生します（当然ですね）。単に `QT_IM_MODULE=fcitx` を設定しただけでは、互換性のあるプラグインがないため効果がないです。

## 解決策

Qt 6.8 SDKと対応する`fcitx5`入力コンテキストプラグインをソースから構築し、それをGPT4Allのプラグインディレクトリに配置します。

## 動作環境

- Ubuntu 24.04 LTS
- `fcitx5` + Mozc
- GPT4All（スタンドアロンインストーラーは[こちら](https://www.nomic.ai/gpt4all)）

## ステップバイステップ

### 1. ビルド依存パッケージのインストール

```bash
sudo apt install cmake extra-cmake-modules \
  libfcitx5core-dev libfcitx5config-dev libfcitx5utils-dev \
  libxkbcommon-dev libwayland-dev wayland-protocols libvulkan-dev
```

### 2. 対応するQt 6.8 SDKのインストール

GPT4AllはQt 6.8をバンドルしていますが、開発ファイルではなくランタイムライブラリのみです。`aqtinstall`を使用してSDKを取得します。

```bash
python3 -m venv /tmp/aqt-env
/tmp/aqt-env/bin/pip install aqtinstall
/tmp/aqt-env/bin/aqt install-qt linux desktop 6.8.0 -O /tmp/qt6.8
```

### 3. fcitx5-qtのクローンとビルド

```bash
cd /tmp
git clone https://github.com/fcitx/fcitx5-qt.git
cd fcitx5-qt
mkdir build && cd build

cmake .. \
  -DCMAKE_PREFIX_PATH=/tmp/qt6.8/6.8.0/gcc_64/lib/cmake \
  -DENABLE_QT4=OFF \
  -DENABLE_QT5=OFF \
  -DENABLE_QT6=ON \
  -DENABLE_QT6_WAYLAND_WORKAROUND=OFF \
  -DENABLE_QT6_GUI_WRAPPER=OFF

make -j$(nproc) -C qt6/platforminputcontext
```

ここで、必要なターゲットのみ (`platforminputcontext`) をビルドします。完全なビルドはGUIラッパーコンポーネントをコンパイルしようとすると失敗するし、そもそも不要。

### 4. プラグインのGPT4Allへのコピー

```bash
cp /tmp/fcitx5-qt/build/qt6/platforminputcontext/libfcitx5platforminputcontextplugin.so \
  ~/gpt4all/plugins/platforminputcontexts/
```

GPT4Allを別の場所にインストールしている場合は、目的のパスに変更してください。

### 5. GPT4Allの起動

```bash
QT_IM_MODULE=fcitx ~/gpt4all/bin/chat
```

Ctrl+Spaceで`fcitx5`/Mozcを切り替えられるようになります。これで日本語入力が可能になります。

### 6. パーマネント化

デスクトップショートカットを使用している場合、`~/.local/share/applications/GPT4All.desktop`ファイルを開き、Exec行に以下の更新を行います（ユーザー名を自分のものに変更してください）。

```
Exec=env QT_IM_MODULE=fcitx "/home/YOUR_USERNAME/gpt4all/bin/chat"
```

## プラグインが正しくロードされるか確認

問題が発生した場合は、デバッグ出力で確認します。

```bash
QT_DEBUG_PLUGINS=1 QT_IM_MODULE=fcitx ~/gpt4all/bin/chat 2>&1 | grep -i fcitx
```

出力に`loaded library`が表示されるはず。もし`undefined symbol`エラーが表示された場合、GPT4AllがバンドルしているQtバージョンとSDKで構築したバージョンが一致していない可能性があります。確認には `strings ~/gpt4all/lib/libQt6Core.so.6 | grep "^6\."` を使用し、必要に応じて `aqt` で対応するバージョンをインストールします。

## クリーンアップ

すべてがうまく動作した後は、ビルドアーティファクトを安全に削除できます。

```bash
rm -rf /tmp/qt6.8 /tmp/fcitx5-qt
```

`-dev`パッケージも必要ない場合は削除可能です。

```bash
sudo apt remove extra-cmake-modules libfcitx5core-dev libfcitx5config-dev libfcitx5utils-dev
```

## 注意

- この手法は、Qtをバンドルしているアプリケーションで`fcitx5`プラグインが欠けている場合に使えるはず。
- GPT4Allの更新によりQtのバージョンが変更された場合、新しいバージョンと対応するように再構築する必要があるかも。
- この方法はUbuntu 24.04でカーネル6.17、GPT4AllがQt 6.8をバンドルし、`fcitx5` 5.1.7にMozcを使用している環境でテストしています。
