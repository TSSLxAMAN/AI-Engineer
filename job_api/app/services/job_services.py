from app.db.memory_db import jobs_db
from app.models.jobs import JobPosting


def create_job(job: JobPosting):
    jobs_db.append(job)
    return job


def get_all_jobs():
    return jobs_db