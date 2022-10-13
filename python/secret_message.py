from tkinter import messagebox, simpledialog, Tk

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message')
    return message

def is_even(number):
    return number % 2 == 0

def get_even_letters(massage):
    even_letters = []
    for counter in range(0, len(massage)):
        if is_even(counter):
            even_letters.append(massage[counter])
    return even_letters

def get_odd_letters(massage):
    odd_letters = []
    for counter in range(0, len(massage)):
        if not is_even(counter):
            odd_letters.append(massage[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message2 = message + 'x'
    even_letters = get_even_letters(message2)
    odd_letters = get_odd_letters(message2)
    for counter in range(0, int(len(message2) / 2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_massage = ''.join(letter_list)
    return new_massage

root = Tk()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = swap_letters(message)
        messagebox.showinfo('Cipheitext of the secret massage is:', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = swap_letters(message)
        messagebox.showinfo('Plaintext of the secret massage is:', decrypted)
    else:
        break

root.mainloop()