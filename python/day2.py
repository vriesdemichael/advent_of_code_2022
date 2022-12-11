from enum import Enum
from typing import Literal, Self
from utils import load_data

class Instruction(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0
    
    @classmethod
    def from_game_enum(cls, game_enum):
        match game_enum:
            case GameEnum.ROCK:
                return cls.LOSE
            case GameEnum.PAPER:
                return cls.DRAW
            case GameEnum.SCISSORS:
                return cls.WIN


class GameEnum(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
    @classmethod
    def from_letter(cls, letter):
        match letter:
            case "A" | "X":
                return cls.ROCK
            case "B" | "Y":
                return cls.PAPER
            case "C" | "Z":
                return cls.SCISSORS
            
    @property
    def wins_against(self):
        match self:
            case GameEnum.ROCK:
                return GameEnum.SCISSORS
            case GameEnum.PAPER:
                return GameEnum.ROCK
            case GameEnum.SCISSORS:
                return GameEnum.PAPER
    
    @property
    def loses_against(self):
        match self:
            case GameEnum.ROCK:
                return GameEnum.PAPER
            case GameEnum.PAPER:
                return GameEnum.SCISSORS
            case GameEnum.SCISSORS:
                return GameEnum.ROCK
    
    @property
    def draw_against(self):
        return self       
    
    def score_part_1(self, other: Self):
        match other:
            case self.wins_against:
                return Instruction.WIN.value + self.value
            case self.loses_against:
                return Instruction.LOSE.value + self.value
            case self.draw_against:
                return Instruction.DRAW.value + self.value
    
    def score_instruction_part_2(self, instruction: Instruction):
        # note: self is the opponent choice in this context
        match instruction:
            case Instruction.WIN:
                return self.loses_against.value + Instruction.WIN.value
            case Instruction.DRAW:
                return self.draw_against.value + Instruction.DRAW.value
            case Instruction.LOSE:
                return self.wins_against.value + Instruction.LOSE.value
            


part_1_score = 0
part_2_score = 0 

for line in load_data():
    
    abc, xyz = line.split()
    # part 1
    opponent_choice, own_choice = GameEnum.from_letter(abc), GameEnum.from_letter(xyz)
    part_1_score += own_choice.score_part_1(opponent_choice)
    # part 2 instruction is what was previously your own choice
    instruction = Instruction.from_game_enum(own_choice)
    part_2_score += opponent_choice.score_instruction_part_2(instruction)
    
print(f"Score part 1 = {part_1_score}")
print(f"Score part 2 = {part_2_score}")