from pymongo import MongoClient
from bson.objectid import ObjectId
from core.config import Config

client = MongoClient(Config.MONGO_URI)
db = client[Config.DB_NAME]
tasks_collection = db[Config.COLLECTION_NAME]


# Serialize MongoDB document to JSON-safe dict
def serialize_task(task):
    return {
        "id": str(task.get("_id", "")),
        "title": task.get("title", ""),
        "description": task.get("description", ""),
        "completed": task.get("completed", False),
    }

# Create a task with optional description
def create_task(title, description=""):
    task = {
        "title": title,
        "description": description,
        "completed": False,
    }

    result = tasks_collection.insert_one(task)

    if not result.acknowledged:
        print("Task creation failed")
        return None

    print(f"Task created with id: {result.inserted_id}")
    return serialize_task(tasks_collection.find_one({"_id": result.inserted_id}))


# Return all tasks as serialized list
def get_all_tasks():
    tasks = list(tasks_collection.find())
    print(f"Found {len(tasks)} task(s)")
    return [serialize_task(task) for task in tasks]

# Get one task by ID
def get_task_by_id(task_id):
    try:
        task = tasks_collection.find_one({"_id": ObjectId(task_id)})
        return serialize_task(task) if task else None
    except Exception as e:
        print(f"Error in get_task_by_id: {e}")
        return None

# Update a task by ID
def update_task(task_id, data):
    try:
        update_data = {}

        if "title" in data:
            update_data["title"] = data["title"]
        if "description" in data:
            update_data["description"] = data["description"]
        if "completed" in data:
            update_data["completed"] = data["completed"]

        if not update_data:
            print("Nothing to update")
            return None

        result = tasks_collection.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": update_data}
        )

        if result.matched_count == 0:
            print(f"Task {task_id} not found for update")
            return None

        print(f"Task {task_id} updated")
        return serialize_task(tasks_collection.find_one({"_id": ObjectId(task_id)}))
    except Exception as e:
        print(f"Error in update_task: {e}")
        return None

# Delete task by ID
def delete_task(task_id):
    try:
        result = tasks_collection.delete_one({"_id": ObjectId(task_id)})
        if result.deleted_count:
            print(f"Task {task_id} deleted")
            return True
        print(f"Task {task_id} not found")
        return False
    except Exception as e:
        print(f"Error in delete_task: {e}")
        return False
