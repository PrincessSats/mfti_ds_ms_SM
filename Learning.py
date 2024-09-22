import math, os
def read_data():
    data = open('/Users/mmms/Developer/war_peace_processed.txt', 'rt').read()
    return data.split('\n')

def find_word_in_chapters(target_word):
   
    text_list = read_data()
    chapters_with_word = 0
    total_chapters = 0
    current_chapter = []
    
    # Iterate over each line in the text
    for line in text_list:
        # Check for chapter delimiter
        if line.strip() == "[new chapter]":
            if current_chapter:  # If there is a previous chapter
                total_chapters += 1
                # Convert chapter to a single string and check for word occurrence
                chapter_text = ' '.join(current_chapter).lower()
                if target_word.lower() in chapter_text.split():
                    chapters_with_word += 1
                # Reset the current chapter
                current_chapter = []
        else:
            # Add lines to the current chapter
            current_chapter.append(line)

    # Handle the last chapter if not followed by "[new chapter]"
    if current_chapter:
        total_chapters += 1
        chapter_text = ' '.join(current_chapter).lower()
        if target_word.lower() in chapter_text.split():
            chapters_with_word += 1

    # Calculate document frequency
    df = chapters_with_word / total_chapters if total_chapters > 0 else 0
    return df

def count_target_word_in_chapter(target_chapter, target_word):
    text_list = read_data()
    combined_text = ' '.join(text_list)

    
    chapters = combined_text.split('[new chapter]')
    
   
    if target_chapter < 0 or target_chapter >= len(chapters):
        return "Invalid chapter number"

   
    chapter_text = chapters[target_chapter]
    

    # Split chapter text into words
    words = chapter_text.split()
    
    # Count occurrences of the target word
    word_count = words.count(target_word)
    tf = word_count/len(words)
    return tf

def tfidf(target_word, target_chapter):
  text_split = read_data()
  df = find_word_in_chapters(target_word)
  idf = 1 / df
  tf = count_target_word_in_chapter(target_chapter, target_word)
  target_tfidf = math.log(1+tf) * math.log(idf)
  return target_tfidf

def tfidf_chapter(target_chapter):
  #grabbing the data
  text_list = read_data()
  #from list to string
  combined_text = ' '.join(text_list)
  #splitting text to chapters
  chapters = combined_text.split('[new chapter]')
  #taking target chapter from chapters
  chapters_words = chapters[target_chapter - 1].split()
  #creating dictionary for 
  word_values = {}
  #calculating tfidf for every word in chapter and storing them as wor:value pair
  for word in chapters_words:
    word_values[word] = tfidf(word, target_chapter)
    #print("Now analyzing:", word, 'result:', word_values[word])

  sorted_dict = sorted(word_values.items(), key=lambda item: item[1], reverse=True)

  first_three_keys = list(sorted_dict.keys())[:3]
  if first_three_keys:
    print(' '.join(first_three_keys))
  else:
    print("Dictionary has fewer than three keys.")


  capters_top_words = []

  chapter_text = chapters[target_chapter]

print(tfidf_chapter(4))