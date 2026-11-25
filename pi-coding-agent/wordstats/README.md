# wordstats

A tiny word-frequency script used to try the pi coding agent.

```console
$ python wordstats.py sample.txt
```

The test in `test_wordstats.py` fails until the script lowercases words and
strips punctuation. Run it with `python -m pytest -q`.

## Files

- `AGENTS.md`: project rules that pi reads automatically.
- `ask_pi.py`: runs `pi --mode json` and prints tool calls and the answer.
- `rpc_demo.py`: drives `pi --mode rpc` from Python.
- `.pi/extensions/guard.ts`: blocks `rm` and adds a `count_lines` tool.
- `.pi/skills/changelog/SKILL.md`: a skill.
- `.pi/prompts/review.md`: the `/review` prompt template.

Run pi with `-a` so it trusts the project-local `.pi/` files.
