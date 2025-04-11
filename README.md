### 1. **Project Title**
- **Python Data-Driven Testing (DDT)**

### 2. **Project Description**
- This project showcases a lightweight, Python-based data-driven testing (DDT) framework using the `unittest` module and the `ddt` library. It reads test data from external sources like JSON and CSV files to drive multiple test scenarios dynamically. Ideal for validating a variety of inputs with minimal code repetition, the framework is modular and ready for integration into CI/CD pipelines.

### 3. **Technologies & Tools Used**
- **Programming Language**: Python 3  
- **Testing Framework**: `unittest`  
- **Data-Driven Utility**: `ddt`  
- **Data Sources**: JSON and CSV  
- **Reporting**: Standard unittest output (can be extended using HTMLTestRunner or Allure)  
- **Version Control**: Git & GitHub  

### 4. **Project Structure**


### 5. **Installation & Setup**
- **Prerequisites:**
  - Python 3.7 or later  
  - `pip` installed  

- **Steps to Set Up the Project:**
  1. Clone the repository:
     ```sh
     git clone https://github.com/MarwanSultan/python_ddt.git
     ```
  2. Navigate to the project directory:
     ```sh
     cd python_ddt
     ```
  3. Install dependencies:
     ```sh
     pip install -r requirements.txt
     ```

### 6. **How to Use**
- Run tests using `unittest`:
  ```sh
  python -m unittest discover tests

Add your data to data/data.json or data/data.csv and the framework will automatically iterate through each row/case.

Extend the test classes for additional modules, endpoints, or functional areas.

7. Contributing
Fork the repository

Create a feature branch (feature-branch-name)

Commit your changes and push them

Create a Pull Request

8. License
This project is licensed under the MIT License

9. Author
Marwan Sultan

LinkedIn: linkedin.com/in/marwansultan

Email: marwan.sultan@gmail.com
