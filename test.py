
import math, time
from collections import Counter, defaultdict

# Start measuring time
start_time = time.time()

def read_data():
    data = open('/Users/mmms/Developer/war_peace_processed.txt', 'rt').read()
    return data.split('\n')

def find_word_in_chapters(target_word, text_list):
   
 
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

def count_target_word_in_chapter(target_word, target_chapter, text_list):
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
  df = find_word_in_chapters(target_word, text_list)
  idf = 1 / df
  tf = count_target_word_in_chapter(target_word, target_chapter, text_list)
  target_tfidf = math.log(1+tf) * math.log(idf)
  return target_tfidf

def tfidf_chapter(target_chapter, text_list):
  #grabbing the data
  #from list to string
  combined_text = ' '.join(text_list)
  #splitting text to chapters
  chapters = combined_text.split('[new chapter]')
  #taking target chapter from chapters
  chapters_words = chapters[target_chapter].split()
  #creating dictionary for 
  word_values = {}
  #calculating tfidf for every word in chapter and storing them as wor:value pair
  for word in chapters_words:
    df = find_word_in_chapters(word, text_list)
    idf = 1 / df
    word_count = chapters_words.count(word)
    tf = word_count/len(chapters_words)
    word_values[word] = math.log(1+tf) * math.log(idf)


  sorted_dict = sorted(word_values.items(), key=lambda item: item[1], reverse=True)
  final_list = []
  count = 0
  


          

  return ' '.join(str(item[0]) for item in sorted_dict[:3])




text_list = read_data()
print(tfidf_chapter(4, text_list))
#print(tfidf("тетушку", 4))
# End measuring time
end_time = time.time()

# Calculate and print the runtime
runtime = end_time - start_time
print(f"Script runtime: {runtime:.2f} seconds")


def read_data():
    # Read the data only once
    with open('/Users/mmms/Developer/war_peace_processed.txt', 'rt') as f:
        data = f.read()
    return data.split('\n')

def process_text():
    # Split the text into chapters and precompute document frequencies (DF)
    text_list = read_data()
    chapters = []
    current_chapter = []
    word_in_chapters = defaultdict(set)  # Tracks in which chapters a word appears
    
    for line in text_list:
        if line.strip() == "[new chapter]":
            if current_chapter:
                chapters.append(current_chapter)
                current_chapter = []
        else:
            current_chapter.append(line)
    if current_chapter:
        chapters.append(current_chapter)

    # Calculate word frequencies in each chapter
    chapter_word_counts = []
    for idx, chapter in enumerate(chapters):
        chapter_text = ' '.join(chapter).lower().split()
        word_count = Counter(chapter_text)
        chapter_word_counts.append(word_count)
        for word in word_count:
            word_in_chapters[word].add(idx)
    # Precompute document frequency (DF) for all words
    df = {word: len(chapter_indices) for word, chapter_indices in word_in_chapters.items()}
    
    return chapters, chapter_word_counts, df

def find_word_in_chapters(df, word):
    # Simply retrieve the precomputed document frequency
    return df.get(word.lower(), 0)

def tfidf_chapter(target_chapter):
    # Preprocess the text and compute DF for all words once
    chapters, chapter_word_counts, df = process_text()

    if target_chapter < 0 or target_chapter >= len(chapters):
        return "Invalid chapter number"
    
    # Get the words and their counts for the target chapter
    chapter_word_count = chapter_word_counts[target_chapter]
    total_words = sum(chapter_word_count.values())
    
    word_values = {}
    
    # Calculate TF-IDF for each word in the chapter
    for word, count in chapter_word_count.items():
        df_value = find_word_in_chapters(df, word)
        if df_value > 0:
            idf = math.log((1 + len(chapters)) / (1 + df_value)) + 1  # Smoothed IDF
            tf = count / total_words
            word_values[word] = tf * idf

    # Sort by TF-IDF values and return top 3 words
    sorted_dict = sorted(word_values.items(), key=lambda item: item[1], reverse=True)
    return ' '.join(item[0] for item in sorted_dict[:3])

# Example usage:
