import io
import unittest.mock

from mock import patch

from examples import quiz


def get_first(iterable):
    for item in iterable:
        return item


class TestQuiz_readQuestions(unittest.TestCase):
    '''Testing the quiz'''

    def test_loadQuestions(self):
        '''Testing read_questions methods'''
        questions = quiz.read_questions("test_questions.txt")
        expected_questions = {'This is the question?': 'answer'}
        self.assertEqual(expected_questions, questions)


class TestQuiz_askQuestions(unittest.TestCase):
    '''Testing the quiz.ask_questions'''

    def setUp(self):
        '''Set up testing objects'''
        self.questions = {'This is the question?': 'answer'}
        self.question, self.answer = get_first(self.questions.items())

    def test_correctAnswers(self):
        '''Testing ask_question correct'''
        expected = ([self.question], [])
        with patch('builtins.input', return_value=self.answer) as _raw_input:
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.assertEqual(expected, quiz.ask_questions(self.questions))
                _raw_input.assert_called_once_with(self.question + ' = ')
                self.assertEqual('Correct!', fake_out.getvalue().strip())

    def test_wrongAnswers(self):
        expected = ([], [self.question])
        with patch('builtins.input', return_value="Not the answer") as raw_input:
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                self.assertEqual(expected, quiz.ask_questions(self.questions))
                raw_input.assert_called_once_with(self.question + ' = ')
                self.assertEqual('Wrong! The correct answer is answer.', fake_out.getvalue().strip())


class TestQuiz_stats(unittest.TestCase):
    '''Testing the quiz.stats'''

    def setUp(self):
        '''Set up testing objects'''
        self.questions = {'This is the question?': 'answer'}
        self.question, self.answer = get_first(self.questions.items())

    def test_correctAnswers(self):
        '''Testing stats method for correct answers'''
        # print(f"\n\nFirst question Key is '{self.question}'.\n\n")
        correct = [self.question]
        wrong = []
        expectedOutput = '**** STATS ****\n\nYou answered 1 questions correctly and 0 questions wrong.'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            quiz.stats(correct, wrong, self.questions)
            self.assertEqual(expectedOutput, fake_out.getvalue().strip())

    def test_wrongAnswers(self):
        '''Testing stats method for wrong answers'''
        correct = []
        wrong = [self.question]
        expectedOutput = '**** STATS ****\n\nYou answered 0 questions correctly and 1 questions wrong.\n' \
                         'These would have been the correct answers:\n' \
                         '  This is the question? = answer'
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            quiz.stats(correct, wrong, self.questions)
            self.assertEqual(expectedOutput, fake_out.getvalue().strip())


if __name__ == '__main__':
    unittest.main(verbosity=2)
