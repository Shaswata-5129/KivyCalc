import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (500, 700)


class CalcGrid(GridLayout):

    def __init__(self, **kwargs):
        super(CalcGrid, self).__init__(**kwargs)
        self.cols = 1

        # self.add_widget(Label(text='Input your Number: '))
        self.userinput = TextInput(multiline=False)
        self.add_widget(self.userinput)
        # Inside Self funcs
        self.inside = GridLayout()
        self.inside.cols = 4
        self.inside.rows = 5

        # self.nine = Button(text= '9',font_size=40)
        self.eight = Button(text='8', font_size=40)
        self.seven = Button(text='7', font_size=40)
        self.six = Button(text='6', font_size=40)
        self.five = Button(text='5', font_size=40)
        self.four = Button(text='4', font_size=40)
        self.three = Button(text='3', font_size=40)
        self.two = Button(text='2', font_size=40)
        self.one = Button(text='1', font_size=40)
        self.zero = Button(text='0', font_size=40)
        self.C = Button(text='C', font_size=40)
        self.CC = Button(text='CC', font_size=40)
        self.plus = Button(text='+', font_size=40)
        self.minus = Button(text='-', font_size=40)
        self.mul = Button(text='*', font_size=40)
        self.div = Button(text='/', font_size=40)
        self.equal = Button(text='=', font_size=40)

        self.inside.add_widget(self.nine)
        self.inside.add_widget(self.eight)
        self.inside.add_widget(self.seven)
        self.inside.add_widget(self.plus)
        self.inside.add_widget(self.six)
        self.inside.add_widget(self.five)
        self.inside.add_widget(self.four)
        self.inside.add_widget(self.minus)
        self.inside.add_widget(self.three)
        self.inside.add_widget(self.two)
        self.inside.add_widget(self.one)
        self.inside.add_widget(self.mul)
        self.inside.add_widget(self.C)
        self.inside.add_widget(self.zero)
        self.inside.add_widget(self.CC)
        self.inside.add_widget(self.div)

        # self.nine.bind(on_press=self.pressed)

        # self.add_widget(self.inside)


class CalcRun(Widget):
    # To find the answer if we press =
    def equal(self):
        answer = 0.00

        prior = self.ids.num_input.text
        if '+' in prior:
            num_equal = prior.split('+')
            print(num_equal)
            for i in num_equal:
                answer = answer + float(i)
            # self.ids.num_input.text = str(answer)
            self.answer(answer)

        elif '-' in prior:
            if prior[-1] == '-':
                pass
            else:
                num_equal = prior.split('-')
                print(num_equal)
                # for i in num_equal:
                answer = int(num_equal[0]) - int(num_equal[1])
            # self.ids.num_input.text = str(answer)
            self.answer(answer)

        elif '×' in prior:
            if prior[-1] == '×':
                pass
            else:
                num_equal = prior.split('×')
                print(num_equal)
                # for i in num_equal:
                answer = int(num_equal[0]) * int(num_equal[1])
            # self.ids.num_input.text = str(answer)
            self.answer(answer)

        elif '÷' in prior:
            if prior[-1] == '÷':
                pass
            else:
                num_equal = prior.split('÷')
                print(num_equal)
                # for i in num_equal:
                answer = int(num_equal[0]) / int(num_equal[1])
            # self.ids.num_input.text = str(answer)
            self.answer(answer)
    # As all the answers is in float for point answers, this will determine if the point has any value or not, if not then Simply remove point
    def answer(self,answer):
        prior = self.ids.num_input.text      # To put the sign after the auto funcs
        print(prior, 'FInal')
        if prior[-1] == '+' or '-' or '÷' or '×':
            sign = prior[-1]
            print(prior[-1],'prior-1')# To put the sign after the auto funcs
        else:
            sign = 0
            print(sign,'sign')
        answer = str(answer)
        if ('.') in answer:
            find = answer.index('.')
            if answer[find + 1] == '0':
                answer = answer[:find]
            else:
                pass
        self.ids.num_input.text = answer+sign
    # To print answer if we continue pressing buttons
    def auto(self,num_list):
        # Differentiating LABEL with INNER NUMBER
        prior = self.ids.num_input.text
        if prior[-1] =='+' or '-':
            answer = 0
        else:
            answer = 1
        print(prior)
        # Checking the condition for auto sum
        num_list = num_list[:-1]
        print(num_list,'num_list')
        if len(num_list)==2:

            # For Addition of auto sum
            if prior[-1]=='+':
                for i in num_list:
                    answer = answer + float(i)
            # For Subtraction of Auto Sum
            elif prior[-1]=='-':
                answer = float(num_list[0])-float(num_list[1])
            # For Multiplication of Auto Sum
            elif prior[-1]=='×':
                answer = float(num_list[0])*float(num_list[1])
            # For Division of Auto Sum
            elif prior[-1]=='÷':
                answer = float(num_list[0])/float(num_list[1])



            self.answer(answer)
        '''
        if prior[-1]=='+':
            prior = prior[:-1]
            print(prior)
            if '+' in prior:
                num_add = prior.split('+')
                print(num_add,'num_add')
                if len(num_add) == 2:
                    for i in num_add:
                        answer = answer + float(i)
                    answer = str(answer) + '+'
                    self.answer(answer)
        
        else:
            pass
        '''
        '''
        elif '-' in prior:
            num_sub = prior.split('-')
        elif '×' in prior:
            num_mul = prior.split('×')
        elif '÷' in prior:
            num_div = prior.split('÷')
     #   print(num_add,'num_add')
        '''

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
            if len(prior) ==1:
                self.ids.num_input.text = '0'
            else:
                self.ids.num_input.text = f'{prior[:-1]}'

    def extra(self):
        pass

    def back(self):
        pass

# To correct the sign function of calculator
    def math_sign(self,sign):
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
            print('numList',num_list)
            self.auto(num_list)



# Mainframe of pogram
class CalcApp(App):
    def build(self):
        return CalcRun()

# running the programe
if __name__ == '__main__':
    CalcApp().run()
