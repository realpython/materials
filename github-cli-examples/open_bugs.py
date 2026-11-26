import json
import subprocess
import sys

repo = sys.argv[1] if len(sys.argv) > 1 else "cli/cli"
command = ["gh", "issue", "list", "-R", repo, "--label", "bug", "--limit", "5"]

result = subprocess.run(
    [*command, "--json", "number,title,url"],
    stdout=subprocess.PIPE,
    text=True,
    check=True,
)

for issue in json.loads(result.stdout):
    print(f"#{issue['number']}: {issue['title']}")
    print(f"    {issue['url']}")
