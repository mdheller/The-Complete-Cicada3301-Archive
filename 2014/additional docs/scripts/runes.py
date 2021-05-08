import string

def find_position(char):
  for set_num in range(len(table)):
    if char in table[set_num]:
      return set_num
  return False

def forge_offsets(key, direction, offset):
  if type(key) is str:
    return [(string.ascii_uppercase.index(x) + offset) * direction for x in key]
  else:
    return [(x + offset) * direction for x in key]

def frequency(text):
  return {letter: text.count(letter) for letter in string.ascii_uppercase}

######
#
#  Scroll down for the bits you should interact with
#
######

table = [
  ["ᚠ", "F"], 
  ["ᚢ", "V"],
  ["ᚦ", "TH"],
  ["ᚩ", "O"],
  ["ᚱ", "R"],
  ["ᚳ", "C"],
  ["ᚷ", "G"],
  ["ᚹ", "W"],
  ["ᚻ", "H"],
  ["ᚾ", "N"],
  ["ᛁ", "I"],
  ["ᛂ", "J"],
  ["ᛇ", "EO"],
  ["ᛈ", "P"],
  ["ᛉ", "X"],
  ["ᛋ", "S"],
  ["ᛏ", "T"],
  ["ᛒ", "B"],
  ["ᛖ", "E"],
  ["ᛗ", "M"],
  ["ᛚ", "L"],
  ["ᛝ", "ING"],
  ["ᛟ", "OE"],
  ["ᛞ", "D"],
  ["ᚪ", "A"],
  ["ᚫ", "AE"],
  ["ᚣ", "Y"],
  ["ᛡ", "IA"],
  ["ᛠ", "EA"]
]

liber_primus = """ᚣᛖᛝᚳ•ᚦᛂᚷᚫ•ᚠᛂᛟ•
ᚩᚾᚦ•ᚾᛖᚹᛒᚪᛋᛟᛇᛁᛝᚢ•ᚾᚫᚷᛁᚦ•ᚻᛒᚾᛡ•
ᛈᛒᚾ•ᛇᛂᚦ•ᚪᛝᚣᛉ•ᛒᛞᛈ•ᛖᛡᚠᛉᚷᚠ•
ᛋᛈᛏᚠᛈᚢᛝᚣᛝᛉᛡ•ᚣᚻ•ᛒᚢ•ᚷᚩᛈ•ᛝᚫᚦ•ᛁ
ᚫᚻᛉᚦᛈᚷ•ᚣᚠᛝᚳᛂ•ᚦᚪᛗᛁᛝᛁᛡᚣ•ᚻᛇ•ᛏᚻᚫ
ᛡ•ᛉᚣ•ᛖᚢᛝ•ᚳᚠᚾᚦ•ᚦᛈ•ᚣᛝᛠ•ᚣᚾ
ᛖᚣ•ᛞᛉᛝ•ᚠᛚᚹᛇᛏᚠᚷᚾ•ᛗᛇᛚᚾ•
ᛝᛗᚠᚱᛡ•ᚪᛋ•ᛠᛗᛝᛉᛉᛇᛞᛒ•ᛟᛞᛗᚩ•ᛠ
ᛇᚻ•ᛞᛝᚷ•ᛟᛝᛚᚢᚱᚾᛏ•ᚫᛋᚣᚢᚻᚱᛏ•ᚻᚳ•ᛋᛟ
ᛏᛟᛝᚢᚱ•ᛋ•ᚠᚩᛖᚹᛠᛟᛚᚠᚫ•ᛗᚱᛝ•ᛞᚪᛗᚱ•ᚹ
ᚪᛁᛗᛋᚾ•ᛋᛟᚱᚢᚹᛋᛚᛡ•ᛟᚪᚫᛝᛋᛞᛈᛏ•ᚳᚱᚦ
ᛡ•ᚱᛒᚩᛞᚦᚠ•ᚣᛉᛁᛏ•ᛟᛁ•ᚠᛚᚩ•ᚠᛠ•ᚱᚩᛟᛗᚻ
ᛗᚷᛈᚻ•ᚫᚻᚾᚩᚻᚣ•ᛟᛋᛚ•ᚾᚷ•ᚫᚣ•ᛟᚳᛒᛚᛂ•ᛝ
ᛚᛟ•ᚫᛂᛠᚹ•ᛠᚦᚩ•ᛒᛟᚣ•ᚳᚠᚳᛂ•ᛚᚫ•ᚾ•ᚦᛈ•
ᚢᛉ•ᛟᛉᚷ•ᛈᚠᛋᛇᚫᛟ•ᛝᛈᛇᚩᛖᚪ•ᚷᚫᛡᛝᚦᚩ
•ᛈᚪᛟᚦᚱᛝᚫ•ᚳᛋᛒᛇᚣᚻ•ᛏᛉᛖᛚᚱ•ᚷᚹᚣ•ᛂᚠ
ᛁᚾᛡᚳᚣᛠᛁᛡ•ᚩᚦ•ᛖᚳᚫᚳᛉᛡᛠ•ᚩᛚᚳ•ᚠᚱ
ᛞᛝᛖᚢ•ᛞᚳᛚᛠᛋᛉᚳᚷᛡ•ᚹᛋᚦ•ᚠᛞᛝ•ᛁᛡ
ᛗᚪᚫᚷ•ᚹᛋ•ᚾᛞ•ᚳᛈᚦᛉᛈᛠᛠ•ᚹᚢ•ᛠᚹ•ᚠᚹ
ᛂᚣ•ᛉᛞᚹᚳᚷᚳᛟ•ᛞᛉᛟ•ᚱᛡᚷ•ᚾᛈᚪᚣᛈ•ᚳ
ᚣᚻ•ᚠᛖᛂᛠᚾ•ᛟᚫ•ᚢᚪ•ᚻᚱ•ᛖᛠᚦᚠᛂᚪ•ᛚᛉ
ᛋᛏ•ᛗᚠᛚᚠᛏ•ᚷᛁᚦ•ᚢᛚᚷ•ᛉᛠᛏᛋᛚᛂᛈ•ᛚᛉᛁ
ᛟᛗ•ᚢ•ᚻᛏ•ᛒᛇᛚᛞᚻᛒᛗ•ᛠᚱᛒ•ᚾᚻᛒᛖᚷᛇ•
ᛞᛚᚹᛇᛡᛈᚩ•ᚻᛖᛠ•ᚹᛁᚱᛁᚻ•ᚢᚦᚻᚣ•ᚾᛉᛒᚷᛂ
ᛈᚢ•ᛝᛠᚠᚾᛁᛖᛞᛡᛝᚱ•ᛞᛒᛂᛡᛟᛗᛁ•ᚠᛏ•ᛂ
ᛞᛁᚦᚱᛚᛋ•ᛖᛇᚩᚷᛒᛏᛞ•ᚦᚪᚾᚳᚣ•ᛡᛋᚦᛞ•ᛝᚠᛚ
ᛖᚷᚻᚳ•ᛖᚩᛁᛏᚾᛉ•ᛈᛏᚠᚻᚱᛞᛖᚠᛏ•ᚫᚹᚻ•ᛒ
ᚳ•ᚠ•ᛈᚪᛚᚢᛠᚾᛚᛂ•ᛂᚳᛚᚹᛠᛞᚢᛞᛇ•ᛠᛉ
ᛞᚹᚻᛠ•ᚦᛡᚫᚳᛚᛏᚹᛖᛁᚳ•ᛈᛟᛞᚳ•ᚾᚻᚪ•ᚱᛁᚷ
ᚦᛠᛖᛏᚷ•ᚦᚻᚩᛡᚹᚫᛂᛖ•ᛝᛠᛞ•ᚩᚫ•ᚪᛚ•ᛒᛂ
ᚳᚢᛉᛏᚪᛒᛂᛈ•ᚠᛠ•ᚻᛞᚾᛡᚢᛈᛋᚢᚹ•
ᛚᛂ•ᛇᚻᛝᚳᚦᛏᚫᛂᛏᛉᚻ•ᛏᚢᛟ•ᛋᛈᚱᚷ
•ᚣᚾᚪᚷᛇᛝᚾ•ᚹᚠᚣᚾᛒᛠᛡ•ᛈᚾᚣᚪᛋᛗ
ᛒ•ᛡᛠᛡᛁ•ᚩᛒᚱᚾᛚᛠ•ᚱᛚᛚᛖᚠ
ᛟᛒ•ᛝ•ᚱᚪᛡᚷᛟᛇᛏᛗᛉ•ᛞᛇ•ᛗᚣᚻᛠ•ᛁᛚᛋ•ᚾ
ᚹᚳᚠᛈᛗᛈᛚ•ᛠᛋᚦᚠᛟᛡ•ᚦᛖᚣ•ᚳᛂᛚᚳᛡᛗ•
ᛒᛞᚳᛇ•ᛂᛁᛏᛟ•ᛞᛠᛖᛡᚾᛏ•
ᛈᛞᚦ•ᛇᛞᛇ•ᚫᛚᚳ•ᛡᛇ•ᛠᚻ•ᚹᛗᚣᚦ
ᚢ•ᚻᛏᚦᚱᚻᛝ•ᛚᛝᛋ•ᚾᚫᛠᚷᛋᛚ•ᛋᛉ
ᚩᚻᚹᛞᛗᛖᛗᚪᚠ•ᚳᚣᚳᚫᚾ•ᛏᚦᚷ•ᛁᛂᛁ
•ᚳᛞᛡᛉ•ᚻᚫᚫᛠᚷ•ᛠᛝ•ᚠᛏᚩᚱᛞᚳᛇ•ᚠᚢ
ᛉᛠᛒᚩ•ᛉᛁᚣᚷᛋᛋᛒᛠ•ᚩᛁᛈ•ᛁᛂᛁᚩᛖ•ᚻᛠᚻ
ᛚᛡ•ᚣᛈᛉᛁᚹᛗᚳᛁ•ᛚᚷᚠᚾᛡᚳᛉ•ᛈᚩᚱᛡ•ᚻ•ᛂ
ᛗ•ᛟᛉᛝ•ᚢᛗᛇᛠᚷᛝ•ᛝᚹᚳ•ᛚᛝᚢ•ᛉᛂᚠᛟ
ᚢ•ᚷᛠ•ᛗᛉ•ᚪᚹ•ᛚᚢᛉᚫ•ᛗᛞᛝᚻᚱᚣ•ᚻᚪ•ᚷᛁ
ᚠᚷᚳ•ᚫᛝᛂᛇᛉᛡ•ᚾᚦᛒᚢᛂᚱ•ᚹ•ᚷᛚᛟᚷ•ᚦᛇᚠ•
ᚦᛠᛁ•ᛋᚷ•ᚷᚣ•ᛠᛡᛈ•ᛡᚫᛚ•ᚦᛠᛉᚫ•ᛖᛗ
ᛖᛏᛟᛏ•ᛠᚳᚠ•ᚳᛠᚷ•ᚦ•ᛈᛁᚳᚾ•ᛇᚣᛝᛂᛝ
ᛗᚹᚳᚾ•ᛒᚣᛠ•ᚩᛟᚷᚱ•ᛗᚱᛗᛈᛡᚹ•ᚫᛟᚦᛟ•ᛈ
ᛉᛂᛚ•ᚱᛚᚱᛒᚪᛈᛏᛉᛚᛏ•ᛗᛉᛁ'ᚹ•ᛂᛋᛟᛗᚾᚱ
ᛖᛒᛋ•ᚳᛏᛚᛟ•ᛋᛒᚠᛉᚦᚪᛠᚢ•ᛇᛉ•ᚱᚷᛏᛇᛠ
ᛁᛂᛒᛟ•ᛉᚷᛂᛝ•ᛠᚦ•ᚱᛝᛒ•ᚾᚢᚪᛝᛒᛈᛋᛠ•ᛈ
ᚹᚩᚻᛖ•ᚫᛇᚷᚾᚫᛋᛇ•ᚩᛈᛗ•ᛖᛉᛡᛒᚹ•ᚢᛖᛁᛞ•
ᛈᚪᛇᚷᛋᚳᚷᛞᛈᚣ•ᛡᛚᚦᚱ•ᚳᚢᚠᛇᚦ•ᛉᛖᛚ•ᚢ
ᚱᚫ•ᛉᚻᛂᚫᛗᛚᚠ•ᚳᛝᛞ•ᛁᛝᚩ•ᚳᛋᛟᛖᚣᛟᚻᚢ•
ᚷᛞᚹᚪ•ᛖᛋᚷᛝᚠᛉ•ᛞᛉᛂ•ᛠᚻᛁ•ᚦᛈᛉᚣ•ᛡ•
ᛇᛞᛇᛝᛇᛝ•ᛖᛠᛞᚱ•ᛚᛇᛏ•ᛉᛏᚣ•ᚱᛇ•ᛈᛝᛇ
ᛈᚩᛁᛚᛖᚠ•ᛇᚫᚪ•ᚣᛝᚠᚣ•ᚠᛞᚾᛚ•ᛉᛏᚾᚫᛋ•ᛁᚩ
ᚳᚢ•ᚣᛠᚾᛏᚷᚳᚪ•ᛉᛡᛇ•ᚦᛂᚣᛂᛚᛟᛖᛚ•ᚣ•
•ᛈᛡ•ᛖᚹᛟ•ᛇᚾᚪ•ᚻᛞᛇᛋ•ᚦᚣᛇᚦᛂᚦᚱᚢ•ᚳᛠ
ᚪ•ᚢᛂᛡᛈ•ᚣᚫᛇᛋ•ᚻᛠᛏᚣᛞᚣᚫᚠᚻᚩ•ᛟᛗ
ᛉᛟᛂᚷ•ᚢᛡᚱᛡᚳ•ᛁᚠᛟ•ᛁᛂᛈᛒ•ᛖᛝᚣᚦᚩᚫᚣ•
ᛠᛉᛡᛖᛚ•ᛁᚱᚣᛞᛠᛂ•ᚫᚳ•ᛗᚷᛁᚫᚢᚪᚫ•ᛂᚪ
ᚻᛈ•ᚠᛞᛚᛁᛠᛈᛟᚣᚩ•ᚢᛒᚷᛝᛟᚢᛝᛋᚢᚳ•ᛏ
ᛞ•ᚫᛈᚩᛂ•ᛒᚻᚱᛁᚷᚻᛂ•ᚣᚹᛗᛇᚾᚫ•ᛞᛝᛇ•ᛟᛂ
ᛝᚳᛖᛠ•ᛉᚪᚱᚣ•ᚪᚢᛏ•ᚳᛈᚳ•ᚩᛇᛟ•ᚫᛈ•ᛏ
ᛉᚳᚻᛞᛇ•ᛉᛒᛠ•ᚫᚾᛂ•ᛠᚪᛒ•ᛖᛠᚹ•ᛡᛚ•
ᚹᛁᛡᛋᛈᛚᚦᚪᛋᛂ•ᛡᛞᚣᚱᛞᛟ•ᚦᚱᛉᛟᚹ•ᚣᛞᛏ•
ᚷᛚᛡᚻᚹᛗᚱ•ᛝᚠᚳ•ᚱᚫᛁᛒᚷᛈᚣ•ᛞᚪᚱᚪᛉᛟ•ᚢ
ᚩᛁᛠ•
ᚪᛏᛉᛒ•ᛗ•ᚷᛡᛋᛒ•ᛉᛇ•ᚷᚾᛠᚫᚷᛝᛞ•
ᛉᛖᛏᚩᚷᛡ•ᛝᚻᛏ•ᚳᛁᚣ•ᛂᛏ•ᛟᚩᚻᚱᛂ•
ᚳᛖᛡᚩ•ᛞᚪᛏᚣᚢᚾᚱᛇ•ᚫᚫᛁᛖᚠᛝᚦᚻ•
ᛉᛁᛟᛋᛁ•ᛗᚪ•ᚢᛂᚳᛋᚹᚾᚣ•ᚩᛈᛉᚱ•ᛚᚫᛟᛏᛡ•ᛂ
ᛈᛗ•ᛞᛋᚠᛗ•ᛟᚹ•ᛞᛚᛏ•ᚷᚱ•ᚩᚢᛋᚻᚪ•ᚣᛇᛡᛚ
ᚢᚻ•ᛈᚹᛂᛚᚷᛒ•ᛗᚢᛂᛗ•ᛇᚾᛇ•"ᚫᛚᚪᛚᚷᚪ•ᛋ
ᚻᛝ•ᛚᚦᛒ•ᛋᚳᚢᚳᚩᛡ"•ᛚᚳᛂ•ᛉᚪᚾᛇᛉ•ᛠ
ᛗᛈᚢ•ᛗᚠᛚᛠᛝ•ᛒᛉᛁ•ᛚᚦᚱ•ᛠᛡᛁᚳ•ᚩᛉᛖ
ᛞᛡ•ᛏᛋᛗᛠᛂᛈ•ᛠᛟ•ᛡᚫᚦᚹᚻᛈᛇᚪᚷᛈᚻ
ᛠ•ᚳᛚᛠᛈ•ᛡᚣᚾᛁ•ᛚᛡᛁᚳ•ᚫᛇᚾ•ᚫᚳᛡᚱᛡᛚ
ᛞ•ᛒᛟᛝᛡ•ᛉᛗᛝ•ᚳᚻᛟᛠᚾᛈᚳᚦ•ᛁᛇᚦ•ᛇᚢᚩ
•ᚦᛈᚪ•ᛡᛚᛟᚹᛡᛈ•ᛂᛗ•ᚷᛒᛈᛋᚾᛇ•ᛏᚩᚷᚢᚾᚫ
ᛖ•ᚾᚣᛁᛖ•ᛞᛝ•ᛞᛝ•ᛚᚢᛚᛉ•ᚪᚾᛝ•ᛇᚪᛂ•ᚻ•ᛞ
ᚹᛈᚫᚹᚫ•ᛇᛁᛚᛝ•ᚦᚾᚳ•ᛒᛁᛏ•ᛠᚳᚩᛇᛖᛝ•ᚳᚻ
ᛟᚻᚫᛂ•ᛟᛉ•ᛁᚳᛖᛏᛋᚹᛖᚾᛡᚣᛂᛗ•ᛖᚳᚪ•
•ᛞᚩ•ᛟᛏᚦᚫ•ᚳᚹᛂ•ᛉᛠ•ᚷᛠᛗ•
ᛉᛁᛉᛗ•ᚢᛉᛗᚳᚦᛈᚩᛒ•ᛡᚾᛏ•ᛠᛉ
•ᛈᚱᚣ•ᚩᚳᛠᛗᛝᚷᛉᛚᚢ•ᛝᛁᛏᚩ•
ᛂᚠᛝ•ᛋᛚᚾᛞ•ᚩᛗ•ᛇᚫ•ᚱᛞᚹᛏᛂᚦ•
ᚣᚦᛋ•ᚫᚣᛖᛋᛉᛟᛒ•ᛠᚱᛇ•ᛈᛝᚢᛈ•ᚩᚦᛉ•ᚪᚻ
ᛟᚱᛝᚢᛖᚱ•ᚣᛚᛉᛚ•ᛡᛚᚱ•ᛈᚹᛇᚾ•ᛠᚪᚱᛉᛝ•
ᚣᛋᚻᚢᛚ•ᛋᚣ•ᚷᚾᚢ•ᛇᚫᚾᚾ•ᚩᚫᛖᛞ•ᚪᚩᛂᛡᚢ
ᚪᛉ•ᚱᛉᛡᛟᛂ•ᛗᛁᛇᛚᛠᚻᚦᛗᛠᚣ•ᚷᛒᚳᛈ
ᛉᚳ•ᚾᛟᛟᛋᚷᛗᛈᛖᛏᛚᚾᛂ•ᛂᚳᛝᚩ•ᛁᚹᛚᛠᛒ•
ᚠᚪᛖ•ᛏᛝ•ᚾᛈᛠᚩᛏᚦ•ᚻᛝᛉᛈᚻᛈᚳᛈᚱᚢ•ᛚ
ᚠᛖᛟ•ᚷᚪᛒᚠᛁᚫᚠᚢᛟ•ᛗᚠᚣᛝᛂᚳ•ᚻᛏᚠᛚᚫ•ᛖ
ᚦᛋᛚᚩᚢ•ᚫᚩᚪᛗᛟᚢᚹᛇ•ᛒᚾᛋᛚᛝᛂᛟᚾ•ᛗᛚᛒ•
ᛟᛏ•ᚾᛞᛒᚩᚾᚦᛡᚻᛟ•ᚱᛈᚾᚠᛈᛞ•ᛋᚩᛁᛠᚣᚾ•ᛇ
ᚣᚹᚫᚷᛂ•ᛝᛗᚪᚹᛈ•ᚪᚢᚾ•ᛈᛡᛗᛖᛞᛟ•ᛁ•ᛉ
ᛡᛗ•ᚠᛈᚩ•ᚦᛉᛞ•ᚩᛞ•ᛋᛈᛉᛡᚷ•ᛟᚻᚠᚦᛉᛂ
ᛟᛋᚦᚣᚦ•ᛏᚻᛋᚣ•ᚻᛠᚷᛚᚫᚱᛏ•ᚢᛋᛟ•ᚦᚠᚠᚣ
ᛟᛡ•ᛇᚳᚣᛒᛚᛝ•ᛠᚱᚻᛞ•ᛂᚣᛏᚫ•ᚻᛞᚳᛋ•ᛉ
ᚠᛞ•ᚦᛗ•ᚳᛇᛝ•ᚫᚾᛡᛠᚹᛁᛡ•ᛒᛗᛝ•ᚷᛈᛁᚳ•ᛠ
ᛚᚷᛉᚣᚣᚱᛂ•ᛉᛁᛂᚢ•ᛖᚣ•ᚪᛝᛈ•ᛡᚫᚳ•ᛖᛠ
ᚹᛒᚦᛟᚠᛗ•ᚫᚱᚠᚩᛏ•ᛝᛉᛞ•ᛗᛖᛡ•ᚩᛈᛋ•ᛇᛞ•
ᛇᛟᚫᚾ•ᚷᛗᚣᛁᚫᛁᛂ•ᛈᛂᚩᛡᚷ•ᛈᚳᛂ•ᛚᛖᛡᚻᛚ
ᚷᚱᛇ•ᛟᚣ•ᛠᚣᛗᚹᚾᚹ•ᚠᛁᛂᚢᛗᚫᚾᚳᛗᛠᛁ•
ᚩᛇ•ᛒᛚᛞ•ᚾᚹᚠᚾᛒᚱ•ᛋᛟᚦᛡ•ᚪᛡᛏᚷᚷᚹ•ᚪᛋᛡᚦ
ᛋᚦᛋᚠᛗᚷᛞᛠ•ᛝᛈᚩᚪᚣᛝᛈᛋ•ᛟᚾᛇᚪᛖ•ᚻᚢ
ᚷ•ᚩ•ᚢᚦᛏ•ᛒᚷᚣᛝᚠᚣᛁᚻ•ᚹᛡᛠᚱᚫᚹᛡᛞᚪᚦ
ᚳ•ᛉᚢ•ᛈᛏᛋᚢᛖ•ᚷᚦᛡᛚ•ᛖᛋᛠᛝᛉᛈᛉ•ᚾ
ᛟ•ᛞᛟᛒ•ᚾᚹᚢᛁᛇᛚᛞ•ᛁ•ᚦᚣᚷ•ᛟᛈᛡ•ᛖᚪ•ᚠᛋᛉ
ᛞ•ᛖᚷᚦᛠ•ᚾᛋ•ᛞᛟᛗᛖ•ᛗᚾᛉ•ᚹᛒᛠᛈᛟ•ᛗ
ᛉᚫ•ᛂᚩᛞᚻᛡᚷᚠ•ᚣᛗ•ᛁᚷᛉᚻᚹ•ᚾ•ᛋᛗᚷᛠ•
ᚣᛚᚱᛂᛗᛉᚣ•ᛇᚱᚢᛟ•ᚣᚦᚢᛟᚩ•ᚱᚢᚹ•ᛁᛒᚳ•
ᛠᛏᛞ•ᛚᛖᛋᛂ•ᚳᛟ•ᚷᛞᛡ•ᚢᚹᛝᚻᚫᚢᛈ•ᛏᛈ
ᚩᚣ•ᚾᛇᚦᛟᛏᛇᚳᚠ•ᛒᚪᚾ•ᛗᚦᛝ•ᛟᛠᚢᛁᚪ•ᚾᚻᛝ
ᛉᚩ•ᛇᛁᛡᚠᛟᛒᚦᚠ•ᛋᛒ•ᚠᛞᛇ•ᚩᚦᛏ•7•ᚷ•ᛚᛂᛖᚫ
•ᚣᛁᚫᚹᚻ•ᚫᛏ•ᛁᛉ•ᛉᚻᛞᚩᛠ•ᚫᛋᛝᛚᛝ•ᛖᚩ
ᚻᛗᚩᛟᛒᚦ•ᚱᛚᛋ•ᚳᚻ•ᚪᛡᚾᛇᚱᛉᚦ•ᚣᛉᚻ•ᛡᚾ
ᚢ•ᛗᛉᚹ•ᛖᛈᛖ•ᚩᚳᛈᚳᛞᚪᛉᚢᛗᛝᛟ•ᛋᚾᛟ
ᛉ•ᚠᚱᚳᛒᚢᛂᚱᚫᛝ•ᛒᛋᛟᛠᛡᚪᛚ•ᛏᛟᚾᚫᛟᚪ•ᛁ•
ᛡᛋᚳᛖ•ᚹᛒ•ᚾᛚᛝ•ᚦᚾᛁᛠ•ᛒᛡᚱᚠᛖᛁᚹ•ᚾᚠᛗᚢ
ᚷᚾ•ᛂᛚᚳᚱ•ᛝᚣᛉᛋᚪᛟᚱᛉᚳ•ᛒᚫ•ᚠᚢᚪᛖᚪᚹ•
ᛚᚾ•ᛂᛉ•ᚻᚦᛉ•ᛗᛚᚾᛖ•ᛏᛝᚦᚪᚩᚢᛗᚣ•ᚠᛝᚪ•
ᚻᛡᛇᛡ•ᛚᛏᛁ•ᛇᛁ•ᚳᚢᚢᛖ•ᚳᛒ•ᚫᛇᚠᚦᚳᛚᚩᛉᛚ
ᚩᛚ•ᚠᚳᛠ•ᚪᚠᛟᚫᚠ•ᚾᚳ•ᚢᛒᚱ•ᚾᛇᚩᛉ•ᛁᚳᛟ•ᛞ
ᛉᛠᛝᚠᚱᛡᚳᛇ•ᛉᛟᛈᛗᛞᚳᚦᚹᛈ•ᛡᚻ•ᚾᚦ
ᛇᛏᚹᛖᚢ•ᚫᛇᚦ•ᛝᛟᛏᚳᚷᛒᛠ•ᚪᚳᛒᚪᚩᚹᚫ•ᛉ
ᚢ•ᚫᛖᛒ•ᛇᛏᚢᚩ•ᛟᛞᚠᚢᛋ•ᛡᛂᛗᚦᛠᛏᚪ•ᛒ
ᚹᚣ•ᛏᛂᚻᚦᚫ•ᛚᚪᚱᚫᛟᚦᚩᚾᛟᛁᛖ•ᛡᚠᚷ•ᛋᚠᚦᛏ•
ᛠᛡᛠᛁᚢᛡᛇᛝᛞ•ᛉᛏᚠᛒᚻᚢᛋᚳᚱᛇᚹ•ᛇᛈ
ᛋᚢᛚᚪᛈᚢᚳᛖᚠᛞᛉ•ᚦᛠᛇᛝᚻ•ᚣᚱᛗ•ᛟᚾᛚ•
•ᛈᚹᛞᚱᛂ•ᚪᛝᛞ•ᛁᚦᛏᚷᚢᚹᚳᚻᛖᚩᚪᛖ•ᛉᚪᚢ•
ᚳᛁ•ᚱᚳᚹ•ᛠᛇᛏ•ᚦᚳᚻᚢ•ᛡᚹᛟ•ᚷᛇᛈ•ᚢᛈᚦ•
ᚷᚣᚢᚪᛗ•ᚹᚳᛖᛝᚱᛠᛞᛏᚻ•ᛂᛁᛈᚻᚠᛉᛝᛈ
ᚾ•ᛒᚳᚪᚷᛋᛟ•ᛉᛠᛈᚪᚩᚷᚠᚳᛡᛂ•ᛠᚢᚠᛋᛚ•
ᚣᛚ•ᚢᛒ•ᛉ•ᚱᚣᚾ•ᛁᛠ•ᛚᚹᛋ•ᚠᚦᚪᛠ•ᛈᚷ•ᛏ
ᚷᛡᛟᛠᛡᛒ•ᛉᛂᛒ•ᛖᚾ•ᛞᚠᛠᛗ•ᚦᚪᛗᚠᚪ•
ᚻᛡ•ᛗᛁᛏᛟ•ᚻᚣᚹᛏ•ᚠᛒᛁ•ᚫᛖ•ᛝᛒ•ᛚᛏᛠᛉ•ᛟ
ᛋᚾᛉ•ᚹᛏᛠᛏ•ᛖᚢᛡᛖ•ᛉᚾᛇ•ᛟᚳᚾᚠᚩᚾᚠ•ᚳ
ᚪ•ᚷᚱᚩ•ᛠᚦᚹᚣ•ᛒᛁ•ᛝᛇᛟ•ᚣ•ᚷᛗᚩ•ᛁᚷᛂ•ᚩᛇ•ᚢ
ᛁᛉᛝᚪᚱᛉ•ᛏᛂᛞᛈ•ᚾᛝᚷᛏᚢ•ᛚᚷᚳᛏ•ᚢᛒᛇ•
ᛈᚩᚣᚢᛏ•ᛡᚫᛏᚹᛏᛇ•ᛡᚫᚫ•ᚦᛏᛝ•ᛠᚳᛁᛉ
ᚻᚦᚣ•ᚻᛚᚾᛋᚱᛡᚫᛚᚫ•ᛖᚷᚻ•ᛞᚾᚻᛠ•ᚠᚪᚹᛖᚠ
ᛂ•ᛒᛇᚱᚹᛏᛉᚾᛠᛖᛁ•ᚠᚾᛡᚳ•ᛋᛟᚹ•ᛈᚷᛝᛟ•
ᚷᚦᚠᛂᚷᚳ•ᛒᛁᛗᛚᛇᛠᚹ•ᚾᚫᚹᚷ•ᚩᚻᚪᛏᚾᛂ•ᚣ
ᛝᛏᛡᛝ•ᚢ•ᚩᚠᚣ•ᛗᚢᛒ•ᛏᚠᛈ•ᚱᚩ•ᛉᚩᛝᛒ•ᛖ
ᛏᚩᛉ•ᚣᛗᚠᛉ•ᛖᚩᚫᚷᚣᛚ•ᚩᛇ•ᚠᛋᚫᛇᛗ•ᛡᛟᚹ
ᚾᚩᚢᚹᛖᛁ•ᚾᚦᚫᛠᚪ•ᛠᛚ•ᚹ•ᛡᚩ•ᚢᚦᛗ•ᛝᛚᚪᚠ
ᛝ•ᛚᚠᛚᚳᛒᚢᛝᛉ•ᚣᛡᚪᚷ•ᚹᛟᚪᚻᚹᚢ•ᛖᛠᚷ•
ᛁᚪᛏᛂᛗ•ᛏᛖᛁ•ᚣᛡ•ᚦᚾᚠᚦ•ᚩᛈᚻᚪ•ᚻᛋᛠ•ᛡᛉ
ᚪᚫ•ᚠᚣᛞᛠᛇᚠᚫ•ᛏᛗ•ᚳᛡᚷ•ᚱᚢᛞ•ᛂ•ᛋᛡᛇᚩ
•ᛚᛟ•ᚦᚱᚫᛒᛚᚦ•ᛖᚪᚦᛗᛚ•ᚦᛉᚪᚱ•ᛟᛖᛒᛂᚱᛂᛖᛁ
ᛈ•ᚪᛖᛠᚠᛂᚢ•ᛞᚹᚦᚣ•ᛉᚷᚩᚳᛡ•ᛇᛗᛞᚳᛏ•
ᚻᛚᚦᛝᛖᛗᚱ•ᛒᚷᛞᛉᛗᛒᛉᚳᛝᚦᚣᛞᚫᛠ•ᛋ
ᛏᛗᛏᚻᚹ•ᛇᚳᚪᛞ•ᛠᚢᛒᛉ•ᛡᛁᛡᛚ•ᚷᛋᚦᛞ•ᚠ
ᚢᚩᛠ•ᛚᛋᚣᛏ•ᛋᚪᛞᚫᚹᛂᛞ•ᛋᛈᛋᛂ•ᚪᛖᛁᛇᛒᛟ
•ᛏᛂ•ᚠᚩᛚᛞ•ᚾᚷᚳ•ᛚᚷᛗ•ᛠᚦᚢ•ᛟᚻᚾᛟᚣᛡ•
ᛇᚻᚣᚪᛈ•ᚾᛋ•ᛞᚫᛠᚳᛉᛂ•ᚦᚹᛋᚱᚦᚫᚾ•ᛡᛚᚣ
ᚫᛋᛖ•ᛟᚣᛝᛡ•ᚦᚣᚷᛇᚱ•ᛋᛠᛏ•ᛡᚳᛉ•ᛠᚷ•
ᚳᛒᛋ•ᚹᚾᚻᛖᛝᛋ•ᚩᛡᛗᛉᛝ•ᛉᚦ•ᛠᛞᚳᛒᚷ
ᛉᚹᛝᚢ•ᛉᛞᛈ•ᛉᛡᛈᛟ•ᚾᛡᚠᛡᚢᛋ•ᛉᚪᛖ
ᚻᚱᚣᛠᛇ•ᛒᛟ•ᚪᛝᛡ•ᚳᚱᚳᛈᚩᛏ•ᚻᚣᚫᛁᛋᚩᚦᛚ
•ᛟᛚ•ᛋᚪᚢᚪᛈᚻ•
•ᚠᚢᛚᛗ•ᚪᛠᚣᛟᚪ•
ᛚᚢᛝᚾ•ᚳᚢ•ᛒᚾᛏᚠᛝ•ᛁᚢᛁᚢ•ᛟᚫᛂᚠᚫ•ᚢ
ᚷᛉᛇᛈᛉ•ᚣᛠᛚᚪᛉ•ᛟᛉᛡᚦᚻᛠ•ᚾ
ᚪᚳ•ᚢᚷᚾ•ᛈᛖᚾᚦᚩᚢᛁᛡᚱ•ᛏᛁᛒᛇᚳᚠᚷ•ᚩ
ᚦᚪ•ᛁᛈᚻᛡᛒ•ᚹᛈᚻᚱᛞᛉᛏᚢ•ᚣᛒ•ᚠᛋᛉᚢ•ᛗᛁ•
ᛡᚱ•ᛝᚢᚠᚦᛝ•ᛈᛟᛒ•ᚻᚷᚻᛡᛚ•ᚩᛞᚪᚳ•ᚦᛈᛞᛋ
ᛡᚻᛇᛚ•ᚢᛏᛋᛞ•ᚦᚢᛞᛝ•ᛚᛉᛝ•ᛏᚩᛚ•ᚪᛚ•ᚣ•ᛟ
ᛡᛉᚣ•ᛒᚻᚫᛂᛡᛁ•ᚱᚦᛚᚠ•ᛠᚾᛝ•ᛉᛗᛒᚩᛠᛈ•
ᛖᛞᚪᚫᛏᚩᛠᛖᛠᛉᚳᛠᛏ•ᚩᛞᚳᛠᚾᚳᚦ
ᛗ•ᛞ•ᚷᛁᚳᚹᛟ•ᚪᚢᛒᚳᚫ•ᚦᚱ•ᛋᚣᚪ•ᛏᚦᛒ•ᛝᚹᛋᚱᛁ
ᛝ•ᛒᛁᚪᚫᛚ•ᛏᚱᛡᚫᚠᛞ•ᛝᛂᚩ•ᛡᛠᛉ•ᚪᛡᚻ•ᚱᛒ
ᛁ•ᛞᛡᛂᚪᛈᚱᛋ•ᚢᛡ•ᚻᚷ•ᛚᛟᚠ•ᚻᚷᚫᛋ•ᛈᚹᚷᚷ
•ᛗᛟᚪᚾᚱ•ᚩᛟᛞ•ᚷᛟᚠᛠ•ᛡᚷᚳ•ᛉᛠᚠᛚ•ᛒᚫ
ᛈ•ᚩᛂᛈ•ᛂᛗᛠ•ᚾ•ᛉᚪ•ᛡᛖᛋᚷᚫᚦ•ᛂᚷᛉᚩᚦ
ᛂᚳᚣ•ᚢᛂᚦᛂᚪᚾᛏᛒ•ᚳᛈᛡᛂᛋᚫ•ᛋᛗ•ᚻᛞᛠ
ᛉᚢᛗ•ᛏᛠᛖᚣᚠ•ᛂᛏᛋᛗᛞᛟᛁᛝᚪᛉᛖᛈ•ᛚ
ᛇᛞᚦ•ᚪᛋᛉ•ᚳᛒᚢᛟᚳᛒᛚᚾᛟᛝᛉᚩ•ᛖᚳ•ᛝᛟ
ᚳᛁᛒᛈᚫ•ᚣᛖᛂᛝ•ᛞᚢᚱ•ᛉᛟᚩ•ᚠᚹᚩ•ᚣᛁᚠᚢᛇ•ᛚ
ᛏᛈᛒᛗ•ᛇᛝ•ᚢᚳᚱᛡ•ᛖᚩᛁᚣᛂᛏᛡ•ᛖᚠᛇᚠᛚ•ᛁ
•ᚣᚷᚠᛝᛡᛈᚷᛒ•ᛡᚩᚷᛡ•ᛟᚾᚹᛡᛈᛟ•ᚦᛈ•ᛟᚷ
ᛚᚦ•ᛈᛞ•ᚦᛇᛒ•ᛡᚪᛒᚪ•ᚾᛗ•ᚳᚾᛖᛡᚹᛝᛏᚱ•ᛝᚫ
ᛚᛟᛁᛇᚣ•ᛝᛡᚾᛏ•ᚱᛁ•ᛋᚪᛖ•ᛇᚢ•ᛝᛞᛂ•ᚠᚱᛠᛗ
ᛠᚪ•ᚫᛈ•ᛏᚠ•ᛖᛏᚷᚾᚠᛁᚠ•ᚱᚻᚱᛇᛒ•ᚻᛈᛏ•ᛇᚱ
ᛝᛡᛒᚹᛚᛏ•ᛗᛉᚦ•ᚾᛂᚳᚫ•ᚷᛈ•ᛋᛖᚩ•ᚢᛝᚩ•ᛏ
ᛈᛁᚣᚾᚪ•ᛏᚹ•ᚠᛗᚾᛟᚾᚳᛒ•ᛂᛉᛡ•ᛟᚪᛁᚫᛝ•ᛒ•
ᛉᛏᛂᛁᛋ•ᛠ•ᚳᛖᚱᚦᚣᚩᚣ•ᛈᚫᚷ•ᛡᛂᛁᚩi •ᚱᚦ
ᛠ•ᛇᚦᚩᛉ•ᚾᚱᚾᚫᛁᛉ•ᛁ•ᛝᚣᚫᛡᚫᛗ•ᚹᛖ•ᛇᚷᚻ
ᛖᛗ•ᚷᚢᛞᚹ•ᛂᚻ•ᛉᚱᚢᛂᚢᚾᛈ•ᛋᚣᛂᚫ•ᛈᚳ
ᚣᚳᛒᛡ•ᚫᛟᚪᚠ•ᛏ•ᚷᚩᛇᛟ•ᛁᚱᛗ•ᛖᛉᛟ•ᛗᛇᚫᛟ
ᚦ•ᚱ•ᛞᛁᚢᚦᚻᛗᛡᚾ•ᛁᚦᚻᛚ•ᛏᚳ•ᚪᚦ•ᚠᚪᚫᚣᚻ
ᛠ•ᚦᚠᛋᚠᛝᚷᚱᛈ•ᛏᛂᛉᛟ•ᚷᛚᚻ•ᚩᚪᚦᛏᚳᛁ•ᚠ
ᚣᚢᛁᚹ•ᛟᚪᚣᛁᛠᛂᚪ•ᛟᛝᚦ•ᛟᚠᚦᚾ•ᛇᚷ•ᛠᛚᛒᚠ
•ᛠᚪᛂᛇᛠᛚ•ᚱᚷᛋ•ᚹᚩᛒᛁ•ᛠᚳ•ᛁᛞᛂ•ᛖᛗᚱ•ᚷ
ᚪᚻᛠᛚᚷᚩ•ᛉᚻ•ᛡᛝ•ᛞᚱᚹᚩᛈᛡ•ᚣᚳᚦ•ᛁᛇᚢᛁ•
ᛟᚦᚠᚳᚻ•ᚩᛁ•ᛝᚾᛁᛞ•ᛏ•ᚫᚱᛝᚫᛈ•ᛠᛞᛇᛉᚳ
ᛠᚩᛟᛖ•ᛗᛈᛒᚦᛝᛋᚢᛡ•ᚻᛡᛏ•ᛉᛇᚷᚠᛡᛡ
ᛟᚢ•ᛡᚦᚣᛞᚪᚫᛝᛒ•ᚳᚩᚷ•ᛏᛞᚦᛁ•ᚠᛒᛖ•ᚦᛟᚳ•
ᚠᚻ•ᛞᚠᚣᛋᚾᛟ•ᛠᛇᛂ•ᛖᛉ•ᚩᛈᛠᛚᚪ•ᛟᚩᚾ•
ᛂᛉᛋ•ᚣᚫᚷᛖᚩᛟᚢᚱᚹᚢ•ᛟᛡᛂᛇᚢᛞᛉ•ᛒᛇ
ᚳ•ᛝᛚᛗᛠᛗ•ᚪᚱᛡᛗᛒᚩᚹ•ᛋᛖᚾᚻᚣ•ᛈ•ᛞᛚᛞ
•ᛈᛏ•ᚪᛞᛚᛉ•ᛟᚱᚾᚹ•ᛠᚠᛁ•ᛟᚾᛒ•ᛇᛟᛖᛝᚳᚠ
ᛏᛞᛏ•ᛇᚫ•ᛝᚢ•ᛠᛡᚫᛖᛟᛞᛝᛠ•ᚠᛗᛒᛚ•ᛏ
ᚢ•ᛈᚱᚹᛟᛇᛉ•ᚳᛟᛈᛏ•ᚢᚠᚳᛞ•ᛂᛋᛞᛈᛚ•ᚠᛝ
ᚱᛂᚣ•ᛞᛗᛖᚣ•ᚢᛖᛝᛠᚳᛞᛈᚩᛠ•ᛏᛒᚳ•ᚷ
ᚾᚩᛟᚾᚠ•ᚩᛁᚠᚢᛋᚾ•ᛞᚹᛠᛇᛈ•ᚱᚩᚩᛂ•ᚪᛟ•ᛇᛠ
ᛂᛁ•ᛟᛂᛞᚢᚳᛝᚩ•ᚱᛝᛋ•ᛂᛁᛈᛉᛖ•ᛞᛁᚾᛗᛗᚳ
•ᛉᚩᛁᛂᛞᚳ•ᚢᚪᛇ•ᚦᛡᛇᚻᛠᚣ•ᛠᚻ•ᚠᚩ•ᛡ
ᛠᛋᛟᚪ•ᚹ•ᚫᚻᚩᛂᚢᚱᚩᚣ•ᛏᚫᚷ•ᛂᛚᛂ•ᛝᛏ
ᛖᛒᛚᛉᚻ•ᚱᚩᚫᛇᛈᛂᛠ•ᚳᛈᛚᚣᛈ•ᚪᛠᚻᚻᛋ
ᚫ•ᚩᛝᚹ•ᛋᛞᚠᚳᛠ•ᚩᛇᚫᚪᚩᚹᛗᚪ•ᚣᚫᚷᚫᛂᚱᚹ
ᛞ•ᚱ•ᚦᚷᚳᚹ•ᚾᚷᛡ•ᛚᛒᚳ•ᛂᚷᚹᚹ•ᚱᛁᚠᛏ•ᚠᛚ•ᛋᛂ
ᛚᚪᛂᚱᛏ•ᛞᚷᚫᛠᚠᛉᛞ•ᚫᚷᚻᛏ•ᛗᚣᛈ•ᛏᛒᛟ
ᛝ•ᛂᛋᚾ•ᛝᛁᚹ•ᚦ•ᛠᛝᛞᚾᛟᚷᚫ•ᛁᛗ•ᛝᛉᚱᛞᛋ
ᛗ•ᚠᚫᚹ•ᛟᛋ•ᚦᛞᛞᛈᛝ•ᛞᛡᚷᛒ•ᚪᛟ•ᚦᛡᛒ•ᚪᚹ•
ᚾᛉᚫ•ᛚᛈᛁ•ᛒ•ᚠᚾᚠ•ᛡᚩᛏᛞᚾᛋᛖᚳᚻ•ᛖᚻ•ᚢᛟ•
ᚪᛖᛗᛝ•ᛠᚫ•ᛈᚩᚪᛞ•ᚠᚫᚻ•ᚠᛏᚦᛂᛚᛂᛒ•ᛗᛇ
ᛈ•ᛂᚢᛒ•ᚷᛁᛇ•ᛈᛉᚣ•ᛈᛟᚦᛞᚱᛠᚪᛡ•ᛝᛡᛒᛚ
ᚻᚦᚫᛉ•ᛟᚫ•ᚪᛇ•ᛉᚳ•ᛠᚠᚫ•ᚢᚣᚦᛋ•ᚠᛝᚠᚱᚹ•
ᛟᛒᛗᚷᛞᚾᛡ•ᛞᚪ•ᚻᚣᛇ•ᚱᛚ•ᛖᚣᛇᚻᛠᚩ•ᚢ
ᚳᚱᚻ•ᛡᛟᛗᛠᛝᛂᚦ•ᛂᚢᛁᛇ•ᛂᛁ•ᛖᚷᛁ•ᚪᛇᛏ•ᛝ
ᛡᚳᛚ•ᛇᚠᛗᚪ•ᚷᛚᛒᛋ•ᛉᛞᚫᛟᛋᛚ•ᚹᛏᛠᛗ•ᛚᚦ
ᛗ•ᛝᚦ•ᚣᛈᚠ•ᚪᛞᛚᚪᛖᛚᚩ•ᚱᚷ•ᛚᚳᛇᛏᚷᚣᛟᛗ•
•ᚪᛁ•ᚷᛂᛒᛡᛗ•ᛞᛈᚪᚳᛠᚷᛋ•ᛏᛈ•ᚩᛋᛏᛗᚱᚣ
ᛋᛉ•ᛁᛂᛚᛝᛚᛁ•ᛉᚢᛠᛗᛇᚢᛋᚻ•ᚳᛉᛂᚩ•ᚠᛂᚠ•
ᛁᚣᛁᛟ•ᛏᚷᚱᚦ•ᛡᛒᛋᚳ•ᛇᚢᚷ•ᛚᚱ•ᛁᛗᚱ•ᛗᛝᚻᛈ
ᚫ•ᛝᛋᚫ•ᛖᛈᛁ•ᛒᛇᚹᚫᚢᛂᚳᛒ•ᚦᛋᚹᚦᚫ•ᛡᛟᚷᛚ•
ᛞᛚᚢᛟᛡ•ᚱᛞᚱᛒᛂᚳᚢᛠ•ᚩᛉᛉ•ᛝᛡᛂ•ᛁᚫᛟ
•ᛖᛗᚹ•ᛖᛉᚦᛗᚪᛋᛉ•ᛞᚦ•ᛡᚢ•ᛉᛗᚫᛋᚳᛖ•
ᚳᚫᛠ•ᛞᚳᚷ•ᚩᛁᛇ•ᚾᛟᚷᚣᚳᚦᚳᚦ•ᛗᚣ•ᛈᚪᛒ
ᛈ•ᚻᚢᚻᚾᛏᚫᛒᛇᚩᛁᛈ•ᚫᚩ'ᚣ•ᛡᚣᛗᚷ•ᚠᚱᛡᛚ
ᛏ•ᛖᛟᚩᛈᛚᚩᚷᛁᛟᛠ•ᛞᛖᚳᛗᛁᚣ•ᛈᛚ•ᛁᚹᛋᛂᚹ•
ᛟᛡᚪ•ᚦᛖᚩᛂᚷᛋᛝᚣᛗᛟᚻ•ᛗᚠᚦᛉᚦᚫᛋᛈᚣᚩ
ᚠ•ᛈᛟᛋᛖᚫᛇᛗᛚᛈᚾ•ᛡᚠᚳᚾᚩᛂᛋᛡ•ᚫᛂᚦᚪᛠ
•ᛈᚻᛋᛟ•ᛗᚹ•ᚱᚣᛁᚢ•ᛉᚹᛋᚱ•ᛞᛈᚦᛈᚩ•ᛞᛂᚩ•
ᚢᛈᛖᚪᚫᛉᚫ•ᛏᚱᛟᛏᛒ•ᛠ•ᚫᚳᚾ•ᛖᛝᚦᛂᛂᚠ
ᛚᚾᚩᛒ•ᛉᚷ•ᚪᚩᛚ•ᚪᚢ•ᛞᚻᚳᚹᛚᛡᛞᛇ•ᛟᚩᛡᛚᚳ
•ᛡᚳᛉ•ᛝᛠᛝᚷᛝᛞᛂᛏ•ᛠᛈ•ᚹᛈᛗ•ᛈᚱ•ᚫ
ᛏᛖᚢᛝᚫᛡ•ᚾᛁᛠᚻᚦᚣᛠ•ᚫ•ᚩᛉᛋᚩ•ᛂᚠᛏᚷ•
ᚹᛁᚪᛁᚩᛁ•ᛝᛠ•ᚾ•ᚷᛗᚹᚦᛖ•ᚷᛟᚪᚹᛞᚻᚢ•ᛡᚹ•
ᚣᚷᛉᛒᚪᚾᛝᛡᛂᛡ•ᚠᚷᛈᚦᚠᚦ•ᛁᛈᚪᛝᛋᛞᛟᚩ
ᛝᛗ•ᛁᚷ•ᛂᚷ•ᚳᚩᚦᛖᚦᛂ•ᚣᚠ•ᚦᚳᛂᛡᛖᚢ•ᛉᛂ
ᚳᚻᛂᚱᛂ•ᚪᚻᚾᚦ•ᛚᚷ•ᚱᚦ•ᛒᚪᚩᛖᚢᛡᛂᚹᛏᚱᚹ
ᛟ•ᚦᚳᛗᚦᚠᚫᚻ•ᛡᚠᛠᚣᚪᚦᛚᛏᛒᚢᛝ•ᛖᛋᛗᚱ•
ᚪᚹᛒ•ᚹᛒᛗᚱᚾᛗᚻᛗᛁᚾᚪᛞ•"ᛡᛖᚩ•ᚾᚹᛡ•ᚢᛂ
ᚦᛠ•ᛚᚳᚷᛚᛇ•ᛟᛠᛠᚪ"•ᛇᛉᚣᚪ•ᚷᛏᚩ•ᛖ
ᚹᛒᛈᚷᛝᛒ•ᛡᚦᚠᛋᚾ•ᛒᚦᚠ•ᛇᛝᛠ•ᚠᚾᛉ•
ᚢᚪ•ᚹᛝᚷᛉᛞᚷ•ᛁᛒᛁ•ᛇᛏᛒᛁᚣ•ᛠᚷᛋᚫ
ᛈᚹᛗᛠ•ᛇᛂᛇ•ᚹᚻᛁ•ᚷᛠᛒᚢᚣᚻᚣ•
ᛝᚹᚢᚱᛋ•ᚩᛡᚠᛡᛠ•ᛞᛟᚦᛗᚳᚾᛉ•
ᛞᚦᛖᚱᛇᚳ•ᚪᛂᛋᛟ•ᚢᚹᚱᛏ•ᛋᛖᛋᛏ•ᚣᚱᛠᚫᚾ
ᛞ•ᛈᛒᛡᛋᚢᛞᛖᚣᚦ•ᛚᚹᛟᛋ•ᚷᛚᛂ•ᚫᛖᚩᚳᚦᚹ
ᛗ•ᚢᚩᚷ•ᚠᚪᚩᛡᛝᛒᛠᚦᚳᚪ•ᚱᛡᛏ•ᛟᚹᚠᚣᛝᚢ
ᚣᛁ•ᛚᛏᚫᚫ•ᚪ•ᚱᛈᚠᛗᚹᚩᛞ•ᛠᛒᛈ•ᛝᛟ•ᚾᚷᛗ•
ᛡᛖᚩ•ᚾᛚᛉᛝ•ᛁᛡᚫᛗ•ᚻᛖᚹᛗ•ᛝᛈᛇᛗᛡᛂ•ᚫ
ᚩᛡ•ᚠᚣᛉᛟᚫᚦ•ᚫᛒᚩ•ᚪᚦᛂᚱᛂᚾᚦ•ᛡᚠᚪᛏᚾᚻ•ᚷ
ᚢ•ᛞ•ᚳᚦᚢᚱᚢᛟ•ᛞᚻᚱ•ᚷᚹᛏᛈᛖᚠ•ᚪᚻᛠᚦ
ᛞᚱᚠ•ᛖᛂᚫ•ᚾᚳᚻᚹ•ᛇᛡᛈᛠᚹ•ᛗᛚ•ᚹᛟᚹᛠ•ᚪ
ᚾᚪ•ᚳᚪ•ᚷᛚᚦᛒᚩᚹᚢ•ᚷᛚᚠᛋᚻ•ᚾᛉᛝᛗ•ᛖᚦᚢᛝ
ᛡ•ᛈᚣᚢ•ᛉᚷᚷ•ᚹᛞᛁᛋ•ᚦᛡᛡᛈᚳᚪᚩ•ᚢᛗᚢ
ᛉᚩᚣᚻᛏ•ᚩᚫᛗᚢ•ᚩᚾᛏᛠᛒᛟᛒᚠᛁᛈ•ᛚᛋᛝᚫᚳ
•ᚫᛟᛏ•ᚢᚩᛉᚾᛡᛋᚠᛖ•ᛉᚱ•ᛗᚩᚩᚫ•ᚠᚢᚦᛖᛞᚾ
ᚣ•ᛡᛋ•ᛋᚱᛚᛟ•ᚢᚻ•ᚢᚾᛈ•ᛁᚻ•ᛖᛉ•ᚦᛞᛗ•ᛈᛟ
ᚠ•ᛈᚠᛝᚫᛝᛋ•ᛟᛂᚹ•ᛠᛒᚣ•ᛟᚹᛞ•ᚠᚣᛂᛁᛏᛉ
ᛚ•ᚩᚦᛝ•ᚠᚪᛋᛡᛁᚻᛒᚱ•ᚪᚢᚣ•ᚫᚢ•ᛟᛠᚪᚣ•ᛖᛟ
ᚫ•ᛖᛈᚠᛒ•ᛈᛂᛁ•ᛋᛝᛒ•ᚱᚦᚳᛇ•ᛚᛁᚢᛈᛏᚳᛒᛉ•
ᛖᚪᚣᚠᛗᚳᚣᚱ•ᚻᚹᛏᚾᛡᛉᚫᚦᛟ•ᚳᚹ•ᛠᚠ•ᛏ
ᛠ•ᛝᚩᚻ•ᛡᛠᛒᛋᚻᛟ•ᚫᛁ•ᛠᛏᛁᛋ•ᛏᚫᚻᚱ•ᚻᛂ
ᛋᛡᚹᚾᚾᛡᚹᛚ•ᚢᛖ•ᛏ•ᚱᛝᚳᚣ•ᚪᛉᛇᛝᛋᛖᛇᛁ
ᚻᚾ•ᚷ•ᚹᛉᚳᛉᚣ•ᛋᛈᚳᛟᚱ•ᛒᚣᛂᛝᛖᛁ•ᚾᚷᚪ•
ᚣᚷ•ᛚᛒ•ᚢᛂᚩ•ᛝᛉᛉᚪᛖ•ᛒᚦᛉᛡᚱ•ᛏᚷᚹᛂᛋ
ᛁᚠ•ᛠᛁᛡᚦᛝᚾᛖᚾᚠᚩᛗᛖᚣᚪ•ᚳᛖᚳᚹᚪᚫᚹ•ᛇ
ᚢᚦᚻᛉᚢᚾ•ᛠᛚᚢᚾᚦᛈᛋᚢᛈᚱ•ᛞᚫᛟᚱᛡᚫᚪ
ᚢ•ᚢᛗᛚᚦᛠ•ᛚᛝᛈᚣ•ᚩᛋᛟᚪᚱᛗᚦᛟᛈ•ᛚᛋ•ᛏᛁ
ᚠᛋᛖᚹᛝ•ᛗᛞᚩ•ᛠᚫᛡᛒᛏᚩᛋ•ᛖᛏᚪᚠ•ᚫᛒ•ᛚᚾ•
ᛋᚪᛉᛟ•ᚾᛚᚹᛖ•ᚩᛚᛁᛂᛏ•ᛒᚪᚠᛉᛏ•ᚩᛟᛂ•ᚾᚷᛋ•
ᚷᛚᚷᛠ•ᛒᚷᛖᚩᚪᚩᛖᛞ•ᚷᛇᛗ•ᚳᚱᚷ•ᛈᛞᚩᚠᚹ
ᛇ•ᛠᛞᚣᛝ•ᚾᛁᚠᛈᛚ•ᛖᛟ•ᚢᚳᛗ•ᛚᚫᛏᛉᛂᚱ
ᛉ•ᛁᛠᚷᛚ•ᚷᚳᛋᚩᛝ•ᚫᚦ•ᛗᚻᛟᚠ•ᚱᛋᚳᚦ•ᚣᚩ•ᛒᛁ
ᚫᚻᛖᚢᛏᛚᛚ•ᛇᚷᛟᚣ•ᛒᚾᚦᚻ•ᛠᛖᛂᛒᚾᛁᛚᛠ
ᚱ•ᛂᚠᚳᛋᛝᚳᛈ•ᚷᚻᛋᛗ•ᛇᛞᛇ•ᚣ•ᛡᛖᛏᛠᚢ
ᛡ•ᚩᚾᛠᚩ•ᛂᚣᛇᛉᛠᚪᛡ•ᚾᛞᛝᚻ•ᛈᛠᚻᛡ
ᚢ•ᛝᚻᚦᛈ•ᛉᚢ•ᛠᚣᛈᛟᚦᛋᚣᛈ•ᚠᛏ•ᛒᛁᛟᚪᚷ
ᛚ•ᛠᚻ•ᛝᛁᛡᛚᛝᚾᛞᚪᛈᚷ•ᚾᛏᚦᛋᛒ•ᛋᛋᛠ•ᚷᚳ
•ᛠᛗᚢ•ᛖᛉᛒᚷᚫᚠᚩᛁᛉ•ᚠᚪ•ᛠᚱᛇ•ᚩᛁᛞᛋᛚ
ᚦᛖᛒᛇ•ᛟᚷᚣᚷᚾᚷ•ᚦᚠᚳᛗ•ᚩᛖᛖ•ᚩᚠᛒᚻᛝ•ᚳᛁ
ᛂᚪᚾᚩᚪ•ᛈᚻᚱᛗ•ᚱᛗᛟ•ᚦᚷᛂ•ᛒᚱᚦᚪᛠ•ᛉᛖᛡ
ᛞᚦ•ᚱᛝᛂᛒ•ᚾᛏᚣ•ᛏᛋᛒᚾᚫ•ᚢᛖᛁᚩᛡ•ᛂᛇᚢᚦᛚ
ᚳᛖ•ᛚᛁ•ᛒᚢᚠᚪᚱᛠ•ᛗᛒ•ᛞᛉᛗ•ᚢᛠᛏᚣ•ᚪᛂ
ᛈᚢᛈᛠᚣᚷ•ᛗᛡᛗᚢᚪᛗᛝ•ᚣᛡ•ᚪᛖᛏ•ᛖ
ᛋᚪᛟ•ᚳᚻᛁᛋᚠᛁᚾ•ᛈᛟᛝ•ᛇᚦᚣᛏᚫᛉ•ᛖᛟᛏ•ᛞᛡ
ᛚᛖᛈᛏᚪ•ᛏᚠᚱᚾ•ᚪᛠᚱ•ᛠᚳ•ᚾᚻᚹᛒᛇᛋ•ᛁᚻᚣ
ᛋᚹᚩᛉᚹ•ᚩᛝᚢ•ᚻᛝᛟ•ᛏᛚᚠ•ᛂᚷᛏᛂᛝ•
ᛗᛈᚣ•ᛚᛋᚩᚪᚫᚻᛚᛖᛇᛁᛗᛚ•ᛚᛋᚳᛈ•ᚾ
ᚻᚷᚢᛡᚻᚢ•ᛒᚠ•ᛞᛂᚢ•ᛒᛖᛁ•ᚫᚠ•ᛈ•
ᚫᛈᚦ•ᚱᛗᛚᚳ•ᛒᚷᚣᛗᛠᛒᚫ•ᚾᚦ•ᛗᚠ
ᛡᛠᚳᛒᚷᚫᚠ•ᛖᛂᚱᚩ•ᛈᛒ•ᚠᛒᚩ•ᛇᚱᛠᚱ•ᛠᚷ
ᛖᛚ•ᛇᚱᚾᛋᚩᚩᚳᚪᛖᚣᛖᛖ•ᛏᚱ•ᚢᚣ•ᛟᛂᛉ•
ᛠᚷᛝ•ᚣᛏᛝᚾ•ᚪᛏᛋ•ᛝᚪᛂ•ᚠᛚᛋᚢ•ᚹᛠᛈᛁᛏ•
ᛁᚾ•ᚱᚱᛝᛗ•ᚣᛗᚠᛁᚫᛁᚪ•ᚢᛟᛒᚹ•ᛗᛁᚻᚣᚹᛞᛚ•ᛟ
ᛏᛞ•ᛟᚳᛒ•ᛡᛒ•ᚪᛏ•ᚹᛏᛈ•ᚹᛠᚩᚱᚩᛖ•ᚣᛚᛋ•
ᚢᛡᚱᚠᛂᛇᚱᛡᚦᛖᚢᛏ•ᛝᚫ•ᚾᚪᛠᚩᚪᚾᚪᚦᚷᚩ•
ᚫᛉᛒᛏᛖᛠᛗᚷᚱᛗ•ᚣᛝᚠᛒ•ᛞᛟᛞᚪ•ᛠᚱᚳᛁ
ᛈᛞᚠᛗᛝᚻ•ᛋᚩ•ᛞᛈᛉᚾ•ᛟᚱᛡᚾᚳᚳᛏ•ᚾᛈᚠ
ᛈᚳ•ᛂᚦᛒᛁᚹ•ᛞᚹᛝᛠᛡᚹᛚ•ᚹᛂᚾᚪᛟ•ᛏᛞᛉᚣ
ᛖᚱᛞ•ᚱᛏᛇᛁᚳᛈ•ᛝ•ᚦᛟᚷᛂᚦ•ᚣᛋ•ᛠᚻ•ᚠᛒᛚ•ᛁ
ᚫᛚᛞᛉᚪ•ᛁᚹᚷ•ᛒᚩᚹᚾᛠ•ᛋᛖᛗᛒᛋ•ᚳᚹᚦᛟᚠᚻᚫ
•ᛞᚢᛁᛒᛞ•ᛇᛝᛈᚠᛁ•ᛟᚢᚣᛏ•ᚻᚱᛖᚾᚳᛈᛡᛈᛞ
ᛂ•ᛁᛏᛗᛋᚫᛉᚩᚣ•ᚪᛂᛗᛡᛖ•ᛇᛂᚠᛗᚱ•ᛞᛟᚪᛒ
ᛞᚻ•ᚾᛈᚪ•ᛇᚱᚻᚾᛝᛠᚠᚾᚠ•ᚩᛗᛋᚾ•ᛠᚪᛁᚢᛚ•
ᚪᚫ•ᛂᛉᛡᚠ•ᛁᛖᛈᛠᚻ•ᚠᛇᚩᚹ•ᛠᛂᛇᛁᛠᚫ•ᛂ
ᛒ•ᛋ•ᚠᛖᚷ•ᛋᛁ•ᛟᛗᛒᛁᛝᛏᚪᚢᛁᚦ•ᚩᛝᛗᚠ•ᚹᛟᛒᛟ
ᛡ•ᚠᚣᛝᚩᛠ•ᚳᛚᛈᚱ•ᛞᛂᚩᛝᛂ•ᚪᛖᛗᛈᚾ•ᚠ
ᛠᚷᛞᛒ•ᚩᛉᚷᚾᚣᚷ•ᛠᛈᛂᛞᚾᛟᚩᚢᚾᚹᛗ•
ᛂ•ᚢᚷᛠ•ᛗ•ᛇᚪ•ᚻᚦᛡ•ᛝᛈᛞᛒ•ᚳᛉᚳ•ᛠ
ᛉ•ᛟᚣ•ᛒᚦᛁᛂᛚᛡᛝᛡ•ᚹᛂᚫ•ᛋᛗᚪᛡᛠᛇᛝᛏ•
ᚦᛞᚷ•ᚢᛏᛚᛏᚣ•ᚢᛝ•ᚷᛟᚪᛏ•ᛂᚦᚣ•ᚫᚻᚪ•ᛒᛝ•
ᚦᚢᚱᚪᚾᛞ•ᛁᛝᚫ•ᛚᚫᚷ•ᚹᛁᛒᚣ•ᚾᚫᚠ•ᛚᛋᛒ•ᛈᛟᚪᛟ
ᛞᚷᛟᚣᛉᚷᛚ•ᛋᛠᛁ•ᚳᛟᛁᚦᛈᚹᛉ•ᛖᚢ•ᛟᛂᛝ
ᛋᚢᛝ•ᚳᛡᛠ•ᛚᛇ•ᛚᚷᚢᛁᛏᛒᛋ•ᛞᛁ•ᚠᚠᚷᚠ•ᚦᛂ
ᚳ•ᚫᛟ•ᛁᛗᛡᛁᛇᚦ•ᚩ•ᚢᛈᛒ•ᚻᛋ•ᛂᚣᛂᛖ•ᛒᛇᛇᚱ•
ᚹᛂᛏᛡ•ᚳᚪᚫ•ᚩᛈᚱ•ᛡᚾᛗᛁᛝ•ᚻᚹᚦ•ᛡᚦᚻᚦ•ᛉ
ᚫᚫᛋᚳᛡᚾᛇ•ᛟᛉᚢ•ᚱᛂᛖ•ᛚᚾᛞ•ᛗ•ᛏᚱᛟᚦ•ᛁᛝ
ᛡᛒ•ᚳᚩᚹᛟ•ᛏᛗᛋᚱᚷ•ᚱᛚᛞᛚ•ᚩᚣ•ᛞᚳᚪᛖᛞᚠ
ᚳ•ᛇᛖᛉᛚᚫ•ᛖᚩᛁᛋ•ᛡᛁᛟᛋᚪᛒᛗ•ᛗᚣᚹᛂ•ᛖᚫᛝ
ᛚ•ᛂᚱᛇ•ᛈᛚᚩᚻ•ᚪᛞ•ᛡᛂ•ᛞᚠᚹᛞᛂᚳ•ᚾᚦᛉ•ᛂ
ᚻ•ᚷᛚ•ᚠᛖᚦ•ᛇᚻ•ᛝᛖᛒᛚᛞᛁᛗᚠ•ᚹᛒᛗᛟᛁᛖᛁᛠ•
ᛈᚻᛝᛖᛞᛟᚩᚻᛂ•ᚹᚩᚾᛂᛈᛗ•ᛖᚳ•ᛖᛇ•ᚷᚻᛗ
ᛞᚪᛈᛖ•ᛗ•ᛉᚫᛒᛇᚱ•ᛖᚣᛟᚣ•ᚱᛠᛈᚢᛠ•ᚣ
ᛖᚪᚻ•ᚩᛉᛠᚢᚻᛡᛟ•ᚷᚫᚩᛒᛉ•ᚫᚱᛞᛋᚩᚱ•ᚷ
ᛠ•ᛉᚻᛁ•ᚷᚳᛞᛠᛡᚳ•ᛂᛠᛉᛇᚻᛋᚹ•ᛝᛡᚷ
ᛖᛡᚣ•ᛠᚩᚷ•ᚱᚦᚠᛟᚩᚦ•ᚦᛁᛏᚱ•ᛇᛉᛇ•ᚢᚷᛠ•
ᛟᛏ•ᚩᚠᛚ•ᛟᛝᛈ•ᚱᛡᚪᚩᛏ•ᚩᛠᚷᚫᛗ•ᛈᛋᚱ•ᛖ
ᚦᚠ•ᛞᚹᚾᛚ•ᛝᚩᛇᛂ•ᚳᛚᚢᚹᛏ•ᚩᛖᛏᚠᚪᛚ•ᛟᛇᛟ•
ᛠᚱᛇ•ᚢᚪᚦᛈᛟᛡᛉ•ᛡᛒᚱᛒᚠᚢᛚᚢᛟ•ᛒᛇᛒ•
ᛉᚦᚹ•ᛝᚣᛖ•ᚳᚫᚣᛟ•ᚹᛁᛝᚫᛏ•ᚫᛇᛈᛡᛟᚠ•ᛚ•ᛝ
ᚠᛡ•ᛞᚪᛚᛈ•ᛋᛁ•ᚢᚣᚪᛚᛠᛝᚹ•ᚪᛏᛈᚳᚣ•ᛝᚫ
ᚻᛗᛞᚷᛚ•ᛠᛉᛒ•ᛇᛡᛋᛖ•ᚣᛁᛚ•ᚣᛠᚣ•ᚻ•
ᚣᛉᚾᛏᚫᛉᛋᚦᚪᚹᛗ•ᚪᚱ•ᚪᚩᚻ•ᛗᛖᚫᛞᛠᛁᛗ
•ᛒᛟᚾᚳᚩᚱᛉ•ᛋᚹᚫ•ᚻᛖ•ᛋᚠᚾ•ᚢᚦᛟᚷᛖᚪᛟᛇᛇ•
ᚦᚳᛒᛝᛏᛉᛡᛞ•ᛋᛡ•ᚩᚠ•ᛈᛖᛞᛋᛁ•ᛚᛁᚻᚾᛝᚱ•
ᚻᛈ•ᛇᚢᚫᛞ•ᛚᚻᛉᚳᛈ•ᛁᛗᛉᚳ•ᛂᚫᚾᛞᛋ•ᛏᛚ
ᛡᚩᛋᛗ•ᛚᛞᚾ•ᛈᚫᛏᚷᛈ•ᚫᚦᛂᛗ•ᛒᚻᚩᚻᛁᚷᚻᚳ•
ᛚᚹᛋᚱᛇᛗᛏ•ᛂᚳᛁ•ᛠᚦᛞ•ᛏᛚ•ᚱᛖᛠᛒᚪ•ᛒᚠᛒ•ᛁ
ᛒᛡᛇᛏᚣ•ᛏᛖᚣᚳᚱᛋᚠ•ᛁᚦᚪᛉ•ᚪᚣᚫᛠ•ᛂ•ᛈ
ᛗ•ᚠᛋ•ᚪᛒᚱ•ᛉᚣᚻ•ᚦᚩ•ᛇᛞᚢ•ᚠᛁ•ᚻᚩᚫᚠᚣᚷ
ᚱᚪᛂ•ᛏᛉᛇ•ᛖᛠᛞ•ᛏᚠᚢᛝ•ᚫᛂᛖᛈᚳᛒᚦᚢ
ᛝ•ᛡᛒᚹᚱ•ᛖᚾᛈᛇᚣᛇ•ᛉᚱᚹ•ᛒᛡᛞ•ᛖᚱᚩᚻᚣ
ᛠᛈᚦ•ᛗᛁᚷᛚ•ᚹᛉᚫ•ᚠᛞᚾ•ᛂᛟ•ᚻᛚᛡ•ᛗᛖᚷ•
ᛟᛁᛡ•ᚻᛟᚱᛇᚹᚣᚠ•ᛈ•ᛂᚷᚦ•ᚪᛒᛝ•ᛈᛒᚪᛖ•ᚢᚹᚻ
ᚩᛒᛋᛉ•ᚹᛞ•ᚦᛇᚱᛖ•ᛂᚾᛞᛝᚹᚪ•ᚻᛖᚹ•ᛟᛡᛂ
ᛡᛟᛝᛂᛉᛚᛂ•ᛞᛉᛟᛈ•ᚱᚪᛁᛏᚷᛉᛝᛇ•ᛠᛗᚩ
ᛚ•ᚦᚫᚹ•ᚫᚢᛈᛡᚳ•ᚹᛝᚻᚹᛒᛗᛋᛟᛖᛁᛡ•ᛟᚹᚦᚻᛒ
•ᛡᚱᛏᚦᚠ•ᚠᚩᚦ•ᚻᚩᛗᛖᛉᚹᛞᛋᛚᚠᛞ•ᛝᛒᛇᛡ
ᛚᚪ•ᚹᛞᚾᚫᛉᛏᚣᛗᚷ•ᚦᚹᛉᛡᚦ•ᚹᛒᛋᚱᛉᛡᛉ
ᚪ•ᚢᛒᚻᛠ•ᚹᛝᚢᚻᛇᛝᛡᛠᛂ•ᛋᛈᚦᛏ•ᛟᛝᚩ
ᛗᛒᚢᛞᛋ•ᛒᛂ•ᛠᚱᛟ•ᛖᚾ•ᚾᚹᚷᚢᛚᚪᚩᚣ•ᚢᛏ
ᚠᛂᛏ•ᚪᚷᛒᛇ•
ᛞᛇ•ᛉᚳᚠᛁᚪᚹᚻᚷ•ᛇᛟ•ᚠᛏᛖᛟᛠᚪ
ᛡᛋᚷ•ᚣᛠᚾᚦᚫᚱ•ᚩᛡᛗ•ᚹᛉᛗ•ᚣ
ᛞᛒᛏᚱ•ᚢᛂᚻ•ᚫᛟ•ᛡᛝᚹᚻᛋᚠᛡ•ᛚᚦ
ᛏ•ᛁᚹᛏ•ᚩᚢᚾᚹᛗᛚ•ᛋᚦᛠᚹᛂ•ᚪᛂᚫᚷᚣᛗᚹᛞ•
ᛈᛡ•ᛖᛂᚹ•ᛖᚢ•ᚻᚹ•ᛝᛁ•ᛋᚫᚷ•ᛂᛚ•
ᛝᚦᛇ•ᛁᚠᚳᛟᛇ•ᛞᚹᚣᛡᚣᚢ•ᚣᚾᚦᚱᛖ
ᛗᛁ•ᛇᛞᚱᚹ•ᛉᚹᚻ•ᚳᛂᛡᚪ•ᚾᚹ•ᚾᛗ•ᚠ
ᛇᛁ•ᛇᚪ•ᚩᛋᛒᛟ•ᛏᛂ•ᛈ•ᛖᛈᛂᚩᚹᚢᛠ
ᛝᚹ•ᛗᚳᚩᛏᛏᚠᚢᛂ•ᛞᛠᛉᚩ•ᛉᚦᚷᛞ•ᛒᚩᛏᛚ
ᛇᛁᛒᛡᚪ•ᛖᚠᛠᚢᛖ•ᛈᛋᚹᛞᛞ•ᛋᛡ•ᚹᚦᛞᛋ•ᛝ
ᛂ•ᛚᚷᚢᛡ•ᚾᛉᚠ•ᚱᚪᚣᛗᚠᚦᚻ•ᚱᚪᚱ•ᚫᚪᚷᛟᛞ•ᛒ
ᛗᛒ•ᚾᚻ•ᛇᛞ•ᚻᛗᛚᛁ•ᛠᚾᛁ•ᚫᛖᚢ•ᛏᚦᛇᛋᛈᚻ
•ᚻᛇᚳᛠᚫ•ᛞᛚᛋᛝ•ᛁᚹ•ᚪᚳᚩᛏᛇᛝᚷ•ᚳᚦᛋᛠᚠ
ᚢᛝᛚᚻ•ᚹᚩᛇᚪᛈᚷ•ᛇᛗᛚᛂᛋᛏ•ᛚᚳᛈ•ᚾᛋᛝ•ᚳᚪ
ᚳ•ᚾᛉ•ᚾᚢᛉᚫᛗᛏᛞᛏᚫ•ᛟᛗᛋᛉ•ᛏᚣᛉ•ᛇ
ᛠᚷ•ᚻᛒᚾᚷᛇᚢᛟ•ᛂᚦᛉᚩ•ᚾᚪ•ᛞ•ᚩᛈ•ᛠᛚᛋ
ᛏ•ᛒᚷᛁᚢᛟᛖᛁ•ᛂᚦᛖᚻᚹ•ᛂᚫᛂᚾᚻᛉᚹ•ᛒᚪᛋ•ᚠᚱ
ᚱᛁᛉᚢᚦᚻ•ᚢᛗᚪ•ᛞᛝᛠᚪ•ᚫᛉᛖᚾᚹ•ᛟ•ᛝᛞ
ᚾ•ᛈᚫᚳᛡ•ᛈᚠᛉᚩ•ᛒᚷᛗᚫ•ᛚᚻᛞᚣᛖᛉᛒ•ᛂᚹ
ᛇ•ᛈᚩᛁᚦᚠ•ᚷᚾᛈᛞᛝᛏᛖᚪ•ᛂᛋᛠ•ᛈᛝᚢ•ᛒᚷ
ᚳᛉ•ᚪᚢᛈᛚ•ᛂᚱᚷᚣᚪ•ᚪᚠ•ᛗᛝᚣᚳᛟ•ᚹᚣᚷ
ᛈ•ᛗᛖᚩᚹᚢ•ᛟᛞᛋᚱ•ᚣᛞᛋᚳᛡᛉ•ᚻᚦᚹᛚᛞ
ᛠᚩᛞᛠᚢᛟᛖ•ᛠᚹ•ᛉᚻᛡᚹᛞ•ᚪᛗ•ᚠᚦᛈ•
ᛝᛏᚳᚪ•ᛠᚣᚷ•ᚳᚦᛖᚾᚢᛁᚫᛁᚢᛡ•ᚹᛚᚳ•ᚻᛈ•ᛞ
ᛂᚳ•ᛗᛒ•ᛗᚪᛂ•ᚩᚪᛞᛁ•ᚩᚱᛟᚠᛖᚣᛟᛁ•ᛇᛟ•ᛁᛈᚣ
ᛚᚪᛡ•ᚳᛏᛠᛋᛖᛒᛝ•ᚫᛟᚫᛞᛖᛞᚣᛡ•ᛠᚪᛖ
ᚦᛚᚫ•ᚳᛋᚪᚩᚷᚹᛚ•ᛈᛖ'ᛏ•ᛂᛉᛝᛚ•ᛏᛉᚩᚣᛝ
ᚠᚩᚣ•ᛁᚻ•ᛟᚫᚷᛂᛝᛡᚾᛗᚣᛟᛡ•ᛝᚷᛖᛉ•ᛟᛉ
ᛈᛚᛋᛉᛠ•ᛚᛡ•ᚱᚪᛞ•ᛠᚷ•ᚱ•ᚳᛇᚻ•ᛗᚪᛟᚷ•
ᛞᚪᛋᛡᚻ•ᛈᚷᛖᚳᛟᚱᛟᚢ•ᛁᚫᛟᚦ•ᛂᚱᛡ•ᚱᛖᚦ
ᛒ•ᚣᛏᛝᛡᚩᛏᚦᚳ•ᛉᚳ•ᛋᚪᚫ•ᛗᚠᛂᚱᛖ•ᛡᛇᛁᛇ
ᛟᛉᚳᚹᚪᛖ•ᛋᚢᛉ•ᛋᛟᛚ•ᛂᚾ•ᛈᛇᛒ•ᚦᚦ•ᛁᚫᛚᛋᛝ
ᛂᛂᛡ•ᛟᚻᛇᚢᛚ•ᛁᚱ•ᛡᚻᛚᛏᚹᛉᛇ•ᚱᛏᛠ•ᛁᚫᛚ
ᛗ•ᛁᚱᚷᛏᛠ•ᛇᛟᚻᛟᚳᛋᛏᚾᚩ•ᛁᚱᚷ•ᚹ•ᛞᚢᚣᛚᛁ
ᛗᛒᚢ•ᛚᚱ•ᛏᛁᚢ•ᚷᚳᚠᛇ•ᛚᛇᚣᛏ•ᛏᚫᚢ•ᚫᛠᛇ
ᛖᚾ•ᚢᚹᛝᚻ•ᚷᚣᚱ•ᚩᛁ•ᛚᚾᛉ•ᚾᚩᛈ•ᚠᛠᚫᚫᚩ•ᛉ
ᚾᛋᛟᚫᛚ•ᚾᚫ•ᚦᚢᛠᚣᚫ•ᛈᛁᛇᚢᚱᛂ•ᛈᛟᛂᚪᛝᛈ
ᚦᛈᚪᛝ•ᚣᛗᛟ•ᛉᛒᚢᛏᛇᛗᛈᚫᚣ•ᛉᚫᚣᚱᚫᚣ
ᚠᚠᛗᛡ•ᛉᛖ•ᚱᚢᛏᚷᚢᚣᚱ•ᛡᚢᚩᛇᛁ•ᛂᚠᛈᛂ
ᛞ•ᛁᚦᚩᚻᛡᚷᚻ•
1 ᛚᚦᛇᛟ•ᚪᚫᛠ•ᛗᛉᚻᚳᛉᚪᛏᚦ•ᚫᛉ•ᚩᛋᚳᛞ
ᛏ•ᚣᚹᚾ•ᛟᛏᛉ•ᚹᛁᛟᛂᚠᛁᚩ•ᛁᚱᛋ•ᛉᚾᛗᚪᛡ•ᚱᛈᛋ
ᛞ•ᛁᛟ•ᚻᛖᛏᚢᚹ•ᛠᛟᛞᛟᛂᛁᛝᛡ•ᛂᚱᛞᛗᛒ•ᚩ
ᚳᚩ•ᚦᛟᚱᚢᛚ•ᚢᚦᛋᚢᛞᛚ•ᚷᛁᚣᛝᚩᛟ•ᛁᛖᚣ•ᛖᚠ•
ᛇᛝᛒᛚᛁᚢᚣᚠᛟᚾᛟ•ᛒᛟᚷᛂᚪᚾᛗᚫ•ᚣᚦᚠ•ᛁᛒᛝᛈ
ᚾᛁᚱᚷ•ᛂᛇᚫ•ᚻᚪ•ᚱᛉᛉ•ᚩᛚᚾᚫ•ᛞᚣᛒᚾᚪ•
2 ᚾᚣᛖᛉ•ᚾᚢᛉᛁ•ᛝᛏᛈᚹᛋᚣ•ᛏᛠᛈᛉ•ᚪᛁ
ᛂᛋᚱᚪᛏᛋᛝᛏ•ᚳᚷᚳᚻ•ᛖᛟᚱᚪᛡᚻᚳ•ᛝᛒᛖᚱ
ᛠᚪ•ᛚᛟᛖᛚᚪ•ᚦᛋ•ᚳᚹᚱᚹ•ᚩᚻᚣ•ᚢᛝᚩ•ᛈᛚᛁᛏᚪ
•ᚠᛋᛝᛞ•ᚳᚪᚱᛒ•ᚹᛈ•ᚾᚩᚦᚳᚦᚾᛗᚩᛖ•ᚣᛇᚾ•ᚠᛒ
3 ᛞᚢᛈ•ᚹᚾᛖᚪ•ᚱᛚᛁᚹ•ᚫᛉ•ᛝᚠᛞᚪᚠ•ᛒᛂᛉ•ᛞ
ᛂᛝᚣᛇᚪ•ᚫᛂ•ᛝᛈᚪ•ᚢᛠ•ᛇᛏᚱ•ᛖ•ᚫᛗ•ᚫᛠ
ᚻ•ᛁᚫᛟ•ᛠᚹᚳᛂᚦᚻ•ᛡᚩᚢ•ᚩᚦᚷᛡ•ᚻᛋᚷᚪᛁᛟᛞ
ᚪᛂ•ᛁᚹᛡᛒ•ᛗᛝᛡᛞᚠᛒᛋᛏ•ᛒᚷᚠ•ᚷᛟᚢᚳᚫᛏᛁ
ᛖ•ᚱᚷᛗᚣ•ᚪᚷᚹ•
4 ᛝᛂᛋᛂᛗᚱᛗ•ᚾᛒᛋᛗᛉᛞᚻᛉᛁ•ᚣᛡᚻᚣ
ᛠᛉᚻ•ᛞᛖ•ᚹᛖᚦ•ᚢᚳ•ᛉᛗᚪᚣᛠ•ᚹᚫᚪᚳ•
ᚢᚫᚳᛇᚳᚣ•ᛡᚫᛏᛖᚳᚠ•ᛋᚻ•ᛋᚱᚢᚦ•ᛁᛋᛝᛗᛞ
ᚫᚢᛠᚢᚪ•ᚾᛝᚳ•ᛖᛈᚹᛉ•ᚢᛉᚫ•ᚾᛈᚳᚻᚱᚣ
ᚹᛚᛉᚱᛒ•ᛗᚫᛟᚣᚩ•ᚳᛇᛗ•
5 ᚻᚫᛉᚦᛒᛟ•ᛏᛟᚹᛂ•ᚫᛠᛗᚠᚫᚳᚷ•ᛇ•ᚻᚹᛗ
ᚻᛝᚣ•ᛁᚩᛁ•ᛏᛁᛖᛡᛂ•ᛗᚣᛚ•ᚻᚱᚩᛞᛒᛡᛈᛠᛗ•
ᚳᛠ•ᛖᛒᚢ•ᚷᛁᚦ•ᛟᚫ•ᛡᚻᛝᛖᚾ•ᚱᛠᛡᛋ•ᚻᛏ
ᛝᚻᚪᚷᚩᛝᚫ•ᚹᛚᛏᚱ•ᚷᛁᚾ•ᛖᛠᛂᛡᛞᛋᚻ•ᛝᚾ
ᚳᛋᚾᛞᛇᚾᛋᛁᚳᛡ•ᚱᛝᛚᚫᚣᛇᛚᚩ•ᚳᛞᚾ•ᛝᚷᛡ•
ᛝᛂ•ᚻᛂᛚᛠᛟ•ᛂᛏᚷ•ᛚᛒᛝᚢᛏ•ᚻᚳ•
•ᚫᛞᛟᚫᛟᛗ•ᛟᚫᚪᚻᚱᛗᚢ•ᚣᚢᚣ•ᛈᛗ•ᚪᛂᚫᛟ
ᛠᛚᚠᛖᛡᚢ•ᛉᚻ•ᚪᚩᛡᛒᛠᚢᚷ•ᚻᛏᛠᚪᛞ•
ᛋᚹ•ᚦ•ᚾᛋᛁᚻᛒ•ᛉᛠᛝ•ᛒᚢᛚᛟᚢᚾ•ᚢᚦᚩᛗᚪ•ᚾ
ᛞᚫᛇ•ᚫᚣᚪᛋ•ᚣᛝᛡᛗᚷᛇᛈ•ᛠᚳᚻᛝᛚ•ᚠᚷ
ᛡ•ᛁᛡᚪᚠᛒᛈ•ᚳᛋᚦᛠᚦᚫᚱ•ᚷᛞᛚᛟ•ᚷᚱᛁᛇ•ᚣᚩ
ᛟᚢᛝᚱᚷ•ᛗᛏᚷᛒᛈᚷ•ᛗᛏ•ᛗᚣᚹᛒᛏᛒ•ᚷᚣᛈ
ᚷ•ᚾᚦᛇᛒᚳ•ᚷᛖᛇᛟᛚᛈ•ᚹᚾ•ᚻᚷᚱᛇᛏ•ᛈᚷᛒ•ᚹ
ᛗᛋᚹᛟᚻ•
ᛡᚳᛋ•ᛈᛞᛋᛡ•ᚪᚹᛏᚳᚹᛟ•ᛗᚹᛁᛒᛞ•ᚷ
ᛇᚢᛚ•ᛉᛋᚫ•ᛟᚻᛚᚦᛒ•ᚣᚪᛚᛞᚦᚠ•ᚻ•
ᛞᛝᚩᚢᛋᚪᚫ•ᛖᚦᛁ•ᛏᛂᛏ•ᛝᚦᚾᚳᛉ
ᛏᛝ•ᚳᛈᛁ•ᚾᛏ•ᛒᚾᛡᚱᛒ•ᚢᛈᛋᚦᛁᚳᛈᛋᛁᚹ•ᚹᛚᚣᚾ
ᚢ•ᛒᛁᚪᛠ•ᚹᛟᚳ•ᛠᚢᚪ•ᛚᚦᚹ•ᚠᚾᛏᚳᛡᛁ•ᛚᚩ•ᚾ
ᛗᛂᛠ•ᚦᛟᛂ•ᚪᚦᚹ•ᛡᚾᛖᛠᛈ•ᛒᛋᛂ•
ᚠᚾᛗ•ᚣᚷᛞᚫᚻ•ᚪᛈᛉᚣᚻ•ᛇᛠᚩᛖ•ᛏᛝ
ᛠ•ᛚᛁᛏᚦᚠ•ᛗᚪᚳᛖ•ᛞᚳ•ᛏᚱᛟᚷᛠᚾ
ᚫᛒᚢᛖᛒᚢ•ᚦᚠᛟ•ᚷᛋᛟ•ᛁᛈ•ᛟᛉᛋᛒ•ᚹᛂᛒ
ᚣᛗᚢᛠ•ᚱᛁᚢᛟᛂᛁ•ᛗᛖᚫ•ᚱᛋᛉᛝ•"ᛠᛈᛚ•
ᛞᚩᛚᛁᛉᛠᛝᛖᚱ"•ᚾᛈᛖᚹᛡ•ᚾᛂᛏᚣ•ᛋᚩᛋ
ᛏᛝ•ᚢᚾᛇᚪ•ᛖᛏᚪᛂᚳᚣ•ᛟᛒ•ᛚᛋ•ᛒᛞᛂ•ᛁᛝᚣᛖ
ᚳ•ᛂᚻᛚᚣ•ᚷᚫᛚᛞ•ᛚᚫᛚᚦᛉ•ᛚ•ᛖᛉᚩᛉᛁᚳᚢᛗ
ᚾᚢ•ᚩᚾᛇ•ᚻᛡᛚᛇᚩᚫᚪ•ᚩᛟᚩ•ᚣᚱ•ᛖᚠᚢ•ᛁᚻ•ᛟᛚ
ᚾᛏ•"ᚠᛞᚱᛠᚷ•ᛈᚩᛇᚩᛗᛠᛒ•ᛂᛡ•ᛋᛗᚠ•ᛏ
ᚠᚫᚩ•ᛟᚳᛚᛞᛡᛚ•ᚩᚳᛝᚢ•ᛈᚹᛏ•ᚷᚳᛋ•ᚢᛟᚷᚦ•
ᚠᛉᚠᛏ•ᚳᛋᛉᛟ•ᚷᚠᛉᚾᛞ•ᛒᛏᛠᛡ"•ᛈᛡ
ᛠᛁᚪ•ᛋᚣᛗᛞᚣᛋ•ᛒᛞᛂᛞ•ᚩᚾᛏᛚ•ᚳᚪᛝ•ᚱᚷ
ᚻᚷ•ᛂᚹᚠ•ᚪᚢᛇ•ᛞᛏᛗᛂᛁ•ᛝᚫ•ᛉᛈᚳᛈᛠ•ᛟᚪ
ᛒᛁᛁᛋ•ᛇᚷᚻᛋ•ᛇᛡᛒ•ᚠᚹᛝ•ᚫᚪᚠᚩᚣᛡᚪᚾᚻ•ᛒᚦᛟ
ᛇᚣᛟᛁᛒ•ᛟ•ᚩᛋᚹ•ᛞᚳᚠᚪᛁ•ᛉᛏᛟᚢᚩᛟᚦᛈᛋᚩ•
ᚻᛇᚦᛝ•ᛏᛠᚠᛝᛠ•ᚩᛗ•ᛏᚠᚣᛚᚣ•ᚹᛚᛞ•ᚪᛉ
ᛠ•ᚪᛂ•ᚩᛋᛒᛚ•ᚳᛖᚾᚪᚩᚱᛏᚦ•ᚱᛒᚳᚣ•ᛠᛗᚹᛚ•
ᚻᛈ•ᛇᛈᛖ•ᛚᛂᚩᛡᚪ•ᛖᛋᚫᚩ•ᛠᛉᛝᚣ•ᛖᚫᛒ
ᛗ•ᛖᚻᚱ•ᛈᚾᛗ•ᚹᛏᛟᚣᚢ•ᚠᛉᛈᛗᚩᚷᚾ•ᛡᛇᚳ
ᚠᛒᛈᛗ•ᛋᛇᛁ•ᛖᛈᚢᚱᛏᚳᚣ•ᛂᛚᚠ•ᚱᛚᚱᚫᛖᚻᛟ
•ᛇᚣᛡ•ᚩᛉ•ᚪᛋᚣᛁᛝ•ᛉᛚᛂ'ᚳ•ᛖᚣᚢᛝᚦᛇᚱ•
ᛠᛁᚫ•ᚦᚠᛟᚷᛠᛁ•ᛈᛋᛒ•ᛗᛒᛂᚠᚾᚳᛖ•ᚻᚫᚩᛂ•
ᛉᛂᛚᛈᚪᛁ•ᛟᚹᚱᛁᚱᚦᛖᛉ•ᚪᚾ•ᛞᛂᚷ•ᛟᛟᚳᛏᛂ
ᛞ•ᛉᚾᛗᚦ•ᛁᛂᚱ•ᛈᛉᚢᚫᚦᛒᚠᛂᚦ•ᚠᚪᛝᛖ•ᚹᚹᚣ
ᛚᛇ•ᚢᚣ•ᚾᚱᚪ•ᛈᚾᚹ•ᛚᚾᛏᛚᚢᛒᚱᛝᚪᛋ•ᚫᛈ•ᛂᛚ
ᚢᚳᚷ•ᛚᛏᛂᚹᛈ•ᚫᛗᛚ•ᛉᛚᛗᛏᛞᚠᛈᛁ•"ᚠᚳᚦ
ᛗᛂᚹᚱᚪᛚ•ᚩᛝᚱᚢᛈᚱᛟᛡ•ᚳᛉᚱ•ᛇᛏᚦᚾ•ᚱᛇᚫ
ᛞᛟᚻ•ᛒᚾᚣ•ᚠᛡᚪᛡᛖᚫᛞᛂᚢᛖ•ᚦᚱ•ᚩᛇᚱᛡ•
ᚣᛁᛉᛇᚻᚩᛠ•ᚫᚻᛡᛝᛠᚦ•ᚾᚣ•ᚾᚠᛁᛝ"•"ᛏ
ᚻᚹᚫ•ᛒᛇ•ᛡᚻᛉᛒ•ᛞᛝᚱᛂᚦᚻ•ᚪᚷᚣᛁᚠᚷ•ᛁᛏᛞ
ᛠᛒᚠᚩᛈ•ᛇᛡᛟᚹᚱᚾᚩᛏ•ᛋᚹᚢ•ᛖᛡᛖᛡᚦ•ᛉ
ᚪᚷᛈᚾ•ᛋᚱᚠᛞᛝᚻᛖᛂᛞ•ᛂᛡ•ᚱᚹ•ᚷᛝᚪᛒ•ᛂᛈ
ᛂ•ᛏᚠᛉ•ᚪᛂ•ᛁᚠᛉᚢᚩᚣᚻᚦ•ᚻᚾᛁᛒ•ᛡᛟᛡᛋᛈᚣ
ᛉ•ᛠᚢᛠᛚ•ᚠᛝᛗᚻ•ᚦᛒᚩ•ᛗᛚ•ᚩᛠᛋᚦᛠ•ᛇ
ᛋᛉ•ᚠᛗᛒ•ᚫᛋᛇᚾᛡᚾ•ᚢᚫᚹ•ᛞᛠᚢᚾᛝᚠᚾᛖᚫ
ᚻᛂ•ᛁᛖᛏᛡ•ᚷᛁᚩᚾ•ᚳᚢᚫᛗᛈᛋᚪᛡ•ᚷᛚᚣᚹᛟ"•
ᚠᚢ•ᛉᚠᚫᛞᚠᛡᛂᚾ•ᚻᛋᚦᚠ•ᛏᚠᛂᚱᚹᚠᛋᚾᚹᛂ
ᛖᛒᚢᚦ•ᚩᛇᚫᛈ•ᛡᛟ•ᚢᛁᚩᛂᚩᛇᛟᛂᛞᚩ•ᛈᚹᛞ
ᚷᚱ•ᚠᛟ•ᛇᚷ•ᛂᛟᛇᚫᛋᚫᚣ•ᛒᛏᛞᛟ•ᛠᚻᛡᚱᛠ
ᛠᛉᛋ•ᚠᚾᚣᚱᚠ•ᚪᚾᛡᚪᛖᚫ•ᚳᛇᛁᛝ•ᛒᛡᛞᛠ
ᚫᛒᛠᚳᛉᚠ•ᚫᛏᛁᚱᚪᛗᚩ•ᛚᛉᛋᚪ•ᛒᚩᛈᚫᚩᛝᚻᛇ
ᛖᛇᚫ•ᚻᛖᛇᛠ•ᚱᛗᛞ•ᚫᛇᛗ•ᚾᚾᚣᛡ•ᚱᚾᛗ
ᛠ•ᛂᛉᛋᛂ•ᛟᛖᛒ•ᛏᚻᚾ•ᚠᚪᚠ•ᛒᚾ•ᚩᚾ•ᛖᛋᛏᛒᚹ
ᛡ•ᚻᛏ•ᚩᛟᚩ•ᛒᚾᛖᚳᛁᚹᚣᛟ•ᛟᚩᛒ•ᛋᛖᚩ•ᚫᚻᛟ
ᚠᚫᚷᚩᛂ•ᛟᛒᚻ•ᚳᛖᛁᛚᚫᚣᛚ•ᚢᛚᛁ•ᚾᛟᛏ•ᚫᛈᛟᛈ
ᛝᛗ•ᚳᚢᛁ•ᚣᛋᚳᚢᛡᛇᚩ•ᚠᛖ•ᚷᛟ•ᚻᚫ•ᛝᚠ•ᛗᚠ
ᛝᛉᛞᛁ•ᛗᛝᚣᚪᛝᚠᛉᛁᛟᚷᛚ•ᛇᚩ•ᚫᛡᛏ•ᛂᛏ
ᛠᚢ•ᚷᚦᚣ•ᚦᚾᛟᚣᚩᛖᚻ•ᛁᛋᛖᚣᚦᚪᛡᛝᛟᛇᛚ•
ᛡᛏᛝ•ᛁᛚ•ᚠᛉᛡᛠᛏ•ᚠᚾᛂᚠᚻᚳ•ᚻᛞᛠᚣᛟ
ᛝ•ᛉᛇᚻᚩᛋᚻ•ᛇᛏᚠ•ᛚᚱᛇᚦᚪᛁᛁ•ᛒᚠᛁᛚ•ᛂᛡᛒᚣ
ᛗᚫᚫ•ᛞᚻᛟ•ᚪᚹᛉᛚᛏᛁᚪ•ᛟᛞᛖᚾᛈᚻᚣ•ᚦᛚᛖᛋ
ᛖᛟᚫᛖ•ᛏᚱᚪ•ᛁᚫᚹᚫ•ᛋᛈᚱ•ᛂᛡᚪᛏ•ᚫᚦ•ᚠᛠᚢ
ᛈᚣᚫᛝ•ᚣᚾᚻᛡ•ᚳᛗᚠᚾ•ᛞᛂ•ᛖᚩ•ᛒᚷᚻᚪ•ᛖᛞ
ᛟᚠᛇᛞᛟ•ᛈᚳᛁᚪᛒᚷᛒᛈᛟ•ᛟᛂᚠᚪᛖ•ᛂᚣᚩᛂ•ᚣ
•ᚫᛋ•ᚦᛁᚫᛂᚫᛏ•ᛖᛇᚻᛟ•ᚣᚠᚹᛞᚷ•ᛡᚱᛒᚢ•ᛒᛚ
ᚢ•ᚷᛈᛂᚪ•ᛏᛡ•ᚳᛂᚠᛡᛝᛚᚣᛒ•ᛗᚻ•ᚱᛚᛟᛠᛋ
ᚦᛝ•ᛏᚳᛟᛉᛁ•ᛂᚱᚳᛖᛏᛂᚷ•ᛡᛈᛏᛉᚩᛁᛂᛟ•ᚷ
ᚩᚪᚢ•ᚣᛖᚪᛋᛟᛇᚢᚪᛡ•ᛗᚱᛚᚳᚠ•ᛒᛗᛝ•ᚻᛉ•
ᛠᛂᚫ•ᛉᚪᚷᚻᚣᛏᛖᛝ•ᛉᛉᛗᚾᚫᛋ•ᚱᛗᛞᛋ
ᚳ•ᚦᛚᛟ•ᛝᛇᚢ•ᚻᚩ•ᛏ•ᚢᛁᚦᛂᚾᚠᚱᚦ•ᛋᛟᚷᛠ
ᛗᚪ•ᛝᛚᚪᛁᛒᛠᚢᛋ•ᚩ•ᛖᛋᛝ•ᚠᛡᚢᛟᛞᛇᚪ•ᛞ
ᛡᛒᚹᚩ•ᛂᛋ•ᛟᛝᛏᚳ•ᚻᚾᛇᛋ•ᛗᛚᚻᛞᛖᛈ•ᚫᛂᚱ
ᚪᚢᚻᚱᚦᚱ•ᛟᛂ•ᛟᛗᚩᛟᛏ•ᚫᛇ•ᛉᛒᚳ•ᛂᛁ•ᚪᚩᛉ•
ᚹᚪᚾᛈᛏᚢᚣ•ᛁᛒᚢ•ᚦᚩᛡ•ᛗᚳᚠᛉᚱᛁ•ᚪᛗᛏᛒ•
ᛗᛚᛁᚦᛏᛠᛋᚾᚷᛚ•ᛏ•ᛇᛈ•ᚩᛚᛞ•ᛚᚹᚳᛂᚹᛉ•ᚪ
ᛡᚹᛇ•ᛖᛖᚹ•ᛏᚪ•ᚣᚠᛉᚳ•ᛗᚩᚷᛞᚷ•ᛚᚳ•ᛒᚣᛋ
ᚣᚠᛞᚣᛝ•ᛠᛇᛏᚩᚢᚫ•ᛟᛁᛒ•ᛏᚾᚫᚠ•ᛂᛟᛗᚾ
ᛈ•ᛠᛡᚩᛏᛡᚪᚱᛞ•ᚪᛝᛈᚹᛗᛂᛟᛠᚩ•ᛚᚹᛉ•
ᚱᛗ•ᚩᛏᚹᛂᚹᚾ•ᚷᚳᛠ•ᛂᚳᚢᚱ•ᛟᛇᛟᚾᚻᚫᛉ•
ᚣᛚᚩ•ᚩᛡᚳᚻᛂ•ᛋᚣᚹᛁ•ᚣᚠᛋᚾᚪ•ᚷᛖᚾᛂᚪᚹᛠ•
ᛞᚠᛟ•ᚢᛁ•ᛖᛇᚦ•ᚫᛞ•ᚳᛂ•ᚷᚢᚻᚣᚻᛁᛒᛉᚾ•ᚹᛝ
ᚻᛏᛉᚫᛁᛂᚢ•ᛞᚠᛡᚫ•ᛋᛁᚹᛝᛈ•ᛗᛉᛂᛈ•ᛞᛗ
ᛝ•ᛇᛚᛞᚣ•ᚠᚩᛞ•ᛝᚷᚾᛇ•ᚷᛖ•ᛚᛉᚣ•ᚫᛚᛖᛉ•
ᛡᛝᛋ•ᚳᛁᚦ•ᚷᛏᚣ•ᚹᚩ•ᛝᛖ•ᛒᚪᛗᛏᚪᚷᛒ•ᛈᛡ
ᛟ•ᚪᛉᛝᛒᛞᛉᛂᚦᚢ•ᛏᛇᛖ•ᚣᚪᚳ•ᛠᚦᚹ•ᛏᛉ
ᚩᚳᛞᛒ•ᛟᚩᛠᚾᚠᚪ•ᛚᛗᛖᛁᚦᚫᚪᛡᛂᛁᚪᚱ•ᚦᚱᛖ
ᛖᚣᛋᚾ•ᛖᛏᚢᚻᛈᚳᚦᛋ•ᚳᛇᛉᛖᛇᚠ•ᛞᛠᛏ
ᛈ•ᚣᛇᛠᚢᛏ•ᛉᚦᚷᚻ•ᚫᚾᛠᚱ•ᛡᛒᛏᛁᛉ•ᚩᚢ
ᛝ•ᛚᛒᛇᚩ•ᛟᛉ•ᚦᛞᚷᚠ•ᚩᚱᛈᚪᛏ•ᚫᛋᚪᚦ•ᛖᛟᚪᛝ
ᚫ•ᚣᛒᛚ•ᛡᚦᚾᚠᛈᛟᛡᚾ•ᛖᚹ•ᛖᛗᚩ•ᛉᚹᚦᛠ•ᛁᚦ
ᛒᛖᚱ•ᛟᚳᛉ•ᛈᛖ•ᛁᚢᚦ•ᛈᚠᛞᛈᛂ•ᛁᛟᚻ•ᛒᚦᛏᚩ
ᚳᚢᛚ•ᛞᛂᛝ•ᚦᛂᛁᚪ•ᚹᚣ•ᚢᛝᚾ•ᛋᚾᛈᚠᚫᛒᛂᚫ•ᛡ
ᛗᚹ•ᛇᚪᚩᚾᛂᚳᛚᛒᛉ•ᚣᛠᚦᚹ•ᛝᛚᛗᚳᛡᛇᚠᚫ
ᛠᛁᚦ•ᛒᛠᛚᚦᚳᛞᛁᛇ•ᚠᚢᛉᛋᛉᛁᚦᚫᛋᛗ•ᚦᚹ•
ᛈ•ᛒᛋᛏᚫᚾᚱᛁ•ᚦᛇᛡᚱᛚᛡᚹ•ᚢᚩᛋᚱ•ᚹᚫ•ᛒᚹᛡᛖ
ᛟᛂ•ᛡᚣᛖᚩᛖᛡᚷᚫᚠᚾᚹ•ᛟᛏᚫᚠᛂᚹᛠ•ᚦᛞ•ᛁ
ᚫᚩᚾ•ᛋᚷᛈᚪᛖᚩ•ᚣᚦᚹ•ᚾᚷ•ᛠᛋᚩᛇᛏ•ᛝᛚᚷᛞ
•ᛒᛈᛈ•ᛗᛁᚪᛖ•ᛚᛏᛁ•ᚫᛂᛖ•ᛒᚾᚠᚪᛋᚷᛒᚠ•ᚫᚹᚣᚷ
ᚢᛡᚠᛠ•ᛖᛋᛞ•ᛚᚳᛒᛞᛏᛈ•ᛖᚾᛈᚣ•ᚱᚠᚻ•ᚫ
ᛝ•ᛟᚪᛗ•ᛒ•ᛡᛚ•ᛝᛋᚱᚢᚹᚱᚣᚻᚹ•ᚹᛡᛈ•ᛁᚻᚾᚻᚱ
•ᚳᛖᛏᚫᚩᛋ•ᚣᛋ•ᛝᚫᛡᛝᚫ•ᚻᚦ•ᛇᚪᛞᛋ•ᛒᛁᚳᛈ
•ᛇᛒᛟᚫ•ᛠᛝᛖ•ᛝᛠᚣ•ᛒᚣᛉᚻᚢᚠᚦᛞᚹ•ᛗ
ᚢᛁᛡᛂᚩ•ᛋᛇᚫᛇᛝᚱ•ᛚᛇᛠ•ᛏᚩᛂ•ᚩᛝᛈ•ᚱᚻ
ᛠᚢᛉᚦ•ᚣᚢᛋ•ᛡᛚᛖᚷᛗᛝᚹᚻᚱᛋ•ᚢᛟᚣᛠ
ᚷᚩᚷ•ᛇᛁᛖ•ᛠᛂᛇᛁᚾᛂᚩᛗᚱᛡᛉ•ᚠᚻᚳ•ᚪᚩᚪᚫ
ᚻᚳᛁᚦ•ᛂᚷ•ᛝᛖᚢ•ᛡᛏᛁ•ᛚᚩᚱᛈ•ᚠᚪ•ᛈᛞᚱᛒ•
ᛝᛁᛋ•ᚷ•ᚠᚾᛈᚠᛒ•ᛟᚦᛁᛠᚪ•ᛡᛏᚾᚳ•ᚦᛟᚻᛈᛖᛚ
ᚫ•ᛟᚠᛗ•ᛡᛝ•ᛒᛝᚦᛝᛠᚠ•ᛇᛗᛟ•ᚩᛠᛈ•ᛁᛡᚱ
•ᚹᚹᛟᚩᛒᚩ•ᚾᚩᛂᛟᚾ•ᚦᛡᚠ•ᚩᛂᛞᚦᛏᛁ•ᛈᚾᚪᚱᛂ•
ᛉᚱᚣ•ᛝᛡ•ᛏᛗ•ᛈᛞᚣᚻ•ᛗᛝᚫᚳᛇ•ᛡᚣᛂᛟ
•ᛝᚩᚢᛇᛁᚱ•ᛏᚪ•ᚩᚻᚪᛚᚫᛚᚪ•ᛋᛈ•ᛏᚪᛂᚳᚦᚢᛏᚹ
ᚦ•ᛗᚷᛖᛗᚣᛡᛁᛞ•ᚢᛋᚠᛒ•ᛟᛚᛟ•ᚪᛒ•ᚦᛚᚣ•ᚳ
ᛠᚣ•ᛞᛇᛁ•ᚹᛉ•ᛟᛝᛒᚢᛋᛞᚻᛞ•ᚢ•ᛠᚱ•ᚫᚩ
ᚻᛝᛒᚪᚹ•ᛈᛡᚾᛚᛇ•ᛖᛟᛝ•ᛡᚠᛇᛡ•ᚳᚦᚹ•ᛚᚦᚪᛁ
ᛈ•ᛞᛟᛂ•ᚢᛉᚢᚾᛠᚠ•ᚩᚾᚪ•ᚱᛠᚷ•ᛗᚢ•ᛗᛁᛂ
ᛒᛗᚱᚾᛗ•ᚩᚾᚠᚣ•ᛗᚠᛇᚠᛂ•ᛒᛡᛈᛂᛖᛡᛏ•ᛈᛟ
ᚫᛏᛟ•ᚻᛖᚾ•ᚳᛇᚩ•ᛋᚻᚫᛇ•ᛝᛁᛟ•ᛇᚠᚢᛞᚣᚪᛚᚠ
ᛡ•ᛖᛂ•ᚠᛚᛟ•ᛁᚳ•ᛁᛝᚷᚦ•ᛗᛋᚫᚷᚪᛠ•ᛗᛁ•ᛒᛡᛏ
ᚾ•ᛝᛗᚦ•ᛏᚣᚫᛂ•ᛖᚻᚠᚪᛡᚷ•ᚪᛗᛁ•ᛞᛉᛏ•ᚢᛖ
ᚦᚾ•ᛖᚪᛈᚹᛠᛚ•ᛒᚢᚱᛡᛟ•ᚪᚣ•ᛟᛇᚹᛂᛈᛞ•
ᚹᚹᛈ•ᚠᛡᛚᛉᛒᚾ•ᚳᛗᚾᚱᛗ•ᚻᚦᚫᛞᛂ•ᛒᛡᚫ•ᛇᚹ
ᛗᚢ•ᚪᛈᛡ•ᛈᛁᛂ•ᚪᚢᚾᛠᛖᛞᛗᚪ•ᛏᛟᛗ•ᛋᛞ
ᛝᚷᛚᛋᛞᛝ•ᛟ•ᛋᛂᛞ•ᛚᛟᚠᛂᚫᚠᚪ•ᛝᛟᚣᛈ•ᚣᚩ
ᛒᚷᚳᛖᛏᚹ•ᚪᛋᛒ•ᛗᛠᚣᛇᛗᚫᛚᚱ•ᚹᛇᛂᛒ•ᛈᛚᚠ
ᛈ•ᚠᛗ•ᛝᚪᛇᚾᛟᚹᛇᛉ•ᚣᚫᛉᛞᛟᚱᛒ•ᛡᚱᛟ•ᚹᛏ
ᚷᚱᛂᛖ•ᛠ•ᛈᛚᛞ•ᚻᚦᚱ•ᚦᚣᛚᛉ•ᛠᛈᚫᚠᚪ•ᚫᚪ
ᛒ•ᛈᛋ•ᛗ•ᛏᚫᚳᛈᛝᚹᚦ•ᚻᛠ•ᛞᚩᛂᚷ•ᛋᚩᛠᚳ
ᛖᛋ•ᚣᛖᚫ•ᛈᚦ•ᛁᛇᛈᚳᛝ•ᛈᚳᛇᚢᛏᚳᛡᛇᛝᚾ
ᚢᚻᚦ•ᚣᚠᛗᚾ•ᛝᚠᛂᛉᛟᚱᛗ•ᛝᛠᛂᛏᚳ•ᚢᚷ
ᚦ•ᚠᚦᛋ•ᚪᛈᚩᚪᚫᛞᛋᛝ•ᛒᛗᚩᚷ•ᚹᚠᛗᛖ•ᛠᛇᚻᚠ
ᚻᚳᚱᚫ•ᛝᛗᛉᚳ•ᛋᚪᚹᛋᛠ•ᚩᚣᛚᛉᛝ•ᛠᛟᛉ
ᛟᛠᛡᛝᛒ•ᛝᚳᚫᛁᚱ•ᛒᚠ•ᛏᚣᚣ•ᛠᛒ•ᚣᛚᚩ•ᛇ
ᛉ•ᚩᚷᛗᚩ•ᚠᛚᛟᛝᚦᛠ•ᚦᚣᛖᚣ•ᚾᚷᚾ•ᛡᛏ•ᛂ
ᛟᚾᛁ•ᛋᛟ•ᛠᚦᚣ•ᛋᛒ•ᚫᛚᚪᛂᛡᛖᚷᛉᛡᚾᛉᛏ•
ᛡᛒᚻᛚᚷ•ᚢᚦᛠ•ᚢᚾᛁᚩᛗᛠᛁᚷ•ᛟᚦᚱᚣ•ᛒᛖ
ᛠᚩᛈ•ᛗᛏᚱᚫᚢᚻᛁᛝ•ᛇᚳᚠ•ᛂᚾᚱᚷ•ᛟᚷᚻᚣᚻ
ᛇᚫᛠᚫᚣ•ᚢᛗᛈ•ᛉᛁᚢᚾᚩᛟᚾ•ᚷᛞᚦ•ᛡᚫᚹ•ᛞ
ᛟᛖᚱ•ᛗᚾᛖᚻᚷᛒᚢᛂ•ᚢᚦᛗᛖᛞᛝ•ᛒᚷᚣᚱ•ᛖ
ᛁᚢᛂ•ᚣᛡᛚᚢ•ᛂᛟ•"ᛠᛉᚣᛇᚱ•ᚩᛈᛋᚳᚫᛗ
ᛇ•ᚾᛂ•ᛖᚠᛋ•ᛖᚠᚪᛝ•ᚢᛝᛂᛇᚷᚠᛝᚱᛁᚦ•ᛂᚢᚫ•
ᚣᛋᚠᛖᚢᛋᚫᚣᛠ•ᛁᛏᛟᚱᛏᛟᚩ•ᚷᚾᚻ•ᛞᛗᚩᚳ
ᛞᛖᛏ•ᚹᛉᛞᛚ•ᚩᚫᛂ•ᛇᚢᛒ"•ᛗᛏ•ᛞᛗᛖ•ᛏ
ᛈᚹᛇᛋ•ᚹᛒᛇᚦ•ᚾᚻᚷᛂ•ᚱᛡᛞᛡᚦᚪᛁᛇᚫᛉᛚ•ᛇ
ᛠ•ᛡᚪᛂ•ᚻᚱ•ᚦᛈᛞᛂᛝᚩ•ᚷᚠᛇᛗᚳ•ᚻᛞᚩᛏᚳ
•ᚢᚱ•ᛈᚾ•
ᚪ•ᛗᛝᛞᛡᚦᛉᛁᛗ•ᛡᛞᛈᛝᚢᚹᚪᛗ•ᛏᚪ
ᛝ•ᛝᚦᛡᚹᛋᚻ•ᛁᚳ•ᚫᛈᚫᚷᚩ•ᛗᛁᚪ•ᛖᚩ•ᛏᚹ
ᚩ•ᚠᚣᚢᛏᛂ•ᚦᛂᛠᛖᚳᚾᛠ•ᚳᛠᛖ•ᚱ
ᚩᚢᛉ•ᛞᚹᚻᛒᛝᚠᚪᚳᛂᚢ•ᚩᛂᛡᛠᛁᛚᚷᚻ•ᛒᚢ
ᛂ•ᛉᚪᚳᚹᛡ•ᛗᚩᛈᚣᛞᛡᛚᛈ•ᛇᛁᚦᚱ•ᚣᚷᛗ•ᛉ
ᛟᚷᛋ•ᛗᛈᛂᛟᛞ•ᛟᛏᛡᛟ•ᛏᛝᛁ•ᛗᛝᚣᚪᚫ•ᛝ•ᚱ
ᚣᛂ•ᚾᛚᚢᛉᛒ•ᚻᛈᛂᚩᛠ•ᚷᚫᚹ•ᛉᛋᛞᚳ•ᚢᛏ•
ᛟᚻᛇᚾᛈᛏ•ᛠᚣᛒᚢᚷ•ᚷᚪᛇ•ᚾᚷᚩᛖᛚᛗᛒᚦ•ᚣ
ᛡᛟᛇᚣ•ᛗᚳᛟᚦ•ᛖᛚᚱᛇᛈᚱᛞᚣ•ᛉᛞ•ᛝᚣᛈ•
ᛋᛖᛉᚹ•ᚳᚷᚠᛞᚱᛖ•ᛞᛖᚹᚩᛇᛟ•ᚻᚩᛟ•ᛒᛋ•ᚻ
ᛠᚪᚳᛁᛗᛉᛂᛗᛖ•ᛗᛚ•ᚷᚩᛏᚦᛉᛖᛠᚱᚷᚣ
ᛝ•ᚫᛗᛁᚹ•ᛋᛒ•ᛉᛗ•ᛋᛇᚷᛞᚦᚫ•ᚠᛡᚪᛒᚳᚢ•ᚹᚱ•ᛒ
ᛠᚠᛉᛁᛗᚢᚳᛈᚻᛝᛚᛇ•ᛗᛋᛞᛡᛈᚠ•ᛒᚻᛇᚳ•
ᛇᛖ•ᛠᛖᛁᚷᛉᚷᛋ•ᛖᛋᛇᚦᚦᛖᛋ•ᚦᛟ•ᚳᛠᛁᛗ
ᚳᛉ•ᛞᛂᚢ•ᛒᛖᛁ•
ᚫᛂ•ᛟᛋᚱ•ᛗᚣᛚᚩᚻ•ᚩᚫ•ᚳᚦᚷᚹ•ᚹᛚᚫ•ᛚ
ᚩᚪᛈ•ᛗᛞᛞᚢᚷᚹ•ᛚ•ᛞᚾᚣᛂ•ᚳᚠᛡ•ᚫᛏ
ᛈᛇᚪᚦ•ᚳᚫ
ᚳᛞ•ᚠᚾ•ᛡᛖ•ᚠᚾᚳᛝ•ᚱᚠ•ᚫᛁᚱᛞᛖ•ᛋᚣᛂᛠᚢ
ᛝᚹ•ᛉᚩ•ᛗᛠᚹᚠ•ᚱᚷᛡ•ᛝᚱᛒ•ᚫᚾᚢᛋ•
ᛈᚪᚱᚪᛒᛚᛖ• ᛚᛁᚳᛖ•ᚦᛖ•ᛁᚾᛋᛏᚪᚱ•ᛏ
ᚢᚾᚾᛖᛚᛝ•ᛏᚩ•ᚦᛖ•ᛋᚢᚱᚠᚪᚳᛖ•
ᚹᛖ•ᛗᚢᛋᛏ•ᛋᚻᛖᛞ•ᚩᚢᚱ•ᚩᚹᚾ•ᚳ
ᛁᚱᚳᚢᛗᚠᛖᚱᛖᚾᚳᛖᛋ• ᚠᛁᚾᛞ•ᚦ
ᛖ•ᛞᛁᚢᛁᚾᛁᛏᚣ•ᚹᛁᚦᛁᚾ•ᚪᚾᛞ•ᛖᛗᛖᚱᚷᛖ•""".split('\n\n')

# forge_offset() makes a list of offsets to be *subtracted* to the corresponding rune when shifting
# i.e. If your offset list is [3, 4, 28, 4, 6, 9] you'll shift the first offset by 3, the second by 4, etc
# It takes three arguments: A base list, a 'direction' and another offset
#
# Base list: What your basic offset looks like, say a list of primes as in the example below
# Direction: Either -1 or 1, this is will be multiplied to the final number so you can add or subtract offsets
# Offset: Offset every number in your list by this
#
# This is because, for page 56, the offsets are a list of prime numbers
# To that list you subtract 1 from every value
# And multiply it by negative 1, or just *add* the offsets from your runes
#
# Special note: Instead of a list, you can supply a piece of alphabetical text to the function
# We work out what number of the alphabet it is and return a list based on that instead
#
# If it doesn't make sense your best shot is to either read the code or just go with it
# The first instance of 'offsets' below will work on page 56
# The second instance works on page 57, and also any runes that are in plaintext

offsets = forge_offsets([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987], 1, -3301)
#offsets = forge_offsets("ULTIMATETRUTHISTHEULTIMATEILLUSION", 1, 0)

# The stuff below is a little more confusing
# We pull each page from the book, and each rune from the page
# If it's a •, add a space to the output
# If it's a rune (i.e. searching for it returns true), then we find the corresponding letter after applying the offset
# If it's not a rune (• or anything else), then we also maintain our subtract value
#
# Just trust me this works

off_num = 0

for page_num in range(len(liber_primus)):

  text = liber_primus[page_num]

  output = ""

  for rune_num in range(len(text)):
    rune = text[rune_num]
    offset = offsets[off_num % len(offsets)]

    if rune == "•":
      output+=" "
    elif type(find_position(rune)) is int:
      off_num += 1
      output+=table[(find_position(rune) - offset) % len(table)][1]

  # We then print the output of our stuff
  # All the frequency() function does is return frequencies in numbers
  # So here we format it to look a little nicer

  freq = frequency(output)

  print(output + "\n\n")

  for entry in freq:
    print(entry + ": " + str(round(freq[entry] / len(output) * 100, 4)))