from tkinter import *
from main import analyse_tweet

# GUI begin
home = Tk()
home.title("Twitter Sentiment Analyser")
#Heading 
head = Label(home, text = "Twitter Sentiment Analyzer")
head.pack(padx=10, pady=5)

#Input Frame for required args
args = Frame(home)
args.pack(padx=10, pady=10, fill=X)

#Input Field
Label(args, text="Enter the term/hashtag: ").grid(row=0, column=0)
tweet_terms = Entry(args, font=('MS Sans',13))
tweet_terms.grid(row=0, column=1)

Label(args, text="Enter number of tweets: ").grid(row=1, column=0)
tweet_count = Entry(args, font=('MS Sans',13))
tweet_count.grid(row=1, column=1)
args.grid_columnconfigure(0, weight=1)

analyse = Button(home, text = "Analyse" , command=analyse_tweet)
analyse.pack(pady=5)

#Result frame
result = Label(home, text="")
result.pack(fill=X, padx=10, pady=10)

home.mainloop()