import quizLib as ql
import pytest
from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

#----------------------------------------------------------
@given('software chooses to ask an addition question')
def software_chooses_to_ask_an_addition_question():
    global sys
    sys = ql.System()
    sys.opNum = 0

#----------------------------------------------------------

@scenario('addition.feature', 'Software addition is correct', example_converters=dict(n1=int, n2=int, result=int))
def test_software_addition_is_correct():
    pass

@given('the software has chosen to ask an addition question')
def the_software_has_chosen_to_ask_an_addition_question():
    assert sys.opNum == 0

@when('I have a number <n1>')
def i_have_a_number_n1(n1):
    pass

@when('a number <n2>')
def a_number_n2(n2):
    pass

@then('the correct result should be <result>')
def the_correct_result_should_be_result(result):
    assert ql.getResult(n1, n2, 0) == result
#----------------------------------------------------------

@scenario('addition.feature', 'Correct user answer', example_converters=dict(n1=int, n2=int, e=int, result=int, xpoints=int, xq=int))
def test_correct_user_answer():
    pass

#Given is done

#When is done

#When and is done

@when('the user enters a number <e>')
def the_user_enters_a_number_e(e):
    assert 0

@when('the correct answer is <result>')
def the_correct_answer_is_result(result):
    assert 0

@then('the number of points should increase by 1 to give <xpoints>')
def the_number_of_points_should_increase_by_1_to_give_xpoints(xpoints):
    assert 0

@then('the number of questions remaining should decrease by 1 to give <xq>')
def the_number_of_questions_remaining_should_decrease_by_1_to_give_xq(xq):
    assert 0

#----------------------------------------------------------
@scenario('addition.feature', 'Incorrect user answer number', example_converters=dict(n1=int, n2=int, e=int, result=int, xpoints=int, xq=int))
def test_incorrect_user_answer_number():
    pass

#Given is done

#When is done

#When and 1 is done

@when('the user enters an incorrect number <e>')
def the_user_enters_an_incorrect_number_e(e):
    assert 0

#When and 3 is done

@then('the number of points should stay the same to give <xpoints>')
def the_number_of_points_should_stay_the_same_to_give_xpoints(xpoints):
    assert 0

#Then and is done

#----------------------------------------------------------

@scenario('addition.feature', 'Invalid user input', example_converters=dict(n1=int, n2=int, e=string, xpoints=int, xq=int))
def test_invalid_user_input():
    pass

#Given is done

#When is done

#When and 1 is done

@when('the user enters an invalid entry <e>')
def the_user_enters_an_invalid_entry_e(e):
    assert 0

@then('the number of questions remaining should stay the same to give <xq>')
def the_number_of_questions_remaining_should_stay_the_same_to_give_xq(xq):
    assert 0

@then('the same number <n1> and <n2> should be asked again')
def the_same_number_n1_and_n2_should_be_asked_again():
    assert 0
