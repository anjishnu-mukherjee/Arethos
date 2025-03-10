from google import genai
from keys import API_KEY

client = genai.Client(api_key=API_KEY)

prompt = """
Here are some question answers:

1. Identify the correct sentence:
a) The dog and the cat is playing.
b) The dog and the cat are playing.
A: The dog and the cat is playing.

2. Which verb correctly completes the sentence?
"Either the manager or the employees ______ responsible."
a) is
b) are
A: is

3. What is the rule for subject-verb agreement with "and"?
A: The verb should match the noun closest to it.

4. How do collective nouns affect subject-verb agreement?
A: They always take a singular verb.

5. Choose the correct sentence:
a) My family is going on vacation.
b) My family are going on vacation.
A: My family are going on vacation.

Here is the comprehension :
Subject-verb agreement is an essential rule in English grammar. It states that a singular subject takes a singular verb, while a plural subject takes a plural verb. For example, "The cat runs fast" is correct because "cat" is singular and "runs" is singular. 
However, "The cat run fast" is incorrect because "run" is a plural verb.

When a sentence has a compound subject connected by "and," the verb is usually plural, as in "John and Mary are going to the park." 
However, when subjects are connected by "or" or "nor," the verb agrees with the subject closest to it. For instance, "Neither the teacher nor the students were present" and "Neither the students nor the teacher was present" are both correct.

Special cases include collective nouns like "team" or "family." Depending on the context, they can take singular or plural verbs. For example, "The team is winning" (as a single unit) versus "The team are arguing" (as individual members).

Reply me in this format:
Question Number : Grade/10
Most apt answer -
"""

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)