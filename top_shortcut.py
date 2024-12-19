import subprocess, webbrowser, json 
from pynput import keyboard

class activate_shortcuts:
    def __init__(self):  
        self.vl = tools()

    def main(self):
        listener = keyboard.Listener(on_press=self.on_press)
        listener.start()
        listener.join()

    def on_press(self, key: str): 
        try: k = key.char
        except: k = key.name

        self.vl.verify_list_(
            k, self.vl.info_obtain(),
            self.vl.run_commands
        )


class tools: 
    def __init__(self):
        self.text = ''

    def verify_list_(self, k, shortcuts=[], function=None): # f == f 
        self.text += str(k)

        for e in shortcuts:
            if e in self.text:
        
                try: function(e)
                except: pass
                self.text = ''

            elif k == 'space': self.text = ''
            else: pass

    def info_obtain(self, opc='shorcut') -> list:
        with open('./secrets-words.json', 'r') as f:
            l_info = json.loads(f.read())['shorcuts']

        if opc == 'shorcut':
            return [sublista[1] for sublista in l_info]
        
        elif opc == 'type':
            return [sublista[0] for sublista in l_info]
        
        elif opc == 'command':
            return [sublista[2] for sublista in l_info]
        
        else:
            return l_info
    
    def run_commands(self, shorcut):
        sc_num_ = self.info_obtain('shorcut').index(shorcut)
        type_ = self.info_obtain('type')[sc_num_]
        command_ = self.info_obtain('command')[sc_num_]

        if type_ == 'local': 
            subprocess.run([command_])

        if type_ == 'web':
            webbrowser.open(command_)

        if type_ == 'cmd':
            subprocess.run([command_], shell=True)

user = activate_shortcuts()
user.main()

#! Encoded: FraVelz