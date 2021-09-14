# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase, letter):
        self.phrase = phrase.lower()
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

    # def display(self, letter):
    #     display_phrase = list(self.phrase)
    #     final_phrase = []
    #     for p in display_phrase:
    #         if p == " ":
    #             final_phrase.append(" ")
    #         elif self.check_letter(p,letter):
    #             final_phrase.append(p)
    #         else:
    #             final_phrase.append("_")
    #     final_phrase = "".join(final_phrase)
    #     print(final_phrase)
    #     if self.check_complete(final_phrase):
    #         print("You Win")
    #     else:
    #         print("Not done")    
            

    def check_letter(self, p):
        return p in self.letter
        
    def check_complete(self, display_list):
        if "_" not in display_list:
            print("Wooohooo, you win ^_^ ")
            return True
        else:
            print("Sorry you lose =(")    


# phrase_guess = Phrase("hello world")
# letter = ["o","h","l","d","e","r","w"]
# phrase = "hello worLD"
# phrase_guess.display(letter)

