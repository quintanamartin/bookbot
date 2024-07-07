
def main():
  book_path = "books/frankenstein.rtf"
  text = open_book(book_path)
  words = word_count(text)
  chars = count_characters(text)
  chars_sorted_list = chars_dict_to_sorted(chars)
  report = create_report(chars_sorted_list)

def open_book(book_path):
  with open(book_path) as f:
    return f.read()

def word_count(content):
  return content.split()

def count_characters(text):
  removed_uppercase = text.lower()
  character_appears = {}
  for word in removed_uppercase:
    if word in character_appears:
      character_appears[word] += 1
    else:
      character_appears[word] = 1
  return character_appears

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted(dict):
  sorted_list = []
  for char in dict:
    sorted_list.append({"char": char, "num": dict[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

def create_report(sorted_list):
  for item in sorted_list:
    if not item["char"].isalpha():
        continue
    print(f"The '{item['char']}' character was found {item['num']} times")

main()
