# Drive-Day-Analyzer
Drive Day Analyzer is a program that allows the user to interactively analyze CSV files of data captured during RFR drive days
    - Easily insert new data to be analyzed by putting the CSV file in the same directory as this assuming it is formatted all the same
    - Select a file to be analyzed
    - Select a command: 
        - Plot on matplotlib
            - Allows you to print the graph of many different types of data and compare using matplotlib
        - Plot on plotly
            - Allows you to print the graph of many different types of data using matplotlib
        - Calculate Distance Driven
            - Calulated by finding the integral of front left wheel speed by time
        - Max & Min of data
        - Load new CSV file
            - Allows the user to select a new CSV file without rerunning the program


How to run:
    1. Open new terminal
    2. python3 analyze.py
