import subprocess


def show_notification(title, message=''):
    subprocess.call(['notify-send', title, message])

