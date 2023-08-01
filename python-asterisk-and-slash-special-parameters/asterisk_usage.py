def asterisk_usage(either, *, keyword_only):
    print(either, keyword_only)


asterisk_usage(either="Frank", keyword_only="Dean")
asterisk_usage("Frank", keyword_only="Dean")

# This would be invalid:
# asterisk_usage("Frank", "Dean")
