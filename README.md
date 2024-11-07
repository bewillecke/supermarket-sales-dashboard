# Supermarket Sales Dashboard

This project is an interactive dashboard developed with Python and Dash for visualizing and analyzing sales data from a fictitious supermarket. The interface allows exploration of information such as gross income and ratings, filtered by city, gender, and payment method.

## Technologies Used

- **Python 3.7+**
- **Dash** (with Dash Bootstrap Components for styling)
- **Plotly** for interactive charts
- **Pandas** and **NumPy** for data manipulation

## Project Structure

- `app.py`: Main code of the dashboard, configured to create and render charts based on sales data.
- `dataset/supermarket_sales.csv`: Public dataset used for analysis, which should be located in the `dataset` folder.
- `requirements.txt`: Libraries needed to run the project.

## Installation and Execution Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/bewillecke/supermarket-sales-dashboard.git
    ```
2. **Install dependencies**:
    Navigate to the project directory and install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
3. **Folder Structure**:
    Ensure that the dataset (`supermarket_sales.csv`) is in the following structure:
    ```
    supermarket-sales-dashboard/
    ├── app.py
    └── dataset/
        └── supermarket_sales.csv
    ```
4. **Run the application**:
    In the project root directory, run the command:
    ```bash
    python app.py
    ```
5. **Access the dashboard**:
    Open your browser and go to [http://localhost:8050](http://localhost:8050) to view the dashboard.

## Notes

- **Port**: The server is configured to run on port `8050`. To modify the port, change the value in the `app.py` file.
- **Debug Mode**: For security, debug mode is disabled in this version. To enable it, change `debug=False` to `debug=True` in `app.py`.

---

This project was developed as part of a study in data analysis, data visualization, and building web apps using Dash and can be adapted for other purposes.
