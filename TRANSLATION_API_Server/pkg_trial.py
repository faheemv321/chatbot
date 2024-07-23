from final import translate
from final import translate_rev
print("inside package")
while 1:
	inp=input("enter hindi text for translation")
	translated=translate(inp)
	print(translated)
	inp=input("enter english text for translation")
	translated=translate_rev(inp)
	print(translated)

