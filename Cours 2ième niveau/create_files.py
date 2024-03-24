import os
from datetime import datetime

def create_markdown_file(today_date, page_number):
    # Create the markdown links
    previous_page_link = f"[page pr\u00e9c\u00e9dente]({today_date}-{page_number-1:02}.md)" if page_number > 1 else ""
    next_page_link = f"[page suivante]({today_date}-{page_number+1:02}.md)" if page_number < 17 else ""

    # Create the markdown file with the specified format
    file_name = f"{today_date}/{today_date}-{page_number:02}.md"
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"{previous_page_link} | {next_page_link}")

    print(f"Markdown file created: {file_name}")

def create_all_markdown_files():
    # Get today's date in the required format
    today_date = datetime.now().strftime("%Y-%m-%d")

    # Check if the 'markdown_files' directory exists, create it if not
    directory = today_date
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a total of 17 files
    for page_number in range(1, 18):
        create_markdown_file(today_date, page_number)

if __name__ == "__main__":
    create_all_markdown_files()
