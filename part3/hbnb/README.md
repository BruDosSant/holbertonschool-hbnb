# HolbertonBnB Part2 

## Project Description

This project is a clone of AirBnB developed as part of the Holberton School Uruguay program. The goal of this phase is to build a scalable system that allows the management of users, reviews, places, and amenities, using a well-defined architecture and applying the logic previously implemented in the first phase.

## Repository Structure

The repository is organized into the following main directories and files:

- **app/**: Directory containing the entire program.

  - **models/**: Contains the data model logic and classes representing the system's entities.

    - `base_model.py`: Base class defining common attributes and methods.
    - `user.py`: User model.
    - `place.py`: Place model.
    - `review.py`: Review model.
    - `amenity.py`: Amenities model.

  - **api/**: Implementation of the RESTful API to interact with the system.

    - `v1/`: Version 1 of the API with specific controllers.
    - `app.py`: API entry point.

  - **services/**: Implements the Facade pattern, simplifying interactions between different layers of the application.
    - `facade.py`: Implements the Facade pattern, simplifying interaction between different layers of the application.

  - **persistence/**: Manages data storage and database interactions.
    - `repository.py`: Defines the repository pattern for managing and storing data, such as users, places, reviews, etc.

- **tests/**: Contains automated test cases to validate system functionality.

  - `test_review.py`: Data validation for review class endpoints.
  - `test_user.py`: Data validation for user class endpoints.
  - `test_place.py`: Data validation for place class endpoints.
  - `test_amenities.py`: Data validation for amenities class endpoints.

- **README.md**: This documentation file provides an overview of the project.

- **config.py**: Defines local environment variables.

- **run.py**: A Python script used to start a web application.

## Flow Diagram

The following flow diagram illustrates the general functioning of the system:

![image](https://github.com/user-attachments/assets/ff6c19cb-88f8-4e94-b66a-6af4a462ae4c)

## Installation and Configuration

### Prerequisites

To run this project, you will need to have installed:

- Python 3
- Flask
- pip (Python package manager)

### Installing Dependencies

Run the following command at the root of the project to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### How to Run the Application

To start the API, run the following command:

```bash
python3 run.py
```

The server will run by default at `http://127.0.0.1:5000/`.

## Authors

[@BruDosSant](https://github.com/BruDosSant)  
[@Rodrigoferrer](https://github.com/Rodrigoferrer)  
[@feratholberton](https://github.com/feratholberton)

