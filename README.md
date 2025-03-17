# Arethos  

This project is an AI-driven answer grading system that utilizes Google's Gemini AI and Pinecone vector database to evaluate and provide feedback on student responses. The system leverages past grading examples stored in Pinecone for more accurate assessments.

## Table of Contents
- [Overview](#overview)
- [How It Works](#how-it-works)

---

## Overview  

This system automates the grading process by:  
1. Extracting questions, answers, and grading feedback from a dataset.  
2. Storing embeddings of past graded answers in Pinecone for future reference.  
3. Generating grading prompts based on previous evaluations.  
4. Using Google's Gemini API to assess answers based on stored examples and predefined grading criteria.  

---

## How It Works  

1. **Extract Questions & Answers:**  
   - Raw context, questions, and answers are loaded from text files.  
   - Text is formatted into structured JSON.  

2. **Store Embeddings (If Enabled):**  
   - Past graded responses are embedded using Gemini Embeddings.  
   - Stored in Pinecone for efficient retrieval.  

3. **Retrieve Relevant Past Grades:**  
   - The system finds similar past responses from Pinecone.  
   - Uses them as a reference for grading new answers.  

4. **Generate Grading Prompt:**  
   - The retrieved examples and new answers are combined into a grading prompt.  
   - The prompt includes grading criteria like correctness, completeness, and relevance.  

5. **Grade Answers Using Gemini:**  
   - The AI evaluates responses based on past examples and grading criteria.  
   - It assigns scores and provides detailed feedback.  

---


