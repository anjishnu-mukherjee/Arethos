from pine import get_similar_result

raw_query = """
Here are some question answers:

1. What is the smallest prime number?
A: 1, because it is the smallest natural number.

2. Why is 2 considered a special prime number?
A: Because it is the first prime number.

3. What is the prime factorization of 84?
A: 84 is a prime number, so it cannot be factored further.

4. Explain the Fundamental Theorem of Arithmetic.
A: It states that numbers can be divided by smaller numbers.

5. Why are prime numbers important in cryptography?
A: They are used for creating patterns in mathematics.

Here is the comprehension :
Mathematics: The Concept of Prime Numbers
A prime number is a natural number greater than 1 that has exactly two distinct factors: 1 and itself. 
The first few prime numbers are 2, 3, 5, 7, 11, and 13. Notably, 2 is the only even prime number because all other even numbers are divisible by 2.

Prime numbers play a crucial role in number theory and cryptography. They are used in encryption algorithms, such as RSA, which secures online transactions. 
The prime factorization of a number involves expressing it as a product of prime numbers. For instance, the prime factorization of 30 is 2 * 3 * 5. 
The Fundamental Theorem of Arithmetic states that every integer greater than 1 is either a prime number or can be uniquely expressed as a product of prime numbers.

Reply me in this format:
Question Number : Grade/10
Most apt answer -

"""
try:
    similar_responses = get_similar_result("comprehension",raw_query)
    print("Fetched Responses\nWriting to file.")
    
    with open("similar_responses.txt",'w') as f:
        for responses in similar_responses:
            f.write(responses+"\n")
        print("Sucessfully written!")
except :
    print("Error retriving responses!")
    print(Exception)



        