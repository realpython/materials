def track_calls():
    track_calls.__dict__["calls"] = track_calls.__dict__.get("calls", 0) + 1
    print(f"Calls: {track_calls.calls}")


track_calls()
track_calls()
track_calls()

print(track_calls.calls)
