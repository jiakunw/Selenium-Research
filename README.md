# Selenium-Research (Derek and Madeleine)
This is a repository for the files created for Selenium and Front End Testing
Research Update 2/23/23 : 
This update will detail the research done for the Selenium IDE and GRID and how to :
-set up IDE testing
-engage in performance testing

ON IDE :
-IDE is simple to download, on Chrome/Firefox, and fairly quick and painless
-Features are numerous and allow for extensive testing (from https://www.softwaretestinghelp.com/selenium-ide-download-and-installation-selenium-tutorial-2/#1_Menu_Bar)
  -File Menu is very much analogous to the file menu belonging to any other application.

  It allows the user to:

      -Create a new test case, open existing test case, save the current test case.
      -Export Test Case As and Export Test Suite As in any of the associated programming language compatible with Selenium RC and WebDriver. It also gives the liberty to the user to prefer amid the available unit testing frameworks like jUnit, TestNG etc. Thus an IDE test case can be exported for a chosen union of programming language, unit testing framework and tool from the selenium package.
      -Export Test Case As option exports and converts only the currently opened Selenium IDE test case.
      -Export Test Suite As option exports and converts all the test cases associated with the currently opened IDE test suite.
      -Close the test case.
      -Most feautres (as of now are in Python 2)
                                                                                                                                                                          
 ON GRID (from Python persepctive): 
 -can be installed from python with : 
      pip install selenium==3.14.1 
      pip install pytest-selenium
      pip install pytest-variables
 -"Gridlastic" accounts are free to create
-NOTE: The python selenium client does not work with selenium version 3.3. Also, starting from selenium version 3.9.1 you must also include "platformName": "windows" in the request when testing with firefox and IE.
-Able to run tests in parallel (save time) w/ command : 
      py.test -n 2 --rerun 2 test_unittest.py
