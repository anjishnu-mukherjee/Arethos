from google import genai
from keys import API_KEY

client = genai.Client(api_key=API_KEY)

prompt = """
Here are some question answers:

1. Suppose you are on the Moon, where gravity is weaker than on Earth. How would your weight change?
A: It would be the same as the mass remains constant.

2. If two planets are twice as far apart as before, how does their gravitational attraction change?
A: It decreases to 1/4 of the original force, since gravity follows an inverse square law.

The Mystery of Gravity
For centuries, humans have wondered why objects fall to the ground when dropped. The ancient Greek philosopher Aristotle believed that heavier objects fall faster than lighter ones. However, this idea was challenged in the 16th century by the Italian scientist Galileo Galilei. According to legend, Galileo conducted an experiment from the Leaning Tower of Pisa, dropping two spheres of different masses. He observed that both spheres hit the ground at the same time, proving that objects fall at the same rate regardless of their mass, assuming no air resistance.

Later, in the 17th century, Sir Isaac Newton formulated his famous law of universal gravitation. He proposed that every object in the universe attracts every other object with a force that depends on their masses and the distance between them. This force, called gravity, explains why planets orbit the Sun and why the Moon orbits the Earth. Newton’s equation for gravitational force is:

F = G m1 m2 / r^2
 
where F is the gravitational force, G is the gravitational constant, m₁ and m₂ are the masses of the two objects, and r is the distance between their centers.

In the early 20th century, Albert Einstein refined our understanding of gravity with his theory of general relativity. Instead of describing gravity as a force, Einstein proposed that massive objects warp the fabric of space-time, causing smaller objects to follow curved paths. This theory was confirmed during a solar eclipse in 1919 when scientists observed that the Sun's gravity bent the light from distant stars.

Even today, gravity remains a fascinating topic in physics. Scientists continue to study its effects, from black holes to gravitational waves, unlocking new mysteries of the universe.
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