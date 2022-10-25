from win10toast import ToastNotifier
from pushbullet import Pushbullet

windows = ToastNotifier()

title = input("enter title of the notification : ")
message = input('enter body of notification : ')
duration = int(input("enter duration of message : "))

windows.show_toast(title, message, duration = duration)

access = "o.Qk10UlkmdhBd9qLoI6LZePYeG5gP3M7P"

mobile = Pushbullet(access)
push = mobile.push_note(title, message)

