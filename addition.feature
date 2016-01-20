Feature: Addition questions
  As a software developer
  I want to check that the addition feature works correctly
  So that my software can function correctly

  Background:
    Given software chooses to ask an addition question

  Scenario Outline: Software addition is correct
    Given the software has chosen to ask an addition question
    When I have a number <n1>
    And a number <n2>
    Then the correct result should be <result>

    Examples:
    | n1    | n2   | result|
    | 2     | 4    | 6     |
    | 12    | 10   | 22    |
    | 1     | 5    | 6     |
    | 10    | 9    | 19    |
    | 11    | 7    | 18    |
    | 5     | 8    | 13    |
    | 0     | 0    | 0     |


  Scenario Outline: Correct user answer
    Given the software has chosen to ask an addition question
    When I have a number <n1>
    And a number <n2>
    And the user enters a number <e>
    And the correct answer is <result>
    Then the number of points should increase by 1 to give <xpoints>
    And the number of questions remaining should decrease by 1 to give <xq>

    Examples:
    | n1    | n2   | e     | result | xpoints | xq  |
    | 2     | 4    | 6     | 6      | 1       | 575 |
    | 12    | 10   | 22    | 22     | 2       | 574 |
    | 1     | 5    | 6     | 6      | 3       | 573 |
    | 10    | 9    | 19    | 19     | 4       | 572 |
    | 5     | 8    | 13    | 13     | 6       | 571 |
    | 11    | 7    | 18    | 18     | 5       | 570 |
    | 0     | 0    | 0     | 0      | 7       | 569 |

  Scenario Outline: Incorrect user answer number
    Given the software has chosen to ask an addition question
    When I have a number <n1>
    And a number <n2>
    And the user enters an incorrect number <e>
    And the correct answer is <result>
    Then the number of points should stay the same to give <xpoints>
    And the number of questions remaining should decrease by 1 to give <xq>

    Examples:
    | n1    | n2   | e     | result | xpoints | xq  |
    | 2     | 4    | 12    | 6      | 0       | 575 |
    | 12    | 10   | 22    | 22     | 0       | 574 |
    | 1     | 5    | 6     | 6      | 0       | 573 |
    | 10    | 9    | 19    | 19     | 0       | 572 |
    | 5     | 8    | 13    | 13     | 0       | 571 |
    | 11    | 7    | 18    | 18     | 0       | 570 |
    | 0     | 0    | 0     | 0      | 0       | 569 |

  Scenario Outline: Invalid user input
    Given the software has chosen to ask an addition question
    When I have a number <n1>
    And a number <n2>
    And the user enters an invalid entry <e>
    Then the number of points should stay the same to give <xpoints>
    And the number of questions remaining should stay the same to give <xq>
    And the same number <n1> and <n2> should be asked again

    Examples:
    | n1    | n2   | e     | xpoints | xq  |
    | 2     | 4    | jl123 | 0       | 576 |
    | 12    | 10   | 12h   | 0       | 576 |
    | 1     | 5    | foo   | 0       | 576 |
    | 10    | 9    | .asd  | 0       | 576 |
    | 12    | 4    | !?    | 0       | 576 |
    | 12    | 4    | ?     | 0       | 576 |
    | 12    | 4    | !     | 0       | 576 |
