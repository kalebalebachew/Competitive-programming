class Solution:
    def interpret(self, command: str) -> str:
        mydict = {'()':'o','(al)':'al'}
        for key, value in mydict.items():
            command = command.replace(key, value)
        return command


        
        