import DecisionTree as dt


# def test_create_stack(self):
#         # ARRANGE
#         my_stack = dt(1)
#         # ACT
#         actual = my_stack.is_empty()
#         # ASSERT
#         self.assertTrue(actual)

def test_tree_correct_output(self):
    #arrange
    my_tree = dt()
    dt.add("Do you want to take the class?")
    dt.add("Do it!","R")
    dt.add("Then don't", "L")
    #act
    actual = dt.print()
    #assert
    self.assertTrue(actual)