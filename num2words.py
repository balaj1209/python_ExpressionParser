import tkinter as tk

class NumberConverter:
    def __init__(self):
        self.number_dict = {
            0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
            17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty", 30: "Thirty", 40: "Forty",
            50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety", 100: "One Hundred"
            }

    def number_to_words(self, user_input):
        if type(user_input) == str:
            if '.' in user_input:
                if user_input[0] == ".":
                    user_input = "0" + user_input
                elif user_input[0] == "-" and user_input[1] == "." :
                    user_input = user_input[0] + "0" + user_input[1:]
                integer_part, fractional_part = str(user_input).split('.')
                integer_words = self.number_to_words(integer_part)
                fractional_part = ' '.join(self.number_dict[int(i)] for i in fractional_part)
                if user_input.startswith('-'):
                    return  integer_words + " point " + fractional_part
                else:
                    return integer_words + " point " + fractional_part
            else:
                if user_input.startswith('-'):
                    return "Minus " + self.number_to_words(user_input[1:])
                elif user_input == '0':
                    return "Zero"
                number=int(user_input)
                if int(user_input) < 100:
                    if number in self.number_dict:
                        return self.number_dict[number]
                    else:
                        if number < 0:
                            return "Minus " + self.number_to_words(number)
                        remainder = number % 10
                        quotient = number // 10
                        c = quotient * 10
                        if remainder == 0:
                            return self.number_dict[c]
                        else:
                            return self.number_dict[c] + " " + self.number_dict[remainder]

                elif number< 1000:
                    remainder = number % 100
                    b = self.number_to_words(str(remainder))
                    quotient = number // 100
                    a = self.number_to_words(str(quotient))
                    if remainder == 0:
                        result = a + " Hundred"
                    else:
                        result = a + " Hundred " + b
                    return result               

                elif number < 100000:
                    remainder= number % 1000
                    b = self.number_to_words(str(remainder))
                    quotient = number // 1000
                    if b == "Zero":
                        result = self.number_to_words(str(quotient)) + " Thousand"
                    else:
                        result = self.number_to_words(str(quotient)) + " Thousand " + b
                    return result

                elif number < 10000000:
                    remainder = number% 100000
                    b = self.number_to_words(str(remainder))
                    quotient = number // 100000
                    if b == "Zero":
                        result = self.number_to_words( str(quotient)) + " Lakh "
                    else:
                        result = self.number_to_words( str(quotient)) +" Lakh "+ b
                    return result
              
                elif number < 1000000000:
                    remainder = number % 10000000
                    b = self.number_to_words(str(remainder))
                    quotient = number // 10000000
                    if b == "Zero":
                        result = self.number_to_words(str(quotient)) + " Crore"
                    else:
                        result = self.number_to_words(str(quotient)) +" Crore"+ b
                    return result
                if number ==1000000000:
                    return "Hundred crore"
                else:
                    raise ValueError("Please enter a number between 0 and 100000000.")

class NumberConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Number to Words Converter")

        self.label = tk.Label(master, text="Enter the Number")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

        self.exit_button = tk.Button(master, text="Exit", command=master.destroy)
        self.exit_button.pack()

        self.converter = NumberConverter()

    def convert(self):
        user_input = self.entry.get()
        try:
            result = self.converter.number_to_words(user_input)
            self.output_label.config(text=result + " only")
        except ValueError as ve:
            self.output_label.config(text=str(ve))
        except Exception as e:
            self.output_label.config(text="Error: " + str(e))

root = tk.Tk()
my_gui = NumberConverterGUI(root)
root.mainloop()
