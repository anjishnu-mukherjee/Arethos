from google import genai
from keys import API_KEY

client = genai.Client(api_key=API_KEY)

prompt = """
Here are some question answers:

Q1. What was unique about the bookstore named Whispering Pages?
A: It had  Mr. Alistair.

Q2. How did Eleanor react when she first opened the leather-bound book?
A: She was confused and surprised to see that the pages were blank.

Q3. What made the book unusual?
A: The book had blank pages.

Q4. What message was written in the book when Eleanor returned as an adult?
A: "Stories do not end; they only wait to be written again."

Here is the comprehension:

In the heart of an ancient city, nestled between towering stone buildings, stood a small bookshop named Whispering Pages. Unlike modern bookstores, this one had no digital catalogs or electronic payment systems—only rows of dusty shelves filled with books that carried the scent of time. The shop belonged to an old man named Mr. Alistair, whose love for literature had kept the place alive for decades.
Among the regular visitors was a young girl named Eleanor. She would spend hours flipping through pages, immersing herself in stories of distant lands and forgotten eras. Mr. Alistair, noticing her fascination, once handed her a peculiar leather-bound book with no title. “This one,” he said, “chooses its reader.”
Curious, Eleanor opened the book and gasped. The pages were blank. Confused, she looked up at Mr. Alistair, who simply smiled and said, “Sometimes, a book does not tell a story. It listens to one.” Puzzled but intrigued, Eleanor took the book home.
That night, as she thought about her day, words began to appear on the once-empty pages. They described her thoughts, her dreams, and even her unspoken fears. It was as if the book was capturing the very essence of her soul. Over time, Eleanor realized that the book was not just a reflection of her mind but also a guide, helping her understand herself better.
Years later, when Eleanor had grown up, she returned to Whispering Pages, only to find it empty. The shelves were bare, and Mr. Alistair was nowhere to be found. On the dusty counter, however, lay the same leather-bound book. This time, it held a single line written in delicate script:
"Stories do not end; they only wait to be written again."

Given a grading system of 10 marks on each question grade each question. Each question is graded on the correctness with the passage. The answer should be the most closest with reference with the passage.

Reply me in this format:
Question Number : Grade/10
Most apt answer -
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)