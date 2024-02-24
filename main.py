"""A short script to create notes using the ObsidiAnki GPT Assistant."""

from time import sleep

from openai import OpenAI

from config.cfg import ASSISTANT_ID, OPENAI_API_KEY, SAVE_LOCATION
from utils.logger import get_logger


def prompt_assistant(
    logger, client: OpenAI, thread, ASSISTANT_ID: str, text: str
) -> str:
    """
    Prompt the OpenAI Assistants API with a user message, and return the response.
    :param client: The OpenAI client.
    :param thread: The thread to prompt.
    :param ASSISTANT_ID: The ID of the assistant to prompt.
    :param text: The user's message to respond to.
    """

    message = client.beta.threads.messages.create(
        thread_id=thread.id, role="user", content=text
    )

    logger.info(f"Message added to thread: {message}")

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=ASSISTANT_ID,
    )

    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
        logger.info(f"Run status: {run.status}")
        for pause in range(5):
            logger.info((pause + 1) * ".")
            sleep(1)

    messages = client.beta.threads.messages.list(thread_id=thread.id)

    logger.info(f"Messages retrieved: {messages}")

    return messages.data[0].content[0].text.value


def main() -> None:
    """
    The main function.
    :return: None
    """

    # Initalise objects
    client = OpenAI(api_key=OPENAI_API_KEY)
    thread = client.beta.threads.create()
    logger = get_logger()

    # Get user input
    topic = input("What topic do you want to generate a note for? ")

    # Prompt the assistant
    note = prompt_assistant(
        logger, client, thread, ASSISTANT_ID, f"Create a note on {topic}."
    )

    logger.info(f"Note generated: {note}")

    # Save the note as a md file
    with open(SAVE_LOCATION / f"{topic}.md", "w") as file:
        file.write(note)


if __name__ == "__main__":
    main()
