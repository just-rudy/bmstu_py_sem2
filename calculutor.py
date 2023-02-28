# Серышева ИУ7-24Б сложение и вычитание вещественных чисел в 5й системе счисления

from tkinter import *
from tkinter import messagebox


class SuperButton(Button):

    def __init__(self, btn_text, btn_command, x, y, width, heigth, smth):
        self.smth = str(smth)
        super().__init__()
        self['text'] = btn_text
        if self.smth != "5":
            self['command'] = self.print_smth
        else:
            self['command'] = btn_command
        canvas.create_window(x, y, window=self, width=width, height=heigth)

    def print_smth(self):
        text = entry_num.get() + self.smth
        entry_num.delete(0, END)
        entry_num.insert(0, text)
        return 0


def check_is_fiveish(num):
    is_correct_five = True
    if len(num) == 0 or num.count("-") > 1 or num.find("-") > 0 or num.count(".") > 1 or num.count(",") > 0:
        is_correct_five = False
    else:
        for i in num:
            if i not in "01234.":
                is_correct_five = False
                break
    return is_correct_five


def clear():
    entry_num.delete(0, END)


def check_words(num):
    answer_field.delete(0, END)
    is_correct = True
    if not check_is_fiveish(num):
        is_correct = False
        answer_field.delete(0, END)
        answer_field.insert(0, "Error")
    return is_correct


def calc_minus(num1, num2):
    after_dot_num1, after_dot_num2 = "", ""
    if "." in num1:
        pre_dot_num1 = num1[:num1.find(".")]
        after_dot_num1 = num1[num1.find(".") + 1:]
    else:
        pre_dot_num1 = num1

    if "." in num2:
        pre_dot_num2 = num2[:num2.find(".")]
        after_dot_num2 = num2[num2.find(".") + 1:]
    else:
        pre_dot_num2 = num2

    down_from_five = 0  # если вычитание
    ans_float = ""
    curr_ind = -1
    if len(after_dot_num1) != len(after_dot_num2):
        after_dot_num1 += "0" * (max(len(after_dot_num1), len(after_dot_num2)) - len(after_dot_num1))
        after_dot_num2 += "0" * (max(len(after_dot_num1), len(after_dot_num2)) - len(after_dot_num2))
    len_fix = len(after_dot_num1)

    while abs(curr_ind) <= len_fix:
        digit1 = after_dot_num1[curr_ind]
        digit2 = after_dot_num2[curr_ind]
        digit_sum = int(digit1) - int(digit2) - down_from_five
        if digit_sum < 0:
            down_from_five = 1
            digit_sum = 5 - digit_sum
        else:
            down_from_five = 0
        ans_float = str(digit_sum) + ans_float
        curr_ind -= 1
    # print(over_the_five, "-", ans_float)

    ans_int = ""
    curr_ind = -1
    len1 = len(pre_dot_num1)
    len2 = len(pre_dot_num2)
    while abs(curr_ind) <= max(len1, len2):
        digit1 = pre_dot_num1[curr_ind] if abs(curr_ind) <= len1 else 0
        digit2 = pre_dot_num2[curr_ind] if abs(curr_ind) <= len2 else 0
        digit_sum = int(digit1) - int(digit2) - down_from_five
        if digit_sum < 0:
            digit_sum = 5 - digit_sum
            down_from_five = 1
        else:
            down_from_five = 0
        ans_int = str(digit_sum) + ans_int
        curr_ind -= 1

    return ans_int + "." + ans_float


def calc_plus(num1, num2):
    after_dot_num1, after_dot_num2 = "", ""
    # выделение целой и вещественной частей для сложения их отдельно
    if "." in num1:
        pre_dot_num1 = num1[:num1.find(".")]
        after_dot_num1 = num1[num1.find(".") + 1:]
    else:
        pre_dot_num1 = num1

    if "." in num2:
        pre_dot_num2 = num2[:num2.find(".")]
        after_dot_num2 = num2[num2.find(".") + 1:]
    else:
        pre_dot_num2 = num2

    over_the_five = 0  # переход через разряд
    ans_float = ""  # вычисленное значение вещественной части
    curr_ind = -1  # обрабатываемые символы
    if len(after_dot_num1) != len(after_dot_num2):
        after_dot_num1 += "0" * (max(len(after_dot_num1), len(after_dot_num2)) - len(after_dot_num1))
        after_dot_num2 += "0" * (max(len(after_dot_num1), len(after_dot_num2)) - len(after_dot_num2))
    len_fix = len(after_dot_num1)

    while abs(curr_ind) <= len_fix:
        digit1 = after_dot_num1[curr_ind] if abs(curr_ind) <= len_fix else 0
        digit2 = after_dot_num2[curr_ind] if abs(curr_ind) <= len_fix else 0
        digit_sum = int(digit1) + int(digit2) + over_the_five
        ans_float = str(digit_sum % 5) + ans_float
        over_the_five = digit_sum // 5
        curr_ind -= 1
    # print(over_the_five, "-", ans_float)

    ans_int = ""
    curr_ind = -1
    len1 = len(pre_dot_num1)
    len2 = len(pre_dot_num2)
    while abs(curr_ind) <= max(len1, len2):
        digit1 = pre_dot_num1[curr_ind] if abs(curr_ind) <= len1 else 0
        digit2 = pre_dot_num2[curr_ind] if abs(curr_ind) <= len2 else 0
        digit_sum = int(digit1) + int(digit2) + over_the_five
        ans_int = str(digit_sum % 5) + ans_int
        over_the_five = digit_sum // 5
        curr_ind -= 1
    if over_the_five > 0:
        ans_int = str(over_the_five) + ans_int
    return ans_int + "." + ans_float


def start_counting():
    frase_to_calc = entry_num.get()
    frase_to_calc = frase_to_calc.replace(" ", "")
    ans = "0"
    if len(frase_to_calc) < 1:
        check_words("5")
        return 0
    # if frase_to_calc[-1] not in "+-":
    #     frase_to_calc += "+"
    if frase_to_calc[0] != "-":
        frase_to_calc = "+" + frase_to_calc
    while frase_to_calc.count("+") + frase_to_calc.count("-") > 0:
        find_plus = frase_to_calc.find("+")
        find_minus = frase_to_calc.find("-")
        if find_plus != -1 and find_plus < find_minus or find_minus == -1:
            frase_to_calc = frase_to_calc[find_plus + 1:]
            i = 0
            num = ""
            while i < len(frase_to_calc) and frase_to_calc[i] not in "+-":
                num += frase_to_calc[i]
                i += 1
            frase_to_calc = frase_to_calc[i:]

            ans = calc_plus(ans, num)

        elif find_minus != -1 and find_minus < find_plus or find_plus == -1:
            frase_to_calc = frase_to_calc[find_minus + 1:]
            i = 0
            num = ""
            while i < len(frase_to_calc) and frase_to_calc[i] not in "+-":
                num += frase_to_calc[i]
                i += 1
            frase_to_calc = frase_to_calc[i:]
            if float(ans) < float(num):
                ans = str((-1) * float(calc_minus(num, ans)))
            else:
                ans = calc_minus(ans, num)
    answer_field.delete(0, END)
    answer_field.insert(0, ans)
    return ans


def show_info():
    messagebox.showinfo("info", "Введите выражение(сложение и вычитание) в верхнее поле в 5сс, ответ будет в нижнем поле")

root = Tk()
root.title("Калькулятор")
root.geometry("400x504")

canvas = Canvas(bg="white", width=400, height=504)
canvas.pack(anchor=CENTER)

entry_num = Entry()
canvas.create_window(120, 40, window=entry_num, width=200, height=30)

answer_field = Entry()
canvas.create_window(120, 100, window=answer_field, width=200, height=30)

btn_clear = SuperButton("Clear", clear, 300, 40, 100, 30, 5)
btn_calc = SuperButton("=", start_counting, 300, 180, 80, 40, 5)
btn_minus = SuperButton("-", start_counting, 60, 180, 80, 40, "-")
btn_plus = SuperButton("+", start_counting, 180, 180, 80, 40, "+") # TODO + place this too
btn_one = SuperButton("1", start_counting, 180, 250, 80, 40, "1")  # TODO 1 place theese buttons in the right place
btn_two = SuperButton("2", start_counting, 300, 250, 80, 40, "2")  # TODO 2 place theese buttons in the right place
btn_three = SuperButton("3", start_counting, 60, 320, 80, 40, "3")  # TODO 3 place theese buttons in the right place
btn_four = SuperButton("4", start_counting, 180, 320, 80, 40, "4")  # TODO 4 place theese buttons in the right place
btn_zero = SuperButton("0", start_counting, 60, 250, 80, 40, "0")  # TODO 0 place theese buttons in the right place
btn_dot = SuperButton(".", start_counting, 300, 320, 80, 40, ".")  # TODO . place theese buttons in the right place
btn_info = SuperButton("?", show_info, 300, 100, 80, 40, 5)  # TODO . place theese buttons in the right place

root.mainloop()
