from unittest import TestCase

import university_record_function

class UniversityRecordTest(TestCase):

        def test_student_record_is_added(self):
            student_record = {"name": Amodu, "age": 28}

            expected = {"name": Amodu, "age": 28}
            actual = university_record_function.create_student_record(student_record)

            self.assertEqual(expected, actual)

        def test_that_student_can_not_be_added_twice(self):
            student_record = {"name": Amodu, "age": 28}

            expected = "Name already exists."
            actual = university_record_function.create_student_record(student_record)

            self.assertEqual(expected, actual)


        def test_that_students_names_can_not_be_mixed_with_numerics(self ):
            student_name = {"Amodu234"}

            expected = "Students name cannot be mixed with numbers. Re-enter students name."
            actual = university_record_function.create_student_record(student_name)

            self.assertEquals(expected, actual)

        def test_that_student_record_can_be_changed_just_in_case_of_mistakes(self):
            student_record = {"name": Amomu, "age": 22}

            expected = {"name": Amodu, "age": 28}
            actual = university_record_function.create_student_record(student_record)

            self.assertEqual(expected, actual)

        def test_that_






        def test_that_student_record_can_be_displayed_fully(self):
            student_record = {"name": Amodu, "age": 28, "home_address": Akinwummi Street, "emial_address": amoduchojo27@gmail.com}

            expected = {"name": Amodu, "age": 28, "home_address": Akinwummi Street, "emial_address": amoduchojo27@gmail.com}
            actual = university_record_function.display_student_record(student_record)

            self.assertEqual(expected, actual)




if __name__ == '__main__':
    unittest.main()
