from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from dotenv import load_dotenv
from routers.journal_router import router as journal_router
import logging

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(title="LearningSteps API", description="A simple learning journal API for tracking daily work, struggles, and intentions")
app.include_router(journal_router)

logger.info("LearningSteps API started")

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")