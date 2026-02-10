import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Import the login function
from login import login_to_hcm

# Call the login function to get the WebDriver object
driver = login_to_hcm(
    "http://172.16.35.74/hcm/login",  # URL to the HCM login page
    "Nauman.ahmad@ptclgroup.com",         # Your email
    "Ufone@123"                           # Your password
)

try:
    # Wait for the "Employee" button to appear and click it
    employee_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@class='dash-link']//span[text()='Employee']"))
    )
    employee_button.click()
    print("Employee button clicked successfully!")
    time.sleep(10)

    # Wait for the Manage Employee heading (h4 element)
    heading_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h4"))
    )

    # Check if the text matches "Manage Employee"
    if heading_element.text.strip() == "Manage Employee":
        print("Manage Employee page opened successfully!")

    # __________________________________________________________________________

    # VERIFY CREATE NEW EMPLOYEE FUNCTIONALITY

    # Locate the "Create New Employee" button by its text
    create_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Create New Employee')]"))
    )

    # Click the button
    create_button.click()
    print("Successfully clicked 'Create New Employee' button!")
    time.sleep(3)

    # __________________________________________________________________________
    # Locate the "Management Level" dropdown by its ID
    #dropdown = driver.find_element(By.ID, "management_level_id")

# Scroll the dropdown into view
    #driver.execute_script("arguments[0].scrollIntoView();", dropdown)

# Now select the "L4" option using the Select class
    #select = Select(dropdown)
    #select.select_by_visible_text("L4")
    



    # ENTER NAME

    # Wait for the input field to be clickable
    name_input = driver.find_element(By.CSS_SELECTOR, "#name.form-control[placeholder='Enter employee name']")
    name_input.click()
    name_input.clear()
    name_input.send_keys("Waheed Test")  # Replace with the desired name
    print("Name entered successfully")
    time.sleep(6)

    # __________________________________________________________________________
    #Enter dob 
   
    dob = driver.find_element(By.ID, "dob")
    driver.execute_script("arguments[0].value = '2000-05-12';", dob)
    time.sleep(3)
    print("DoB Entered Successfully")
    
    #Enter username
    username = driver.find_element(By.ID, "username")
    username.click()                 # Click inside the input
    username.clear()                 # Clear existing text (optional)
    username.send_keys("myUser123")  # Type your username

    print("Username entered successfully")
    
    
    
    
    
    
    
    
    
    
    

    # ENTER PHONE NUMBER

    # Find the phone input field using the placeholder attribute
    phone_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter employee phone']")
    phone_input.clear()
    phone_input.send_keys("02231919101")  # Replace with the desired phone number
    print("Phone entered successfully")
    time.sleep(6)

    # _________________________________________________________________________

    # ENTER EMAIL

    # Locate the email input field using the placeholder attribute
    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter employee email']")
    email_input.clear()
    email_input.send_keys("atest76029@gmail.com")  # Replace with the desired email
    print("Email entered successfully")
    time.sleep(6)

    # __________________________________________________________________________

    # ENTER PASSWORD

    # Locate the password input field using its placeholder attribute
    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter employee password']")

    # Clear the field (if necessary) and enter a password
    password_input.clear()
    password_input.send_keys("EasyPass@1")  # Replace with the desired password
    print("Password entered successfully")
    time.sleep(6)

    #____________________________________________________________________________

    # ENTER ADDRESS

    textarea = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Enter employee address']"))
    )

    # Clear the field and enter the test address
    textarea.clear()
    textarea.send_keys("123 Test Street, Example City, 12345")

    print("Test address entered successfully!")
    time.sleep(6)

    #___________________________________________________________________________

    # ENTER EMP NUMBER 

    # Locate the input field using XPath and placeholder
    emp_no_input = driver.find_element(By.XPATH, "//*[@placeholder='Enter EMP No.']")

    # Clear the input field and enter the employee number
    emp_no_input.clear()
    emp_no_input.send_keys("77000111")  # Replace with the actual employee number
    print("Employee number entered successfully")
    time.sleep(6)

    #___________________________________________________________________________

    # SELECT BRANCH 

    # Locate the dropdown element using its ID
    branch_dropdown = driver.find_element(By.ID, "branch_id")

    # Create a Select object to interact with the dropdown
    select = Select(branch_dropdown)
    time.sleep(4)

    # Select the "Ufone" option by its visible text
    select.select_by_visible_text("Ufone")
    print("Branch entered successfully")

    # Optional: Wait to verify the action
    time.sleep(4)

    #___________________________________________________________________________

    # SELECT DEPARTMENT

    # Locate the dropdown element using its ID
    department_dropdown = driver.find_element(By.ID, "department_id")

    # Create a Select object to interact with the dropdown
    select_department = Select(department_dropdown)
    time.sleep(4)  

    # Select the "Ufone Customer Care" option by its visible text
    select_department.select_by_visible_text("Ufone Customer Care")
    print("Department entered successfully")

    time.sleep(4)  

    #_______________________________________________________________________________

    # SELECT SUB DEPARTMENT 

    # Locate the dropdown element using its ID
    sub_department_dropdown = driver.find_element(By.ID, "sub_department_id")

    # Create a Select object to interact with the dropdown
    select_sub_department = Select(sub_department_dropdown)
    time.sleep(4)  

    # Select the "Automation" option by its visible text
    select_sub_department.select_by_visible_text("Automation")
    print("Sub Department entered successfully")

    time.sleep(4)  

    #___________________________________________________________________________

    # SELECT DESIGNATION

    designation_dropdown = driver.find_element(By.ID, "designation_id")

    # Create a Select object to interact with the dropdown
    select_designation = Select(designation_dropdown)
    time.sleep(4)  

    # Select "Assistant manager" by its visible text
    select_designation.select_by_visible_text("Assistant manager")
    print("Designation entered successfully")

    time.sleep(4)  

    #___________________________________________________________________________
    #Add REGION 
    
    # WAIT for the dropdown to appear
    region_dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "region_id"))
)

# Scroll into view (optional but helps)
    driver.execute_script("arguments[0].scrollIntoView();", region_dropdown)

# SELECT the option by visible text
    select_region = Select(region_dropdown)
    select_region.select_by_visible_text("North")

    time.sleep(2)
    print("Region 'North' selected successfully!")



    # ENTER CNIC 

    # Locate the CNIC field
    cnic_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cnicInput"))
    )

    # Scroll the CNIC field into view
    driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", cnic_field)
    time.sleep(2)  # Give time for scrolling animation to complete

    # Ensure the field is interactable after scrolling
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cnicInput"))
    )

    # Interact with the CNIC field
    cnic_field.clear()  # Optional, if you want to clear the field first
    cnic_field.send_keys("12919-1559191-9")  # Replace with your CNIC value
    print("Successfully entered CNIC")
    time.sleep(4)  

    #___________________________________________________________________________

    # ENTER NTN NUMBER

    # Locate the NTN Number field
    #ntn_field = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.NAME, "ntn_number"))
    #)
    # Ensure the field is clickable before interacting
    #WebDriverWait(driver, 10).until(
     #   EC.element_to_be_clickable((By.NAME, "ntn_number"))
    #)

    # Interact with the NTN field
    #ntn_field.clear()  # Optional: Clear the field if pre-filled
    #ntn_field.send_keys("123459")  # Replace with the desired NTN number
    #print("Successfully entered NTN Number")
    #time.sleep(4)  

    #____________________________________________________________________________

    # ENTER PASSPORT NUMBER 

    # Locate the Passport Number field
    #passport_field = WebDriverWait(driver, 10).until(
     #   EC.presence_of_element_located((By.NAME, "passport_number"))
    #)
    
    # Interact with the Passport Number field
    #passport_field.clear()  # Optional: Clear the field if pre-filled
    #passport_field.send_keys("AB123456")  # Replace with the desired passport number
    #print("Successfully entered Passport Number")
    #time.sleep(4)  

    #__________________________________________________________________________

    # UPLOAD PROFILE PICTURE

    try:
        # Locate the 'Choose file here' button (this is the div containing the text and icon)
        choose_file_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "bg-primary.profile"))
        )

        # Click the 'Choose file here' button to open the file input dialog
        choose_file_button.click()
        time.sleep(3)  # Small delay to ensure the file input dialog is open

        # Find the file input element (next element after the div with class "bg-primary profile")
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        )

        # Send the path of the profile picture file to the file input field
        file_input.send_keys("C:\\Users\\hyperlink\\Desktop\\testing\\images.jpg")  # Replace with actual file path

        print("Profile picture selected successfully!")
    except Exception as e:
        print(f"An error occurred while uploading the profile picture: {e}")

    

    # CROP AND SAVE THE PROFILE PICTURE
    # Wait until the button is visible
    button = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "cropAndSave"))
)

    # Click on the button
    button.click()
    print("Clicked on save button successfully!")
    time.sleep(4) 

    #___________________________________________________________________________
    
    #SELECT EMPLOYMENT TYPE
    
    # Locate the dropdown element
    dropdown = driver.find_element(By.ID, "employment_type")

   # Scroll into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)

   # Select the "Permanent" option
    select = Select(dropdown)
    select.select_by_visible_text("et11")
    time.sleep(5)
    print("Employment Type entered successfully!")
    
    #_________________________________________________________________________
    
    # SELECT EMPLOYMENT STATUS 
    
    dropdown = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "employment_status"))
    )

# Scroll the dropdown
    driver.execute_script("arguments[0].scrollIntoView();", dropdown)

    select = Select(dropdown)
    select.select_by_visible_text("Permanent")
    time.sleep(3)

    # __________________________________________________________________________
    
    # SELECT MANAGEMANT LEVEL 
    
    # Locate the "Management Level" dropdown by its ID
    #management_level_dropdown = driver.find_element(By.ID, "management_level_id")

    # Scroll the dropdown into view
    #driver.execute_script("arguments[0].scrollIntoView();", management_level_dropdown)

    # Create a Select object to interact with the dropdown
    #select_management_level = Select(management_level_dropdown)

    # Select "L4" by its visible text
    #select_management_level.select_by_visible_text("L4")
    #print("Management Level selected successfully")

    #time.sleep(4)
    
    #____________________________________________________________________
    
    # SELECT EMPLOYMENT CITY 
    
     # Locate the "Employmnet City " dropdown by its ID
    employment_city_dropdown = driver.find_element(By.ID, "employment_city")

    # Scroll the dropdown into view
    driver.execute_script("arguments[0].scrollIntoView();", employment_city_dropdown)

    # Create a Select object to interact with the dropdown
    select_employment_city = Select(employment_city_dropdown)

    # Select "Adilpur" by its visible text
    select_employment_city.select_by_visible_text("Adilpur")
    print("Employment city selected successfully")
    time.sleep(4)
    #___________________________________________________________________
    
    # SELECT GRADE 
    
     # Locate the "Grade " dropdown by its ID
    grade_dropdown = driver.find_element(By.ID, "grade")

    # Scroll the dropdown into view
    driver.execute_script("arguments[0].scrollIntoView();",grade_dropdown)

    # Create a Select object to interact with the dropdown
    select_grade= Select(grade_dropdown)

    # Select Grade by its visible text
    select_grade.select_by_visible_text("g1")
    print(" Grade selected successfully")
    time.sleep(4)
    
    #____________________________________________________________
    
    # SELECT LINE MANAGER 
    
    # Wait for the dropdown to be visible and present
   # line_manager_dropdown = WebDriverWait(driver, 10).until(
    #EC.presence_of_element_located((By.ID, "reports"))  # Make sure this is the correct ID
#)
    

    # Scroll the dropdown into view
    #driver.execute_script("arguments[0].scrollIntoView();", line_manager_dropdown)

    # Create a Select object to interact with the dropdown
    #select_line_manager = Select(line_manager_dropdown)
   

    # Optionally, wait for all options to be loaded if needed
    #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#reports option")))
    #print("dropdown options loaded")
    #time.sleep(4)
#____________________________________________
    # Select by index - adjust the index as needed (e.g., selecting the 4th option)
    #select_line_manager.select_by_index(4)  # Change this index to the desired manager's position

    
    #print("Line Manager selected successfully")
    #time.sleep(10)
   # line_manager_dropdown = WebDriverWait(driver, 10).until(
    #    EC.presence_of_element_located((By.ID, "reports"))  # Make sure this is the correct ID
    #)

    # Scroll the dropdown into view
    #driver.execute_script("arguments[0].scrollIntoView();", line_manager_dropdown)

    # Create a Select object to interact with the dropdown
    #select_line_manager = Select(line_manager_dropdown)

    # Optionally, wait for all options to be loaded if needed
    #WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#reports option")))

    # Print out all available options in the dropdown
    #options = select_line_manager.options
    #print("Dropdown options:")
    #for option in options:
     #   print(option.text)

    # Then, select by the desired visible text (change the text accordingly)
    #select_line_manager.select_by_visible_text("Noor Javed - 267")  # Change this text as needed

    #print("Line Manager selected successfully")
    #time.sleep(4)
   
    
    
    #_________________________________________________________________
    
    # SELECT Employment Type Effective Date
    
     # Locate the Date field using its ID
    date_field = driver.find_element(By.ID, "company_doj")

    # Scroll the element into view (optional, to ensure visibility)
    driver.execute_script("arguments[0].scrollIntoView();", date_field)
    date_field = driver.find_element(By.ID, "company_doj")

    # Set the correct value using JavaScript
    driver.execute_script("arguments[0].value = '2026-12-03';", date_field)

   # Optionally trigger a change event (if needed by the app)
    driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", date_field)

    print("Employment Type Effective Date added successfully")
    time.sleep(4)
    
    #_________________________________________________________________________
    
     # Locate the "Create" button
    create_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(), 'Create')]")

    # Scroll to the "Create" button
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", create_button)

    # Wait for the scrolling animation to complete
    time.sleep(2)

    # Click the "Create" button
    create_button.click()
    print("Create button clicked successfully!")

    # Add a delay to observe the result (can be removed later)
    time.sleep(10)
        

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
