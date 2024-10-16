from scripts.fetch_papers.fetch_papers import fetch_and_summarize_papers
from scripts.summarize_papers.summarize import summarize_legal_document
from scripts.classify_papers.classify import classify_summary_groq
from scripts.synthesize_papers.synthesize import synthesize_papers
from config.config_template import config
import asyncio
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting the legal research pipeline...")

    start_date = config['start_date']
    end_date = config['end_date']
    queries = config['queries']
    abstract = config['paper_abstract']

    # Fetch and summarize papers
    relevant_papers = await fetch_and_summarize_papers(queries, abstract, start_date, end_date)
    logger.info(f"Found {len(relevant_papers)} relevant papers.")

    # Synthesize relevant papers
    synthesis = await synthesize_papers(relevant_papers, abstract)
    logger.info(f"Synthesis complete. Here is the result:\n{synthesis}")

if __name__ == "__main__":
    asyncio.run(main())
