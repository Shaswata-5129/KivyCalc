import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen ,ScreenManager
Window.size = (500, 700)


class auto_sum(Screen):
    pass
class auto_sub(Screen):
    pass
class auto_mul(Screen):
    pass
class auto_div(Screen):
    pass
class selector(Screen):
    pass

class WindowsManager(ScreenManager):
    pass


class CalcRun(Screen):
    # To find the answer if we press =
    def equal(self):
        answer = 0.00

        prior = self.ids.num_input.text
        if '+' in prior:
            num_equal = prior.split('+')
            print(num_equal)
            for i in num_equal:
                answer = answer + float(i)
            answer = str(answer)

        elif '-' in prior:
            if prior[-1] == '-':
                pass
            else:
                num_equal = prior.split('-')
                print(num_equal)
                # for i in num_equal:
                answer = float(num_equal[0]) - float(num_equal[1])
                answer = str(answer)

        elif '×' in prior:
            if prior[-1] == '×':
                pass
            else:
                num_equal = prior.split('×')
                print(num_equal)
                # for i in num_equal:
                answer = float(num_equal[0]) * float(num_equal[1])
                answer = str(answer)

        elif '÷' in prior:
            if prior[-1] == '÷':
                pass
            else:
                num_equal = prior.split('÷')
                print(num_equal)
                # for i in num_equal:
                answer = float(num_equal[0]) / float(num_equal[1])
                answer = str(answer)


        if ('.') in answer:
            find = answer.index('.')
            if answer[find + 1] == '0':
                answer = answer[:find]
            else:
                pass
        self.ids.num_input.text = answer

    # As all the answers is in float for point answers, this will determine if the point has any value or not, if not then Simply remove point
    def answer(self, answer):
        prior = self.ids.num_input.text  # To put the sign after the auto funcs
        print(prior, 'FInal')
        if prior[-1] == '+' or '-' or '÷' or '×':
            sign = prior[-1]
            print(prior[-1], 'prior-1')  # To put the sign after the auto funcs
        else:
            sign = 0
            print(sign, 'sign')
        answer = str(answer)
        if ('.') in answer:
            find = answer.index('.')
            if answer[find + 1] == '0':
                answer = answer[:find]
            else:
                pass
        self.ids.num_input.text = answer + sign

    # To print answer if we continue pressing buttons
    def auto(self, num_list):
        # Differentiating LABEL with INNER NUMBER
        prior = self.ids.num_input.text
        if prior[-1] == '+' or '-':
            answer = 0
        else:
            answer = 1
        print(prior)
        # Checking the condition for auto sum
        num_list = num_list[:-1]
        print(num_list, 'num_list')
        if len(num_list) == 2:

            # For Addition of auto sum
            if prior[-1] == '+':
                for i in num_list:
                    answer = answer + float(i)
            # For Subtraction of Auto Sum
            elif prior[-1] == '-':
                answer = float(num_list[0]) - float(num_list[1])
            # For Multiplication of Auto Sum
            elif prior[-1] == '×':
                answer = float(num_list[0]) * float(num_list[1])
            # For Division of Auto Sum
            elif prior[-1] == '÷':
                answer = float(num_list[0]) / float(num_list[1])

            self.answer(answer)



    # to clear the total screen
    def clear(self):
        self.ids.num_input.text = '0'

    # to assign the numbers and signs and all button according to the label
    def button_press(self, button):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''
            self.ids.num_input.text = f'{button}'
        else:
            self.ids.num_input.text = f'{prior}{button}'

    def backspace(self):
        prior = self.ids.num_input.text
        if prior == '0':
            pass
        else:
            if len(prior) == 1:
                self.ids.num_input.text = '0'
            else:
                self.ids.num_input.text = f'{prior[:-1]}'

    def extra(self):
        pass

    def back(self):
        pass

    # To correct the sign function of calculator
    def math_sign(self, sign):
        num_list = []
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''
        # If last str is +,-,*,/ skip
        elif prior[-1] == '÷':
            pass
        elif prior[-1] == '+':
            pass
        elif prior[-1] == '-':
            pass
        elif prior[-1] == '×':
            pass
        # if signs are not there it will simply add the strs
        else:
            prior = f'{prior}{sign}'
            self.ids.num_input.text = prior
            num_list = prior.split(sign)
            print('numList', num_list)
            self.auto(num_list)


kv = Builder.load_file('calc.kv')

# Mainframe of pogram
class CalcApp(App):
    def build(self):
        return kv


# running the programe
if __name__ == '__main__':
    CalcApp().run()