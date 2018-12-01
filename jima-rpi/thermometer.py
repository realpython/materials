#!/usr/bin/env python3
import argparse
import datetime
import json
import logging
import os
import tkinter as tk
import urllib.request


class Application(tk.Frame):
    def __init__(self):
        self.parse_command_line()
        logger.warning("In init")
        root = tk.Tk()
        root.iconify()
        root.configure(background="black")
        # root.overrideredirect(True)
        root.geometry( "{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        toplevel = tk.Toplevel(root)
        toplevel.configure(background="black")
        toplevel.overrideredirect(1)  # Remove border
        self.frame = tk.Frame(toplevel)
        self.frame.configure(background="black")
        # JHA TODO move this info parser?
        if self.create_close:
            close = tk.Button(
                self.frame, text="Close Window", command=lambda: root.destroy()
            )
            close.pack(fill=tk.BOTH, expand=1)
        big_font = ("Times", "96", "bold")
        med_font = ("Times", "64", "bold")
        self.time = tk.Text(
            self.frame,
            height=1,
            width=10,
            font=big_font,
            bg="black",
            fg="grey",
            borderwidth=0,
            highlightthickness=0,
        )
        self.temp = tk.Text(
            self.frame,
            height=1,
            width=15,
            font=med_font,
            bg="black",
            fg="grey",
            borderwidth=0,
            highlightthickness=0,
        )
        self.blank = tk.Text(
            self.frame,
            height=1,
            width=10,
            font=big_font,
            bg="black",
            fg="grey",
            borderwidth=0,
            highlightthickness=0,
        )
        self.time.pack()
        self.temp.pack()
        self.blank.pack()
        self.frame.pack()
        self.update_temp()
        self.update_time()
        self.frame.mainloop()

    def update_time(self):
        time_str = datetime.datetime.now().strftime("%I:%M")
        self.time.delete("1.0", tk.END)
        self.time.insert(tk.END, time_str)
        self.frame.after(1000, self.update_time)

    def update_temp(self):
        response = urllib.request.urlopen(self.url)
        json_string = response.read()
        response.close()
        parsed_json = json.loads(json_string.decode("utf-8"))
        temp_f = parsed_json["current_observation"]["temp_f"]
        wind = parsed_json["current_observation"]["wind_mph"]
        temp_str = "{0}F".format(temp_f)
        if wind > 30:
            temp_str += " Very"
        if wind > 10:
            temp_str += " Windy!"
        self.temp.delete("1.0", tk.END)
        self.temp.insert(tk.END, temp_str)
        self.frame.after(30000, self.update_temp)

    def parse_command_line(self):
        """ Manage command line options """
        parser = argparse.ArgumentParser(description="Thermometer Script")
        parser.add_argument(
            "-v",
            "--verbose",
            action="store_true",
            help="print debug output while processing",
        )
        parser.add_argument(
            "-z",
            "--zipcode",
            action="store",
            default=os.environ.get("ZIPCODE", None),
            help="zipcode of weather report " "(env var: 'ZIPCODE')",
        )
        parser.add_argument(
            "-k",
            "--key",
            action="store",
            default=os.environ.get("TEMPERATURE_KEY", None),
            help="wunderground key " "(env var: 'TEMPERATURE_KEY')",
        )
        parser.add_argument(
            "-b",
            "--button",
            action="store_true",
            help="create a close button for testing",
        )

        args = parser.parse_args()
        if not args.zipcode or not args.key:
            exit(parser.print_help())

        self.create_close = args.button

        self.url = (
            "http://api.wunderground.com/api/{0}/conditions/q/"
            "{1}.json".format(args.key, args.zipcode)
        )

        # Create handlers
        if args.verbose:
            c_handler = logging.StreamHandler()
            c_handler.setLevel(logging.WARNING)
            c_format = logging.Formatter(
                "%(name)s - %(levelname)s" " - %(message)s"
            )
            c_handler.setFormatter(c_format)
            logger.addHandler(c_handler)

        f_handler = logging.FileHandler("temperature.log")
        f_handler.setLevel(logging.ERROR)
        f_format = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s" " - %(message)s"
        )
        f_handler.setFormatter(f_format)
        logger.addHandler(f_handler)

        logger.warning("Configured to read temperature from:")
        logger.warning(self.url)

        return args


if __name__ == "__main__":
    # Create a global logger
    logger = logging.getLogger(__name__)

    app = Application()
