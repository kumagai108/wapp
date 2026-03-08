# クレジットカード明細変換ツール

クレジットカードの明細CSVファイルを、確定申告用のフォーマットに変換するGUIツールです。

## ✨ 特徴

- 🖱️ **簡単操作**: GUIでファイルを選択するだけ
- 📅 **年度指定**: 特定の年のデータだけを抽出
- 📁 **複数ファイル対応**: 複数の明細を一度に処理
- 🔄 **自動ソート**: 日付順に自動整列
- 💻 **クロスプラットフォーム**: Windows, Mac, Linux対応

## 🚀 使い方

### Windows ユーザー（Pythonなし）

1. **[Releases](../../releases)** ページから、お使いのWindowsに合ったEXEをダウンロード:
   - **64bit版（推奨）**: `meisai_converter_x64.exe`
     - Windows 10/11 の大半はこちら
   - **32bit版**: `meisai_converter_x86.exe`
     - 古いPCや32bit Windowsの場合

2. ダブルクリックで起動
3. CSVファイルを選択して変換

**それだけです！Pythonのインストールは不要です。**

**Windowsのバージョン確認方法:**
- 設定 → システム → バージョン情報 → "システムの種類" を確認
- "64 ビット" と表示されていれば x64版を選択

### 開発者・Python環境がある方

#### 方法1: uvを使う（推奨）

```bash
# uvをインストール（初回のみ）
# https://github.com/astral-sh/uv

# 実行
uv run meisai_converter_gui.py
```

または起動スクリプトを使用：
```bash
# Windows
run.bat

# Mac/Linux
./run.sh
```

#### 方法2: Pythonを使う

```bash
python meisai_converter_gui.py
```

## 📦 ビルド方法（開発者向け）

### GitHub Actionsで自動ビルド（推奨）

```bash
# バージョンタグを作成してpush
git tag v1.0.0
git push origin v1.0.0
```

GitHub Actionsが自動的に：
- Windows用EXEファイルをビルド
- SHA256ハッシュ値を生成
- Releasesページに公開

### ローカルでビルド（Windows）

```bash
# Python環境が必要
build_gui.bat
```

`dist/meisai_converter.exe` が作成されます。

## 📄 入出力フォーマット

### 入力CSV
- エンコーディング: Shift-JIS
- 日付形式: YYMMDD（例: 260115 = 2026/01/15）

### 出力CSV
- エンコーディング: UTF-8 with BOM（Excel互換）
- カラム: 日付, 利用金額, 返金額, 内容

例：
```csv
日付,利用金額,返金額,内容
2026/1/15,5000,,スーパーマーケット
2026/2/20,12000,,電気店
```

## ⚠️ ウイルス警告について

Windows Defenderなどが警告を出す場合がありますが、これは **偽陽性（False Positive）** です。

**理由:**
- PyInstallerで作成されたEXEは、実行時にファイルを展開する動作をするため
- コード署名証明書（高額）がないため

**安全性の確認:**
- ✅ ソースコードは全て公開されています
- ✅ GitHub Actionsで自動ビルドされています（ビルドログが公開）
- ✅ SHA256ハッシュ値で改ざん検証が可能

実行時に「WindowsによってPCが保護されました」と表示された場合：
1. 「詳細情報」をクリック
2. 「実行」をクリック

## 🛠️ トラブルシューティング

### Q: 文字化けする
**A:** 入力CSVファイルがShift-JISエンコーディングか確認してください

### Q: データが抽出されない
**A:** 対象年が正しく選択されているか確認してください

### Q: Googleドライブでウイルス検出される
**A:** GitHub Releasesから直接ダウンロードすることを推奨します。
または、ZIPファイルに圧縮して送付してください。

詳細: [VIRUS_DETECTION_SOLUTIONS.txt](VIRUS_DETECTION_SOLUTIONS.txt)

### Q: 「互換性がありません」「x86/x64が必要」エラーが出る
**A:** お使いのWindowsと違うアーキテクチャのEXEをダウンロードした可能性があります。
- **64bit Windows**: `meisai_converter_x64.exe` を使用
- **32bit Windows**: `meisai_converter_x86.exe` を使用

**確認方法:**
1. Windowsキー + I で設定を開く
2. システム → バージョン情報
3. "システムの種類" を確認
   - "64 ビット オペレーティング システム" → x64版
   - "32 ビット オペレーティング システム" → x86版

## 📚 ドキュメント

- [QUICKSTART.txt](QUICKSTART.txt) - クイックスタートガイド
- [GIT_COMMANDS.txt](GIT_COMMANDS.txt) - Gitコマンド集
- [GITHUB_ACTIONS_GUIDE.txt](GITHUB_ACTIONS_GUIDE.txt) - GitHub Actionsの使い方
- [DISTRIBUTION_GUIDE.txt](DISTRIBUTION_GUIDE.txt) - 配布方法ガイド
- [VIRUS_DETECTION_SOLUTIONS.txt](VIRUS_DETECTION_SOLUTIONS.txt) - ウイルス誤検知の対策

## 🔧 必要要件

### エンドユーザー
- **Windows**: なし（EXEファイルをダウンロードするだけ）
- **Mac/Linux**: Python 3.7以降 または uv

### 開発者
- Python 3.7以降 または uv
- インターネット接続（依存パッケージのダウンロード用）

## 📝 ライセンス

MIT License

## 🤝 コントリビューション

Pull Requestsを歓迎します！

1. このリポジトリをFork
2. Feature branchを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をCommit (`git commit -m 'Add amazing feature'`)
4. Branchにpush (`git push origin feature/amazing-feature`)
5. Pull Requestを作成

## 📮 サポート

問題が発生した場合は、[Issues](../../issues)で報告してください。
