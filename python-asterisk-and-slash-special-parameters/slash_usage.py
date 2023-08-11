def slash_usage(position_only, /, either):
    print(position_only, either)


slash_usage("Frank", either="Dean")
slash_usage("Frank", "Dean")

# This would be invalid:
# slash_usage(position_only="Frank", either="Dean")
# slash_usage(position_only="Frank", "Dean")
