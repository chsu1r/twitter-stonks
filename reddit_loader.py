import praw
import pandas as pd
from datetime import datetime
import sys
import matplotlib.pyplot as plt
import os

def import_reddit_data(keyword):
    client_id = os.environ.get('REDDIT_CLIENT_ID', None)
    client_secret = os.environ.get('REDDIT_CLIENT_SECRET', None)
    if client_id is None or client_secret is None:
        print("Run 'source .env.constants' to set env variables")
        return None

    reddit = praw.Reddit(client_id=client_id,
                        client_secret=client_secret,
                        user_agent='local:stonks-tracker:v1.0 (by /u/u/CreativePerformer971)',
                        )

    assert reddit.read_only

    reddit_popularity_table = []
    reddit_comment_table = []

    subreddit_all = reddit.subreddit('all')

    resp = subreddit_all.search(keyword, limit=10000, sort="relevance")
    for post in resp:
        ts = int(post.created_utc)
        reddit_popularity_table.append([post.id, datetime.utcfromtimestamp(ts), post.score, post.num_comments])
    
        # print("Created UTC: ", datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
        # print("Score: ", post.score)
        # print("Text: ", post.selftext[:120].encode('ascii', 'ignore'))
        # print("Subreddit: ", post.subreddit.display_name)

    df = pd.DataFrame(reddit_popularity_table, columns=['PostID', 'DateTime','Score', 'Comments'])
    df_score_medians = df[['DateTime', 'Score']].resample('D', on='DateTime').median()
    df_comment_medians = df[['DateTime', 'Comments']].resample('D', on='DateTime').median()
    df_counts = df[['DateTime', 'Score']].resample('D', on='DateTime').apply({'Score':'count'})
    return {"median_scores": df_score_medians, "median_comments":df_comment_medians, "post_counts":df_counts}

def chart_reddit_data(reddit_data, keyword, plt_ax, show_plot=False, save_fig=False, start_time='2020-08-15', end_time='2021-02-09', fig_size=(12,4)):
    reddit_data["post_counts"].reset_index().plot.scatter(x='DateTime',y='Score',c='b', figsize=fig_size, ax=plt_ax)
    reddit_data["median_scores"].reset_index().plot.scatter(x='DateTime',y='Score',c='r',ax=plt_ax)
    reddit_data["median_comments"].reset_index().plot.scatter(x='DateTime',y='Comments',c='g',ax=plt_ax)
    plt_ax.set_xlim(pd.Timestamp(start_time), pd.Timestamp(end_time))
    plt_ax.set_ylim(0, 100)
    plt_ax.set_title(keyword + " reddit performance")
    if save_fig:
        plt.savefig("figures/" + keyword + "_reddit.png")
    if show_plot:
        plt.show()
    return plt_ax
