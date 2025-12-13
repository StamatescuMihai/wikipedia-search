from fastapi import APIRouter, Query
from typing import Dict

from ..core.search.ranking_model import RankingModel
from ..database import get_db

router = APIRouter()


@router.get("/search")
def search(
    q: str = Query(..., description="Search query"),
    limit: int = Query(10, description="Maximum number of results")
) -> Dict:
    with get_db() as db:
        ranking_model = RankingModel(db)
        results = ranking_model.search(q, limit)

    response = {
        "query": q,
        "count": len(results),
        "results": results
    }

    return response
