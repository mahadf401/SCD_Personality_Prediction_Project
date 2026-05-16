# Personality Assessment Web App

This project is a web application built with Flask that assesses personality based on user responses to a set of questions. The application presents questions to the user, collects their responses, and generates a personality chart based on their answers.

## Features

- User-friendly interface for answering personality assessment questions.
- Data visualization using Chart.js to display personality traits.
- Backend processing of user responses to generate personality insights.
- Integration with two K-means clustering models stored in the `models` directory for personality analysis.

## Files and Folders

- **app.py**: Flask application file that defines routes and handles user interactions.
- **Test.py**: Python script containing functions for generating personality charts based on user responses.
- **questions.csv**: CSV file containing the questions for the personality assessment.
- **css/**: Folder containing CSS files for styling the web interface.
- **templates/**: Folder containing HTML templates for rendering the web pages.
- **models/**: Folder containing two K-means clustering models used for personality analysis.

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/pravincoder/personality_app.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Access the application in your web browser at `http://localhost:5000`.

## Usage

1. Answer the questions presented on the web interface.
2. Submit your responses.
3. View the generated personality chart based on your responses.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- This project was inspired by my friend in our Mini Project Mumbai university.
- Thanks to the Flask and Chart.js communities for providing excellent resources and documentation.
- Thanks to kaggle dataset (source)[!https://www.kaggle.com/datasets/tunguz/big-five-personality-test/data] 