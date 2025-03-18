# School Management System

This  **School Management System**  is a desktop application developed in  **Python**  using  **Tkinter**  for the GUI and  **MySQL**  for database management. It was created as part of the  **Children Science Congress**  during my 11th grade and was selected for both  **subdistrict**  and  **district**  levels. The system is designed to manage student records efficiently, providing features like adding, updating, deleting, and searching for student information.

----------

## Features

1.  **Student Management**:
    
    -   Add new student records with details like ID, name, mobile number, email, address, gender, and date of birth.
        
    -   Update existing student records.
        
    -   Delete student records.
        
    -   Search for students using various criteria (ID, name, email, etc.).
        
2.  **Database Integration**:
    
    -   Connects to a  **MySQL**  database to store and retrieve student data.
        
    -   Automatically creates the database and table if they don’t exist.
        
3.  **Data Export**:
    
    -   Export student data to a  **CSV**  file for external use.
        
4.  **User-Friendly Interface**:
    
    -   Intuitive and responsive GUI built with  **Tkinter**  and  **ttkthemes**.
        
    -   Real-time clock and date display.
        
5.  **Error Handling**:
    
    -   Validates user input to ensure data integrity.
        
    -   Displays error messages for invalid operations (e.g., duplicate IDs, empty fields).
        

----------

## Technologies Used

-   **Programming Language**: Python
    
-   **GUI Framework**: Tkinter, ttkthemes
    
-   **Database**: MySQL (using PyMySQL for connection)
    
-   **Additional Libraries**: Pillow (for image handling), pandas (for CSV export)
    

----------

## Installation and Setup

### Prerequisites

1.  **Python 3.x**: Ensure Python is installed on your system. Download it from  [python.org](https://www.python.org/).
    
2.  **MySQL**: Install MySQL Server and MySQL Workbench (or any MySQL client).
    
3.  **Required Python Packages**:
    
    -   Install the necessary packages using pip:
        ```bash
        pip install pymysql pillow pandas ttkthemes 
        ```
     

### Steps to Run the Project

1.  **Clone the Repository**:
  
    ```bash 
    git clone https://github.com/your-username/school-management-system.git
    cd school-management-system
    ```
    
2.  **Set Up the Database**:
    
    -   Open MySQL and create a database named  `studentmanagementsystem`  (or use the default one in the code).
        
    -   Update the database connection details in the  `connect_database()`  function in  `sms.py`  if needed:
        
        ```python
        con = pymysql.connect(host='localhost', user='root', password='your_password')
        ```
        
3.  **Run the Application**:
    
    -   Execute the  `login.py`  file to start the application:
        
        ```bash
        python login.py
        ```
        
    -   Use the following credentials to log in:
        
        -   **Username**:  `Vivek`
            
        -   **Password**:  `1234`
            
4.  **Explore the Features**:
    
    -   Connect to the database using the "Connect Database" button.
        
    -   Use the buttons in the left frame to add, search, update, delete, or export student data.
        




----------

## Future Enhancements

-   **User Authentication**: Implement a more secure login system with multiple user roles (admin, teacher, student).
    
-   **Advanced Search**: Add filters and sorting options for student records.
    
-   **Reports**: Generate PDF reports for student data.
    
-   **Backup and Restore**: Add functionality to backup and restore the database.

----------

## License

This project is licensed under the  **MIT License**. See the  [LICENSE](https://license/)  file for details.

----------

## Acknowledgments

-   **Teachers and Mentors**: For guiding me through the development process.
    
-   **Children Science Congress**: For providing a platform to showcase this project.
    
-   **Open Source Community**: For the libraries and tools that made this project possible.
    

----------

## Connect!

If you have any questions or want to connect, feel free to reach out to me:

-   **Email**:  [ishantmanjit@gmail.com](https://mailto:ishantmanjit@gmail.com/)
    
-   **Twitter**:  [@Astro_iSHU](https://twitter.com/Astro_iSHU)
