from fastapi import APIRouter
from app.models.jobs import JobPosting
from app.services.job_services import create_job, get_all_jobs

router = APIRouter()


@router.post("/jobs")
def add_job(job: JobPosting):
    return create_job(job)


@router.get("/jobs")
def list_jobs():
    return get_all_jobs()