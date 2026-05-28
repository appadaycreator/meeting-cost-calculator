# 会議コスト計算ツール【無料】簡単・無料計算 - 技術仕様書

## 概要

**サービス名**: Meeting Cost Calculator
**バージョン**: 1.0.0
**更新日**: 2026-05-27
**URL**: https://appadaycreator.com/meeting-cost-calculator/

参加者数・平均時給・時間から会議の機会コストをリアルタイム計算。登録不要・完全無料でご利用いただけます。

## データ管理

- **ストレージ**: ブラウザ localStorage（外部API通信なし）
- **永続化**: ページ読み込み時に自動復元
- **クリア**: ブラウザのサイトデータ削除で初期化

## 技術スタック

- HTML5 / CSS3 / Vanilla JavaScript
- PWA対応（manifest.json / Service Worker）
- レスポンシブデザイン（モバイルファースト）

## 使い方

1. 入力フォームの各項目を確認する
2. 必要な数値・条件をすべて入力する
3. 計算ボタンをクリックして結果を取得する
4. 計算結果と詳細な内訳を確認する
5. 条件を変えて複数パターンを比較する

## よくある質問（FAQ）

**Q: 会議コスト計算ツールは無料で使えますか？**

はい、完全無料・登録不要でご利用いただけます。

**Q: 計算結果は正確ですか？**

参考値としてご活用ください。重要な判断の際は専門家・公式機関にご確認ください。

**Q: 何回でも計算できますか？**

はい、回数制限なく何度でもご利用いただけます。条件を変えて比較にお使いください。

**Q: 入力したデータはどこかに保存されますか？**

いいえ。すべての計算はブラウザ内で処理され、データのサーバー送信は行いません。

**Q: スマートフォンで利用できますか？**

はい、PC・スマートフォン・タブレットすべてに対応しています。


## 関連サービス

- [TaskFlow Timer](https://appadaycreator.github.io/taskflow-timer/)
- [OKRトラッカー](https://appadaycreator.github.io/okr-tracker/)
- [Saas Tool Advisor](https://appadaycreator.github.io/saas-tool-advisor/)

## テスト

| ファイル | フレームワーク | 概要 |
|---------|--------------|------|
| `tests/e2e/` | Playwright | 本番URL対象E2E（Jest対象外） |

## デプロイ

GitHub Pages（mainブランチ push → 自動デプロイ）

## ライセンス

MIT License
