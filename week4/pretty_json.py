# Now that you have examined the structure of a returned JSON object, it is time to put that knowledge to use! Here is your task:
# Iterate over the list of dictionaries you receive from the API, and extract all the adjectives returned to you. 
# (See Python For LoopsLinks to an external site. for additional help.) 
# Compose a sentence where you combine the word you submitted, together with the adjectives returned by the API, 
# into one sentence. Each adjective should be separated by a comma.


data = [
  {
    "word": "northern",
    "score": 1001
  },
  {
    "word": "southern",
    "score": 1000
  },
  {
    "word": "eastern",
    "score": 999
  },
  {
    "word": "western",
    "score": 998
  },
  {
    "word": "southeastern",
    "score": 997
  },
  {
    "word": "modern",
    "score": 996
  },
  {
    "word": "southwestern",
    "score": 995
  },
  {
    "word": "central",
    "score": 994
  },
  {
    "word": "colonial",
    "score": 993
  },
  {
    "word": "independent",
    "score": 992
  },
  {
    "word": "contemporary",
    "score": 991
  },
  {
    "word": "day",
    "score": 990
  },
  {
    "word": "rural",
    "score": 989
  },
  {
    "word": "united",
    "score": 988
  },
  {
    "word": "northeastern",
    "score": 987
  },
  {
    "word": "east",
    "score": 986
  },
  {
    "word": "west",
    "score": 985
  },
  {
    "word": "former",
    "score": 984
  },
  {
    "word": "southwest",
    "score": 983
  },
  {
    "word": "southeast",
    "score": 982
  },
  {
    "word": "south",
    "score": 981
  },
  {
    "word": "urban",
    "score": 980
  },
  {
    "word": "federal",
    "score": 979
  },
  {
    "word": "rich",
    "score": 978
  },
  {
    "word": "northwestern",
    "score": 977
  },
  {
    "word": "native",
    "score": 976
  },
  {
    "word": "postcolonial",
    "score": 975
  },
  {
    "word": "precolonial",
    "score": 974
  },
  {
    "word": "today",
    "score": 973
  },
  {
    "word": "democratic",
    "score": 972
  },
  {
    "word": "niger",
    "score": 971
  },
  {
    "word": "war",
    "score": 970
  },
  {
    "word": "unified",
    "score": 969
  },
  {
    "word": "north",
    "score": 968
  },
  {
    "word": "cameroon",
    "score": 967
  },
  {
    "word": "century",
    "score": 966
  },
  {
    "word": "neighbouring",
    "score": 965
  },
  {
    "word": "coastal",
    "score": 964
  },
  {
    "word": "biafra",
    "score": 963
  },
  {
    "word": "ibadan",
    "score": 962
  },
  {
    "word": "all",
    "score": 961
  },
  {
    "word": "northwest",
    "score": 960
  },
  {
    "word": "dahomey",
    "score": 959
  },
  {
    "word": "made",
    "score": 958
  },
  {
    "word": "postwar",
    "score": 957
  },
  {
    "word": "presentday",
    "score": 956
  },
  {
    "word": "benin",
    "score": 955
  },
  {
    "word": "modem",
    "score": 954
  },
  {
    "word": "midwestern",
    "score": 953
  },
  {
    "word": "defunct",
    "score": 952
  },
  {
    "word": "muslim",
    "score": 951
  },
  {
    "word": "neighboring",
    "score": 950
  },
  {
    "word": "live",
    "score": 949
  },
  {
    "word": "nearby",
    "score": 948
  },
  {
    "word": "ghana",
    "score": 947
  },
  {
    "word": "nord",
    "score": 946
  },
  {
    "word": "lagos",
    "score": 945
  },
  {
    "word": "populous",
    "score": 944
  },
  {
    "word": "speaking",
    "score": 943
  },
  {
    "word": "torn",
    "score": 942
  },
  {
    "word": "anglo",
    "score": 941
  },
  {
    "word": "20th",
    "score": 940
  },
  {
    "word": "steyr",
    "score": 939
  }
]

adjectives = ", ".join([i['word'] for i in data]) # get the all the adjectives returned to me

print("Adjectives for the word Nigeria: " + adjectives) # prints the message
print() # prints a blank line
print("Learning how to access APIs and process the JSON returned is a valuable skill!") # prints final message

