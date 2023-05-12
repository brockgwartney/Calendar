from gui import *

def main():

    window = Tk()
    window.title('Calendar')
    window.geometry('1001x650')
    window.resizable(False,False)
    GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()