# Step 1: Read the file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Step 2: Filter subreddits based on keywords
def filter_subreddits(subreddits):
    filtered_subreddits = []
    keywords = ["india", "desi", "delhi"]
    for line in subreddits:
        subreddit, count = line.strip().split('\t')
        for keyword in keywords:
            if keyword in subreddit.lower():
                filtered_subreddits.append((subreddit, count))
                break
    return filtered_subreddits

# Step 3: Generate HTML table
def generate_html_table(subreddits):
    html_content = "<html><head><title>Filtered Subreddits</title></head><body>"
    html_content += "<table border='1'><tr><th>S.no</th><th>Subreddit name [Subreddit linked]</th><th>Sub count</th></tr>"
    for i, (subreddit, count) in enumerate(subreddits, start=1):
        html_content += f"<tr><td>{i}</td><td><a href='https://www.reddit.com/r/{subreddit}'>{subreddit}</a></td><td>{count}</td></tr>"
    html_content += "</table></body></html>"
    return html_content

# Main function
def main():
    file_path = "subreddits.txt"
    subreddits = read_file(file_path)
    filtered_subreddits = filter_subreddits(subreddits)
    html_content = generate_html_table(filtered_subreddits)
    with open("filtered_subreddits.html", "w") as html_file:
        html_file.write(html_content)

if __name__ == "__main__":
    main()
