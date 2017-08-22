from .exceptions import *


class GuessAttempt(object):
    def __init__(self, character, hit=False, miss=False):
        self.character = character
        self.hit = hit
        self.miss = miss
        if self.hit == True and self.miss == True:
            raise InvalidGuessAttempt
    
    def is_hit(self):
        return self.hit
    
    def is_miss(self):
        return self.miss
        
  
class GuessWord(object):
    def __init__(self, answer):
        self.answer = answer
        if self.answer == '':
            raise InvalidWordException
        self.masked = len(answer) * '*'
        
    def perform_attempt(self, character):
        if len(character) > 1:
            raise InvalidGuessedLetterException
        if character in self.answer:
            return GuessAttempt(character, hit=True)
        else:
            return GuessAttempt(character, miss=True)
            
        

            
class HangmanGame(object):
    pass
