from tkinter import Tk, Text, Label, Button, Entry, IntVar, StringVar, END, W, E, CENTER, LEFT, BOTH, YES, Frame, ttk
from tkinter.ttk import Combobox, Radiobutton
from tkinter.font import Font
from datetime import datetime
from recording_logic import RecordingLogic as RL


class Gui:
    def __init__(self, master):
        self.master = master

        my_font = Font(family="Times New Roman", size=14)
        option_style = ttk.Style()
        option_style.configure('FRL.TCombobox', font=my_font)

        # button_style = ttk.Style()
        # button_style.configure('FRL.TButton', font=my_font)

        self.master.option_add('*TCombobox*Listbox.font', my_font)
        self.master.option_add('*TCombobox*Arrow', 100)

        self.hours = self._initiate_hours()
        self.minutes = self._initiate_minutes()
        self.stations = self._initiate_stations()

        self.master.title("Digital Audio Recorder")
        self.master.geometry('1000x400')

        self.choose_station_box = Combobox(self.master, font=my_font)
        self.choose_station_box['values'] = list(self.stations.keys())
        self.choose_station_box.current(0)
        self.choose_station_box.grid(row=0, columnspan=10, padx=(20, 20), pady=(20, 20))

        # Start Time

        self.start_time_label = Label(self.master, text='Record Start Time', font=my_font)
        self.start_time_label.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))

        self.start_time_hour_box = Combobox(self.master, font=my_font)
        self.start_time_hour_box['values'] = self.hours
        self.start_time_hour_box.current(0)
        self.start_time_hour_box.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.start_time_minute_box = Combobox(self.master, font=my_font)
        self.start_time_minute_box['values'] = self.minutes
        self.start_time_minute_box.current(0)
        self.start_time_minute_box.grid(row=1, column=2, padx=(20, 20), pady=(20, 20))

        self.start_time_am_or_pm = StringVar(None, 'AM')

        self.start_time_am = Radiobutton(self.master, text='AM', value='AM', variable=self.start_time_am_or_pm)
        self.start_time_am.grid(row=1, column=3, padx=(20, 20), pady=(20, 20))

        self.start_time_pm = Radiobutton(self.master, text='PM', value='PM', variable=self.start_time_am_or_pm)
        self.start_time_pm.grid(row=1, column=4, padx=(20, 20), pady=(20, 20))

        # End Time

        self.end_time_label = Label(self.master, text='Record End Time', font=my_font)
        self.end_time_label.grid(row=2, column=0, padx=(20, 20), pady=(20, 20))

        self.end_time_hour_box = Combobox(self.master, font=my_font)
        self.end_time_hour_box['values'] = self.hours
        self.end_time_hour_box.current(0)
        self.end_time_hour_box.grid(row=2, column=1, padx=(20, 20), pady=(20, 20))

        self.end_time_minute_box = Combobox(self.master, font=my_font)
        self.end_time_minute_box['values'] = self.minutes
        self.end_time_minute_box.current(0)
        self.end_time_minute_box.grid(row=2, column=2, padx=(20, 20), pady=(20, 20))

        self.end_time_am_or_pm = StringVar(None, 'AM')

        self.end_time_am = Radiobutton(self.master, text='AM', value='AM', variable=self.end_time_am_or_pm)
        self.end_time_am.grid(row=2, column=3, padx=(20, 20), pady=(20, 20))

        self.end_time_pm = Radiobutton(self.master, text='PM', value='PM', variable=self.end_time_am_or_pm)
        self.end_time_pm.grid(row=2, column=4, padx=(20, 20), pady=(20, 20))

        self.record_button = Button(self.master, text="Record", command=self._record_button_clicked, font=my_font)
        self.record_button.grid(row=10, column=10, padx=(20, 20), pady=(20, 20))

    def _record_button_clicked(self):
        station = self.stations[self.choose_station_box.get()]
        print(f"Station: {station}")

        start_time = self._derive_time(int(self.start_time_hour_box.get()),
                                       int(self.start_time_minute_box.get()),
                                       self.start_time_am_or_pm.get())

        end_time = self._derive_time(int(self.end_time_hour_box.get()),
                                     int(self.end_time_minute_box.get()),
                                     self.end_time_am_or_pm.get())

        print(start_time.strftime("%H:%M"))
        print(end_time.strftime("%H:%M"))

        if start_time >= end_time:
            exit()

        if station.strip() == '':
            exit()

        print('Button Pressed')

        RL(station, start_time, end_time)

    def _derive_time(self, hour, minute, am_pm):
        if am_pm == 'PM' and hour != 12:
            hour = hour + 12
        if am_pm == 'AM' and hour == 12:
            hour = hour - 12

        return datetime(datetime.now().year, datetime.now().month, datetime.now().day, hour, minute, 0)

    def _initiate_hours(self):
        hours_list = []
        for x in range(1, 13):
            hours_list.append(x)
        return hours_list

    def _initiate_minutes(self):
        minutes_list = []
        for x in range(0, 61):
            minutes_list.append(x)
        return minutes_list

    def _initiate_stations(self):
        stations = {}
        with open("stations.txt", "r") as stations_file:
            line = stations_file.readline()
            while line:
                station = line.split(',')
                stations[station[0].strip()] = station[1].strip()
                line = stations_file.readline()
        stations_file.close()
        print(stations)
        return stations


root = Tk()
my_gui = Gui(root)
root.mainloop()
