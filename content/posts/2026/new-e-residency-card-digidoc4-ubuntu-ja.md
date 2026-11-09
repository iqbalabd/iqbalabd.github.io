Title: Ubuntu 24.04で新しいe-ResidencyカードがDigiDoc4に認識されない？OpenSCを確認してみよう
Slug: new-e-residency-card-not-detected-digidoc4-ubuntu
Lang: ja
Date: 2026-11-09 15:30
Modified: 2026-11-09 15:30
Tags: エストニア; e-residency; ubuntu; digidoc4; opensc; linux;
Status: published
Authors: Iqbal Abdullah
Summary: 新しいe-Residencyカードが認識されない原因は、Ubuntu ProのESMが優先する古いOpenSCだった。確認方法と解決方法をまとめた。

エストニアのe-Residency（電子居住権）の交換カードが届いた。早速UbuntuのDigiDoc4で使おうとしたが、カードが認識されない。古いカードは問題なく動くし、DigiDoc4も最新版だ。調べてみると、原因はカードでもDigiDoc4でもなかった。Ubuntu ProのESM（Expanded Security Maintenance）リポジトリが、新しいチップに対応していない古い`opensc`パッケージを優先していた。

Ubuntu Proを有効にしていて、2025年11月17日以降に発行されたカードを使っている人は、この問題にハマるかもしれない。確認方法と解決方法をまとめておく。

## 背景

エストニアは2025年11月17日から、新しい世代のIDカードの発行を始めた。e-ResidencyのデジタルIDカードもその対象だ。チップがIDEMIA CosmoからThales MultiApp V5.1に変わり、新しいカードを使うにはID-software 25.10以降が必要になった（[id.ee](https://www.id.ee/en/article/id-card-generations-supported-in-different-versions-of-the-id-software/)）。

また、2021年12月10日から2023年8月16日までに発行されたe-Residencyカードの証明書は、2026年12月9日に失効になる。対象は番号UA0051053からUA0076261までのカードだ（[エストニア警察・国境警備庁](https://www.politsei.ee/en/instructions/e-resident-s-digital-id/cards-issued-until-august-2023)）。今まさにカードを交換している人は多いはずで、交換後に届くのは新しいThalesカードになる。

## 問題

新しいカードを挿しても、DigiDoc4に何も表示されない。「My eID」の画面も空のままだ。古いカードを挿せば普通に読み込める。カードリーダーのLEDは点滅しているし、`lsusb`でもリーダーはちゃんと見えている。

## 動作環境

- Ubuntu 24.04.5 LTS（noble）、カーネル 7.0.0-42-generic
- ID-software 26.7.0（Ubuntu版）、DigiDoc4 4.11.0
- カードリーダー ACS ACR38U-CCID
- Ubuntu Pro（ESM Apps有効）

## 診断

DigiDoc4には診断画面がある。まず画面右上の「Settings」を開く。

![DigiDoc4のメイン画面。右上の「Settings」を赤枠で示している]({static}/images/estonia/digidoc4-settings.webp)

次に、左のメニューから「Diagnostics」を選ぶ。確認する場所は2つある。`Libraries:`の欄にある`opensc`の行と、下にスクロールした先の`Smart Card readers:`の欄だ。

![DigiDoc4の診断画面。左のメニューの「Diagnostics」と、opensc 0.27.1-0RIA3の行を赤枠で示している]({static}/images/estonia/digidoc4-diagnostics.webp)

この画像は解決後に撮ったので、`opensc`は0.27.1-0RIA3と表示されている。解決前の表示はこれだった。

```
opensc (0.25.0~rc1-1ubuntu0.2+esm1)
```

新しいカードを挿した状態での`Smart Card readers:`はこうなる。

```
Smart Card readers:
ACS ACR 38U-CCID 00 00 max APDU size 65536
Reader state: CHANGED, PRESENT
ATR - 3BFF9600008031FE438031B85365494464B085051012233F1D
AID_IDEMIA: 6a82 (Not found)
AID_THALES: 9000 (OK)
ID - XXXXXXXXXXX
```

`AID_THALES: 9000 (OK)`とあるので、カード上のThalesアプレットは応答している。つまり、pcscdとカードリーダーはカードを認識できている。DigiDoc4もThales対応のバージョンだ。となると、問題はその間にある層にあるはずだ。

Linuxでは、DigiDoc4はOpenSC（PKCS#11）経由でカードにアクセスする。Thalesカードへの対応は、ID-software 25.10でRIA（エストニア情報システム庁）のOpenSCに追加された（[リリースノート](https://www.id.ee/en/article/id-software-versions-info-release-notes/)）。私の環境に入っていたのは、2024年初頭のUbuntu版OpenSCにESMのパッチを当てたもの。Thalesカードができる前の世代のOpenSCだった。

## 原因

`apt policy opensc`で確認すると、理由が分かった。

```
$ apt policy opensc
opensc:
  Installed: 0.25.0~rc1-1ubuntu0.2+esm1
  Candidate: 0.25.0~rc1-1ubuntu0.2+esm1
  Version table:
     0.27.1-0RIA3 500
        500 https://installer.id.ee/media/ubuntu noble/main amd64 Packages
 *** 0.25.0~rc1-1ubuntu0.2+esm1 510
        510 https://esm.ubuntu.com/apps/ubuntu noble-apps-security/main amd64 Packages
```

[RIAのリポジトリ](https://www.id.ee/en/article/install-id-software/)には`opensc 0.27.1-0RIA3`がある。しかし、Ubuntu ProのESM Appsリポジトリのピン優先度は510で、RIAの500より高い。aptはバージョン番号より先に優先度を見る。そのため`apt upgrade`を何度実行しても、古いESM版のままになってしまう。`apt policy opensc-pkcs11`も同じ結果だった。

この問題に当たるのは、Ubuntu Pro（ESM）を有効にしている場合だけのようだ。ESMがなければ両方とも優先度500なので、aptはバージョンの新しいRIA版を選んでくれる。

## 解決策

RIA版のOpenSCを、バージョンを指定してインストールする。

```bash
sudo apt install opensc=0.27.1-0RIA3 opensc-pkcs11=0.27.1-0RIA3
sudo systemctl restart pcscd
```

読む時点でRIAからより新しいパッケージが出ている場合は、`apt policy opensc`に表示されるバージョンに置き換えてほしい。

次に、今後のアップグレードでESM版に戻らないようにピン留めする。

```bash
sudo tee /etc/apt/preferences.d/ria-opensc <<'EOF'
Package: opensc opensc-pkcs11
Pin: origin installer.id.ee
Pin-Priority: 600
EOF
```

DigiDoc4を起動し直せば、新しいカードがちゃんと認識されるはずだ。

## カードが認識されたら

- DigiDoc4の「My eID」でPIN2を変更する。新しいカードは、PIN2を一度変更するまで署名に使えない（[id.ee](https://www.id.ee/en/article/thales-id-card/)）
- 2025年11月17日以降に発行されたカードは、まだ外国のe-serviceの認証に使えない。欧州委員会がエストニアのeIDの仕組みの変更を承認し次第、使えるようになる予定だ（[id.ee](https://www.id.ee/en/article/id-cards-issued-from-17-november-onwards-cannot-be-used-for-e-services-provided-by-foreign-countries/)）
- Thalesカードでは、PUKをDigiDocアプリから変更できない（[id.ee](https://www.id.ee/en/article/thales-id-card/)）

## 原因ではなかったもの

- ID-softwareとDigiDoc4のバージョン（26.7と4.11.0はThalesに対応済み）
- カードリーダー（ACR38Uは動いている）
- pcscd（起動していて、カードも検出している）
- WaylandかX11かの違い

## 確認手順

同じ症状に当たったら、次の順に確認してほしい。

1. `apt policy opensc`を実行する。インストールされているバージョンが`installer.id.ee`のものか？
2. DigiDoc4の「Diagnostics」で、`AID_THALES`が`9000`を返しているか？
3. 1が「いいえ」で2が「はい」なら、RIA版のOpenSCをインストールしてピン留めする
