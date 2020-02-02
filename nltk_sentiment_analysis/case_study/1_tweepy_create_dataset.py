import re
import time
import traceback

import tweepy as tweepy


def read_tokens(filepath):
    with open(filepath, "r") as token_file:
        tokens = token_file.readlines()
        return tokens[0].strip(), tokens[1].strip(), tokens[2].strip(), tokens[3].strip()


def handle_auth(source):
    if source == "twitter":
        api_key, api_sec_key, acc_tok, acc_tok_sec = read_tokens("tokens.txt")
        auth = tweepy.OAuthHandler(api_key, api_sec_key)
        auth.set_access_token(acc_tok, acc_tok_sec)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            traceback.print_exc()
            print("Error during authentication")

    else:
        raise NotImplementedError("{} is not implemented yet".format(source))
    return api


def get_full_text(status):
    tweet_text = ""
    try:
        if not status.entities.get("media", []) and not status.entities.get("urls", []):
            if not hasattr(status, "retweeted_status"):
                tweet_text = status.full_text
    except Exception:
        pass

    if len(tweet_text.split()) > 5:
        return tweet_text

    return ""


if __name__ == "__main__":
    for handle, airline_name in [
        ("@Delta", "delta"),
        ("@AmericanAir", "americanair"),
        ("@united", "united"),
        ("@SouthwestAir", "southwestair")
    ]:
        with open("case_study_dataset_{}.csv".format(airline_name), "w") as file_handle:
            file_handle.write("tweet_text\n")
            api = handle_auth("twitter")
            tweets = tweepy.Cursor(api.search, q=handle, count=100, tweet_mode="extended").items()
            count = 0
            loop_count = 0
            for tweet in tweets:
                loop_count = loop_count + 1
                line = get_full_text(tweet)
                if line and line.count(handle) == 1:
                    line = re.sub(r"[\n\r\t]", " ", line)
                    line = re.sub(r"\s+", " ", line)
                    line = "{},{}\n".format(line, airline_name)
                    file_handle.write(line)
                    print(line)
                    count = count + 1
                    if count >= 2000:
                        break
                print(count)
                print(loop_count % 100)
            time.sleep(20 * 60)
