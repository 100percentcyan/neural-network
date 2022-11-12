from dataclasses import dataclass
from Stilix import STILIX_LIST_COUNT
@dataclass
class array_text:
          item: any = None
          horizontal_or_vertical: str = None
          def text_array(self,array: list,text_file: str):
                    with open (text_file,"w") as file:
                              file.write(str(array))      
                                        
          def text_array_display(self,array: list,text_file: str,horizontal_or_vertical: str):
                    with open (text_file,"w") as file:
                              for item in array:
                                        if horizontal_or_vertical == "horizontal":
                                                  file.write(item)
                                        if horizontal_or_vertical == "vertical":
                                                  file.write(f"{item}\n") 

          def multi_text(self,array: list,text_file: str,modes: list):
                    for item in modes:
                              with open (text_file,item) as file:
                                        if item == "r":
                                                  print(file.read())
                                        if item == "w":
                                                  if self.item is not None and self.item == "" and self.horizontal_or_vertical == "horizontal" or self.horizontal_or_vertical == "vertical":
                                                            self.text_array_display(array,text_file,self.horizontal_or_vertical)
                                                  if self.item is None and self.item != "":
                                                            self.text_array(array,text_file)
ARRAY_TEXT = array_text()



class multi_text:
          def text_arrays(self,arrays: list[list],file: str,modes: list[str]):
                    ARRAY_TEXT.item ,ARRAY_TEXT.horizontal_or_vertical = "" , "vertical"
                    ARRAY_TEXT.multi_text(arrays,file,modes)
          
          def text_multiple_files(self,arrays: list[list],files: list[str],modes: list[str]):
                    value = 0
                    while value < STILIX_LIST_COUNT.list_length(arrays) - 1:
                              for file in files:
                                        ARRAY_TEXT.multi_text(arrays[value],file,modes)
                                        value += 1
                              else:
                                        break
                     

MULTI_TEXT = multi_text()

