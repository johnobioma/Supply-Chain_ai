from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Portfolio SaaS Demo API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Product(BaseModel):
    sku: str
    name: str
    category: str = "General"
    stock: int = 0
    reorder_level: int = 0
    warehouse: str = "Main warehouse"

class DraftRequest(BaseModel):
    message: str
    customer_name: Optional[str] = "there"

@app.get("/health")
def health():
    return {"status": "ok", "message": "Portfolio demo API is running"}

@app.get("/api/inventory")
def inventory():
    return [
        {"sku":"SKU-1042","name":"Wireless Headphones","stock":1240,"reorder_level":300,"warehouse":"Lagos Central"},
        {"sku":"SKU-2081","name":"Smart Watch Pro","stock":186,"reorder_level":250,"warehouse":"Abuja Hub"},
        {"sku":"SKU-4107","name":"USB-C Charging Hub","stock":42,"reorder_level":150,"warehouse":"Port Harcourt"},
    ]

@app.post("/api/inventory")
def add_product(product: Product):
    # Demo only: replace with database persistence before production.
    return {"created": True, "product": product.model_dump()}

@app.post("/api/support/draft")
def draft_reply(request: DraftRequest):
    # Safe placeholder: connect an LLM and approved knowledge retrieval later.
    return {
        "draft": f"Hi {request.customer_name}, thanks for contacting us. "
                 "I'd be happy to help. Could you share your order reference "
                 "so our team can verify the details?",
        "requires_human_review": True,
        "source": "placeholder"
    }
