
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title="EduGenie",
    description="AI-Powered Educational Assistant",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request Models
class QuestionRequest(BaseModel):
    question: str


class QuizRequest(BaseModel):
    topic: str


class SummaryRequest(BaseModel):
    text: str


class LearningPathRequest(BaseModel):
    topic: str


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to EduGenie!",
        "status": "Running successfully"
    }


# Ask Question
@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.lower()

    if "largest ocean" in question:
        answer = "The Pacific Ocean is the largest ocean in the world."

    elif "pythagoras" in question:
        answer = (
            "The Pythagorean theorem states that in a right-angled triangle, "
            "the square of the hypotenuse equals the sum of the squares "
            "of the other two sides: a² + b² = c²."
        )

    elif "river" in question:
        answer = (
            "A river is a natural flowing water body that usually moves "
            "towards an ocean, sea, lake, or another river."
        )

    else:
        answer = (
            "Great question! EduGenie is ready to help you learn. "
            "AI model integration will provide detailed answers."
        )

    return {"answer": answer}


# Generate Quiz
@app.post("/generate-quiz")
def generate_quiz(request: QuizRequest):

    topic = request.topic

    return {
        "topic": topic,
        "quiz": [
            {
                "question": f"What is the main concept of {topic}?",
                "options": [
                    "Basic understanding",
                    "Advanced programming",
                    "Unrelated topic",
                    "None of these"
                ],
                "answer": "Basic understanding"
            },
            {
                "question": f"Why should we learn {topic}?",
                "options": [
                    "To improve knowledge",
                    "To avoid learning",
                    "To forget concepts",
                    "None of these"
                ],
                "answer": "To improve knowledge"
            }
        ]
    }


# Summarize Text
@app.post("/summarize")
def summarize(request: SummaryRequest):

    words = request.text.split()

    summary = " ".join(words[:50])

    if len(words) > 50:
        summary += "..."

    return {
        "summary": summary
    }


# Generate Learning Path
@app.post("/learning-path")
def learning_path(request: LearningPathRequest):

    topic = request.topic

    return {
        "topic": topic,
        "learning_path": [
            {
                "level": "Beginner",
                "duration": "1 Week",
                "topics": [
                    f"Introduction to {topic}",
                    "Basic concepts",
                    "Fundamentals"
                ]
            },
            {
                "level": "Intermediate",
                "duration": "2 Weeks",
                "topics": [
                    "Core concepts",
                    "Practical examples",
                    "Mini projects"
                ]
            },
            {
                "level": "Advanced",
                "duration": "3 Weeks",
                "topics": [
                    "Advanced concepts",
                    "Real-world applications",
                    "Final project"
                ]
            }
        ]
    }