from connect_db import init_connection

def get_tasks():
    with init_connection() as client:
        tasks_str = []
        tasks_api = client.tasks_api()
        tasks = tasks_api.find_tasks_iter()

        for task in tasks:
            tasks_str.append(f"{task.name}\t - \t{task.status}")

        return tasks_str       

def aggregate_flux_query(from_bucket, to_bucket):
    flux = \
        """
        option task = {
            name: "{task_name}",
            every: 5m
        }
        
        from(bucket: "{from_bucket}") 
            |> range(start: -task.every) 
            |> filter(fn: (r) => (r.["_measurement"] == "railData"))
            |> to(bucket: {to_bucket})
        """.format(
            task_name="sample-task", 
            from_bucket=from_bucket, 
            to_bucket=to_bucket
        )

def aggregate_task_preset():
     with init_connection() as client:
        tasks_api = client.tasks_api()
        tasks = tasks_api.find_tasks_iter()

        return tasks      