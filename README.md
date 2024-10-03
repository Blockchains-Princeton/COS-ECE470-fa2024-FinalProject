# ECE/COS 470 Principles of Blockchains: Final Project Guidelines

**Project Title:** Crowdsourcing to Build a Powerful AI Assistant for Learning the Course

**Goal:** Leverage collective effort to create a dataset and train an AI assistant to better understand and solve hard blockchain-related tasks.

This project involves three stages: 
- Dataset Creation
- Dataset Evaluation
- AI-Assistant Tuning

Below are the detailed guidelines, evaluation criteria, and rubrics for each stage.

## **Stage 1: Dataset Creation**

### **Task**
In this stage, you will create a dataset consisting of challenging tasks for GPT-4o and their solutions. Specifically, your goal is to find tasks related to the course material where GPT-4o does not perform well when directly provided with all course content. These "hard tasks" should represent problems that require more sophisticated problem-solving or deeper understanding than GPT-4o currently demonstrates.

### **Submission Format**
1. **Baseline Performance Log:** Submit a full chat history showing GPT-4o's baseline performance. This must use all course materials in the prompt without alteration to ensure consistency.
2. **Desirable Solution:** Provide a solution that clearly explains the rationale and logic of solving the problem. The solution should be instructional, providing reasoning steps for audience comprehension.
   - Options for submission include:
     - Your prompt history with GPT-4o, which guides the AI to a correct solution step-by-step.
     - An interactive example where you craft both the questions and answers, demonstrating the expected interaction with the AI.
     - A detailed written solution explaining the task and steps comprehensively.
3. **Rationale:** Provide a detailed rationale explaining why the data you created is beneficial for improving AI performance on these tasks.

### **Criteria for Hard Tasks**
- **Baseline Failure:** A task is considered hard if GPT-4o cannot solve it using the course materials directly.
- **Complexity and Depth:** The task should require a deep understanding of blockchain concepts, multi-step reasoning, or advanced application of knowledge.
- **Learning Opportunity:** The task should represent a meaningful opportunity for AI improvement, with a clear path to a better solution.

### **Grading Criteria for Dataset Creation**
- **Completeness (30%)**: All required components (baseline log, solution, rationale) are included and well documented.
- **Difficulty (20%)**: The task should be genuinely challenging for GPT-4o while being solvable for a knowledgeable student.
- **Quality of Solution (30%)**: The solution should clearly explain the reasoning, with a step-by-step approach that makes it easy for others to understand.
- **Usefulness of Rationale (20%)**: The rationale should explain why the solution process provides a learning opportunity for the AI, with specific insights on how it helps GPT-4o overcome current limitations.

## **Stage 2: Dataset Evaluation**

### **Task**
You will be assigned a set of data entries created by other groups. Your job is to evaluate these entries against a rubric that you design. Each entry will receive 2-3 evaluations to ensure consistency. Your evaluation quality will also impact your grade for Stage 1.

### **Evaluation Guidelines**
- Create rubrics to assess the quality of the datasets.
- Each evaluation must include a score and detailed feedback explaining the strengths and weaknesses of the entry.
- Your rubric should focus on evaluating completeness, quality, educational value, and potential for improving GPT-4o.

### **Suggested Rubrics for Evaluation**
1. **Completeness (25%)**: Is the baseline log clear? Is the solution detailed and comprehensive?
2. **Quality of Task (20%)**: Is the task challenging enough for GPT-4o? Does it align well with the course material?
3. **Solution Clarity (25%)**: Does the solution provide sufficient instructional value? Is the explanation logically structured?
4. **Rationale Effectiveness (20%)**: Is the rationale insightful? Does it demonstrate why and how the AI can learn from this entry?
5. **Formatting and Presentation (10%)**: Is the submission well-organized, easy to read, and appropriately formatted?

### **Grading Criteria for Evaluation**
- **Depth of Feedback (50%)**: Each evaluation should provide meaningful and detailed feedback, showing a deep understanding of the entry.
- **Fairness (30%)**: Scores should align with the quality of the entry, and similar entries should receive similar grades.
- **Rubric Design (20%)**: Your rubric should be comprehensive, covering all critical aspects of the dataset entry.

## **Stage 3: AI-Assistant Tuning**

### **Task**
After creating and evaluating the dataset, students will use the top entries to fine-tune an AI assistant. You may use any available methods to try to improve GPT-4o’s performance on these tasks. The objective is to explore different ways of enhancing the AI’s ability to solve hard blockchain problems using the dataset created by students.

### **Deliverables**
1. **Final Code or Prompt:** Submit the final version of your code or prompts used for fine-tuning or improving GPT-4o.
2. **Report:** Write a report summarizing the method you used, why you chose it, and how effective it was.

### **Grading Criteria for AI-Assistant Tuning**
- **Approach (40%)**: How innovative or effective was your approach to improving the AI? Did you use available resources creatively?
- **Results (30%)**: Was there a measurable improvement in the AI's performance? Did your method succeed in addressing weaknesses identified during dataset creation?
- **Clarity of Report (30%)**: Is the report well-structured, explaining your method, rationale, and results clearly and concisely?

## **General Best Practices for Using AI**
- Treat AI as a collaborator, not just a tool—guide it through complex problems, iterating when it falls short.
- Be thorough in testing the AI; hard tasks often require multiple attempts or refined prompts.
- Always focus on instructional clarity, ensuring that any audience (AI or human) can understand the thought process behind the solution.

**Timeline**: The final deliverables are due by the Dean’s Date. All three stages must be completed by this deadline.

### **Project Timeline Overview**
- **Stage 1: Dataset Creation** — Initial submission by [specified date]
- **Stage 2: Dataset Evaluation** — Peer review by [specified date]
- **Stage 3: AI-Assistant Tuning** — Final code/prompt and report due by Dean’s Date.
