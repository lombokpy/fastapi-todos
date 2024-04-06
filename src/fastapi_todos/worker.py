from task import laphar_task, lapharsiaga_task, lapharsus_task

from core.celery_app import celery_app

laphar_task.stay()
lapharsus_task.stay()
lapharsiaga_task.stay()


@celery_app.task(acks_late=True)
def test_celery(word: str) -> str:
    return f"test task return {word}"
