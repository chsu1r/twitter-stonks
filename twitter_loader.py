from searchtweets import ResultStream, gen_request_parameters, load_credentials,collect_results

search_args = load_credentials("./twitter_keys.yaml",
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)

query = gen_request_parameters("#ENZC", results_per_call=250)

tweets = collect_results(query,
                         max_tweets=250,
                         result_stream_args=search_args) # change this if you need to

[print(tweet.text, end='\n\n') for tweet in tweets[0:10]]