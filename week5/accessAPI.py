import sys

import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

print("Welcome to the Book of Mormon Summary Tool!")

user_response = True  # set the initial response to True


def check_requested_book():
    """function to check if the requested book is available
    """
    book_check_response = requests.get(base_url)
    b_check = book_check_response.json()
    list_of_books = [_id['_id'] for _id in b_check['books']]
    if book_request.replace(" ", "").lower() not in list_of_books:
        sys.exit(1)


def check_requested_chapter():
    """
    function to check requested chapter exists
    """
    chapter_check = requests.get(base_url + book_request.replace(" ", ""))
    c_check = chapter_check.json()
    list_of_chapters = [_id['_id'][len(book_request.replace(" ", "").lower()):] for _id in c_check['chapters']]
    if chapter_request not in list_of_chapters:
        print(
            f"That chapter doesn't exist, please enter a number between {list_of_chapters[0]} and {list_of_chapters[-1]}")
        sys.exit(1)


while user_response:  # Check user response state

    chapter_num = ""
    book_name = ""

    book_request = input("Which book of the Book of Mormon would you like? ")  # ask user for book name

    # check if request book exists
    check_requested_book()

    is_name_the_same = book_request == book_request.replace(" ",
                                                            "")  # check to see if book name is composed of two parts

    if not is_name_the_same:  # handles Book of Mormon names with numbers e.g. 1 Nephi
        split_it = book_request.split(" ")  # split the name using the included spaces
        chapter_num = split_it[0]
        book_name = split_it[1]

    chapter_request = input(
        f"Which chapter of {chapter_num + ' ' + book_name.capitalize() if not is_name_the_same else book_request.capitalize()} are you interested in? ")  # ask user for chapter

    # check if requested chapter exists
    check_requested_chapter()

    response = requests.get(
        base_url + book_request.replace(" ", "") + '/' + chapter_request)  # Use the url string to ask for the content
    data = response.json()  # We want the data returned as json

    print(
        f"Summary of {chapter_num + ' ' + book_name.capitalize() if not is_name_the_same else book_request.capitalize()} chapter {chapter_request}:")

    print('--' + data['chapter']['summary'], "\n")

    answer = input("Would you like to view another (Y/N)? ")
    if answer.upper() == "N":  # ask user if they want to continue
        user_response = False

print("Thank you for using Book of Mormon Summary Tool!")
