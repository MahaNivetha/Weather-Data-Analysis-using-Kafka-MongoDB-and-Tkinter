import tkinter as tk
from pymongo import MongoClient
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class WeatherAnalyzerGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Weather Data Analyzer")

        # MongoDB connection
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['weather_db']
        self.collection = self.db['weather_collectionss']

        # Analysis Options
        self.analysis_options = tk.StringVar()
        self.analysis_options.set("temperature")  # Default analysis option

        # GUI Components
        self.label = tk.Label(master, text="Select Analysis Option:")
        self.label.pack()

        options = [
            "temperature", "humidity", "windSpeed",
            "cloudBase", "cloudCeiling", "cloudCover",
            "dewPoint", "evapotranspiration", "freezingRainIntensity",
            "humidity", "iceAccumulation", "iceAccumulationLwe",
            "precipitationProbability", "pressureSurfaceLevel", "rainAccumulation",
            "rainAccumulationLwe", "rainIntensity", "sleetAccumulation",
            "sleetAccumulationLwe", "sleetIntensity", "snowAccumulation",
            "snowAccumulationLwe", "snowIntensity", "temperatureApparent",
            "uvHealthConcern", "uvIndex", "visibility", "weatherCode",
            "windDirection", "windGust", "windSpeed"
        ]
        self.option_menu = tk.OptionMenu(master, self.analysis_options, *options)
        self.option_menu.pack()

        self.analyze_button = tk.Button(master, text="Analyze", command=self.analyze_data)
        self.analyze_button.pack()

        # Matplotlib Figure
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack()

    def analyze_data(self):
        analysis_option = self.analysis_options.get()

        # Retrieve data from MongoDB
        data = self.collection.find({}, {"_id": 0, "timelines.hourly.values." + analysis_option: 1, "timelines.hourly.time": 1})
        times = []
        values = []

        for entry in data:
            if "timelines" in entry and "hourly" in entry["timelines"]:
                for hourly_entry in entry["timelines"]["hourly"]:
                    if "time" in hourly_entry and "values" in hourly_entry and analysis_option in hourly_entry["values"]:
                        times.append(hourly_entry["time"])
                        values.append(hourly_entry["values"][analysis_option])

        # Plot only 5 data points
        times = times[:5]
        values = values[:5]

        # Plot the data
        self.ax.clear()
        self.ax.plot(times, values, marker='o')
        self.ax.set_title(f"Analysis of {analysis_option}")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel(analysis_option.capitalize())

        # Rotate x-axis labels to horizontal and set font size
        self.ax.set_xticklabels(times, fontsize=6)

        # Draw the plot on the Tkinter canvas
        self.canvas.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAnalyzerGUI(root)
    root.mainloop()
