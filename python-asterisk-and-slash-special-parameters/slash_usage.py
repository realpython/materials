def slash_usage(position_only, /, keyword_only):
    print(position_only, keyword_only)


slash_usage("Frank", keyword_only="Dean")

slash_usage(position_only="Frank", keyword_only="Dean")

# slash_usage(position_only="Frank", "Dean")
