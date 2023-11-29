import wikipedia

topic_of_interest = input("Enter a topic you want to see a Wikipedia summary for: ")

try: 
    result = wikipedia.page(topic_of_interest)
    print(result.summary)
except ValueError:
    print("Not a title of a page")