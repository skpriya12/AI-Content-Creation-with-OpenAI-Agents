# AI-Content-Creation-with-OpenAI-Agents
This project demonstrates how to use OpenAI's GPT-3.5-turbo and chat-based models to create a multi-agent workflow for generating, writing, and editing content. The workflow is built using Gradio for a user-friendly interface. The system consists of three agents:

1. **Content Planner**: Plans the content based on the given topic, identifying trends, audience analysis, and creating an outline with SEO keywords.
2. **Content Writer**: Uses the content plan provided by the Planner to write a comprehensive blog post.
3. **Content Editor**: Proofreads and edits the blog post for grammar, style, and alignment with the brand's voice.

### How It Works:
1. **Planner Agent**: Given a topic, the Planner generates a content plan, including key trends, audience analysis, an outline, and SEO keywords.
2. **Writer Agent**: The Writer uses the content plan to create a compelling blog post based on the provided outline and topic.
3. **Editor Agent**: The Editor reviews the blog post, making necessary improvements to grammar and alignment with the brand’s voice.

### Features:
- Create content in three stages: Planning, Writing, and Editing.
- Use OpenAI's GPT-3.5-turbo for each agent's tasks.
- Gradio interface for easy user interaction.
- Easily configurable to generate content for any topic.

### Requirements:
- Python 3.7+
- `openai` library
- `gradio` library

### Setup Instructions:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-content-creation.git
   cd ai-content-creation
