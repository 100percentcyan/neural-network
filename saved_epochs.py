from array_text import ARRAY_TEXT
from dataclasses import dataclass

@dataclass
class epochs_array:
          array: list[int] = None
          def save_epochs(self,file_: str):
                    ARRAY_TEXT.item , ARRAY_TEXT.horizontal_or_vertical = "" , "vertical"
                    ARRAY_TEXT.multi_text(self.array,file_,["w","r"])

EPOCHS_ARRAY = epochs_array()

