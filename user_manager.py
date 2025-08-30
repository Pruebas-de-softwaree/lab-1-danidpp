import time
class Usermanager:
    def __init__(self):
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = Usermanager()
    for i in range(1000):
        user_manager.add_user(i,f"Yo soy el num: {i}")
    print(user_manager.get_all_names())
    print(user_manager.find_user(8))
    user_manager.delete_user(15)
    print(user_manager.find_user(15))
    print(user_manager.get_all_names())
    print(user_manager.average_user_id())
    start = time.time()  
    print(user_manager.get_all_names())
    end = time.time()
    print("duration:", end - start, "seconds")
    user_manager.add_user(18,"Dani")
    duplicados = []
    for i in user_manager.get_all_names():
        if user_manager.get_all_names().count(i) > 1 and i not in duplicados:
            duplicados.append(i)
    print("Duplicados:", duplicados)