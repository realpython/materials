"""Summarize a CSV of sales figures, with a handful of optional modes.

This is the baseline version: every import is eager, so running
``--help`` pays for the HTTP server, the async runtime, and the GUI
toolkit even though none of them are used on that code path.
"""

import argparse
import csv

import asyncio
import http.server
import statistics
import tkinter
import xml.etree.ElementTree as ET

import handlers
import handlers.csv_out
import handlers.json_out

def load_rows(path):
    with open(path, newline="", encoding="utf-8") as csv_file:
        return [float(row["amount"]) for row in csv.DictReader(csv_file)]

def summarize(rows):
    return (
        f"count={len(rows)} "
        f"mean={statistics.mean(rows):.2f} "
        f"median={statistics.median(rows):.2f}"
    )

def export_xml(rows):
    root = ET.Element("report")
    for row in rows:
        ET.SubElement(root, "amount").text = f"{row:.2f}"
    return ET.tostring(root, encoding="unicode")

def serve(rows, port):
    body = summarize(rows).encode("utf-8")

    class Handler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(body)

    with http.server.HTTPServer(("", port), Handler) as httpd:
        httpd.serve_forever()

def show_window(rows):
    root = tkinter.Tk()
    tkinter.Label(root, text=summarize(rows)).pack()
    root.mainloop()

async def _fetch(url):
    await asyncio.sleep(0)
    return f"pretending to fetch {url}"

def fetch(url):
    return asyncio.run(_fetch(url))

def build_parser():
    parser = argparse.ArgumentParser(
        prog="report", description="Summarize a CSV of sales figures."
    )
    parser.add_argument("path", nargs="?", default="sales.csv")
    parser.add_argument("--serve", type=int, metavar="PORT")
    parser.add_argument("--gui", action="store_true")
    parser.add_argument("--fetch", metavar="URL")
    parser.add_argument("--export-xml", action="store_true")
    parser.add_argument("--list-formats", action="store_true")
    parser.add_argument(
        "--load-all",
        action="store_true",
        help="touch every optional import, for benchmarking",
    )
    return parser

def main():
    args = build_parser().parse_args()

    if args.list_formats:
        print(handlers.available())
        return

    if args.load_all:
        loaded = [asyncio, http.server, statistics, tkinter, ET]
        print(f"loaded {len(loaded)} optional modules")
        return

    rows = load_rows(args.path)

    if args.fetch:
        print(fetch(args.fetch))
    if args.export_xml:
        print(export_xml(rows))
    if args.gui:
        show_window(rows)
    if args.serve:
        serve(rows, args.serve)

    print(summarize(rows))

if __name__ == "__main__":
    main()
