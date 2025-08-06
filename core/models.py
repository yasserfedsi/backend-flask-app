from pymongo import MongoClient
from bson.objectid import ObjectId
from core.config import Config


class Models:
    def __init__(self):
        self.client = MongoClient(Config.MONGO_URI)
        self.db = self.client[Config.DB_NAME]
        self.tasks_collection = self.db[Config.COLLECTION_NAME]

    # Serialize MongoDB document to JSON-safe dict
    def serialize_task(self, task):
        return {
            "id": str(task.get("_id", "")),
            "title": task.get("title", ""),
            "description": task.get("description", ""),
            "completed": task.get("completed", False),
        }

    # Create a task with optional description
    def create_task(self, title, description=""):
        task = {
            "title": title,
            "description": description,
            "completed": False,
        }

        result = self.tasks_collection.insert_one(task)

        if not result.acknowledged:
            print("Task creation failed")
            return None

        print(f"Task created with id: {result.inserted_id}")
        return self.serialize_task(self.tasks_collection.find_one({"_id": result.inserted_id}))

    # Return all tasks as serialized list
    def get_all_tasks(self):
        tasks = list(self.tasks_collection.find())
        print(f"Found {len(tasks)} task(s)")
        return [self.serialize_task(task) for task in tasks]

    # Get one task by ID
    def get_task_by_id(self, task_id):
        try:
            task = self.tasks_collection.find_one({"_id": ObjectId(task_id)})
            return self.serialize_task(task) if task else None
        except Exception as e:
            print(f"Error in get_task_by_id: {e}")
            return None

    # Update a task by ID
    def update_task(self, task_id, data):
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

            result = self.tasks_collection.update_one(
                {"_id": ObjectId(task_id)},
                {"$set": update_data}
            )

            if result.matched_count == 0:
                print(f"Task {task_id} not found for update")
                return None

            print(f"Task {task_id} updated")
            return self.serialize_task(self.tasks_collection.find_one({"_id": ObjectId(task_id)}))
        except Exception as e:
            print(f"Error in update_task: {e}")
            return None

    # Delete task by ID
    def delete_task(self, task_id):
        try:
            result = self.tasks_collection.delete_one({"_id": ObjectId(task_id)})
            if result.deleted_count:
                print(f"Task {task_id} deleted")
                return True
            print(f"Task {task_id} not found")
            return False
        except Exception as e:
            print(f"Error in delete_task: {e}")
            return False
