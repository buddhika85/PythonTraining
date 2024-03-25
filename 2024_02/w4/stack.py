def push_job(job_stack):
    job_stack.append(f'Job {len(job_stack)}')

def pop_job(job_stack):
    if len(job_stack) == 0:
        return None
    else:
        return job_stack.pop(len(job_stack) - 1)

jobs = []
print(jobs)
push_job(jobs)
push_job(jobs)
print(jobs)
print(f'Popped: {pop_job(jobs)}')
print(jobs)