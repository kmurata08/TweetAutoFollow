# TweetAutoFollow
ツイッター自動フォローシステム

## Description
プロフィールまたはツイートから文字列検索が行われ、ユーザが自動的にフォローされる

## Usage
```
プロフィールに対するキーワード検索を行い、対象の文字列が含まれるユーザをフォロー
$ python main.py profile_follow

最新ツイートに対するキーワード検索を行い、対象の文字列が含まれるユーザをフォロー
$ python main.py tweet_follow
```

## Anything Else
main.pyがあるディレクトリに
```
CONSUMER_KEY : コンシューマーキー
CONSUMER_SECRET : コンシューマーシークレット
ACCESS_TOKEN : APIトークン
ACCESS_TOKEN_SECRET : APIトークンシークレット
```
を記述したconfig.pyの作成が必要。

## Author
[@Canon11](https://github.com/Canon11/)
