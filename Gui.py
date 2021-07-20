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

    def equal(self):
        answer = 0
        prior = self.ids.num_input.text
        if '+' in prior:
            num_equal = prior.split('+')
            print(num_equal)
            for i in num_equal:
                answer = answer + int(i)
            self.ids.num_input.text = str(answer)

        elif '-' in prior:
            num_equal = prior.split('-')
            print(num_equal)
           # for i in num_equal:
            answer = int(num_equal[0])-int(num_equal[1])
            self.ids.num_input.text = str(answer)

        elif '×' in prior:
            num_equal = prior.split('×')
            print(num_equal)
           # for i in num_equal:
            answer = int(num_equal[0])*int(num_equal[1])
            self.ids.num_input.text = str(answer)

        elif '÷' in prior:
            num_equal = prior.split('÷')
            print(num_equal)
           # for i in num_equal:
            answer = int(num_equal[0])/int(num_equal[1])
            self.ids.num_input.text = str(answer)


    def auto(self):
        prior = self.ids.num_input.text
        print(prior)
        print(len(prior))
        answer = 0
        if len(prior)>=3:
            if '+' in prior:

                num_add = prior.split('+')
                del num_add[-1]
                for i in num_add:
                    answer = answer + int(i)
                self.ids.num_input.text = str(answer)+'+'

        if len(prior)>=3:
            if '-' in prior:

                num_sub = prior.split('-')
                del num_sub[-1]
                print(num_sub)
                #for i in num_add:
                answer = int(num_sub[0])-int(num_sub[1])
                self.ids.num_input.text = str(answer)+'-'


    def clear(self):
        self.ids.num_input.text = '0'

    def button_press(self, button):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''
            self.ids.num_input.text = f'{button}'
        else:
            self.ids.num_input.text = f'{prior}{button}'

    def backspace(self, button):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''
            self.ids.num_input.text = f'{button}'
        else:
            self.ids.num_input.text = f'{prior}{button}'

    def extra(self):
        pass

    def back(self):
        pass

    def add(self):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''

        elif prior[-1]=='÷':
            pass
        elif prior[-1]=='+':
            pass
        elif prior[-1] == '-':
            pass
        elif prior[-1] == '×':
            pass

        else:
            self.ids.num_input.text = f'{prior}+'
            self.auto()

    def sub(self):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''

        elif prior[-1]=='÷':
            pass
        elif prior[-1]=='+':
            pass
        elif prior[-1] == '-':
            pass
        elif prior[-1] == '×':
            pass

        else:
            self.ids.num_input.text = f'{prior}-'
            self.auto()

    def mul(self):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''

        elif prior[-1]=='÷':
            pass
        elif prior[-1]=='+':
            pass
        elif prior[-1] == '-':
            pass
        elif prior[-1] == '×':
            pass

        else:
            self.ids.num_input.text = f'{prior}×'

    def div(self):
        prior = self.ids.num_input.text
        if prior == '0':
            self.ids.num_input.text = ''

        elif prior[-1]=='÷':
            pass
        elif prior[-1]=='+':
            pass
        elif prior[-1] == '-':
            pass
        elif prior[-1] == '×':
            pass

        else:
            self.ids.num_input.text = f'{prior}÷'

           # prior = f'{prior}÷'
           # self.sign_man(prior)




class CalcApp(App):
    def build(self):
        return CalcRun()


if __name__ == '__main__':
    CalcApp().run()
