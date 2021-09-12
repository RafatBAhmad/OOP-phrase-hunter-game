# Create your Phrase class logic here.
class Phrase:
    
    def __init__(self, phrase):
        self.phrase = phrase.lower()


    def display(self, phrase, letter):
        display_phrase = list(phrase)
        i = 0

        
        if i in range(len(display_phrase)):
            for p in display_phrase:
                if p == " ":
                    display_phrase[i] = " "
                elif self.check_letter(p, letter):
                    display_phrase[i] = p
                else:
                    display_phrase[i] = "_"
                i +=1        
        display_phrase = "".join(display_phrase)
        print(display_phrase)
        if self.check_complete(display_phrase):
            print("You Win")
        else:
            print("Not done")

    # def display(self, phrase, letter):
    #     display_phrase = list(phrase)
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
            

    def check_letter(self, p, letter):
        return p in letter
        
    def check_complete(self, display_list):
        return "_" not in display_list


phrase_guess = Phrase("hello world")
letter = ["o","h","b","d","e","r","w"]
phrase = "hello world"
phrase_guess.display(phrase,letter)

