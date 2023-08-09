
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import math
import glob


postings = {}
docfreq = {}
total_doc_word = {}
docLength = {}


def documnetID_path():
    """
    saves a dictionary with docID and doc path in docID_path variable ---> {0 : "documents\\1.txt" , 1 : "documents\\2.txt"}
    """
    global docID_path

    #doc_path variable is a list of document paths
    doc_path = glob.glob("./doc/*.txt")


    docID_path= dict(zip(range(len(doc_path)), doc_path))




def initializing_term_and_postings():

    #read file
    for id in docID_path:
        with open(docID_path[id], "r") as f:
            document = f.read()

        document = tokenization(document, id)
    print(document)




def tokenization(text, docID):
    """
    tokenize text
    :param text: string
    :param docID: int
    :return: save inverted index as dictionary in postings variable
    example : postings = {"token_1" : {docID : term frequency} , "token_2" : {docID : term frequency}
    """


    # tokenize words
    text_tokens = word_tokenize(text)
    # print(text_tokens)

    # delete stop words
    text_tokens = [word for word in text_tokens if not word in stopwords.words('english')]
    # print(text_tokens)

    # delete puctuations example --> "" . : , ! @ # $ ?
    text_tokens = [word for word in text_tokens if word.isalnum()]
    # print(text_tokens)

    # make tokens lowercase
    text_tokens = [word.lower() for word in text_tokens]

    # we make list of text_tokens to use .count method to calculate term frequency
    text_tokens_list = text_tokens


    # remove duplicate tokens and save unique terms as set datatype
    unique_text_tokens = set(text_tokens)


    #save number of total words for each document in total_doc_word dictionary that we wil use in calculating Tf(Term frequency) formula
    total_doc_word[docID] = len(unique_text_tokens)

    for term in unique_text_tokens:
        if term in postings:

            """
            Before
            postings = {"token_1" : {docID : term frequency} , "token_2" : {docID : term frequency}
            example : term = first , docID = 1
            posting = {"first" , {0 : 1} }
            
            """
            # merge two dict with | symbol
            postings[term] = postings[term] | {docID:text_tokens_list.count(term)}

            """
            After

              posting = {"first" , {0 : 1 , 1 : 3} }
            """
        else:
            # add   { "token" , {docID : term frequency}}   to postings dictionary
            postings[term] = {docID:text_tokens_list.count(term)}


    return postings



def normal_term_frequency(term , id) :
    """
    normal tf formula = term frequency of word in doc / total word numbers in same doc

    postings = { "token_1" : {docID : term frequency} }
    postings = { "first" : {0 : 1}}

    total_doc_word = {docID : total word numbers}
    total_doc_word = {0 : 8}

    tf for term first = 1 / 8 = 0.125

    :param term: example --> "first"
    :param id: doument id
    :return: normal_term_frequency
    """
    if id in postings[term]:

        return postings[term][id]/total_doc_word[id]
    else:
        return 0.0


def normal_inverse_document_frequency(term , id):
    """
    normal idf formula = 1 + log (total number of documents /  number of documents which the word is mentioned)

    docID_path = {0 : "documents\\1.txt" , 1 : "documents\\2.txt"}
    total number of documents = len(docID_path) = 2


    postings = { "token_1" : {docID : term frequency} }
    postings = { "first" : {0 : 1}}
    number of documents which the word is mentioned = len(postings[term])
    number of doucuments which the word is mentioned in this example is = len(postings["first"]) = 1

    idf for term first = 1 + log ( 2 / 1) = 2.0

    :param term: example --> "first"
    :param id: doument id
    :return: normal_inverse_document_frequency
    """
    if id in postings[term]:
        return 1 + math.log( len(docID_path) / len(postings[term]), 2)
    else:
        return 0.0


def doc_lengths():
    """
    Computes the length for each document

    doc = sqrt(tf1 ** 2 + tf2 ** 2 + ...)
    """
    global docLength
    for id in docID_path:
        l = 0
        for term in postings:
            l += normal_term_frequency(term, id) ** 2
        docLength[id] = math.sqrt(l)

    print(docLength)



def cos_similarity(query , docID):
    """Returns the cosine similarity between query and document id.


       :param query: list of tokens in query
       :param id: document ID
       :returns: similarity of document with query
       """
    similarity = 0.0

    for term in query:

        if term in postings:
            # For every term in query which is also in vocabulary,
            # calculate tf-idf score of the term and add to similarity
            similarity += normal_term_frequency(term, docID) * normal_inverse_document_frequency(term, docID)

    similarity = similarity / docLength[docID]

    return similarity



def query():
    """
    Asks the user what they would like to search for, and returns a
    list of relevant documents, in decreasing order of cosine similarity

    :return:
    """
    query = input("Search query >> ")

    # Exit if query is empty
    if query == []:
        sys.exit()

    # tokenize words
    query = word_tokenize(query)
    # print(text_tokens)

    # delete stop words
    query = [word for word in query if not word in stopwords.words('english')]
    # print(text_tokens)

    # delete puctuations example --> "" . : , ! @ # $ ?
    query = [word for word in query if word.isalnum()]
    # print(text_tokens)

    # make tokens lowercase
    query = [word.lower() for word in query]

    scores = sorted(
        [(id, cos_similarity(query, id)) for id in range(len(docID_path))],
        key=lambda x: x[1],
        reverse=True,
    )
    print(scores)
    return scores


def print_result(scores):
    """Prints scores in a tabular format with two columns like
    | Score | Document |
    --------------------
    | 0.523 | foo      |
    --------------------

    :param scores: list of (id, score)
    """
    print("-" * 42)
    print("| {} | {} |".format("Score", "Document"))
    print("-" * 42)

    for (id, score) in scores:
        if score != 0.0:
            print("| {} | {} |".format(str(score)[:5], docID_path[id]))

    print("-" * 42, end="\n\n")



documnetID_path()
initializing_term_and_postings()
doc_lengths()
result = query()
print_result(result)
