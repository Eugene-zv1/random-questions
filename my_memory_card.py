from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup,QRadioButton, QHBoxLayout,QGroupBox,  QWidget , QPushButton , QLabel , QVBoxLayout
from random import shuffle , choice
class Question():
    def __init__(self,q, r_a, w_a1,w_a2,w_a3):
        self.question = q
        self.right_answer = r_a
        self.wrong_answer1 = w_a1
        self.wrong_answer2 = w_a2
        self.wrong_answer3 = w_a3

questions = []
questions.append(Question('Какая область  Росии считается уралом ???','Свердловская', 'Еврейский автономный округ','Республика татастан','Московская область'))
questions.append(Question('Какая страна БОЛЬШЕ??','Россия', 'Китай','Казахстан','Египет'))
questions.append(Question('Что хочет делать большая часть людей?', 'Отдыхать','Спать','Работать','Играть'))
questions.append(Question('Что какое блюдо питательней??', ' гречка с хлебом','быстрое питание',' макароны','бутерброд'))


def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rtb.setChecked(False)
    rtb1.setChecked(False)
    rtb2.setChecked(False)
    rtb3.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
        

def show_result():
    button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    AnsGroupBox.show()
    print('Статистика')
    print('Всего вопросов:',main_win.total)
    print('Правильных ответов:', main_win.score)
    print('Рейтинг:',main_win.score / main_win.total *100,'%' )
def ask(q:Question):
    shuffle(buttons)
    buttons[0].setText(q.right_answer)
    buttons[1].setText(q.wrong_answer1)
    buttons[2].setText(q.wrong_answer2)
    buttons[3].setText(q.wrong_answer3)
    winner.setText(q.question)
    winner2.setText(q.right_answer)
    show_question()


def check_answer():
    if buttons[0].isChecked():
        winner1.setText('Правильно!!!!')
        main_win.score += 1
        show_result()
    elif buttons[1].isChecked() or buttons[2].isChecked() or buttons[3].isChecked():
        winner1.setText('Неправильно!')
        show_result()     

def next_question():
    main_win.total += 1
    rand_q = choice(questions)
    ask(rand_q)
     
app = QApplication([])


main_win = QWidget()

main_win.score = 0
main_win.total = 0

main_win.setWindowTitle('Memory Card')
main_win.resize(400,400)

winner = QLabel('Вопрос:')
winner1 = QLabel('Правильно/Неправильно')
winner2 = QLabel('Правильно!')
button = QPushButton('Ответить')
button1 = QPushButton('Следующий вопрос')

rtb = QRadioButton('1')
rtb1 = QRadioButton('2')
rtb2 = QRadioButton('3')
rtb3 = QRadioButton('4')

buttons = [rtb , rtb1 , rtb2 , rtb3]

RadioGroup = QButtonGroup()
RadioGroup.addButton(rtb)
RadioGroup.addButton(rtb1)
RadioGroup.addButton(rtb2)
RadioGroup.addButton(rtb3)

RadioGroupBox = QGroupBox('Варианты ответов')

V_line = QVBoxLayout()
V_line1 = QVBoxLayout()
V_line2 = QVBoxLayout()

H_line = QHBoxLayout()
H_line1 = QHBoxLayout()
H_line2 = QHBoxLayout()
H_line3 = QHBoxLayout()

V_line.addWidget(rtb)
V_line.addWidget(rtb1)
V_line1.addWidget(rtb2)
V_line1.addWidget(rtb3)

H_line.addLayout(V_line)
H_line.addLayout(V_line1)

RadioGroupBox.setLayout(H_line)
AnsGroupBox = QGroupBox('Результат теста')
AnsGroupBox.hide()
V_line3 = QVBoxLayout()
V_line3.addWidget(winner1)
V_line3.addWidget(winner2)
# V_line3.addWidget(button1)
AnsGroupBox.setLayout(V_line3)
H_line1.addWidget(winner)
H_line2.addWidget(RadioGroupBox)
H_line2.addWidget(AnsGroupBox)
H_line3.addWidget(button) 

V_line2.addLayout(H_line1)
V_line2.addLayout(H_line2)
V_line2.addLayout(H_line3)

main_win.setLayout(V_line2)

next_question()
button.clicked.connect(start_test)
main_win.show()
app.exec_()