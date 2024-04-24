import os
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def list_csv_files(directory):
    # List all files in the given directory
    files = os.listdir(directory)
    # Filter and return only CSV files
    return [file for file in files if file.endswith('.csv')]

def load_csv_file():
    directory = '.'  # Current directory
    csv_files = list_csv_files(directory)
    if not csv_files:
        print("No CSV files found in the directory.")
        return None

    print("CSV Files available:")
    for index, file in enumerate(csv_files, start=1):
        print(f"{index}. {file}")

    file_index = int(input("Select a file by number: ")) - 1
    filename = csv_files[file_index]
    return pd.read_csv(filename, skiprows=18, header=None)

def plot_matplotlib(data, data_details):
    while True:
        print("\nAvailable Data Types:")
        for index, detail in enumerate(data_details, start=1):
            print(f"{index}. {detail['name']} ({detail['unit']})")
        print("Enter 'exit' to quit to main menu.")
        print("Enter 'compare' to compare two graphs.")

        user_input = input("Enter a number, 'compare', or 'exit': ")
        if user_input.lower() == 'exit':
            break
        elif user_input.lower() == 'compare':
            print("Select the first data type for comparison:")
            first_index = int(input("Enter a number: ")) - 1
            first_data = data_details[first_index]

            print("Select the second data type for comparison:")
            second_index = int(input("Enter a number: ")) - 1
            second_data = data_details[second_index]

            # Plotting the data for comparison
            plt.figure(figsize=(15, 5))

            # First data plot
            plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
            plt.plot(data[0], data[first_data['column'] - 1], label=f"{first_data['name']} ({first_data['unit']})")
            plt.title(f"{first_data['name']} Over Time")
            plt.xlabel('Time (s)')
            plt.ylabel(f"{first_data['name']} ({first_data['unit']})")
            plt.legend()
            plt.grid(True)

            # Second data plot
            plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
            plt.plot(data[0], data[second_data['column'] - 1], label=f"{second_data['name']} ({second_data['unit']})")
            plt.title(f"{second_data['name']} Over Time")
            plt.xlabel('Time (s)')
            plt.ylabel(f"{second_data['name']} ({second_data['unit']})")
            plt.legend()
            plt.grid(True)

            plt.show()
        else:
            selected_index = int(user_input) - 1
            selected_data = data_details[selected_index]

            print(f"You have selected: {selected_data['name']}")

            # Plotting the single data
            plt.figure(figsize=(10, 5))
            plt.plot(data[0], data[selected_data['column'] - 1], label=f"{selected_data['name']} ({selected_data['unit']})")
            plt.title(f"{selected_data['name']} Over Time")
            plt.xlabel('Time (s)')
            plt.ylabel(f"{selected_data['name']} ({selected_data['unit']})")
            plt.legend()
            plt.grid(True)
            plt.show()

def plot_plotly(data, data_details):
    while True:
        print("\nAvailable Data Types:")
        for index, detail in enumerate(data_details, start=1):
            print(f"{index}. {detail['name']} ({detail['unit']})")
        print("Enter 'exit' to quit to main menu.")

        user_input = input("Enter a number or 'exit': ")
        if user_input.lower() == 'exit':
            break

        selected_index = int(user_input) - 1
        selected_data = data_details[selected_index]

        print(f"You have selected: {selected_data['name']}")

        # Plotting the data using Plotly
        fig = go.Figure(data=go.Scatter(x=data[0], y=data[selected_data['column'] - 1],
                                        mode='lines+markers', name=selected_data['name']))
        fig.update_layout(title=f"{selected_data['name']} Over Time",
                          xaxis_title='Time (s)',
                          yaxis_title=f"{selected_data['name']} ({selected_data['unit']})")
        fig.show()


def calc_distance(data):
    # Assuming time is column 0 and wheel speed in km/h is column 14
    time = data[0]
    speed_miles_per_hr = data[14]

    speed_m_per_s = speed_miles_per_hr / 2.237
    time_intervals = time.diff().fillna(0)
    distances = speed_m_per_s * time_intervals
    total_distance_m = distances.sum()
    total_distance_miles = total_distance_m / 1609

    print(f"Total distance driven: {total_distance_miles:.2f} miles")

def max_min_data(data, data_details):
    while True:
        print("\nAvailable Data Types for Max & Min Analysis:")
        for index, detail in enumerate(data_details, start=1):
            print(f"{index}. {detail['name']} ({detail['unit']})")
        print("Enter 'exit' to quit to main menu.")

        user_input = input("Enter a number or 'exit': ")
        if user_input.lower() == 'exit':
            break

        selected_index = int(user_input) - 1
        selected_data = data_details[selected_index]

        print(f"You have selected: {selected_data['name']}")

        # Calculate and display max and min
        max_value = data[selected_data['column'] - 1].max()
        min_value = data[selected_data['column'] - 1].min()

        print(f"Maximum {selected_data['name']} ({selected_data['unit']}): {max_value}")
        print(f"Minimum {selected_data['name']} ({selected_data['unit']}): {min_value}")

def plot_temperature_data(data):
    # Extract the time series and temperature data
    time = data[0]  # Assuming the first column is the time
    engine_oil_temp = data[7]  # Column 7 for Engine Oil Temp
    gbox_oil_temp = data[8]  # Column 8 for Gearbox Oil Temp
    coolant_temp = data[6]  # Column 6 for Coolant Temp

    # Create a plot
    plt.figure(figsize=(12, 6))
    plt.plot(time, engine_oil_temp, label='Engine Oil Temp (°C)', linestyle='-', color='red')
    plt.plot(time, gbox_oil_temp, label='Gearbox Oil Temp (°C)', linestyle='-', color='blue')
    plt.plot(time, coolant_temp, label='Coolant Temp (°C)', linestyle='-.', color='green')

    # Adding titles and labels
    plt.title('Engine Oil, Gearbox Oil, and Coolant Temperatures Over Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    # Show grid
    plt.grid(True)

    # Display the plot
    plt.show()

def main():
    data = load_csv_file()
    if data is None:
        return

    data_details = [
        {"name": "Battery Current", "column": 2, "unit": "A"},
        {"name": "Engine Power", "column": 3, "unit": "kW"},
        {"name": "Fuel Level", "column": 4, "unit": "l"},
        {"name": "Battery Volts", "column": 5, "unit": "V"},
        {"name": "Coolant Temp", "column": 6, "unit": "C"},
        {"name": "Engine Oil Temp", "column": 7, "unit": "C"},
        {"name": "Gbox Oil Temp", "column": 8, "unit": "C"},
        {"name": "Brake Temp FL", "column": 9, "unit": "C"},
        {"name": "Brake Temp FR", "column": 10, "unit": "C"},
        {"name": "Brake Temp RL", "column": 11, "unit": "C"},
        {"name": "Brake Temp RR", "column": 12, "unit": "C"},
        {"name": "Brake Pressure Front", "column": 13, "unit": "kPa"},
        {"name": "Brake Pressure Rear", "column": 14, "unit": "kPa"},
        {"name": "Wheel Speed FL", "column": 15, "unit": "km/h"},
        {"name": "Wheel Speed FR", "column": 16, "unit": "km/h"},
        {"name": "Wheel Speed RL", "column": 17, "unit": "km/h"},
        {"name": "Wheel Speed RR", "column": 18, "unit": "km/h"}
    ]

    while True:
        print(f"\nWhat will you do today?")
        print(f"1. Plot using matplotlib")
        print(f"2. Plot using plotly")
        print(f"3. Calculate Distance Driven")
        print(f"4. Max & Min of data")
        print(f"5. Load a new CSV file")
        print(f"6. Plot temperature data")
        print(f"Enter 'exit' to exit the program.")
        command = input(f"Enter a number or 'exit': ")

        if command.lower() == 'exit':
            break

        try:
            command = int(command)
        except ValueError:
            print("Please enter a valid number or 'exit'.")
            continue

        if command == 1:
            plot_matplotlib(data, data_details)
        elif command == 2:
            plot_plotly(data, data_details)
            pass    
        elif command == 3:
            calc_distance(data)
            pass
        elif command == 4:
            max_min_data(data, data_details)
            pass
        elif command == 5:
            data = load_csv_file()
            if data is None:
                print("Failed to load a new file, exiting.")
                break
        elif command == 6:
            plot_temperature_data(data)
            pass

if __name__ == '__main__':
    main()
