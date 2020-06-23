import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data_tests import RegisterCoursesCSVDataTests

# Get all test from the test classes
test_case_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combination all test classes
smoke_test = unittest.TestSuite([test_case_1, test_case_2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
