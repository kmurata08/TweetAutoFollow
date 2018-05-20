# TweetAutoFollow
自動フォロー系スクリプト

## 概要
プロフィールまたはツイートから文字列検索を行い、ユーザをフォローする

## 使い方
```
プロフィールに対するキーワード検索を行い、対象の文字列が含まれるユーザをフォロー
$ python main.py profile_follow

最新ツイートに対するキーワード検索を行い、対象の文字列が含まれるユーザをフォロー
$ python main.py tweet_follow
```

## その他
main.pyがあるディレクトリに
```
CONSUMER_KEY : コンシューマーキー
CONSUMER_SECRET : コンシューマーシークレット
ACCESS_TOKEN : APIトークン
ACCESS_TOKEN_SECRET : APIトークンシークレット
```
を記述したconfig.pyの作成が必要。
