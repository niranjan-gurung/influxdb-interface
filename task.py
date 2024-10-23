from influxdb_client import TaskCreateRequest
from connect_db import init_connection

def get_tasks():
    with init_connection() as client:
        tasks_api = client.tasks_api()
        tasks = tasks_api.find_tasks_iter()     
        tasks_str = []

        # convert 'tasks' into array of json objects:
        # idk how to iterate over paginated list... 
        for task in tasks:
            tasks_str.append(task)

        return tasks_str       

def create_task_preset(from_bucket, to_bucket, task_name="downsample-task"):
    # TODO:
    # measurement needs to dynamic template.
    # need to get measurement from client api... (idk how yet) 
    with init_connection() as client:
        flux = \
            '''
            option task = {{
                name: "{task_name}",
                every: 10m
            }}
            
            from(bucket: "{from_bucket}") 
                |> range(start: -task.every) 
                |> filter(fn: (r) => r["_measurement"] == "railData")
                |> aggregateWindow(every: 10s, fn: mean)
                |> to(bucket: "{to_bucket}", org: "{org}")
            '''.format(
                task_name=task_name, 
                from_bucket=from_bucket, 
                to_bucket=to_bucket,
                org=client.org
            )

        tasks_api = client.tasks_api()
        task_req = TaskCreateRequest(
            flux=flux,
            org=client.org,
            description="downsample mqtt metrics",
            status="active"
        )
        task = tasks_api.create_task(task_create_request=task_req)

        return task 