from pynput.keyboard import Key,Controller
from pynput import keyboard
import time


no_action=[Key.up,Key.left,Key.down,Key.right,Key.ctrl,Key.alt,Key.caps_lock,Key.tab,Key.f1,Key.f2,Key.f3,Key.f4,Key.f5,Key.f6,Key.f7,Key.f8,Key.f9,Key.f10,Key.f11,Key.f12,Key.insert,Key.print_screen,Key.delete,Key.home,Key.page_up,Key.page_down,Key.end,Key.backspace,Key.enter,Key.shift]
keyboar = Controller()
word=[]
now=0

def timer():
    global now
    now=(int(time.strftime("%M%S")))

timer()


def deleting():
    keyboar.press(Key.backspace)
    keyboar.release(Key.backspace)


done = (int(time.strftime("%M%S")))

def on_press(key):
    global now
    global done
    global word

    nnow=(int(time.strftime("%M%S")))

    if done >=(nnow-5):
        word=[]
    else:
        pass


    if now == 0:
        pass


    elif now <= (nnow-5):

        if key in no_action:
            pass
        elif str(key)== 'Key.esc':

            return False
        else:
            word.append(key)


            if str(key) == 'Key.space':

                up=0
                wordy =[]
                try:

                    while True:
                        rr=str(word[up])
                        wordy.append(rr[1])
                        up+=1
                        if up==len(word)-1:
                            break


                    zero=0
                    final_word=''

                    while True:
                        final_word=final_word+(wordy[zero])
                        zero+=1
                        if zero==len(wordy):
                            break
    #                final=(str(final_word))
                    word=[]

                    with open("list.txt",encoding='utf-8')as searching:
                        if final_word in searching.read():
                            pass

                        else:
                            for i in range(len(final_word)+1):
                                deleting()
                            keyboar.press(Key.shift)
                            keyboar.press(Key.alt)
                            keyboar.release(Key.shift)
                            keyboar.release(Key.alt)

                            keyboar.type(final_word)
                            keyboar.press(Key.space)
                            keyboar.release(Key.space)

                            timer()
                            word=[]
                            done = (int(time.strftime("%M%S")))


                except IndexError:
                    pass

    else:
        pass


with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()