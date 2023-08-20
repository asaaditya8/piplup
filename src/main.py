import os
import subprocess
from rich import print as rprint
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def greet():
    rprint("""Hello and
        welcome to...       
       _       _             
 _ __ (_)_ __ | |_   _ _ __  
| '_ \| | '_ \| | | | | '_ \ 
| |_) | | |_) | | |_| | |_) |
| .__/|_| .__/|_|\__,_| .__/ 
|_|     |_|           |_|    

This exercise compiles successfully. The remaining exercises contain a compiler
or logic error. The central concept behind Rustlings is to fix these errors and
solve the exercises. Good luck!

The source for this exercise is in `exercises/intro/intro1.rs`. Have a look!
Going forward, the source of the exercises will always be in the success/failure output.""")



class MyHandler(PatternMatchingEventHandler):
    def __init__(self, patterns=None, ignore_patterns=None,
                 ignore_directories=False, wait_for_process=False,
                 drop_during_process=False):
        super().__init__(
            patterns=patterns, ignore_patterns=ignore_patterns,
            ignore_directories=ignore_directories)

    def on_any_event(self, event):
        # print(event)
        return super().on_any_event(event)

    def on_closed(self, event):
        clear_screen()
        src_path = event.src_path

        x = subprocess.run(["ipython", src_path], capture_output=True)
        if x.returncode == 0:
            rprint(f'[green] ✅ Successfully ran {src_path}!')
            rprint('\n🎉 🎉 The code is working! 🎉 🎉\n')
            rprint('Output:\n====================')

            print(x.stdout.decode())

            # greet()
            rprint('\n====================')
            rprint("""You can keep working on this exercise,
or jump into the next one by removing the `[b]I AM NOT DONE[/b]` comment:

10 |  # what it outputs in your terminal. Try removing a semicolon and see what happens!
11 |  
12 |  # [b]I AM NOT DONE
13 |  """)
        else:
            rprint(f'⚠️  [red]Execution of {src_path} failed! Please try again. Here\'s the output:\n')

            print(x.stdout.decode())


path = '.'

event_handler = MyHandler(patterns=['exercises/*/*.ipynb'])
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        try:
            print('Welcome to watch mode! You can type \'help\' to get an overview of the commands you can use here.')
            x = input()

            if x in {'help', 'hint', 'clear', 'quit'}:
                if x == 'quit':
                    print("""Bye!
We hope you're enjoying learning about Python!
If you want to continue working on the exercises at a later point, you can simply run `piplup watch` again""")
                    break
                elif x == 'hint':
                    # TODO: add hints
                    pass
                elif x == 'clear':
                    clear_screen()
                else:
                    print("""Commands available to you in watch mode:
        hint  - prints the current exercise's hint
        clear - clears the screen
        quit  - quits watch mode
        help  - displays this help message

Watch mode automatically re-evaluates the current exercise
when you edit a file's contents.""")
            else:
                rprint('[blue]unknown command:', x)
        except:
            break
        
finally:
    observer.stop()
    observer.join()