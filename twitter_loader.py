from searchtweets import ResultStream,gen_request_parameters, load_credentials,collect_results


search_args = load_credentials("twitter.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)

query = gen_request_parameters("#ENZC", results_per_call=100, tweet_fields="id,created_at,text", start_time="2021-02-22", end_time="2021-02-24")

# tweets = collect_results(query, max_tweets=250, result_stream_args=search_args) # change this if you need to

rs = ResultStream(request_parameters=query, max_results=500, max_pages=1, **search_args)

#[print(tweet["text"], end='\n\n') for tweet in tweets[0:10]]

tweets = list(rs.stream())
print(len(tweets))
print(tweets[0])
#for tweet in rs.stream():
    #print(tweet.id)
    #print(tweet.created_at_datetime)
    #print(tweet.all_text)
