# ECE/COS 470 Principles of Blockchains: Final Project Guidelines

**Project Title:** Crowdsourcing to Build a Powerful AI Assistant for Learning the Course

**Goal:** Leverage collective effort to create a dataset and train an AI assistant to better understand and solve challenging blockchain-related tasks.

This project involves three stages: 
- Dataset Creation
- Dataset Evaluation
- AI-Assistant Tuning

  
**Categories:**
Before the project, each group will sign up for subcategories where their focus will be on creating tasks and solving the tasks with AI inside the subcategory.
- Category 1: Lecture contents and homework questions, e.g. creating new questions for homework based on lecture contents;
- Category 2: Coding Assignment 1-3: Implementing basic structures for blockchains;
- Category 3: Coding Assignment 4-5: Mining and Network;
- Category 4: Coding Assignment 6-8: Putting everything together **(2% extra credit)**;
- Category 5: Beyond the course: Anything you find interesting and appropriate to include in this course but not covered yet, e.g. suggesting extensive reading for students who want to learn more about a topic.

At most 6 groups are allowed for each subcategory.

Below are the detailed guidelines, evaluation criteria, and rubrics for each stage.


## Stage 1: Dataset Creation (32%) 

### **Task**
In this stage, you will create a dataset consisting of challenging tasks for GPT-4o and their solutions. Specifically, your goal is to find tasks related to the course material of COS/ECE-470 where GPT-4o does not perform well when directly provided with all course content. These "hard tasks" should represent problems that require more sophisticated problem-solving, deeper understanding, or clearer step-by-step instructions than GPT-4o currently demonstrates. 

Possible directions for designing such tasks include:
1. Tasks where GPT fails or produces misleading answers when used for assistance in homework or assignments.
2. Planning tasks for coding assignments (e.g., how to structure the repository when building a Bitcoin Client from scratch).
3. Reasoning tasks for homework (e.g., questions regarding lecture notes or homework that GPT fails to answer correctly). 
4. Any other tasks within the scope of this course that GPT struggles with.

To qualify for a valid entry in the dataset, the baseline performance using our given prompt (simply feed all course materials into the prompt, which will be released soon) should be unsatisfactory. You will then include a more desirable solution in the dataset. 

Please keep in mind that the data is intended to improve AI's performance as an assistant for learning the course, so the task should reflect questions a student is likely to ask while learning the material.

### **Criteria for Challenging Tasks**
- **Baseline Failure:** The task should demonstrate a clear failure (or unsatisfactory response) of GPT-4o using the baseline prompt.
- **Course Relevance:** The task should be within the scope of blockchain principles and require a deep understanding of blockchain concepts, multi-step reasoning, or advanced application of knowledge.
- **Learning Opportunity:** The task should present a meaningful opportunity for AI improvement, with a clear path to a better solution.

  
### **Submission Format**
Data entries will be collected via Google Forms.
1. **Baseline Performance Log:** Submit a full chat history showing GPT-4o's baseline performance. Please strictly follow the baseline prompt without alteration to ensure consistency.
2. **Desirable Solution:** Provide a solution that clearly explains the rationale and logic of solving the problem. The solution should be instructional, with reasoning steps for audience comprehension.
   - Options for submission include:
     - Your prompt history with GPT-4o, which guides the AI to a correct solution step-by-step.
     - An interactive example where you craft both the questions and answers, demonstrating the expected interaction with the AI.
     - A detailed written solution explaining the task and steps comprehensively.
3. **Rationale:** Provide a detailed rationale explaining why the data you created is beneficial for improving AI performance on these tasks.

### **Deliverables**
Each group should submit at least 10 data entries. Due date: Oct 30, 9pm. 

### **Baseline**

Baseline Prompt: 
[Upload the three files: bitcoin_client_data.jsonl, ed_discussion_fa2023.json, lecture_notes.json using "Attach File"]
"You're a professional assistant for me to learn the course ECE/COS 470 Principles of Blockchains (https://web3.princeton.edu/principles-of-blockchains/).  
All the materials of this course are attached below, 
including the programming assignment GitHub repo (bitcoin_client_data.jsonl), 
Ed discussion log from last year's course (ed_discussion_fa2023.json), 
and the tex source file of all lecture notes (lecture_notes.json). 

I may ask you questions related to lecture notes, programming assignments, or homeworks, and you are expected to solve any of my confusion and provide step-by-step instructions and reasoning for your response. 
Please calm down, think step by step, and double check your answer before finalizing the response. 
When you are not confident about the answer, say "Sorry but I'm not sure" instead of producing random misleading responses. 
Here is my question: 

..."

An example of baseline: https://chatgpt.com/share/67060269-9568-8012-aab3-daf425e5598f

To guarantee consistency, please do not modify anything except for "..." in the baseline prompt, and use GPT-4o for generating baseline response. 


### **Grading Criteria for Stage 1 (for a total of 32%)**
- **Completeness (16%)**: At least 10 data entries are submitted by each group. All required components (baseline log, solution, rationale) are included and well-documented.
- **Quality of Solution (4%)**: The solution should clearly explain the reasoning, with a step-by-step approach that makes it easy for others to understand.
- **Usefulness of Rationale (4%)**: The rationale should explain why the solution provides a learning opportunity for the AI, with specific insights into how it helps GPT-4o overcome current limitations.
- **Peer-graded Dataset Quality (8%)**: Grades received in peer-grading phase in stage 2. TAs will moderate the process, accept appeals for grades in this part, and hold the final interpretation right for the grades.
- **Extra Credit (at most 10%)**: Incorporate videos, images, or any form of multimedia in the dataset.

## **Stage 2: Dataset Evaluation (20%)**

### **Task**
You will be assigned a set of data entries created by other groups. Your job is to evaluate these entries against a rubric that you design. Each entry will receive 2-3 evaluations to ensure consistency.

### **Evaluation Guidelines**
- Create rubrics to assess the quality of the datasets.
- Each evaluation must include a score and detailed feedback explaining the strengths and weaknesses of the entry.
- Your rubric should focus on evaluating completeness, quality, educational value, and potential for improving GPT-4o.
- The average grade of all data entries you grade should be around 90 out of 100, but certain upshifts or downshifts are certainly acceptable as long as your rubrics and reviews are clear.

### **Deliverables**
Each group will review and evaluate other groups' data entries within the same category. Reviews should be submitted via Google form. Due date: Nov 4, 10pm. 
Based on your own experience when creating the data entries and reviewing others' dataset entry, each group will produce an interim report on:
(1) What are the properties of a good dataset entry; (2) Any strategy or thought for creating a data entry.
Due date: Nov 8, 10pm.


### **Example Rubrics for Evaluating a Data Entry**
1. **Completeness (50%)**: Does the data entry consist of all the required components?
2. **Quality of Task (15%)**: Does the task align well with the course material? Is the baseline log a failure of GPT-4o?
3. **Solution Clarity (15%)**: Does the solution provide sufficient instructional value? Is the explanation logically structured?
4. **Rationale Effectiveness (10%)**: Is the rationale insightful? Does it demonstrate why and how the AI can learn from this entry?
5. **Formatting and Presentation (10%)**: Is the submission well-organized, easy to read, and appropriately formatted?

### **Grading Criteria for Stage 2 (for a total of 20%)**
- **Peer Evaluation (8%)**: The rubrics are clear and easy to follow. The evaluation is consistent and fair. Each evaluation should provide meaningful and detailed feedback.
- **Interim Report (12%)**: Your report comprehensively summarizes your findings during stage 1 and stage 2.

## **Stage 3: AI-Assistant Tuning (48%)**

### **Task**
After creating and evaluating the dataset, students will use the top entries to fine-tune an AI assistant. You may use any free-access-to-all (e.g. GPT-4o, Llama, but you shouldn't use any paid services) methods and their combination to try to improve AI’s performance on these tasks. The objective is to explore different ways of enhancing the AI’s ability to solve challenging blockchain problems using the dataset created by students.

### **Deliverables**
1. **Presentation:** On Nov 15 and Nov 22, each group will present their current findings in class. You can talk about your report in stage 1 and 2, your ideas for stage 3, etc. Each group will have 6 minutes to present and 2 minutes for the Q&A session. 
2. **Final Code or Prompt:** Submit the final version of your code or prompts used for fine-tuning or improving AI's performance.
3. **Final Report:** Write a report summarizing the method you used, why you chose it, and how effective it was. Due to the time limit, you may not have enough time to implement the ideas, especially if you choose to fine-tune open-source models. You can sketch your idea and predict possible outcomes in your report. Also, you can summarize the best practices for using AI as a learning assistant in this course.
Final Code, prompt, and report are due on Dean's Date (Dec 13). No extension is allowed according to the university's regulations. 

### **Grading Criteria for Stage 3 (for a total of 48%)**
- **Presentation (16%)**: Is the presentation clear, intelligible, and well-prepared? Does your presentation contain creative ideas or interesting findings? 
- **Final Code or Prompt (10%)**: How innovative or effective was your approach to improving the AI? Did you use available resources creatively?
- **Final Report (22%)**:  Is the report well-structured, clearly explaining your method, rationale, and results? Was there a measurable improvement in the AI's performance? Did your method succeed in addressing weaknesses identified during dataset creation?


## **Important Dates**
- **Stage 1: Dataset Creation** — Submission by Google Form, due **Oct 30, 9pm**.
- **Stage 2: Dataset Evaluation** — Peer review by Google Form, due **Nov 4, 10pm**. Interim report on Canvas, due **Nov 8, 10pm**.
- **Stage 3: AI-Assistant Tuning** — Presentation slides due **1:30pm on presentation day (Nov 15 or Nov 22)**. Final code/prompt and report due Dean's date (**Dec 13, 11:59pm**). 
