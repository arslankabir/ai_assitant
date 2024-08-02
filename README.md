# Liberte AI Assistant

Liberte AI Assistant is a customized AI chatbot integrated within a Django application. It uses OpenAI's GPT-4 model along with LangChain components to manage data retrieval and conversation flows. The assistant is designed to maintain a consistent identity and respond according to the specific instructions set by the Liberte team.

## Features

- **Identity Management**: The assistant consistently identifies as "Liberte AI Assistant" and follows strict guidelines for responses.
- **Custom Response Handling**: Special handling for specific prompts, including data logging for future training.
- **Integration with Django**: Easily integrated with Django web applications, providing a seamless user experience.
- **Data Persistence**: Uses a vector store for efficient data retrieval and indexing.

## Installation

### Prerequisites

- Python 3.x
- Django
- Virtualenv (recommended)
- Git

### Setup

1. **Clone the Repository**

   \`\`\`bash
   git clone https://github.com/arslankabir/ai_assitant.git
   cd ai_assitant
   \`\`\`

2. **Create and Activate Virtual Environment**

   \`\`\`bash
   # Create a virtual environment
   python -m venv lbtvenv

   # Activate the virtual environment
   # On Windows
   lbtvenv\Scripts\activate
   \`\`\`

3. **Install Dependencies**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Setup Django**

   \`\`\`bash
   python manage.py migrate
   \`\`\`

5. **Run the Server**

   \`\`\`bash
   python manage.py runserver
   \`\`\`

   The application will be available at \`http://127.0.0.1:8000/\`.

## Usage

- **Interacting with the Chatbot**: Navigate to the chat interface in the application and type your queries. The assistant will respond according to the defined instructions.
- **Special Commands**: Certain commands like \`ak47333\` can trigger specific behaviors such as logging data for review.

## Customization

- **Custom Prompts**: Modify \`CUSTOM_PROMPT\` in \`liberte_ai.py\` to adjust the initial prompt.
- **Data Handling**: Add new data to the \`data\` directory for additional context during responses.
- **.gitignore**: Customize \`.gitignore\` to exclude unnecessary files from version control.

## Contributing

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature/your-feature-name\`).
3. Make your changes.
4. Commit your changes (\`git commit -m 'Add some feature'\`).
5. Push to the branch (\`git push origin feature/your-feature-name\`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the OpenAI team for developing GPT-4.
- Special thanks to the LangChain community for their helpful tools and resources.

## Contact

For questions or issues, please open an issue in the repository or contact the project maintainers.
