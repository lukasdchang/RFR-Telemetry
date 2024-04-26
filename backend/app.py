from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from analyze import load_csv_file, plot_matplotlib, plot_plotly, calc_distance, max_min_data, plot_temperature_data, plot_temperature_data_plotly

app = Flask(__name__, static_folder='../frontend/build', static_url_path='/')
CORS(app)

@app.route('/')
def index():
    """Serve the main entry point of the web app, which is the React app in production."""
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/files', methods=['GET'])
def get_files():
    """Endpoint to list all available CSV files in the current directory."""
    csv_files = [file for file in os.listdir('.') if file.endswith('.csv')]
    return jsonify(csv_files)

@app.route('/load_data', methods=['POST'])
def load_data():
    """Endpoint to load data from a selected CSV file."""
    filename = request.json.get('filename')
    data = load_csv_file(filename)
    return jsonify(data.to_dict())

@app.route('/analyze_data', methods=['POST'])
def analyze_data():
    """Endpoint to perform data analysis."""
    filename = request.json.get('filename')
    data = load_csv_file(filename)
    # Assume calc_distance is an example function that might calculate and return data
    result = calc_distance(data)  # Example function
    return jsonify(result)

@app.route('/plot_data', methods=['POST'])
def plot_data():
    """Endpoint to generate plots."""
    filename = request.json.get('filename')
    data_type = request.json.get('data_type')
    data = load_csv_file(filename)
    if data_type == 'matplotlib':
        plot_path = plot_matplotlib(data)  # This function needs to return a path or URL to the generated plot image
        return send_from_directory('path_to_plot_images', plot_path)
    elif data_type == 'plotly':
        plot_html = plot_plotly(data)  # This function could return HTML or a URL to an HTML file
        return jsonify({'html': plot_html})

if __name__ == '__main__':
    app.run(debug=True)
