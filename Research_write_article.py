import openai
import gradio as gr
import os
from openai import OpenAIError

# Setting up OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key


# Define the OpenAI-powered agent responses
def create_planner_agent(topic):
    # The Planner Agent will create a content plan for the given topic
    messages = [
        {"role": "system", "content": "You are a helpful content planner."},
        {"role": "user",
         "content": f"Create a content plan for a blog about {topic}. Include key trends, audience analysis, a content outline, and SEO keywords."}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except OpenAIError as e:
        return f"Error generating Planner response: {e}"


def create_writer_agent(topic, content_plan):
    # The Writer Agent will craft a blog post based on the planner's content
    messages = [
        {"role": "system", "content": "You are a skilled content writer."},
        {"role": "user",
         "content": f"Write a blog post based on the following content plan about {topic}: {content_plan}. Include SEO keywords and follow the content structure."}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except OpenAIError as e:
        return f"Error generating Writer response: {e}"


def create_editor_agent(blog_post):
    # The Editor Agent will edit the blog post for grammar, clarity, and brand voice
    messages = [
        {"role": "system", "content": "You are an expert editor."},
        {"role": "user",
         "content": f"Proofread and improve the following blog post: {blog_post}. Ensure it is grammatically correct and aligned with the brand's voice."}
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=800,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except OpenAIError as e:
        return f"Error generating Editor response: {e}"


# Gradio Interface Functions
def generate_blog_content(topic):
    # Step 1: Create a content plan using the Planner Agent
    content_plan = create_planner_agent(topic)

    # Step 2: Generate a blog post using the Writer Agent based on the content plan
    blog_post = create_writer_agent(topic, content_plan)

    # Step 3: Edit the blog post using the Editor Agent
    edited_blog_post = create_editor_agent(blog_post)

    return content_plan, blog_post, edited_blog_post


# Define the Gradio UI
iface = gr.Interface(
    fn=generate_blog_content,
    inputs=gr.Textbox(label="Enter Topic", placeholder="E.g., Artificial Intelligence", lines=1),
    outputs=[gr.Textbox(label="Content Plan"), gr.Textbox(label="Blog Post Draft"),
             gr.Textbox(label="Edited Blog Post")],
    title="AI Content Creation",
    description="Create a content plan, write a blog post, and edit it with the help of OpenAI-powered agents."
)

# Launch the interface
iface.launch()
