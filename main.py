import sys

from modules.action.follow import FollowAction
from config import SEARCH_PROFILE_KEYWORD, SEARCH_TWEET_KEYWORD

if __name__ == "__main__":

    functions = {
        "profile_follow" : {
            "description": "プロフィールを検索してフォロー"
        },
        "tweet_follow" : {
            "description": "ツイートを検索してフォロー"
        }
    }

    try:
        print("==============================================")
        print("exec....")

        args = sys.argv
        if len(args) == 1:
            # 引数がなければ警告
            print("第2引数を指定してください")
            for key in functions.keys():
                print(key + ": " + functions[key]["description"])
            raise Exception

        if args[1] not in functions:
            # 第1引数に一致する関数がなければエラー
            print("引数が正しくありません")
            raise Exception

        # 引数に一致する関数を探して実行
        if args[1] == "profile_follow":
            FollowAction.follow_from_prof_search(SEARCH_PROFILE_KEYWORD)
        elif args[1] == "tweet_follow":
            FollowAction.follow_from_tweet_search(SEARCH_TWEET_KEYWORD)

    finally:
        print("==============================================")
