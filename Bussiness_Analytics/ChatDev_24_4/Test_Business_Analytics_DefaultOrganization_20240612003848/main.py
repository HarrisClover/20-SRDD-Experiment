'''
This is the main file that will be executed to run the application. It imports and uses the other modules to load, analyze, and visualize the data, and to create and update the dashboard. Error handling has been added to ensure a smooth user experience and prevent unexpected crashes.
'''
# Ensure that the DataLoader module is in the same directory as this file or in a directory that is in the PYTHONPATH
import sys
sys.path.append('/path/to/directory/containing/DataLoader')
try:
    import DataLoader
except ModuleNotFoundError:
    print("Module 'DataLoader' not found. Please ensure it is in the same directory as this file or in a directory that is in the PYTHONPATH.")
    sys.exit(1)
import DataAnalyzer
import DataVisualizer
import Dashboard
def main():
    try:
        # Ask user for the data file path
        path_to_data_file = input("Please enter the path to your data file: ")
        # Create instances of the classes (no initialization parameters required)
        data_loader = DataLoader.DataLoader(path_to_data_file)
        data = data_loader.load_data()
    except FileNotFoundError:
        print("The file was not found. Please check the file path and try again.")
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    try:
        # Preprocess the data
        data = data_loader.preprocess_data(data)
        # Analyze the data and generate a report
        report = data_analyzer.analyze_data(data)
        data_analyzer.generate_report(report)
    except Exception as e:
        print(f"An error occurred during data processing or analysis: {e}")
        return
    try:
        # Visualize the data
        data_visualizer = DataVisualizer.DataVisualizer()
        plot = data_visualizer.plot_data(data)
        data_visualizer.show_plot(plot)
        # Create and update the dashboard
        dashboard = Dashboard.Dashboard()
        dashboard.create_dashboard()
        dashboard.update_dashboard(report, plot)
    except Exception as e:
        print(f"An error occurred during data visualization or dashboard update: {e}")
        return
if __name__ == "__main__":
    main()