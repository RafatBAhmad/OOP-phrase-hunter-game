class Phrase:


    def __init__(self, phrase, letter):
        self.phrase = phrase
        self.letter = letter


    def display(self):
        display_phrase = list(self.phrase)
        i = 0
        if i in range(len(display_phrase)):
            for p in display_phrase:
                if p == " ":
                    display_phrase[i] = " "
                elif self.check_letter(p):
                    display_phrase[i] = p
                else:
                    display_phrase[i] = "_"
                i +=1
        display_phrase = "".join(display_phrase)
        return display_phrase


    def check_letter(self, p):
        return p in self.letter


    def check_complete(self, display_list):
        if "_" not in display_list:
            print("Wooohooo, you win ^_^ ")
            return True
        else:
            print("Sorry you loss =(")
            return False
